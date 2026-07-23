# Dia 2 — Teoria: Node.js, APIs REST e TDD

> Material de apoio para o checklist de teoria em [DIA_2_node_rest_tdd.md](DIA_2_node_rest_tdd.md).
> Ler antes de começar os exercícios, e voltar aqui sempre que precisar relembrar um conceito.

---

## 1. Node.js e Event Loop

**O que é Node.js:**
Um runtime JavaScript construído sobre o motor V8 (o mesmo do Chrome), que permite rodar JS fora do navegador — em servidores, CLIs, scripts, etc. Node adiciona APIs que o navegador não tem (sistema de arquivos, rede, processos) e remove as que não fazem sentido fora do browser (DOM, `window`).

**Single-threaded, mas não bloqueante:**
Node executa o código JavaScript em uma única thread principal. Isso significa que, em teoria, duas linhas de código nunca rodam "ao mesmo tempo" no seu programa. Mas Node consegue lidar com milhares de conexões simultâneas porque **operações de I/O (rede, disco, banco de dados) não bloqueiam essa thread**.

Como isso funciona na prática:
1. Sua thread principal executa o código síncrono.
2. Quando encontra uma operação assíncrona (ex: ler um arquivo, fazer uma query, uma requisição HTTP), Node delega essa tarefa para o **libuv** (uma biblioteca em C que gerencia um pool de threads internamente para I/O) ou para o sistema operacional, e **continua executando o resto do código** sem esperar.
3. Quando a operação assíncrona termina, o resultado (callback, promise resolvida) é colocado em uma fila.
4. O **Event Loop** é o mecanismo que fica checando essa fila continuamente: assim que a thread principal fica livre (a call stack esvazia), ele pega o próximo item da fila e executa.

**Analogia simples para explicar em entrevista:**
"É como um garçom que não fica parado esperando a cozinha preparar um prato. Ele anota o pedido, manda pra cozinha, e vai atender outras mesas. Quando o prato fica pronto, ele volta e entrega. A cozinha (I/O) pode ter vários 'cozinheiros' trabalhando em paralelo, mas o garçom (thread principal) é um só."

**Por que isso importa para APIs REST:**
Um servidor Express consegue atender múltiplas requisições "ao mesmo tempo" mesmo sendo single-threaded, porque enquanto uma requisição está esperando o banco de dados responder, a thread já está livre para processar outra requisição. Isso é ótimo para I/O-bound (muitas conexões, pouca CPU), mas ruim para CPU-bound (cálculos pesados travam tudo, já que não há outra thread pra assumir).

**Pontos que costumam cair em entrevista:**
- Diferença entre **Call Stack**, **Callback Queue** (ou Task Queue) e **Microtask Queue** (onde Promises resolvem — elas têm prioridade sobre a Callback Queue).
- Node não é "assíncrono por mágica": é o event loop + libuv que orquestram isso.
- Operações de CPU intensa (loop pesado, processamento de imagem síncrono) bloqueiam o event loop e travam o servidor inteiro — por isso se usa `worker_threads` ou processos filhos para esses casos.

---

## 2. REST: verbos HTTP, status codes e idempotência

**O que é REST:**
Um estilo arquitetural (não um protocolo) para construir APIs que expõem **recursos** (ex: `/livros`, `/usuarios`) manipulados através de verbos HTTP padrão, com respostas via status codes também padronizados.

### Verbos HTTP

| Verbo | Uso | Corpo na requisição? | Idempotente? |
|-------|-----|----------------------|---------------|
| `GET` | Buscar um recurso ou lista | Não | Sim |
| `POST` | Criar um novo recurso | Sim | Não |
| `PUT` | Substituir um recurso inteiro | Sim | Sim |
| `PATCH` | Atualizar parcialmente um recurso | Sim | Não (na prática pode ser, depende da implementação) |
| `DELETE` | Remover um recurso | Não (geralmente) | Sim |

### Status codes mais usados

- **2xx — Sucesso**
  - `200 OK`: sucesso genérico (ex: GET, PUT, PATCH bem-sucedidos).
  - `201 Created`: recurso criado com sucesso (resposta padrão de um `POST` que cria algo). Normalmente retorna o objeto criado, e idealmente um header `Location` com a URL do novo recurso.
  - `204 No Content`: sucesso, mas sem corpo de resposta (comum em `DELETE`).
- **4xx — Erro do cliente**
  - `400 Bad Request`: a requisição está malformada ou falhou validação (ex: campo obrigatório ausente).
  - `401 Unauthorized`: não autenticado (o cliente não provou quem é).
  - `403 Forbidden`: autenticado, mas sem permissão para aquela ação.
  - `404 Not Found`: o recurso não existe.
- **5xx — Erro do servidor**
  - `500 Internal Server Error`: erro inesperado no servidor (bug, exceção não tratada).

**Diferença entre 401 e 403 (pergunta clássica):** 401 é "eu não sei quem você é" (falta login/token). 403 é "eu sei quem você é, mas você não pode fazer isso".

### Idempotência

Uma operação é **idempotente** quando executá-la uma vez ou várias vezes seguidas produz o mesmo resultado final no servidor.

- `GET`, `PUT`, `DELETE` são idempotentes: chamar `DELETE /livros/5` dez vezes deixa o sistema no mesmo estado que chamar uma vez (o livro 5 não existe, seja da primeira vez que foi apagado ou nas seguintes, mesmo que a resposta HTTP mude de 204 para 404).
- `POST` **não** é idempotente: chamar `POST /livros` várias vezes com o mesmo corpo cria múltiplos livros diferentes (cada um com um `id` novo).
- `PATCH` depende da implementação: se o PATCH é "seta o campo X para o valor Y", é idempotente. Se é "incrementa o estoque em 1", não é.

**Por que isso importa na prática:** clientes HTTP, proxies e navegadores podem reenviar requisições idempotentes automaticamente em caso de falha de rede, sem medo de duplicar efeitos colaterais. Isso não é seguro fazer com `POST`.

---

## 3. Estrutura de uma API Express

Uma API Express típica tem três camadas de responsabilidade bem separadas:

### 3.1 Rotas (Routes)

Definem **qual URL + verbo HTTP** aciona qual função (controller). Ficam limpas, sem lógica de negócio:

```js
router.get('/livros/:id', livrosController.buscarPorId);
router.post('/livros', livrosController.criar);
```

### 3.2 Middlewares

Funções que rodam **entre** a requisição chegar e a rota final ser executada. Toda middleware tem a assinatura `(req, res, next)` (ou `(err, req, res, next)` para tratamento de erro) e decide se chama `next()` para passar adiante, ou encerra a resposta.

Usos comuns:
- Parsing de body (`express.json()`).
- Autenticação/autorização (checar token antes de deixar passar).
- Logging (registrar método + rota + tempo de resposta).
- Validação de entrada.
- Tratamento de erros centralizado (middleware especial, com 4 argumentos, definido por último com `app.use`).

A ordem de registro dos middlewares importa — eles rodam em sequência, como uma pipeline.

### 3.3 Tratamento de erros

Express reconhece um middleware de erro pela sua assinatura de **4 parâmetros**: `(err, req, res, next)`. Ele deve ser registrado **depois** de todas as rotas. Rotas assíncronas precisam encaminhar erros manualmente para esse middleware (ex: `try/catch` chamando `next(err)`), já que Express não captura rejeições de Promise automaticamente em versões anteriores à 5.

```js
app.use((err, req, res, next) => {
  const status = err.status || 500;
  res.status(status).json({ error: err.message });
});
```

### 3.4 Separação `app.js` / `server.js`

Prática comum: `app.js` monta o `express()`, registra middlewares e rotas, e **exporta** o app **sem chamar `.listen()`**. `server.js` importa esse app e chama `.listen()`.

**Por quê:** isso permite que testes de integração (ex: com `supertest`) importem o `app` e façam requisições simuladas contra ele **sem precisar subir um servidor real numa porta**. Mantém os testes rápidos e evita conflitos de porta ao rodar testes em paralelo.

---

## 4. Validação de entrada

Validar dados que chegam do cliente (body, query params, params de rota) antes de processá-los, para não deixar dados inválidos chegarem à lógica de negócio ou ao banco.

### Validação manual

```js
if (!req.body.titulo) {
  return res.status(400).json({ error: 'titulo é obrigatório' });
}
if (req.body.estoque < 0) {
  return res.status(400).json({ error: 'estoque não pode ser negativo' });
}
```

Funciona, mas fica repetitiva e difícil de manter conforme o número de campos/regras cresce.

### Validação com biblioteca de schema (`zod`, `joi`)

Define-se um **schema** declarativo que descreve o formato esperado dos dados, e a lib faz a validação (e geralmente também a conversão de tipos) de uma vez:

```js
// zod
const livroSchema = z.object({
  titulo: z.string().min(1),
  estoque: z.number().int().nonnegative(),
});

const resultado = livroSchema.safeParse(req.body);
if (!resultado.success) {
  return res.status(400).json({ error: resultado.error.issues });
}
```

**Vantagens sobre validação manual:**
- Regras centralizadas em um único lugar (o schema), reaproveitável.
- Mensagens de erro consistentes e detalhadas.
- Muitas libs (como `zod`) também dão **inferência de tipos** em TypeScript a partir do schema.
- Reduz a chance de esquecer de validar um campo.

---

## 5. TDD — Test-Driven Development

**O ciclo RED → GREEN → REFACTOR:**

1. **RED:** escreva um teste para um comportamento que ainda não existe. Rode o teste e veja ele **falhar** (isso confirma que o teste está realmente testando algo, e não passando por acidente).
2. **GREEN:** escreva o **mínimo código possível** para fazer aquele teste passar. Não se preocupe com elegância ainda — só fazer passar.
3. **REFACTOR:** com o teste passando como uma rede de segurança, melhore o código (nomes, duplicação, estrutura) sem mudar o comportamento. Rode os testes de novo para garantir que nada quebrou.

Repete-se esse ciclo em incrementos pequenos.

**Por que escrever o teste antes do código (pergunta clássica de entrevista):**
- **Força pensar no comportamento esperado (a interface) antes da implementação** — você define "o que" antes de "como".
- Garante que todo código de produção tem um teste que o motivou a existir — evita código morto ou não testado.
- O teste falhando primeiro (RED) prova que ele é capaz de detectar a ausência da funcionalidade — um teste que nunca falha não está testando nada de verdade (falso positivo).
- Gera um design mais desacoplado, porque código difícil de testar (muitas dependências escondidas, funções fazendo coisas demais) fica doloroso de testar *antes* de existir, o que empurra para interfaces mais simples.
- Dá feedback rápido: cada ciclo é curto, então erros são pegos imediatamente, não depois de uma feature inteira pronta.

**Contraponto que pode ser perguntado:** TDD não é obrigatório para tudo (ex: pode ser exagero para scripts descartáveis ou protótipos exploratórios), e não substitui outros tipos de teste (integração, E2E, testes manuais de UX). É uma técnica de design de código tanto quanto uma técnica de garantia de qualidade.

**Referência complementar no repo:** `api_node_com_TDD/regras_TDD_Estudos.md`.

---

## Resumo rápido para revisão de última hora

- **Event loop:** single-threaded, I/O não-bloqueante via libuv, event loop drena a fila quando a call stack esvazia.
- **REST:** GET/POST/PUT/PATCH/DELETE; 2xx sucesso, 4xx erro do cliente, 5xx erro do servidor; PUT e DELETE são idempotentes, POST não é.
- **Express:** rotas → middlewares → controllers; erro tratado em middleware de 4 argumentos registrado por último; `app.js` sem `listen()` para facilitar testes.
- **Validação:** manual funciona mas não escala; `zod`/`joi` centralizam regras e dão mensagens consistentes.
- **TDD:** RED (teste falha) → GREEN (mínimo pra passar) → REFACTOR (melhora com segurança); testar antes força pensar na interface e evita falsos positivos.

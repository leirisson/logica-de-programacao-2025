# TDD — Test Driven Development com Node.js

> Guia progressivo para dominar TDD do zero, construindo uma API Node.js passo a passo.

---

## O que é TDD?

TDD é uma técnica de desenvolvimento onde você **escreve o teste antes do código**.

O ciclo se repete o tempo todo:

```text
RED → GREEN → REFACTOR
```

| Fase | O que fazer | Por quê |
| --- | --- | --- |
| RED | Escrever um teste que **falha** | Provar que o teste detecta ausência de comportamento |
| GREEN | Escrever o **mínimo de código** para o teste passar | Foco no comportamento, não na perfeição |
| REFACTOR | Melhorar o código **sem quebrar os testes** | Qualidade sem medo |

### Regra de ouro

> Nunca escreva código de produção sem antes ter um teste falhando que justifique aquele código.

---

## Mentalidade Correta

Antes de escrever qualquer linha, responda:

1. **O que esse código deve fazer?** (comportamento esperado)
2. **Como eu saberia que está funcionando?** (critério de aceitação)
3. **Qual é o menor teste que prova isso?** (teste unitário)

Erros comuns de quem está aprendendo:

- Escrever o código e depois o teste (isso não é TDD)
- Escrever testes muito grandes de uma vez (escreva um de cada vez)
- Pular a fase REFACTOR (o código acumula dívida técnica)
- Testar detalhes de implementação em vez de comportamento

---

## Roteiro de Estudos

| # | Tópico | Conceito TDD praticado |
| --- | --- | --- |
| 1 | Setup do ambiente (vitest + Node) | Estrutura de testes, `describe` e `it` |
| 2 | Funções puras | RED → GREEN → REFACTOR básico |
| 3 | Módulos e dependências | Testes isolados, sem efeitos colaterais |
| 4 | API com Express — rotas GET | Teste de integração de rotas |
| 5 | API com Express — rotas POST | Validação de entrada com testes |
| 6 | Banco de dados (em memória) | Mocks e stubs |
| 7 | Banco de dados real (SQLite/PostgreSQL) | Testes de integração com banco |
| 8 | Autenticação (JWT) | TDD em fluxos de segurança |
| 9 | Refactor guiado por testes | Mudar implementação sem mudar testes |
| 10 | API completa com cobertura de testes | Relatório de coverage |

---

## Fase 1 — Setup do Ambiente

### Estrutura de pastas

```text
api_node_com_TDD/
├── src/
│   └── (código de produção aqui)
├── tests/
│   └── (testes aqui, espelhando src/)
├── package.json
└── jest.config.js
```

### Instalação

```bash
npm init -y
npm install --save-dev jest
```

### package.json — script de teste

```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  }
}
```

### jest.config.js

```js
module.exports = {
  testEnvironment: 'node',
  testMatch: ['**/tests/**/*.test.js'],
  collectCoverageFrom: ['src/**/*.js'],
};
```

---

## Fase 2 — Primeiro Ciclo RED → GREEN → REFACTOR

### Problema: Criar uma função que soma dois números

#### Passo 1 — RED (escreva o teste PRIMEIRO)

Arquivo: `tests/calculadora.test.js`

```js
const { somar } = require('../src/calculadora');

describe('calculadora', () => {
  it('deve retornar a soma de dois números', () => {
    const resultado = somar(2, 3);
    expect(resultado).toBe(5);
  });
});
```

Execute: `npm test` → **o teste deve falhar** (RED confirmado).

#### Passo 2 — GREEN (escreva o mínimo de código)

Arquivo: `src/calculadora.js`

```js
function somar(a, b) {
  return a + b;
}

module.exports = { somar };
```

Execute: `npm test` → **o teste deve passar** (GREEN confirmado).

#### Passo 3 — REFACTOR (melhore se necessário)

O código está simples o suficiente — sem refactor necessário.
Adicione mais um teste antes de continuar:

```js
it('deve funcionar com números negativos', () => {
  expect(somar(-1, -4)).toBe(-5);
});

it('deve funcionar com zero', () => {
  expect(somar(0, 5)).toBe(5);
});
```

> Repita o ciclo para cada novo comportamento.

---

## Fase 3 — Módulos com Validação

### Problema: Criar uma função que calcula desconto

**Regras de negócio (defina antes de testar):**

- Recebe valor e percentual de desconto
- Retorna o valor com desconto aplicado
- Lança erro se o valor for negativo
- Lança erro se o desconto for maior que 100%

#### RED — escreva todos os testes primeiro

```js
const { calcularDesconto } = require('../src/desconto');

describe('calcularDesconto', () => {
  it('deve aplicar o desconto corretamente', () => {
    expect(calcularDesconto(100, 10)).toBe(90);
  });

  it('deve retornar o valor cheio se desconto for 0', () => {
    expect(calcularDesconto(200, 0)).toBe(200);
  });

  it('deve lançar erro se valor for negativo', () => {
    expect(() => calcularDesconto(-50, 10)).toThrow('Valor inválido');
  });

  it('deve lançar erro se desconto for maior que 100', () => {
    expect(() => calcularDesconto(100, 110)).toThrow('Desconto inválido');
  });
});
```

#### GREEN — implemente para os testes passarem

```js
function calcularDesconto(valor, desconto) {
  if (valor < 0) throw new Error('Valor inválido');
  if (desconto > 100) throw new Error('Desconto inválido');
  return valor - (valor * desconto) / 100;
}

module.exports = { calcularDesconto };
```

---

## Fase 4 — API com Express (TDD de rotas)

### Instalação

```bash
npm install express
npm install --save-dev supertest
```

> `supertest` permite testar rotas HTTP sem subir o servidor de verdade.

### Estrutura de arquivos

```text
src/
├── app.js        (configura Express, sem chamar listen())
└── server.js     (chama listen() — não é testado diretamente)
```

> Separar `app.js` de `server.js` é essencial para testar rotas sem abrir porta de rede.

### RED — teste de rota GET

```js
const request = require('supertest');
const app = require('../src/app');

describe('GET /health', () => {
  it('deve retornar status 200 e mensagem ok', async () => {
    const response = await request(app).get('/health');
    expect(response.status).toBe(200);
    expect(response.body).toEqual({ status: 'ok' });
  });
});
```

### GREEN — implementação mínima

```js
// src/app.js
const express = require('express');
const app = express();

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

module.exports = app;
```

---

## Fase 5 — POST com Validação

### RED — teste de criação de recurso

```js
describe('POST /usuarios', () => {
  it('deve criar um usuário e retornar 201', async () => {
    const response = await request(app)
      .post('/usuarios')
      .send({ nome: 'Ana', email: 'ana@email.com' });

    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.nome).toBe('Ana');
  });

  it('deve retornar 400 se nome estiver ausente', async () => {
    const response = await request(app)
      .post('/usuarios')
      .send({ email: 'ana@email.com' });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('erro');
  });
});
```

---

## Fase 6 — Mocks e Stubs

Quando o código depende de algo externo (banco, API, e-mail), use **mocks** para isolar.

### Conceitos

| Conceito | O que é | Quando usar |
| --- | --- | --- |
| Mock | Substituto que verifica se foi chamado | Verificar que uma função foi chamada |
| Stub | Substituto que retorna valor fixo | Simular retorno de banco ou API |
| Spy | Observa chamadas sem substituir | Verificar quantidade/ordem de chamadas |

### Exemplo com Jest mock

```js
const usuarioService = require('../src/usuarioService');
const usuarioRepository = require('../src/usuarioRepository');

jest.mock('../src/usuarioRepository');

describe('usuarioService.criar', () => {
  it('deve chamar o repositório com os dados corretos', async () => {
    usuarioRepository.salvar.mockResolvedValue({ id: 1, nome: 'Ana' });

    const resultado = await usuarioService.criar({ nome: 'Ana', email: 'ana@email.com' });

    expect(usuarioRepository.salvar).toHaveBeenCalledWith({ nome: 'Ana', email: 'ana@email.com' });
    expect(resultado.id).toBe(1);
  });
});
```

---

## Checklist por Ciclo

Use este checklist a cada novo comportamento que for implementar:

- [ ] Defini claramente **o que** o código deve fazer?
- [ ] Escrevi o teste **antes** do código?
- [ ] O teste **falhou** por razão correta (RED)?
- [ ] Escrevi o **mínimo de código** para passar (GREEN)?
- [ ] Há algo para melhorar sem mudar comportamento (REFACTOR)?
- [ ] Todos os testes anteriores continuam passando?

---

## Comandos do Dia a Dia

```bash
npm test                  # roda todos os testes uma vez
npm run test:watch        # modo watch (roda ao salvar)
npm run test:coverage     # relatório de cobertura
npx jest tests/arquivo.test.js  # roda um arquivo específico
```

---

## Referências

- [Jest — documentação oficial](https://jestjs.io/docs/getting-started)
- [Supertest — testes de HTTP](https://github.com/ladjs/supertest)
- [Test Driven Development by Example — Kent Beck](https://www.amazon.com.br/Test-Driven-Development-Kent-Beck/dp/0321146530)

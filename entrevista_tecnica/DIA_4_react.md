# Dia 4 — React.js (Front-end)

> Progresso geral: [PROGRESSO.md](PROGRESSO.md)

**Objetivo:** cobrir o segundo requisito obrigatório de front-end.

Domínio sugerido: front-end consumindo a API de livros construída no Dia 2 (pode usar dados mockados se a API não estiver rodando).

---

## Teoria (checklist)

- [ ] JSX, componentes funcionais, props vs state.
- [ ] Hooks essenciais: `useState`, `useEffect` (dependências, cleanup), `useContext`.
- [ ] Ciclo de vida de um componente funcional (mount, update, unmount via `useEffect`).
- [ ] Listas e `key` — por que é importante.
- [ ] Consumo de API REST no front (`fetch` ou `axios`), tratamento de loading/erro.
- [ ] Formulários controlados (`value` + `onChange`).

---

## Exercícios (20)

1. [ ] Criar um projeto React novo (Vite: `npm create vite@latest`) e rodar o "hello world" padrão.
2. [ ] Criar um componente `Ola({ nome })` que recebe `nome` via props e renderiza `Olá, {nome}`.
3. [ ] Criar um componente `Contador` com `useState`, com botões de incrementar e decrementar.
4. [ ] Criar um componente `ListaLivros` que recebe um array de livros via props e renderiza em `<ul>`, usando `key={livro.id}` corretamente.
5. [ ] Quebrar `ListaLivros` propositalmente usando `key={index}` com uma lista que reordena, e observar/explicar o problema que isso causa.
6. [ ] Criar um componente `BuscaLivro` com um `<input>` controlado (`value` + `onChange`) que filtra a lista de livros por título em tempo real.
7. [ ] Criar `LivroCard` que recebe um livro e mostra um badge "Estoque baixo" se `estoque < 5` (renderização condicional).
8. [ ] Usar `useEffect` com array de dependência vazio `[]` para buscar a lista de livros da API (Dia 2) assim que o componente monta.
9. [ ] Adicionar estado de `loading` enquanto a requisição do exercício 8 não termina, mostrando um "Carregando..." na tela.
10. [ ] Adicionar tratamento de erro na busca (try/catch ou `.catch`), mostrando uma mensagem se a API falhar.
11. [ ] Criar um formulário controlado `NovoLivroForm` com campos `titulo`, `autor`, `estoque`, cada um com seu próprio `useState` (ou um único objeto de estado).
12. [ ] Fazer o `NovoLivroForm` do exercício 11 chamar `POST /livros` (Dia 2) ao submeter, e atualizar a lista na tela sem recarregar a página.
13. [ ] Adicionar validação simples no formulário (não permitir submit se `titulo` estiver vazio), desabilitando o botão de salvar.
14. [ ] Criar um `useEffect` com cleanup: um componente `Relogio` que usa `setInterval` para atualizar a hora a cada segundo, limpando o interval no unmount.
15. [ ] Criar um `Context` (`useContext`) simples para compartilhar o tema (claro/escuro) entre componentes sem prop drilling.
16. [ ] Extrair a lógica de busca de livros (exercícios 8-10) para um hook customizado `useLivros()` reutilizável.
17. [ ] Implementar um botão de deletar em `LivroCard` que chama `DELETE /livros/:id` e remove o item da lista local após sucesso.
18. [ ] Implementar edição inline: clicar em "Editar" no `LivroCard` troca a visualização por um input controlado, e "Salvar" chama `PATCH /livros/:id/estoque`.
19. [ ] Explicar em voz alta, com exemplo de código, por que renderizar uma lista sem `key` (ou com key errada) pode causar bugs visuais/de estado em atualizações.
20. [ ] Montar a tela final juntando tudo: lista de livros + busca + formulário de criação + exclusão, consumindo a API real do Dia 2 (ou mock se preferir).

---

## Perguntas de entrevista

1. Qual a diferença entre `props` e `state`?
2. Para que serve o `useEffect` e quando ele é executado?
3. Por que usar `key` em listas renderizadas no React? O que acontece se não usar (ou usar o índice)?

---

## Dúvidas do dia

| Exercício | Dúvida | Resolvido? |
|-----------|--------|------------|
| | | |

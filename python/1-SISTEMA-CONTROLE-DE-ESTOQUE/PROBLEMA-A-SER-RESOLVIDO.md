SISTEMA 1: CONTROLE DE ESTOQUE
Descrição do Problema
Desenvolver um sistema para gerenciar produtos em estoque, controlando entradas, saídas e verificando disponibilidade.

Objetivo
Permitir o cadastro de produtos, consulta de estoque, registro de movimentações e alertas de baixo estoque.

Fluxo Principal
Menu inicial com opções: Cadastrar Produto, Consultar Estoque, Registrar Entrada, Registrar Saída

Validação de dados em cada operação

Atualização do estoque após movimentações

Verificação de limites mínimos

Exercícios

1. Cadastro de Produtos
Sub-tarefas:
- Solicitar código, nome, quantidade inicial e estoque mínimo
- Verificar se código já existe
- Validar dados (quantidade não negativa)
- Armazenar produto na memória

2. Consulta de Estoque
Sub-tarefas:
- Listar todos os produtos com estoque
- Pesquisar produto por código
- Destacar produtos com estoque abaixo do mínimo
- Calcular valor total do estoque

3. Registro de Entrada
Sub-tarefas:
- Localizar produto por código
- Validar quantidade de entrada
- Atualizar estoque
- Registrar data/hora da operação

4. Registra Saída
Sub-tarefas:
- Verificar se produto existe
- Confirmar estoque suficiente
- Atualizar estoque após saída
- Gerar alerta se estoque ficar abaixo do mínimo

5. Relatório de Produtos Críticos
Sub-tarefas:
- Filtrar produtos com estoque abaixo do mínimo
- Ordenar por prioridade (mais críticos primeiro)
- Calcular quantidade necessária para repor
- Exibir relatório formatado
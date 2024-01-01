# Simulador de Banco em Python

Este é um simulador simples de banco em Python que oferece funcionalidades como depósito, saque, extrato e saída do programa.

## Funcionalidades

### Depósito
Permite ao usuário realizar um depósito na conta bancária. Ele solicita o valor do depósito e o adiciona ao saldo atual da conta.

### Saque
Possibilita ao usuário realizar um saque da conta bancária. Requer o valor a ser sacado e verifica se é viável (saldo suficiente, dentro do limite diário e individual de R$500). Após a validação, o valor é subtraído do saldo.

### Extrato
Exibe um resumo das transações realizadas até o momento, incluindo depósitos e saques, além do saldo atual da conta.

### Saída
Oferece ao usuário a opção de sair do programa.

## Aprendizado da Linguagem de Programação

Este código demonstra alguns conceitos fundamentais da linguagem Python:

- Estruturas de repetição (`while`) para manter o programa em execução até a escolha de saída.
- Uso de listas para armazenar o histórico de transações (extrato).
- Condicional (`if`, `elif`, `else`) para verificar e executar diferentes operações com base na escolha do usuário.
- Manipulação de strings para exibição de mensagens e formatação do extrato.
- Entrada de dados do usuário por meio da função `input()` e conversão de tipos de dados (`int`, `float`) para validar e realizar operações.

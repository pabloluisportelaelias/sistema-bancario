# Sistema Bancário em Python

Este projeto consiste na implementação de um sistema bancário simplificado, desenvolvido com a linguagem de programação Python. Seu objetivo é simular operações bancárias fundamentais, como depósitos, saques e emissão de extrato, além de classificar o cliente em categorias com base em seu saldo.

## Objetivos do Projeto

- Aplicar conceitos básicos de lógica de programação.
- Utilizar estruturas de controle como laços, condicionais e funções.
- Desenvolver a manipulação de strings, datas e entradas do usuário.
- Promover boas práticas de codificação para programas interativos em console.

## Funcionalidades

- Registro de depósitos com data e hora.
- Saques controlados por limite de valor e quantidade diária.
- Emissão de extrato com histórico das movimentações.
- Classificação automática do cliente como Bronze, Prata ou Ouro, conforme o saldo em conta.

## Requisitos

- Python 3.6 ou superior instalado no sistema.
- Editor de código ou terminal para execução via linha de comando.

## Execução

1. Clone o repositório ou faça o download do arquivo:

```bash
git clone https://github.com/pabloluisportelaelias/sistema-bancario.git
cd sistema-bancario

| Faixa de Saldo (R\$)    | Categoria |
| ----------------------- | --------- |
| ≥ 5.000,00              | Ouro      |
| ≥ 2.000,00 e < 5.000,00 | Prata     |
| < 2.000,00              | Bronze    |

Estrutura do Código
O programa é executado em um laço de repetição while, permitindo múltiplas operações até o encerramento manual.

As funções utilizam a biblioteca datetime para registrar o horário de cada transação.

As validações de entrada evitam operações inválidas e controlam regras como o limite de saques.

Possibilidades de Expansão
Implementação de interface gráfica (GUI) com bibliotecas como Tkinter ou PyQt.

Integração com banco de dados para persistência de dados.

Modularização do código em múltiplos arquivos ou pacotes.

Autor
Pablo Luis Portela Elias
GitHub: https://github.com/pabloluisportelaelias


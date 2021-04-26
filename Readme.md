<h1 align=center>Sistemas Distribuídos</h1>

<h2 align=center>Aracity</h2>

## Descrição

Fechamento de compra\
O caixa da Aracity finaliza a compra armazenando a lista de produtos comprados no servidor. O servidor deve responder confirmando a compra ou não.

## O que foi usado?

* [Python 3](https://www.python.org/)
* [Socket](https://docs.python.org/3/library/socket.html)
* [Pony ORM](https://ponyorm.org/)

## Como executar?

O projeto está dividido em duas pastas, uma para o server e outra para o client

Antes de rodar o projeto execute o comando:

```bash
pip3 install -r requirements.txt
```

O comando acima vai instalar o pony orm, que é utilizado para a gerencia dos dados

1. Em um terminal aberto na raiz do projeto, execute o comando:

```bash
python3 server/main.py
```

em um novo terminal execute:

```bash
python3 client/main.py
```

2. No terminal onde o client está sendo executado, basta adicionar o input com dois números:

```bash
7 12
```

Onde o primeiro número é o código do produto e o segundo a quantidade desejada

## Equipe

* [Jailson Soares](https://github.com/jailsonsf)

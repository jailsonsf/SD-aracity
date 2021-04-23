import socket
import sys

from database.db import *
from controller import *

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

while True:
    con, client = tcp.accept()
    print('Conectado com ', con)

    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print(client, msg.decode())

    print('Finalisando conexão com ', client)
    con.close()
    break

with db_session:
    if Produto.select().first() is None:
        populate_database()


# input lista de compras
# data = json.load(open('server/data.json'))['lista_compras']

# products = []
# for p in data:
#     products.append(p)

# checkout(products)

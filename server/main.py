import socket

from database.db import *
from controller import *

with db_session:
    if Produto.select().first() is None:
        populate_database()

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

while True:
    con, client = tcp.accept()
    print('Conectado com ', con)
    con.send(all_products().encode())
    init = con.recv(1024)

    products = []
    while True:
        msg = con.recv(1024)
        if not msg:
            break

        if msg.decode() == 'f':
            con.send(checkout(products).encode())
            break

        products.append(msg.decode())

    break

print('Finalisando conexão com ', client)
con.close()

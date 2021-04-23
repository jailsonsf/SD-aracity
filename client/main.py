import socket
import json
from time import sleep

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

tcp.send(b'Connect')
data = tcp.recv(1024).decode()
data = json.loads(data)

print('Produtos disponíveis:')
print('{:<6} {}'.format('ID', 'Produto'))
print('--'*10)
for p in data:
    print('{:<6} {}'.format(p['id'], p['nome']))
print('--'*10)

print('Digite 0 para finalizar lista.')
print('Digite o ID do produto e a quantidade que deseja.')
msg = input()
while msg != '0':
    number, amount = map(int, msg.split())

    req = {
        'id': number,
        'amount': amount
    }

    req = json.dumps(req)
    tcp.send(req.encode())

    msg = input()

tcp.send(b'f')
data = tcp.recv(1024).decode()
data = json.loads(data)
print(data)

tcp.close()

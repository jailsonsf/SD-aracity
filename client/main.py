import socket

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

print('Digite 0 para sair.')
msg = input('Mensagem: ')

while msg != '0':
    byt = msg.encode()
    tcp.send(byt)
    msg = input('Mensagem: ')

tcp.close()

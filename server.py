# https://hackernoon.com/creating-command-line-based-chat-room-using-python-oxu3u33

import socket
import threading

host = 'localhost'
port = 7976

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ASCII'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print('Connected with {}'.format(str(address)))
        client.send('NICKNAME'.encode('ASCII'))

        nickname = client.recv(1024).decode('ASCII')
        nicknames.append(nickname)
        clients.append(client)

        print('Nickname is {}'.format(nickname))
        broadcast('{} joined!'.format(nickname).encode('ASCII'))

        client.send('Connected to server!'.encode('ASCII'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()

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
            print(message)
            if 'kill' in message.decode('UTF8'):
                client.close()
                break
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('UTF8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print('Connected with {}'.format(str(address)))

        nickname = client.recv(1024).decode('UTF8')
        nicknames.append(nickname)
        clients.append(client)

        print('Nickname is {}'.format(nickname))
        broadcast('{} joined!\n'.format(nickname).encode('UTF8'))

        client.send('Connected to server!\n'.encode('UTF8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()

import socket
import threading

nickname = input('Choose your nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7976))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ASCII')
            if message == 'NICKNAME':
                client.send(nickname.encode('ASCII'))
            else:
                print(message)
        except:
            print('Deu ruim mermao')
            client.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ASCII'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

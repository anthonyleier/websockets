import socket
import threading


class Server:
    def __init__(self):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 7976
        self.clients = []
        self.nicknames = []

    def conectar(self):
        self.conexao.bind((self.host, self.port))
        self.conexao.listen()

    def desconectar(self):
        self.conexao.close()

    def broadcast(self, client_atual, message):
        for client in self.clients:
            if client != client_atual:
                client.send(message)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(client, message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(client, '{} left!'.format(nickname).encode('UTF8'))
                print('{} left!'.format(nickname).encode('UTF8'))
                self.nicknames.remove(nickname)
                break

    def receive(self):
        while True:
            client, address = self.conexao.accept()
            print('Connected with {}'.format(str(address)))

            nickname = client.recv(1024).decode('UTF8')
            self.nicknames.append(nickname)
            self.clients.append(client)

            print('Nickname is {}'.format(nickname))
            self.broadcast(client, '{} joined!\n'.format(nickname).encode('UTF8'))

            client.send('Connected to server!\n'.encode('UTF8'))
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def iniciar_chat(self):
        recebimento_thread = threading.Thread(target=self.recebimento)
        recebimento_thread.start()
        envio_thread = threading.Thread(target=self.envio)
        envio_thread.start()


def main():
    server = Server()
    server.conectar()
    server.receive()


if __name__ == "__main__":
    main()

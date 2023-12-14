import socket
import threading


class Server:
    def __init__(self, host, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.clients = []
        self.nicknames = []

    def connect(self):
        self.connection.bind((self.host, self.port))
        self.connection.listen()

    def disconnect(self):
        self.connection.close()

    def broadcast(self, current_client, message):
        for client in self.clients:
            if client != current_client:
                if type(message) is str:
                    formatted_message = (str(message) + '\n').encode('UTF8')

                if type(message) is bytes:
                    formatted_message = message

                client.send(formatted_message)

    def send_message(self, client, message):
        formatted_message = (str(message) + '\n').encode('UTF8')
        client.send(formatted_message)

    def connect_client(self, client):
        nickname = client.recv(1024).decode('UTF8')
        self.nicknames.append(nickname)
        self.clients.append(client)

        self.broadcast(client, f'{nickname} entrou no chat!')
        self.send_message(client, 'Conectado no servidor!')

    def disconnect_client(self, client):
        index = self.clients.index(client)
        self.clients.remove(client)
        client.close()

        nickname = self.nicknames[index]
        message = f"{nickname} saiu do chat!"
        self.broadcast(client, message)
        self.nicknames.remove(nickname)

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(client, message)

            except:
                self.disconnect_client(client)
                break

    def receive(self):
        while True:
            client, address = self.connection.accept()
            print(f'Conectado com {address}')
            self.connect_client(client)

            thread = threading.Thread(target=self.handle, args=[client])
            thread.start()


def main():
    server = Server('localhost', 7976)
    server.connect()
    server.receive()


if __name__ == "__main__":
    main()

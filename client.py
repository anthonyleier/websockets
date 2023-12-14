import socket
import threading


class Client:
    def __init__(self, host, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.nickname = None

    def connect(self):
        self.connection.connect((self.host, self.porta))

    def disconnect(self):
        self.connection.close()

    def register(self, nickname):
        self.nickname = nickname
        self.connection.send(nickname.encode('UTF8'))

    def start_chat(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send)
        send_thread.start()

    def receive(self):
        while True:
            try:
                message = self.connection.recv(1024).decode('UTF8')
                print(message)

            except Exception as erro:
                print(f'Ocorreu um erro no recebimento das mensagens: {erro}')
                self.disconnect()
                break

    def send(self):
        while True:
            try:
                message = '{}: {}'.format(self.nickname, input(''))
                self.connection.send(message.encode('UTF8'))

            except Exception as erro:
                print(f'Ocorreu um erro no envio das mensagens: {erro}')
                self.disconnect()
                break


def main():
    client = Client('localhost', 7976)
    client.connect()
    client.register(input("Nickname:"))
    client.start_chat()


if __name__ == "__main__":
    main()

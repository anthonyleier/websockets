import socket
import threading


class Client:
    def __init__(self):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.porta = 7976
        self.nickname = None

    def conectar(self):
        self.conexao.connect((self.host, self.porta))

    def desconectar(self):
        self.conexao.close()

    def cadastrar(self, nickname):
        self.nickname = nickname
        self.conexao.send(nickname.encode('UTF8'))

    def iniciar_chat(self):
        recebimento_thread = threading.Thread(target=self.recebimento)
        recebimento_thread.start()
        envio_thread = threading.Thread(target=self.envio)
        envio_thread.start()

    def recebimento(self):
        while True:
            try:
                message = self.conexao.recv(1024).decode('UTF8')
                print(message)
            except Exception as erro:
                print(f'Ocorreu um erro no recebimento das mensagens: {erro}')
                self.desconectar()
                break

    def envio(self):
        while True:
            try:
                message = '{}: {}'.format(self.nickname, input(''))
                self.conexao.send(message.encode('UTF8'))
            except Exception as erro:
                print(f'Ocorreu um erro no envio das mensagens: {erro}')
                self.desconectar()
                break


def main():
    client = Client()
    client.conectar()
    client.cadastrar(input("Nickname:"))
    client.iniciar_chat()


if __name__ == "__main__":
    main()

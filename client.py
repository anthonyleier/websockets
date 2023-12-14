import socket
import threading


class Client:
    def __init__(self):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = 'localhost'
        self.porta = 7976
        self.nickname = None

    def cadastrar(self, nickname):
        self.nickname = nickname
        self.conexao.send(nickname.encode('ASCII'))

    def iniciar_chat(self):
        recebimento_thread = threading.Thread(target=self.recebimento)
        recebimento_thread.start()
        envio_thread = threading.Thread(target=self.envio)
        envio_thread.start()

    def recebimento(self):
        while True:
            try:
                message = self.conexao.recv(1024).decode('ASCII')
                print(message)
            except:
                print('Deu ruim mermao')
                self.conexao.close()
                break

    def envio(self):
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            self.conexao.send(message.encode('ASCII'))

    def conectar(self):
        self.conexao.connect((self.ip, self.porta))

    def desconectar(self):
        self.conexao.close()


def main():
    cliente = Client()
    cliente.conectar()
    cliente.cadastrar(input("Qual o seu nome?"))
    cliente.iniciar_chat()


if __name__ == "__main__":
    main()

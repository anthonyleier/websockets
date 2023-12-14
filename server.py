import asyncio
import websockets


class Server:
    def __init__(self, websocket):
        self.websocket = websocket
        self.clients = []

    async def registar_client(self):
        identificacao = await self.websocket.recv()
        self.clients[identificacao] = self.websocket

    async def enviar_mensagem(self):
        mensagens_texto = '\n'.join(self.mensagens)
        print(mensagens_texto)
        await self.websocket.send(mensagens_texto)

    async def receber_mensagem(self):
        mensagem_recebida = await self.websocket.recv()
        self.mensagens.append(mensagem_recebida)


clientes = {}


async def rodar_servidor(websocket):
    identificacao = await websocket.recv()
    await websocket.send(f'Identificado como {identificacao}')
    clientes[identificacao] = websocket

    async for mensagem in websocket:
        destinatario, conteudo = mensagem.split(":")
        destinatario_socket = clientes.get(destinatario)

        if not destinatario_socket:
            await websocket.send("Destinatario não encontrado")

        if destinatario_socket:
            await destinatario_socket.send(f"Mensagem de outra pessoa: {conteudo}")


asyncio.get_event_loop().run_until_complete(websockets.serve(rodar_servidor, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

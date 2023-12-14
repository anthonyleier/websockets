import asyncio
import websockets


class Server:
    def __init__(self, websocket):
        self.websocket = websocket
        self.mensagens = []

    async def enviar_mensagem(self):
        mensagens_texto = '\n'.join(self.mensagens)
        print(mensagens_texto)
        await self.websocket.send(mensagens_texto)

    async def receber_mensagem(self):
        mensagem_recebida = await self.websocket.recv()
        self.mensagens.append(mensagem_recebida)


async def rodar_servidor(websocket):
    server = Server(websocket)
    while True:
        await server.receber_mensagem()
        await server.enviar_mensagem()


asyncio.get_event_loop().run_until_complete(websockets.serve(rodar_servidor, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

import asyncio
import websockets
from websockets.exceptions import ConnectionClosedOK


class Client:
    def __init__(self, websocket):
        self.websocket = websocket

    async def enviar_mensagem(self, texto):
        await self.websocket.send(texto)

    async def receber_mensagem(self):
        try:
            resposta = await self.websocket.recv()
            print(resposta)
        except ConnectionClosedOK:
            print("Conexão fechada pelo servidor")


async def rodar_cliente():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        client = Client(websocket)
        while True:
            mensagem_para_enviar = input('Digite (ou "sair" para encerrar): ')

            if mensagem_para_enviar.lower() == 'sair':
                break

            await client.enviar_mensagem(mensagem_para_enviar)
            await client.receber_mensagem()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(rodar_cliente())

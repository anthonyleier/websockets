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

        identificacao = input('Identificação:')
        await client.enviar_mensagem(identificacao)
        await client.receber_mensagem()

        while True:
            destinatario = input("Digite o identificador do destinatario:")
            conteudo = input("Digite a mensagem:")
            mensagem = f"{destinatario}:{conteudo}"

            await client.enviar_mensagem(mensagem)
            await client.receber_mensagem()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(rodar_cliente())

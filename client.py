import os
import asyncio
import websockets


async def enviar_mensagens():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        websocket.send(input('identi'))


async def receber_mensagens():
    uri = "ws://localhost:8765"
    historico = ''

    async with websockets.connect(uri) as websocket:

        with open('texto.txt', 'w', encoding='UTF8') as arquivo:
            arquivo.write('start\n')

        while True:
            resposta = await websocket.recv()

            if resposta != historico:
                historico = resposta
                with open('texto.txt', 'a', encoding='UTF8') as arquivo:
                    arquivo.write(historico)

if __name__ == "__main__":
    asyncio.gather(enviar_mensagens(), receber_mensagens())
    asyncio.get_event_loop().run_forever()
    # asyncio.get_event_loop().run_until_complete(rodar_cliente())

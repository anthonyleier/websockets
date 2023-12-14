import asyncio
import websockets


async def rodar_servidor(websocket, caminho):
    mensagens = []

    while True:
        mensagem_recebida = await websocket.recv()
        mensagens.append(mensagem_recebida)

        mensagens_texto = '\n'.join(mensagens)
        print(mensagens_texto)
        await websocket.send(mensagens_texto)

asyncio.get_event_loop().run_until_complete(websockets.serve(rodar_servidor, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

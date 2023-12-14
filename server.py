import asyncio
import websockets

mensagens = []


def gerar_mensagens_texto():
    texto = ''
    for mensagem in mensagens:
        texto += f"{mensagem['user']} - {mensagem['message']}\n"
    return texto


async def rodar_servidor(websocket):
    mensagens.append({'user': 'server', 'message': 'opa'})

    while True:
        print(await websocket.recv())
        mensagens_texto = gerar_mensagens_texto()
        print(mensagens_texto)
        await websocket.send(mensagens_texto)


asyncio.get_event_loop().run_until_complete(websockets.serve(rodar_servidor, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

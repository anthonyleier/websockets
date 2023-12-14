import asyncio
import websockets

mensagens = []

clients = {}


async def servidor(websocket, caminho):
    identificacao = await websocket.recv()
    print(f'identificacao: {identificacao}')
    clients[identificacao] = websocket

    try:
        async for mensagem in websocket:
            print(f'mensagem: {mensagem}')
            destinatario, conteudo = mensagem.split(":")
            destinatario_socket = clients.get(destinatario)
            mensagens.append(mensagem)
            mensagens_texto = '\n'.join(mensagens)

            if destinatario_socket:
                await destinatario_socket.send(mensagens_texto)
    finally:
        del clients[identificacao]

asyncio.get_event_loop().run_until_complete(websockets.serve(servidor, 'localhost', 8765))
asyncio.get_event_loop().run_forever()

import asyncio
import websockets


async def cliente():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        identificador = input("Se identifique:")
        await websocket.send(identificador)

        while True:
            destinatario = input("Digite o identificador do destinatário: ")
            conteudo = input("Digite a mensagem: ")
            mensagem = f"{destinatario}:{conteudo}"

            await websocket.send(mensagem)

            resposta = await websocket.recv()
            print(f"Resposta: {resposta}")


asyncio.get_event_loop().run_until_complete(cliente())

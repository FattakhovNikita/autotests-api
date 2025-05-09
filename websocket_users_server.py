import asyncio
import websockets

from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение {message}")

        for _ in range(5):
            response = f"{_ + 1} Сообщение пользователя: {message}"
            await websocket.send(response)


async def asyncserver():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(asyncserver())

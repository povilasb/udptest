from typing import Tuple

from curio import socket
import curio


class Server:
    def __init__(self, port: int) -> None:
        self._port = port
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._tasks = curio.Queue()

    async def run(self) -> None:
        self._sock.bind(('0.0.0.0', self._port))
        await curio.spawn(join_tasks, self._tasks)

        async with self._sock:
            while True:
                data, addr = await self._sock.recvfrom(4096)
                await self._on_data(data, addr)

    async def _on_data(self, data: bytes, addr: Tuple[str, int]) -> None:
        task = await curio.spawn(self._sock.sendto, b'response', addr)
        await self._tasks.put(task)


async def join_tasks(tasks: curio.Queue) -> None:
    while True:
        t = await tasks.get()
        await t.join()


def main() -> None:
    server = Server(3000)
    curio.run(server.run)


main()

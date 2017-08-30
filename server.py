from curio import socket
import curio


async def run_server() -> None:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind(('0.0.0.0', 3000))

    tasks = curio.Queue()
    await curio.spawn(join_tasks, tasks)

    async with server_sock:
        while True:
            data, addr = await server_sock.recvfrom(4096)

            task = await curio.spawn(server_sock.sendto, b'response', addr)
            await tasks.put(task)


async def join_tasks(tasks: curio.Queue) -> None:
    while True:
        t = await tasks.get()
        await t.join()


def main() -> None:
    curio.run(run_server)


main()

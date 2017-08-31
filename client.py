import random
import string
import struct
from typing import Tuple

from curio import socket
import curio


def main():
    target = ('127.0.0.1', 3000)
    packet_count = 100
    timeout = 1  # seconds

    test = Test(target, packet_count, timeout)
    test.run()

    print('Packets sent:', packet_count)
    print('Packets received:', test.packets_received)


class Test:
    def __init__(self, target: Tuple[str, int], packet_count: int,
            timeout: int=3) -> None:
        self._target = target
        self._packet_count = packet_count
        self._timeout = timeout

        self.packets_received = 0

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._keep_running = True

    def run(self) -> None:
        curio.run(self._run_test)

    async def _run_test(self) -> None:
        recv_task = await curio.spawn(self._recv_packets)
        await self._send_packets()
        print('All packets sent')
        await curio.sleep(self._timeout)
        await recv_task.cancel()

    async def _send_packets(self) -> None:
        for nr in range(self._packet_count):
            await self._sock.sendto(make_packet(nr, 1500), self._target,)

    async def _recv_packets(self) -> None:
        while self._keep_running:
            data, addr = await self._sock.recvfrom(4096)
            print('Received:', data)
            self.packets_received += 1
            if self.packets_received >= self._packet_count:
                self._keep_running = False


def make_packet(id_: int, size: int) -> bytes:
    return struct.pack('!H', id_) + \
        ''.join(random.choice(string.ascii_lowercase) for i in range(size - 2))\
            .encode('ascii')


main()

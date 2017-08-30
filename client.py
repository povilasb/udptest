import socket
import random
import string
import struct
from threading import Thread
from typing import Tuple
import time


def main():
    target = ('127.0.0.1', 3000)
    packet_count = 100
    wait_for_response = 3  # seconds

    test = Test(target, packet_count)
    test.run()

    print('Packets sent:', packet_count)
    print(f'Sleep for {wait_for_response} seconds')
    time.sleep(wait_for_response)
    print('Packets received:', test.packets_received)


class Test:
    def __init__(self, target: Tuple[str, int], packet_count: int) -> None:
        self._target = target
        self._packet_count = packet_count

        self.packets_received = 0

        self._server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._recv_thread = Thread(target=self._recv_packets)

    def __del__(self) -> None:
        self._server_sock.close()

    def run(self) -> None:
        self._recv_thread.start()
        for nr in range(self._packet_count):
            self._server_sock.sendto(
                make_packet(nr, 1500),
                self._target,
            )

    def _recv_packets(self) -> None:
        while True:
            data, addr = self._server_sock.recvfrom(4096)
            print(data)
            self.packets_received += 1


def make_packet(id_: int, size: int) -> bytes:
    return struct.pack('!H', id_) + \
        ''.join(random.choice(string.ascii_lowercase) for i in range(size - 2))\
            .encode('ascii')


main()

=====
About
=====

.. image:: https://travis-ci.org/povilasb/udptest.svg?branch=master
    :target: https://travis-ci.org/povilasb/udptest

Small `UDP <https://en.wikipedia.org/wiki/User_Datagram_Protocol>`_ testing
tool written in Python and based on `curio <https://github.com/dabeaz/curio>`_
async library.

It's a combination of simple UDP server and client applications.

You can schedule multiple packets to be sent, get a response and measure
how many packets made the round trip.

Server
======

::

    Usage: server.py [OPTIONS]

    Options:
      -p, --port INTEGER  UDP port to listen for incomming requests.
      --help              Show this message and exit.

Client
======

::

    Usage: client.py [OPTIONS]

    Options:
      -h, --host TEXT             Target address.
      -p, --port INTEGER          UDP port to listen for incomming requests.
      -c, --packet-count INTEGER  Number of packets to send.
      --recv-timeout INTEGER      Timeout after N seconds of waiting for
                                  responses.
      --help                      Show this message and exit.

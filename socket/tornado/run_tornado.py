from functools import partial
import socket
import errno
from tornado import iostream
from tornado.ioloop import IOLoop


def connection_ready(sock, fd, events):
    while True:
        try:
            connection, address = sock.accept()
        except socket.error, e:
            if e[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
                raise
            return

        connection.setblocking(0)
        stream = iostream.IOStream(connection)
        stream.write(
            "HTTP/1.0 200 OK\r\nContent-Length: 9\r\n\r\nPingPong!\r\n",
            stream.close
        )


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    sock.bind(("localhost", 8080))
    sock.listen(5000)

    io_loop = IOLoop.instance()
    callback = partial(connection_ready, sock)
    io_loop.add_handler(sock.fileno(), callback, io_loop.READ)

    try:
        print 'Starting server...'
        io_loop.start()
    except KeyboardInterrupt:
        print 'Exiting...'
        io_loop.stop()
        print 'Exited.'
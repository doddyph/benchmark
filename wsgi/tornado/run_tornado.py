from pong import application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer


def main():
    container = WSGIContainer(application)
    http_server = HTTPServer(container)
    http_server.listen(8080)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
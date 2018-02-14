import lxml as lxml
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.soap import Soap11


class Fibonacci(ServiceBase):
    @srpc(Integer,_returns=Iterable(Integer))
    def fib(n):
        final = []
        a, b = 0, 1
        final.append(a)
        final.append(b)
        for i in range(n - 2):
            a, b = b, a + b
            final.append(a)
        return final

if __name__=='__main__':
    app = Application([Fibonacci], 'spyne.examples.hello.http',
                      in_protocol=Soap11(validator='lxml'),
                      out_protocol=Soap11(),
                      )
    wsgi_app = WsgiApplication(app)
    server = make_server('127.0.0.1', 7859, wsgi_app)

    print("server: http://127.0.0.1:7859")
    print("wsdl: http://localhost:7859/?wsdl")

    server.serve_forever()
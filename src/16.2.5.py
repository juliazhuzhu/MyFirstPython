from twisted.internet import protocol
from twisted.internet import reactor
from time import ctime

port = 19876

class MyProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.transport.getPeer().host
        print('客户端',client,'已经连接')
    
    def dataReceived(self, data):
        self.transport.write(ctime().encode(encoding='utf-8')+b' ' +data)

factory = protocol.Factory()
factory.protocol = MyProtocol
print('正在等待客户连接')
reactor.listenTCP(port,factory)
reactor.run()

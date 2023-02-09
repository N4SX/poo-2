import socket, threading

class ClientThread(threading.Thread):

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.name = ''
        print('Nova conexão: {}'.format(clientAddress))

    def run(self):
        self.name = self.csocket.recv(1024).decode()
        print(self.name, 'se conectou')
        msg = ''
        while(True):
            data = self.csocket.recv(1024)
            msg = data.decode()
            if msg == 'bye':
                break
            print('from', self.name+': ', msg)
            self.csocket.send(msg.encode())
        print('Client at', clientAddress, 'Desconectado')

if __name__ == '__main__':

    LOCALHOST = ''
    PORT = 7003
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((LOCALHOST, PORT))
    print('Servidor iniciado')
    print('Aguardando nova conexão')
    while(True):
        server.listen(1)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()
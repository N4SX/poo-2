import socket
host = 'localhost'
port = 8006
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''Definindo portas e ips'''
serv_socket.bind(addr)
'''Definindo o limite da conexão'''
serv_socket.listen(10)
print('Aguardando conexão')
'''Servidor aguardando conexão'''
con, cliente = serv_socket.accept()
print('Conectado')
print('Aguardando mensagem')

while(True):
    try:
        '''Definindo pacotes recebidos são até 1024bytes'''
        recebe = con.recv(1024)
        print('Mensagem recebida:'+recebe.decode())
        enviar = input('Digite uma mensagem a ser enviada ao cliente: ')
        con.send(enviar.enconde())

    except:
        serv_socket.close()
        break    
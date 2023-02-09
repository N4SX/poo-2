import socket
ip = '10.180.47.52'
port = 5003
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)


while(True):
    try:

        mensagem = input('Digite a mensagem a ser enviada: ')
        client_socket.send(mensagem.encode())
        print('mensagem enviada')
        #print('mensagem enviada: '+client_socket.recv(1024).decode())

    except:
        client_socket.close()
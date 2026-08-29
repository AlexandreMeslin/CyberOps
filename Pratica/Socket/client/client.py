'''
Cliente de socket simples.
Este cliente deve ser executado em uma rede Docker.

:Author: Alexandre Meslin
:Date: 2026-08-29
'''

# ---------------------------------------------------------------------------
# Módulos
# ---------------------------------------------------------------------------
import socket

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
SERVER_HOST = "server"
SERVER_PORT = 5000

def create_socket():
    '''
    Cria um socket TCP/IP para o cliente.
    Retorna o socket criado.

    :return: socket do cliente
    '''
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def connect(client_socket):
    '''
    Conecta o socket do cliente ao servidor.

    :param client_socket: socket do cliente
    :return: None
    '''
    print(f"Conectando ao servidor {SERVER_HOST}:{SERVER_PORT}...")
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Conectado ao servidor.")
    return

def sendall(client_socket):
    '''
    Envia mensagens para o servidor e recebe respostas.

    :param client_socket: socket do cliente
    :return: None
    '''
    while True:
        mensagem = input("Cliente: ")
        if mensagem.lower() == "sair":
            break
        client_socket.sendall(mensagem.encode())
        data = client_socket.recv(1024)
        print(f"Servidor: {data.decode()}")
    return

def close(client_socket):
    '''
    Fecha o socket do cliente.

    :param client_socket: socket do cliente
    :return: None
    '''
    client_socket.close()
    print("Conexão encerrada.")
    return

def main():
    client_socket = create_socket()
    connect(client_socket)
    sendall(client_socket)
    close(client_socket)
    return
    

if __name__ == "__main__":
    main()

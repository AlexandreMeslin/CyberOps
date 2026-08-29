'''
Servidor de socket simples.
Este servidor deve ser executado em uma rede Docker.

:Author: Alexandre Meslin
:Date: 2026-08-29
'''

# ----------------------------------------------------------------------------
# Módulos
# ---------------------------------------------------------------------------
import socket

# ----------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
HOST = "0.0.0.0"
PORT = 5000

def create_socket():
    '''
    Cria um socket TCP/IP para o servidor.
    Retorna o socket criado.

    :return: socket do servidor
    '''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return server_socket

def bind(server_socket):
    '''
    Associa o socket do servidor a um endereço e porta específicos.

    :param server_socket: socket do servidor
    :return: None
    '''
    server_socket.bind((HOST, PORT))
    return

def listen(server_socket):
    '''
    Coloca o socket do servidor em modo de escuta para conexões.

    :param server_socket: socket do servidor
    :return: None
    '''
    server_socket.listen(1)
    return

def accept(server_socket):
    '''
    Aceita uma conexão de um cliente.

    :param server_socket: socket do servidor
    :return: tupla com a conexão e o endereço do cliente
    '''
    print(f"Servidor aguardando conexão na porta {PORT}...")
    conn, addr = server_socket.accept()
    return conn, addr

def recv(conn, addr):
    '''
    Recebe mensagens do cliente e envia respostas.

    :param conn: conexão com o cliente
    :param addr: endereço do cliente
    :return: None
    '''
    print(f"Cliente conectado: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensagem = data.decode()
        print(f"Cliente: {mensagem}")
        resposta = input("Servidor: ")
        conn.sendall(resposta.encode())
    return

def close(conn, server_socket):
    '''
    Fecha a conexão com o cliente e o socket do servidor.

    :param conn: conexão com o cliente
    :param server_socket: socket do servidor
    :return: None
    '''
    conn.close()
    server_socket.close()
    print("Conexão encerrada.")
    return

def main():
    '''
    Função principal do servidor.
    Cria o socket, associa, escuta, aceita conexões e recebe mensagens.
    '''
    server_socket = create_socket()
    bind(server_socket)
    listen(server_socket)
    conn, addr = accept(server_socket)
    recv(conn, addr)
    close(conn, server_socket)
    return

if __name__ == "__main__":
    main()

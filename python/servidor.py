import socket

HOST = "0.0.0.0"  # Escuta em todas as interfaces
PORT = 8000  # Porta do servidor

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"🚀 Servidor rodando em {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"🔗 Nova conexão de {addr}")
        conn.sendall(f"Olá, {addr}! Mensagem recebida com sucesso.".encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    start_server()

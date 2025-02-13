import socket
import threading
import time

# Função para criar e conectar um cliente
def client_task(id):
    try:
        print(f"🎯 Cliente {id} tentando conectar...")  # Debug
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5)  # Timeout de 5s para evitar travamentos
        client.connect(("127.0.0.1", 8000))  # Certifique-se de que a porta é a correta
        print(f"✅ Cliente {id} conectado!")

        message = f"Cliente {id} diz oi!"
        client.send(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        print(f"💬 Cliente {id} recebeu: {response}")

        client.close()
    except Exception as e:
        print(f"❌ Erro no cliente {id}: {e}")

# Função para rodar N clientes ao mesmo tempo
def run_clients(n):
    print(f"\n🔥 Rodando {n} clientes simultaneamente...")
    threads = []
    for i in range(n):
        thread = threading.Thread(target=client_task, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Espera todos os clientes terminarem

# Testando os diferentes números de clientes
for num_clients in [1, 2, 5, 10]:
    run_clients(num_clients)
    time.sleep(2)  # Pequeno intervalo entre testes

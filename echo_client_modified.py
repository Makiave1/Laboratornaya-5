import socket

HOST = 'localhost'  # Адрес сервера
PORT = 12345        # Порт сервера

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print("Соединение с сервером...")
        client_socket.connect((HOST, PORT))
        print("Соединение установлено.")

        while True:
            message = input("Введите строку для отправки (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                client_socket.sendall(message.encode())
                print("Отправка команды 'exit'. Завершение работы клиента.")
                break
            
            client_socket.sendall(message.encode())
            print(f"Отправка данных серверу: {message}")

            data = client_socket.recv(1024)
            print(f"Прием данных от сервера: {data.decode()}")

        print("Разрыв соединения с сервером...")

if __name__ == "__main__":
    run_client()

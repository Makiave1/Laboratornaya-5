import socket

HOST = '0.0.0.0'  # Привязка к всем доступным интерфейсам
PORT = 12345       # Порт сервера

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print("Сервер запущен.")
        server_socket.listen()
        print(f"Начало прослушивания порта {PORT}...")

        while True:
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Подключение клиента: {addr}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    
                    message = data.decode()
                    print(f"Прием данных от клиента: {message}")

                    # Проверка на команду "exit"
                    if message.lower() == 'exit':
                        print("Клиент запросил завершение соединения.")
                        break

                    # Отправка данных обратно клиенту
                    client_socket.sendall(data)
                    print(f"Отправка данных клиенту: {message}")

                print(f"Отключение клиента: {addr}")

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")

#Лабораторная работа №5 Жидков А. В. ДПИ22-1
#TCP- Сервер
class TCPServer:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        import socket
        import threading

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Сервер запущен. Ожидание подключения...")

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"Подключен клиент: {addr}")
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler.start()
        except KeyboardInterrupt:
            print("Остановка сервера.")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket):
        print("Подключение клиента установлено.")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"Прием данных от клиента: {message}")

                if message.lower() == "exit":
                    print("Клиент завершил соединение.")
                    break

                client_socket.sendall(data)  # Эхо-ответ
                print(f"Отправка данных клиенту: {message}")
        finally:
            client_socket.close()
            print("Отключение клиента.")

if __name__ == "__main__":
    server = TCPServer()
    server.start()

#Лабораторная работа №5 Жидков А. В. ДПИ22-1
#TCP-Клиент
class TCPClient:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        import socket

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.port))
            print("Соединение с сервером установлено.")

            while True:
                message = input("Введите строку для отправки (или 'exit' для выхода): ")
                self.client_socket.sendall(message.encode())
                print(f"Отправка данных серверу: {message}")

                if message.lower() == 'exit':
                    break

                response = self.client_socket.recv(1024)
                print(f"Прием данных от сервера: {response.decode()}")
        finally:
            self.client_socket.close()
            print("Разрыв соединения с сервером.")

if __name__ == "__main__":
    client = TCPClient()
    client.start()

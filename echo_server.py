#Лабораторная работа №5
# Жидков А. В.
# ДПИ22-1
# Код сервера
import socket

HOST = 'localhost'  # Адрес сервера
PORT = 12345        # Порт сервера

def run_server():
    # Создание TCP-сокета
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print("Сервер запущен.")
        server_socket.listen()
        print(f"Начало прослушивания порта {PORT}...")

        while True:
            # Ожидание подключения клиента
            client_socket, addr = server_socket.accept()
            with client_socket:
                print(f"Подключение клиента: {addr}")
                while True:
                    # Прием данных от клиента
                    data = client_socket.recv(1024)  # Чтение порцией 1 КБ
                    if not data:
                        break  # Если данных нет, выходим из цикла
                    print(f"Прием данных от клиента: {data.decode()}")
                    
                    # Отправка данных обратно клиенту
                    client_socket.sendall(data)
                    print(f"Отправка данных клиенту: {data.decode()}")

                print(f"Отключение клиента: {addr}")

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")

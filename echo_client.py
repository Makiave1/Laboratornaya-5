#Лабораторная работа №5
# Жидков А. В.
# ДПИ22-1
# Код клиента
import socket

HOST = 'localhost'  # Адрес сервера
PORT = 12345        # Порт сервера

def run_client():
    # Создание TCP-сокета
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        print("Соединение с сервером...")
        client_socket.connect((HOST, PORT))
        print("Соединение установлено.")

        while True:
            # Считывание строки с ввода
            message = input("Введите строку для отправки (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break
            
            # Отправка данных серверу
            client_socket.sendall(message.encode())
            print(f"Отправка данных серверу: {message}")

            # Прием данных от сервера
            data = client_socket.recv(1024)  # Чтение порцией 1 КБ
            print(f"Прием данных от сервера: {data.decode()}")

        print("Разрыв соединения с сервером...")

if __name__ == "__main__":
    run_client()

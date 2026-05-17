import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print('\nПолучено:', data.decode('utf-8'))
        except:
            break

def send_messages(client_socket):
    while True:
        print("Для выхода q")
        message = input('Введите сообщение: ')
        if message == "q":
            client_socket.send(message.encode('utf-8'))
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))
        
    

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5001))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_messages(client_socket)
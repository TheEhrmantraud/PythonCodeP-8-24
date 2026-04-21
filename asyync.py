# import time
# print('nachalo 1 proctssa')
# time.sleep(3)
# print('nachalo 2 proctssa')


# import requests
# import time
# print('Начинаю скачивать 1 картинку')
# requests1=requests.get('https://i.pinimg.com/736x/ee/e0/2e/eee02efa9b39a1655c1587e7b19445c2.jpg')
# print("1 картинка скачалась")
# print('Начинаю скачивать 2 картинку')
# requests2=requests.get('https://i.pinimg.com/736x/ee/e0/2e/eee02efa9b39a1655c1587e7b19445c2.jpg')
# print("2 картинка скачалась")
# print('Гтово')




# import asyncio

# async def say_hello():
#     print('Привет')
#     await asyncio.sleep(1)
#     print("Мир")
    
# async def main(): #Запускается 2 процесса и работают одновременно
#     task1=asyncio.create_task(say_hello())
#     task2=asyncio.create_task(say_hello())
    
#     await task1
#     await task2
# asyncio.run(main())


# import requests
import asyncio
import time

# import aiohttp

# async def download_image(session, url, name):
#     print(f'Начали загпружать картинку {url}')
#     async with session.get(url) as responce:
#         image=await responce.read()
#         print(f'Картинка скачаалась {name}')
#         return image
    
# async def main():
#     async with aiohttp.ClientSession() as session:
#         task1=download_image(session,'https://i.pinimg.com/736x/ee/e0/2e/eee02efa9b39a1655c1587e7b19445c2.jpg', "Картинка1")
#         task2=download_image(session, 'https://i.pinimg.com/736x/ee/e0/2e/eee02efa9b39a1655c1587e7b19445c2.jpg', 'Картинка2')
#         task3=download_image(session, 'https://i.pinimg.com/736x/ee/e0/2e/eee02efa9b39a1655c1587e7b19445c2.jpg', "Картинка3")
        
#         await asyncio.gather(task1, task2, task3)
# asyncio.run(main())



#Поток - одна линия выполнения процессов.
# Многопоточность - использование неск линий для 1 задачи
# Асинхронность - метод для работы над задачей
import threading

# def worker():
#     print('Поток начал')
#     time.sleep(3)
#     print("ПОток остановился")
    
# print("Главная программа: создаем поток")

# t=threading.Thread(target=worker)
# print("Запускается поток")
# t.start()
# print("Ожидание завершения")
# t.join()
# print("Завершилось")

# # Первый поток - worker
# # Второй поток - t=threading.Thread(target=worker)

# def cook_eggs():
#     print("НАчали варить яйки")
#     time.sleep(2)
#     print("Закончили варить яйки")
# def make_coffee():
#     print("НАчали варить кофе")
#     time.sleep(2)
#     print("Закончили варить кофе")


# t1=threading.Thread(target=cook_eggs)
# t2=threading.Thread(target=make_coffee)
# t1.start
# t2.start

# t1.join
# t2.join


#Где не нужен поток
# def count():
#     count=0
#     for i in range(20_000_000):
#         count+=i
# start=time.time()
# count()
# end=time.time()
# print("Один поток", round(end-start,2),"Сек")


# def download(name):
#     print(f"Начали загрузку {name}")
#     time.sleep(3)
#     print(f"ЗАкончили загрузку")
    
# start = time.time()
# threads =[]
# for i in range(5):
#     t = threading.Thread(target=download, args=(f'файл_{i}',))
#     t.start()
#     threads.append(i)
# for i in threads:
#     t.join()
    
# end = time.time()
# print("Всего времени затрачено", round(end-start, 2), "сек")






# lock = threading.Lock()
# counter=0
# def f():
#     global counter
#     for i in range(10000):
#         with lock:
#             counter+=i
# t1=threading.Thread(target=f)
# t2=threading.Thread(target=f)

# t1.start()
# t2.start()

# t1.join()
# t2.join()











import socket
import threading

clients = []
client_lock = threading.Lock()


def listt(message, sender=None):
    with client_lock:
        for client in clients:
            if client != sender:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    clients.remove(client)



def handle_client(client_socket, client_address):
    print(f"Клиент {client_address} подключен")
    listt(f"Пользователь {client_address} вошел в чат", client_socket)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode("utf-8")

        if message == "q":
            with client_lock:
                if client_socket in clients:
                    clients.remove(client_socket)

            print(f"Клиент отключился {client_address} (общий канал)")
            listt(f"Пользователь {client_address} вышел из чата (широковещалка)")

            client_socket.close()
            break

        print(f"{client_address}: {message} (общий канал)")
        listt(f"{client_address}: {message} (широковещалка)", client_socket)
        
    with client_lock:
        if client_socket in clients:
            clients.remove(client_socket)
            
    client_socket.close()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5001))
server.listen()

print("Сервер ждет подключения")

while True:
    client_socket, client_address = server.accept()
    with client_lock:
        clients.append(client_socket)

    client_socket.send(f"Привет {client_address} (админка)".encode("utf-8"))

    thread = threading.Thread(target=handle_client,args=(client_socket, client_address),daemon=True)
    thread.start()
# from queue import Queue
# import requests
# import threading
# from concurrent. futures import ThreadPoolExecutor
# import time

# url=[
#     "https://edu.1cfresh.com/a/edu_erp_actual/1473240/ru_RU/",
#     "https://edu.1cfresh.com/a/edu_erp_actual/1473240/ru_RU/"
# ]

# def proisv(url):
#     responce=requests.get(url)
#     return f"{url}: {len(responce.content)} bytes"

# start=time.time()

# with ThreadPoolExecutor(max_workers=4) as exector:
#     results=exector.map(proisv, url)

# for result in results:
#     print(result)

# print(f"Затраченное время {time. time()-start :.2f} сek")




# def count(n):
#     while n>0:
#         n=-1

# start= time.time()

# threrds=[threading.Thread(target=count, args=(50_000_000,)) for _ in range(4)]

# for t in threrds:
#     t.start()

# for t in threrds:
#     t.join()

# print(f"noTOKn {time.time()-start}")


# import time
# start=time.time()
# count(200_000_000)
# print(f"один поток {time.time()-start}")


# import multiprocessing
# import os

# def worker(a):
#     print(f"Привет от процесса: {a}, PID={os.getpid()}")
    
# if __name__=="__main__":
#     p=multiprocessing.Process(target=worker, args=("Иван",))
#     p.start()
#     p.join()


from multiprocessing import Process, Queue
def worker(q):
    q.put([42,"hhhhd",None])
def main():
    q=Queue(maxsize=10)
    p=Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()


if __name__ =="__main__":
    main()
    
    
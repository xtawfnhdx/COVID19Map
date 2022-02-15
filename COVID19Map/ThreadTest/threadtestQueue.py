import threading
import requests
import time
import queue
import  random

urls = [
    f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)
]


def single_fun():
    for url in urls:
        craw(url)


def multi_fun():
    thread = []
    for url in urls:
        thread.append(threading.Thread(target=craw, args=(url,)))
    for t in thread:
        t.start()
    for t in thread:
        t.join()


def do_craw(createQueue: queue.Queue, htmlQueue: queue.Queue):
    while True:
        url = createQueue.get()
        r = requests.get(url)
        htmlQueue.put(r.text)
        print(f"docraw: createQueue.size {createQueue.qsize()},thread id is {threading.current_thread().name}")
        time.sleep(random.randint(1, 2))


def exe_craw(htmlQueue: queue.Queue):
    while True:
        html = htmlQueue.get()
        print(f"exe_craw: htmlQueue.size {htmlQueue.qsize()},thread id is {threading.current_thread().name}")
        time.sleep(random.randint(1, 2))


def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


if __name__ == "__main__":
    # strat=time.time()
    # print("start single fun")
    # single_fun()
    # end=time.time()
    # print(f"end single fun. execute {end-strat} seconds")
    #
    # strat=time.time()
    # print("start multi fun")
    # multi_fun()
    # end=time.time()
    # print(f"end multi fun. execute {end-strat} seconds")

    createQueue = queue.Queue()
    htmlQueue = queue.Queue()
    for url in urls:
        createQueue.put(url)
    for inx in range(3):
        t = threading.Thread(target=do_craw, args=(createQueue, htmlQueue), name=f"do {inx}")
        t.start()
    for i in range(2):
        t = threading.Thread(target=exe_craw, args=(htmlQueue,), name=f"parse {i}")
        t.start()

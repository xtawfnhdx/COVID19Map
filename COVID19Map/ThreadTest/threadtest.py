import threading
import requests
import time

urls = [
    f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)
]

def single_fun():
    for url in urls:
        craw(url)

def multi_fun():
    thread=[]
    for url in urls:
        thread.append(threading.Thread(target=craw,args=(url,)))
    for t in thread:
        t.start()
    for t in thread:
        t.join()




def craw(url):
    r = requests.get(url)
    print(url, len(r.text))




if __name__ == "__main__":
    strat=time.time()
    print("start single fun")
    single_fun()
    end=time.time()
    print(f"end single fun. execute {end-strat} seconds")

    strat=time.time()
    print("start multi fun")
    multi_fun()
    end=time.time()
    print(f"end multi fun. execute {end-strat} seconds")



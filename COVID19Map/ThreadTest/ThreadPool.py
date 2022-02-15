from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

pool = ThreadPoolExecutor()
urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


def ThreadPoolTest():
    with pool:
        results = pool.map(Craw, urls)
        for res in results:
            print(res)
    with ThreadPoolExecutor() as po:
        features = [po.submit(Craw, url) for url in urls]
        for fe in features:
            print(fe.result())
        for fu in as_completed(features):
            print((fe.result()))


def Craw(url):
    r = requests.get(url)
    print(url, len(r.text))


if __name__ == "__main__":
    ThreadPoolTest()

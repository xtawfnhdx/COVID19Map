import threading
import time

lockabc = threading.Lock()


class Cir(object):
    def __init__(self, acount):
        self.acount = acount


def declare(acount: Cir, nums):
    with lockabc:
        if acount.acount > nums:
            time.sleep(0.1)
            acount.acount -= nums
            print(f"扣减成功,扣减以后为{acount.acount}")
        else:
            print(f"扣减失败")


if __name__ == "__main__":
    cir = Cir(1000)

    t1 = threading.Thread(name="t1", target=declare, args=(cir, 800))
    t2 = threading.Thread(name="t2", target=declare, args=(cir, 800))

    t1.start()
    t2.start()

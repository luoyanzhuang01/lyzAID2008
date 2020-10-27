from multiprocessing import Process
from time import sleep
from signal import *

def worker():
    for i in range(3):
        sleep(2)
        print("I'm Levi")
        print("I'm working")

# 忽略子进程退出
signal(SIGCHLD,SIG_IGN)
p = Process(target=worker)
p.start()
# p.join()
while True:
    pass
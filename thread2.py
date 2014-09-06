import time,threading
# 假定这是你的银行存款:
balance=0
lock=threading.Lock()
def changeIt(n):
    # 先存后取，结果应该为0:
    global balance
    balance=balance+n
    balance=balance-n

def runThread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            changeIt(n)
        finally:
            lock.release()
        
t1=threading.Thread(target=runThread,args=(8,))
t2=threading.Thread(target=runThread,args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
import threading
# 创建全局ThreadLocal对象:
localSrudent=threading.local()

def processStudent():
    print 'Hello, %s (in %s)' % (localSrudent.student, threading.current_thread().name)
    
def processThread(name):
    # 绑定ThreadLocal的student:
    localSrudent.student=name
    processStudent()
    
t1 = threading.Thread(target= processThread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= processThread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

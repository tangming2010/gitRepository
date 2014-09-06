from multiprocessing import Pool
import os,time,random

def runTaskByTime(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start=time.time()
    time.sleep(random.random()*30)
    end=time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(10):
        p.apply_async(runTaskByTime,args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    
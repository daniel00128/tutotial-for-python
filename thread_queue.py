#python vession 3.6
#測試thread +queue
#author:daneil

import threading
from  queue import Queue

class DoRun(threading.Thread):
    def __init__(self,aQueue):
        threading.Thread.__init__(self)
        self.m_Queue=aQueue
    
    def run(self):
        #取回Queue內容(item)
        while not self.m_Queue.empty():
            ip=self.m_Queue.get()
            print(ip)
def main():
    threads=[]
    thread_count=10
    #建立Queue
    m_Queue=Queue(255)
    #新增Queue(先進先出)
    for i in range(255):
        s='192.168.24.'+str(i)
        m_Queue.put(s)
    #建立執行緒
    for i in range(thread_count):
        threads.append(DoRun(m_Queue))
    #啟動執行緒
    for i in range(thread_count):
        threads[i].start()
    for i in range(thread_count):
        threads[i].join()
if "__main__" == __name__:
    main()

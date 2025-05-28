#=====================================================
# 이중 연결 리스트를 이용하여 큐(queue)을 구현하기
#=====================================================
from DList import *

class QueueUnderFlow(Exception):
    pass

class Queue(DList):
    def add(self, value):
        self.append(value)

    def remove(self):
        if self.isEmpty():
            raise QueueUnderFlow("Queue is Empty!!")
        else:
            returnValue = self.head.data
            super().remove(self.head)
            return returnValue
        
            





# queue = Queue()

# queue.add(100)
# queue.add(200)

# print(queue.remove())

from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,value):
        self.value=value
        self.queue.appendleft(value)
    def dequeue(self):
        self.queue.pop()
    def is_empty(self):
        return (len(self.queue)==0)
    def size(self):
        return len(self.queue)
    def display(self):
        return self.queue
    def peek(self):
        print('fist element is:',self.queue[-1])
        print('last element is:',self.queue[0])
        return self.queue[-1],self.queue[0]
que=Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
print('Queue:',que.display())
que.dequeue()
print('Queue after dequeue:',que.display())
print("size of queue is:",que.size())
(que.peek())

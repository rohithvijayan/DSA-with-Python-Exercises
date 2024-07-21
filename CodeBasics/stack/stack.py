from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    def pop(self):
        return self.stack.pop()
    def push(self,value):
        self.stack.append(value)
    def peek(self):
        print(self.stack[-1])
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
stack1=Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.peek()
print(stack1.is_empty())
print(stack1.size())
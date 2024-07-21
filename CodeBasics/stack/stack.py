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
    def display(self):
        return self.stack
    def rev(self):
        return self.stack.reverse()
    def reverse_string(self,word):    
        self.word=word
        word_list=word.split(sep=" ")
        for item in word_list:
            stack1.push(item)

        print("\nStack :",stack1.display())

        stack1.rev()
        revstack=(stack1.display())
        for i in revstack:
            print(i[::-1],end=" ")
        
stack1=Stack()
word=input("\nenter a sentence or word:")
stack1.reverse_string(word)
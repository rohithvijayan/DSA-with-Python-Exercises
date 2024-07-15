class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def empty(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    def pop(self):
        if self.head is None:
            return None
        elif(self.head.next is None):
            self.head=None
            self.tail=None
            self.length=0
        else:
            temp=self.head
            pre=self.head
            while temp.next is not None:
                pre=temp
                temp=temp.next
            self.tail=pre 
            self.tail.next=None
            self.length-=1
                
                    
my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
        
    
my_linked_list.pop()
print("AFTER POPPING 2")
my_linked_list.print_list()
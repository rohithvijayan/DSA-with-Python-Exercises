class Node:
    def __init__(self,value,prev,next):
        self.value=value
        self.prev=prev
        self.next=next
class Dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_end(self,value):
        if self.head is None and self.tail is None:
            new_node=Node(value,self.tail,None)
            self.head=new_node
            self.tail=new_node
        elif self.head==self.tail:
            new_node=Node(value,self.tail,None)
            self.tail.next=new_node
            self.tail=new_node
        else:
            new_node=Node(value,self.tail,None)
            self.tail.next=new_node
            self.tail=new_node
            
    def print_forward(self):
        if self.head is None:
            print("emtpy dll")
        else:
            print("\nDLL In Forward:")
            temp=self.head
            while temp:
                print(str(temp.value)+"-->",end="")
                temp=temp.next
    def print_backward(self):
        if self.tail is None:
            print("Empty DLL")
        else:
            temp=self.tail
            print("\nDLL In Backwards:")
            while temp:
                print(str(temp.value)+"-->",end="")
                temp=temp.prev
                
ll=Dll()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)
ll.print_forward()
print("\n")
ll.print_backward()
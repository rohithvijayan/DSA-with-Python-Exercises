class Node:
     def __init__(self,value,next):
         self.value=value
         self.next=next
class LL:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print("Empty LL")
            return
        else:
            temp=self.head
            while temp is not None:
                print(temp.value,"--->",end="")
                temp=temp.next
            print()
    def insert_start(self,value):
        node=Node(value,self.head)
        self.head=node
    def remove_start(self):
        if self.head is None:
            print("empty list nothing to remove")
            return
        else:
            temp=self.head
            self.head=temp.next
    def insert_end(self,value):
        if self.head is None:
            self.head=Node(value,None)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=Node(value,None)
    def remove_index(self,index):
        if index<0 or index>=self.length_ll():
            print("\nInvalid Index")
            return
        elif index==0:
            self.remove_start()
            return
        else:
            count=0
            temp=self.head
            while temp:
                if count==index-1:
                    temp.next=temp.next.next
                    return
            temp=temp.next
                
    def insert_at(self,value,index):
        if index<0 or index>=self.length_ll():
            print("\niNVALID index")
            return
        elif index==0:
            self.insert_start(value)
            return
        else:
            temp=self.head
            count=0
            while temp:
                if count==index-1:
                    new_node=Node(value,temp.next)
                    temp.next=new_node
                temp=temp.next
                count+=1
            return
            
                   
    def length_ll(self):
        length=0
        temp=self.head
        while temp is not None:
            length+=1
            temp=temp.next
        return length

ll=LL()
ll.insert_start(1)
ll.insert_start(2)
ll.insert_start(3)
ll.printll()
ll.remove_start()
print("\nafter removal of start element:")
ll.printll()
ll.remove_start()
print("\nafter removal of start element:")
ll.printll()
print("\n after inserting 4 at end")
ll.insert_end(4)
ll.printll()
print("\n after inserting 5 at end")
ll.insert_end(5)
ll.printll()
ll.remove_index(1)
print("\nafter removing element at index 1:")
ll.printll()
ll.insert_at(3,1)
print("\nafter inserting 3 at index 1:")
ll.printll()

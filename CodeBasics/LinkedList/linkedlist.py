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
    def remove_end(self):
        if self.head is None:
            print("\nEmpty LinkedList")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def insert_after(self,value,after_value):
        if self.head is None:
            print("\nEMpty LInkedLIst")
            return
        elif self.head.next is None:
            if self.head.value!=after_value:
                print("\nValue not found in LinkedList")
                return
            else:
                self.insert_end(value)
        else:
            temp=self.head
            while temp:
                if temp.value==after_value:
                    new_node=Node(value,temp.next)
                    temp.next=new_node
                temp=temp.next
    
    def remove_value(self,value):
        if self.head is None:
            print("\nEmpty LinkedLIst")
        elif self.head.next is None:
            if self.head.value==value:
                self.head=None
            else:
                print("\ninvalid value")
        else:
            temp=self.head
            prev=temp                
            while temp:
                if temp.value==value:
                    if temp is self.head:
                        self.head=temp.next
                        break
                    else:
                        prev.next=prev.next.next
                        print("\nValue removed:",value)
                        break
                prev=temp
                temp=temp.next
                    
                
                              
    def set_value(self,value,index):
        if index<0 or index>=self.length_ll():
            print("\nIndex Invalid")    
            return
        elif index==0:
            self.head.value=value
        else:
            count=0
            temp=self.head
            while temp:
                if count==index:
                    temp.value=value
                    print("\n value updated to:",value)
                    return
                temp=temp.next
                count+=1   
    def get_node(self,index):
        if index<0 or index>=self.length_ll():
            print("\nIndex Invalid")    
            return
        elif index==0:
            print(f"value of node at index:{index} is {self.head.value}")
            return
        else:
            count=0
            temp=self.head
            while temp:
                if count==index:
                    print(f"value of node at index:{index} is {temp.value}")
                    return
                temp=temp.next
                count+=1
                   
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
ll.get_node(2)
ll.set_value(7,2)
ll.printll()
ll.remove_end()
ll.printll()
ll.insert_after(4,3)
ll.printll()
ll.insert_after(5,4)
ll.printll()
print("\n after removing 1")
ll.remove_value(1)
ll.printll()
print("\n after removing 5")
ll.remove_value(5)
ll.printll()
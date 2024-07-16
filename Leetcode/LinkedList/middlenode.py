'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length=0
        temp=head
        while temp is not None:
            length+=1
            temp=temp.next
        if length%2==0:
            mid=length//2+1
        else:
            mid=(length//2)+1
        temp=head
        count=0
        while temp:
            count=count+1
            if count==mid:
                return temp
            temp=temp.next 
    
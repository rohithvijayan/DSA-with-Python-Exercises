'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # If we need to remove the head
        if n == length:
            temp=head
            head=temp.next
            return head
        
        # Find the node before the one we want to remove
        current = head
        for i in range(length - n - 1):
            current = current.next
        
        # Remove the nth node from the end
        current.next = current.next.next
        
        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        fake_head = ListNode(0)  #creat a dummy head node
        fake_head.next = head
        before = fake_head  #before refers to the last node before m
        for i in range(m-1):
            before = before.next
            
        reversed_tail = before.next  #the mth node will be the tail after reversing
        pre = None  #record the pre one before current
        cur = revered_tail   #record the current during move
        before.next = None   #the one next of m-1 is none for now
        for i in range(n-m+1):
            next = cur.next  #move to the next
            cur.next = pre   #change the link of current to the pre one
            pre = cur  #move pre to cur
            cur = next #move cur to next
            
        before.next = pre         #pre is the n node
        reversed_tail.next = cur  #cur is the n+1 node
        
        return fake_head.next
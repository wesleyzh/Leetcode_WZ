class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)  #dummy is created before head
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1 #add the smaller node to the next
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next #move current to next
            
        if l1:
            current.next = l1
        else:
            currnet.next = l2
                
        return dummy.next
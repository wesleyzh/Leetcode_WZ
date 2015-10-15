class Solution:
    def mergeKLists(self, lists):
        if lists == []: return 
        
        dummy = ListNode(0)
        current = dummy
        heap = []  #contains the sorted heal list
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
                
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
                
        return dummy.next
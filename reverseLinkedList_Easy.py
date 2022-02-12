# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#credit: NeetCode youtube channel

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #iterative approach with 2 pointers: T O(n), M O(1)
        '''
        prev, curr = None, head 
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
                
        return prev
        '''
        
        #recursive approach: T O(n), M O(n)
        if not head:
            return None
        
        newHead = head
        
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#credit: NeetCode Youtube channel


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        #find the middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        #reverse the second half of the linked list
        prev = None  
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
            
        #compare the reverse second half to the first half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            

            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        prev, slow, fast = dummy, head, head.next

        while fast:
            if fast.val != slow.val:
                if slow.next == fast:
                    prev.next = slow
                    prev = slow
                    slow = slow.next
                else:
                    slow = fast
            fast = fast.next

        if slow.next == None:
            prev.next= slow
        else:
            prev.next = None

        return dummy.next 
                

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        # Special case: the empty list or a single node list
        if not head or not head.next:
            return None
        # Locate the middle node index
        curr = head
        slow = head
        fast = head
        prev = None
        # 'fast' pointer moves twice as fast as the 'slow' 
        # so 'slow' pointer will be just 1 node over half way through the list when 'fast' reaches the final node
        # 'prev' node will be pointing the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Remove the middle node
        prev.next = prev.next.next
        
        return head
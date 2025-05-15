# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        max_sum = 0
        
        # Locate start of the second half of the list (the middle node)
        while fast:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second portion of linked list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        head_2 = prev # Head of 2nd portion of linked list

        # Find the max twin sum
        while head_2:
            max_sum = max(max_sum, head.val + head_2.val)
            head = head.next
            head_2 = head_2.next
        
        return max_sum

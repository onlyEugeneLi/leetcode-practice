# Solution: https://leetcode.com/problems/odd-even-linked-list/solutions/4761304/simple-beginner-friendly-dry-run-two-approach-full-explanation-time-o-n-space-o-1-gits

# from collections import 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Null or sinlge case
        if not head or not head.next: 
            return head
        odd = ListNode(0)
        odd_ptr = odd
        even = ListNode(0)
        even_ptr = even
        idx = 1

        while head:
            if idx % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            idx += 1
        
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next
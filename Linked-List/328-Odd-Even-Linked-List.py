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

        """
        Traverse list to change attribute [next]
        """

        # Base case: Null or sinlge case
        if not head or not head.next: 
            return head
        # Initialisation
        odd = ListNode(0) # Dummy odd head (temporary var)
        odd_ptr = odd # Set up odd pointer
        even = ListNode(0) # Dummy even head (temporary var)
        even_ptr = even # Set up even pointer
        idx = 1

        while head:
            if idx % 2 == 0: # Detect odd / even
                even_ptr.next = head
                even_ptr = even_ptr.next # Move pointer to the tail to prepare for new node
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next # Move pointer to the tail to prepare for new node
            head = head.next # Move on to next node in the Linked List
            idx += 1
        
        even_ptr.next = None # Set as the tail of the whole list
        odd_ptr.next = even.next # Connect Odd list and Even list
        return odd.next # Return head of list
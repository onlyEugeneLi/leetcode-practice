# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution_merge_sort:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empyt or single element linked list
        if head is None or head.next is None:
            return head
        
        # Split the list in half
        def split(node):
            slow = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            # When fast node reaches the end, slow points at the end of first half
            mid = slow.next # Mid node is the start of the second half
            slow.next = None # Break up the link
            return node, mid

        # Sort and merge 2 sections
        def merge_sort(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
            sorted_head = ListNode() # Instantiate an empty linked list to store sorted nodes
            curr_node = sorted_head # Set a pointer to traverse the list

            # Sorting
            while left and right:
                if left.val < right.val:
                    curr_node.next = left
                    left = left.next
                else:
                    curr_node.next = right
                    right = right.next
                # Increase index in the temporary sorted linked list
                curr_node = curr_node.next
            
            if left:
                curr_node.next = left
            else:
                curr_node.next = right
            
            return sorted_head.next
        
        # Main sortList()
        left, mid = split(head)
        left = self.sortList(left)
        mid = self.sortList(mid)

        # Key recurssive entry for the algorithm to work
        return merge_sort(left, mid)
    
'''Faster solution'''
class Solution_brute_force:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        li.sort()
        dummy=ListNode()
        current=dummy
        for val in li:
            current.next=ListNode(val)
            current=current.next
        return dummy.next
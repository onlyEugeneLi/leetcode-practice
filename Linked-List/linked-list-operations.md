# Linked List Common Operations

## Find the middle node

```
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
```

## Reverse second half of list (Reverse a sublist of linked list)

Reference:

1. [Geeksforgeeks - Reverse a sublist of linked list](https://www.geeksforgeeks.org/reverse-sublist-linked-list/)
1. [Geeksforgeeks - Reverse a linked list](https://www.geeksforgeeks.org/reverse-a-linked-list/)
1. [Leetcode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
1. [Leetcode 2130. Maximum Twin Sum of a LInked List Solution](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/solutions/1680417/c-python-mid-and-reverse-solution)

> **Tuple unpacking**
>
> Python [simultaneous assignment](https://stackoverflow.com/a/14836456/20601905) makes this swap viable. 
> `curr.next` on the right-hand side is always the original `curr.next`.
>even though curr.next is being modified, Python already saved its original value in memory during the evaluation of the right-hand side. That’s why we don’t need a separate temporary variable.

```
while curr:
    curr.next, prev, curr = prev, curr, curr.next
```
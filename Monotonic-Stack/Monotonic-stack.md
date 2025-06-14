[Introduction to Monotonic Stack - Data Structure and Algorithm Tutorials](https://www.geeksforgeeks.org/dsa/introduction-to-monotonic-stack-2/)

# Monotonic Increasing Stack

Elements are placed in increasing order from the bottom to the top. 

Each new element added to the stack is greater than or equal to the one below it. 

If a new element is smaller, we remove elements from the top of the stack until we find one that is smaller or equal to the new element, or until the stack is empty. 

This ensures that the stack always stays in increasing order.

```
def monotonicIncreasing(nums):
    stack = []
    result = []

    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is more than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element into the stack
        stack.append(num)

    # Construct the result array from the stack
    while stack:
        result.insert(0, stack.pop())

    return result

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicIncreasing(nums)
print("Monotonic increasing stack:", result)

# Console Output:
# Monotonic increasing stack: 1 1 2 6
```



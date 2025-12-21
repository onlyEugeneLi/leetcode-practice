# Array

## 🔔 Attributes

**Time Complexity of In Operator in Python**

- ✅ O(1) Set & Dict — ⬇️ Hashmap
- ❌ O(n) List — ⬇️ Linear Search, iterate until found

## 🔔 Object assignment (pass-by-object-reference)

1. Assigning an Array
    ```python
    arr1 = [1, 2, 3]
    arr2 = arr1

    arr2[0] = 99
    print(arr1)  # [99, 2, 3]
    ```
    * arr2 points to the same list as arr1.
    * Changing one affects the other. 

1. Copy (Creates a New List)
    ```python
    arr1 = [1, 2, 3]
    arr2 = arr1.copy()    # or arr1[:] or list(arr1)
    arr2[0] = 99
    print(arr1)  # [1, 2, 3]

    arr1 = [[1, 2], [3, 4]]
    arr2 = arr1.copy()
    arr2[0][0] = 99
    print(arr1)  # [[99, 2], [3, 4]]
    ```

    🚨 Inner objects still referenced → shallow copies fail for nested structures.

1. List slicing

    List slicing creates a *new* list containing elements from index 0 to 1
    ```python
    arr1 = [1, 2, 3]
    arr2 = arr1[:2]
    arr2[0] = 99

    print(arr1)  # [1, 2, 3]
    print(arr2)  # [99, 2]
    ```


## 🔔 Operaitons on Array

### Insertion

Insert element
* at the beginning `arr.insert(0, value)`
* at given position `arr.insert(index, value)`
* at the end `arr.append(value)`

Append array
```python
arr = [a, b, c]
arr.extend([1, 2, 3])
# output: [a, b, c, 1, 2, 3]
```

### Deletion

Delete an Element from the given position

```python
# Remove the first element 
del arr[0]
```

Delete First Occurrence of Given Element from an Array
```python
arr.remove(element)
```

Delete an Element from the end of an array
```python
arr.pop()
```

### Searching

Linear search: Simply traverse the list


[Binary search](https://www.geeksforgeeks.org/dsa/binary-search/)
```python
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1
```

### Subarray & Subsequence

[Subarray/Substring vs Subsequence and Programs to Generate them](https://www.geeksforgeeks.org/dsa/subarraysubstring-vs-subsequence-and-programs-to-generate-them/)

Every subarray is a subsequence. More specifically, Subsequence is a generalization of substring.

A subarray or substring will always be contiguous, but a subsequence need not be contiguous.

Subsequence is the full permutation of the array. 

## 🦸 Techniques

### Iteration (nested loops), Recursion & backtracking (binary decision tree)
### Prefix and suffix sum
### Sorting
### Two pointers
### Hashing
### Binary search
### Swapping elements in place
### Maths: Sum of array, 平方差公式, Number of occurrences
### Kadane algorithm (Slow and fast pointer)
### Floyd's algorithm 
### Bit manipulation (XOR operant and Extracting the rightmost set bit equation)
### Sliding window


## 🔔 Basic problems

### ▶️ Alternate elements of an array (skip an element)

---

<details>
<summary>Recursive approach</summary>

```python
# Recursive Python Program to print alternate elements
# of the array

# Recursive function to store all alternate elements
def getAlternatesRec(arr, idx, res):
    if idx < len(arr):
        res.append(arr[idx])
        getAlternatesRec(arr, idx + 2, res)

def getAlternates(arr):
    res = []
    getAlternatesRec(arr, 0, res)
    return res

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))
```
</details>

<details>
<summary>Iterative Approach</summary>

```python
# Iterate Python Program to print alternate elements
# of the array

def getAlternates(arr):
    res = []
    
    # Iterate over all alternate elements
    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))
```
</details>

### ▶️ [Leaders in an array](https://www.geeksforgeeks.org/dsa/leaders-in-an-array/)
---
Problem: \
Given an array arr[] of size n, the task is to find all the Leaders in the array. \
An element is a Leader if it is greater than or equal to all the elements to its right side.

Edge case:
* Does it always include right-most element?

Examples:
```
Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
```

<details>
<summary>[Naive Approach] Using Nested Loops - O(n^2) Time and O(1) Space</summary>


</details>

<details>
<summary>[Expected Approach] Using Suffix Maximum - O(n) Time and O(n) Space: </summary>
Scan all the elements from **right to left** in an array and keep track of the maximum till now.

```python
# Function to find the leaders in an array
def leaders(arr):
    result = []
    n = len(arr)

    # Start with the rightmost element
    maxRight = arr[-1]

    # Rightmost element is always a leader
    result.append(maxRight)

    # Traverse the array from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    # Reverse the result list to maintain
    # original order
    result.reverse()

    return result
```
</details>

### ▶️ Check if an Array is Sorted

---

<details>
<summary>[Approach 1] Recursive approach - O(n) Time and O(n) Space</summary>

```python
def isSortedhelper(arr, n):

    # Base case
    if (n == 0 or n == 1):
        return True
        
    # Check if current and previous elements are in order
    # and recursively check the rest of the array
    return (arr[n - 1] >= arr[n - 2] and isSortedhelper(arr, n - 1))
            
def isSorted(arr):
    
    n = len(arr)
    
    return isSortedhelper(arr, n)
    
if __name__ == "__main__":
    arr = [ 10, 20, 30, 40, 50 ]

    if (isSorted(arr)):
       print("true")
    else:
       print("false")
```
</details>

<details>
<summary>[Approach 2] Iterative approach - O(n) Time and O(1) Space</summary>

</details>

[Approach 3] Using Built-in Methods `sorted(arr)`

### ▶️ Remove duplicates from Sorted Array

---

<details>
<summary>[Expected Approach] Compare previous and current element - O(n) Time and O(1) Space</summary>

```python 
#Prints all subarrays in arr[0..n-1]
def sub_array(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()  # New line after each subarray

# Driver code
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)
```
</details>

<details>
<summary>Using Hash Set - Works for Unsorted Also - O(n) Time and O(n) Space</summary>

```python 
def removeDuplicates(arr):
    
    # To track seen elements
    seen = set()
    
    # To maintain the new size of the array
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    # Return the size of the array 
    # with unique elements
    return idx

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    newSize = removeDuplicates(arr)

    for i in range(newSize):
        print(arr[i], end=" ")
```
</details>

### ▶️ [Generating all Subarrays](https://www.geeksforgeeks.org/dsa/generating-subarrays-using-recursion/)

---

<details>
<summary>Iterative Approach</summary>

```python 
#Prints all subarrays in arr[0..n-1]
def sub_array(arr):
    n = len(arr)

    # Pick starting point
    for i in range(n):
        # Pick ending point
        for j in range(i, n):
            # Print subarray between current starting and ending points
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()  # New line after each subarray

# Driver code
arr = [1, 2, 3, 4]
print("All Non-empty Subarrays:")
sub_array(arr)
```
</details>

<details>
<summary>Recursive Approach</summary>

```python
# Python3 code to print all possible subarrays 
# for given array using recursion

# Recursive function to print all possible subarrays 
# for given array
def printSubArrays(arr, start, end):
    
    # Stop if we have reached the end of the array    
    if end == len(arr):
        return
    
    # Increment the end point and start from 0
    elif start > end:
        return printSubArrays(arr, 0, end + 1) # Direction 1: Move end index to print all element before it
        
    # Print the subarray and increment the starting
    # point
    else:
        print(arr[start:end + 1])
        return printSubArrays(arr, start + 1, end) # Direction 2: Move start index 
        
# Driver code
arr = [1, 2, 3]
printSubArrays(arr, 0, 0)
```
</details>

<details>
<summary>Claude recursive approach</summary>

```python
def generateSubarrays(arr, index=0, result=None):
    if result is None:
        result = []
    
    # Base case: processed all elements
    if index == len(arr):
        return result
    
    # Choice 1: Start new subarrays from this index
    for end in range(index, len(arr)):
        result.append(arr[index:end + 1])
    
    # Choice 2: Recurse to next index
    return generateSubarrays(arr, index + 1, result)
```
</details>

### ▶️ [Sum of all Subarrays](https://www.geeksforgeeks.org/dsa/sum-of-all-subarrays/)

---

<details>
<summary>[Naive Approach] Using Nested Loop - O(n^2) Time and O(1) Space</summary>

```python
def subarraySum(arr):
    n = len(arr)
    result = 0
    
    # pick starting point
    for i in range(n):
        temp = 0
        
        # pick ending point
        for j in range(i, n):
          
            # sum subarray between current starting 
            # and ending points
            temp += arr[j]
            result += temp
    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr))
```
</details>

<details>
<summary>[Expected Approach] Element Occurrences Method - O(n) Time and O(1) Space</summary>

```python
def subarraySum(arr):
    
    n = len(arr)
    result = 0

    # Computing sum of subarrays using the formula
    for i in range(n):
        result += arr[i] * (i + 1) * (n - i) # value * number of iteration with this element * each iteration occurrences

    # Return the sum of all subarrays
    return result

if __name__ == "__main__":
    arr = [1, 4, 5, 3, 2]
    print(subarraySum(arr))
```
</details>

### ▶️ [Rearrange array such that even positioned are greater than odd](https://www.geeksforgeeks.org/dsa/rearrange-array-such-that-even-positioned-are-greater-than-odd/)

---

<details>
<summary>[Approach 1] - Rearranging array by swapping elements</summary>

```python 
# Python program to Rearrange array such that even positioned are greater than odd


def rearrangeArray(arr):
    n = len(arr)

    # Traverse the array and make adjustments to satisfy the condition
    for i in range(n - 1):

        # Check if the index is even (1-based), i.e., i+1 is even
        if (i + 1) % 2 == 0:
            # Ensure that the current element is greater than
            # or equal to the previous element
            if arr[i] < arr[i + 1]:
                arr[i], arr[i+1] = arr[i + 1], arr[i]
        else:
            # Ensure that the current element is less than or
            # equal to the previous element
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr

if __name__ == "__main__":

    inputArray = [1, 2, 2, 1]

    resultArray = rearrangeArray(inputArray)

    print(" ".join(map(str, resultArray)))
```

</details>

<details>
<summary>[Approach 2] - Assign Maximum Elements to Even Positions</summary>

```python
# Python program to Rearrange array such that even positioned are greater than odd

def rearrangeArray(arr):
    # Sort the array
    arr.sort()

    n = len(arr)
    result = [0] * n
    ptr1, ptr2 = 0, n - 1

    for i in range(n):
      
        # Assign even indexes (1-based) with maximum elements
        if (i + 1) % 2 == 0:
            result[i] = arr[ptr2]
            ptr2 -= 1
            
        # Assign odd indexes (1-based) with remaining elements
        else:
            result[i] = arr[ptr1]
            ptr1 += 1

    return result

 
arr = [1, 2, 2, 1]
res = rearrangeArray(arr)
print(res)
```

</details>


### ▶️ [Stock Buy and Sell - Multiple Transaction Allowed](https://www.geeksforgeeks.org/dsa/stock-buy-sell/)

---

Note: Sum up all up trend difference
<details>
<summary>[Better Approach] Using Local Minima and Maxima - O(n) Time and O(1) Space</summary>

```python
def maxProfit(prices):
    n = len(prices)
    lMin = prices[0]  
    lMax = prices[0]  
    res = 0
  
    i = 0
    while i < n - 1:
      
        # Find local minima
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        
        # Local Maxima
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
      
        # Add current profit
        res += (lMax - lMin)
  
    return res

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maxProfit(prices))
```
</details>


<details>
<summary>[Expected Approach] By Accumulating Profit - O(n) Time and O(1) Space</summary>

```python
def maxProfit(prices):
    res = 0

    # Keep on adding the difference between
    # adjacent when the prices a
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            res += prices[i] - prices[i - 1]

    return res

if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maxProfit(prices))
```
</details>


### ▶️ [Unique Number I](https://www.geeksforgeeks.org/dsa/find-element-appears-array-every-element-appears-twice/)

---

<details>
<summary>[Expected Approach] Using XOR Operation - O(n) Time and O(1) Space</summary>

XOR 异或 (相异为真的 或运算)
* ❌ **Cancels** out **identical** numbers (results in 0)
* ✅ **Retains** **different** numbers

💡 Look for difference/duplicate → XOR operation!

```python
def findUnique(arr):
    res = 0
    
    # Find XOR of all elements
    for num in arr:
        res ^= num
    
    return res

if __name__ == '__main__':
    arr = [2, 3, 5, 4, 5, 3, 4]
    print(findUnique(arr))
```
</details>


<details>
<summary>[Better Approach] Using Hash Map - O(n) Time and O(n) Space</summary>

Hash map - requires extra space \
2 traversals

```python
def findUnique(arr):
    # Dictionary to store the count of each element
    cnt = {}

    # Store frequency of each element
    for num in arr:
        cnt[num] = cnt.get(num, 0) + 1

    # Return the value with count = 1
    for key, value in cnt.items():
        if value == 1:
            return key

    # If no element exists that appears only once
    return -1

arr = [2, 3, 5, 4, 5, 3, 4]
print(findUnique(arr))
```
</details>

### ▶️ [Find the Missing Number](https://www.geeksforgeeks.org/dsa/find-the-missing-number/)

---

<details>
<summary>[Naive Approach] 一个一个对着找 Linear Search for Missing Number - O(n^2) Time and O(1) Space</summary>

```python
def missingNum(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))
```
</details>

<details>
<summary>[Better Approach] Using Hashing - O(n) Time and O(n) Space</summary>

```python
def missingNum(arr):
    n = len(arr) + 1

    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for i in range(n - 1):
        hash[arr[i]] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    return -1

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res)
```
</details>


<details>
<summary>[Expected Approach 1] 总和减现有的元素 Using Sum of n terms Formula - O(n) Time and O(1) Space</summary>

```python
def missingNum(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expSum = n * (n + 1) // 2

    # Return the missing number
    return expSum - totalSum

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))
```
</details>

<details>
<summary>[Expected Approach 2] 异或运算筛选丢失元素 Using XOR Operation - O(n) Time and O(1) Space</summary>

#### XOR Properties

```
# Property 1: Self-cancellation
a ^ a = 0

# Property 2: Identity
a ^ 0 = a

# Property 3: Commutative & Associative
a ^ b ^ c = c ^ b ^ a  # Order doesn't matter

# Property 4: Self-inverse
(a ^ b) ^ b = a
```

* Numbers that appear will cancel out (because x ^ x = 0)
* Only the missing number remains!

```python
def missingNum(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0

    # XOR all array elements
    for i in range(n - 1):
        xor2 ^= arr[i]

    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor1 ^= i

    # Missing number is the XOR of xor1 and xor2
    return xor1 ^ xor2

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    res = missingNum(arr)
    print(res)
```
</details>

### ▶️ [Missing and Repeating in an Array](https://www.geeksforgeeks.org/dsa/find-a-repeating-and-a-missing-number/)

---

<details>
<summary>[Naive Approach] Using Visited Array - O(n) Time and O(n) Space</summary>

```python
def findTwoElement(arr):
    n = len(arr)

    # frequency array to count occurrences
    freq = [0] * (n + 1)
    repeating = -1
    missing = -1

    # count frequency of each element
    for num in arr:
        freq[num] += 1

    # identify missing and repeating numbers
    for i in range(1, n + 1):
        if freq[i] == 0:
            missing = i
        elif freq[i] == 2:
            repeating = i

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1])
```
</details>

<details>
<summary>[Approach 2] Using Array Marking - O(n) Time and O(1) Space</summary>

```python
def findTwoElement(arr):
    n = len(arr)

    # REPEATING
    repeating = -1
    # 变负数 -- mark visited indices by negating the value 
    # at that index
    for i in range(n):
        val = abs(arr[i])

        # if value at index val - 1 is already negative,
        # val is repeating
        if arr[val - 1] > 0:
            arr[val - 1] = -arr[val - 1] 
        else:
            # Already visited → repeating element
            repeating = val  

    # MISSING
    missing = -1
    # the index with a positive value corresponds 
    # to the missing number
    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
            break

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    print(ans[0], ans[1])
```
</details>

<details>
<summary>[Approach 3] Making Two Math Equations - O(n) Time and O(1) Space</summary>

```python
def findTwoElement(arr):
    n = len(arr)

    # Expected sum and sum of squares for numbers from 1 to n
    s = (n * (n + 1)) // 2
    ssq = (n * (n + 1) * (2 * n + 1)) // 6

    missing = 0
    repeating = 0

    # Subtract actual sum and sum of squares from expected values
    for num in arr:
        s -= num
        ssq -= num * num

    # After negating the input array
	# s = missing - repeating
    # ssq = missing^2 - repeating^2
    # Let x = missing, y = repeating
    # => s = x - y and ssq = x^2 - y^2 = (x - y)(x + y)
    # => x = (s + ssq // s) // 2, y = x - s
    missing = (s + ssq // s) // 2
    repeating = missing - s

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)
    
    print(ans[0], ans[1])
```
</details>

<details>
<summary>[Approach 4] Using XOR - O(n) Time and O(1) Space</summary>

<details>
<summary>Reference: Numbers with odd occurrences</summary>

[Reference solution: Using Bit Manipulation - O(n) time and O(1) space](https://www.geeksforgeeks.org/dsa/find-the-two-numbers-with-odd-occurences-in-an-unsorted-array/)


The strategy -- using the rightmost set bit to divide all elements into 2 groups
* one group will have X - **same** on that bit → duplicate will be cancelled out, leaving only odd-occurrence element
* one group will have Y - **different** on that bit → duplicate will be cancelled out, leaving only odd-occurrence element

XOR 抵消相同的元素，保留不相同的 \
最后剩下不相同的两个数的运算结果 `x ^ y`

```python
# After XOR-ing all elements, we get: x ^ y
# (where x and y are the two odd-occurring numbers)

xorVal = x ^ y

# This xorVal has some bits set to 1
# Each 1 bit represents where x and y differ

# Pick any set bit (rightmost is easiest)
setBit = xorVal & ~(xorVal - 1)

# Now divide all numbers into two groups:
# Group 1: Numbers with this bit SET
# Group 2: Numbers with this bit NOT SET

# x will be in one group, y in the other!
# XOR each group separately to get x and y
```

```python
# odd occurrences in an unsorted array

# Function to find the two elements
# with odd occurrences.
def twoOddNum(arr):
    n = len(arr)
    
    # Get the XOR of the two numbers we need to find
    xorVal = 0
    for num in arr:
        xorVal ^= num

    # ! Get its last set bit -- the rightmost set bit (1) where two odd ocurrence elements differ
    xorVal &= -xorVal # JUST REMEMBER THIS FORMULA
    # THIS IS LIKE A FILTER OR MASK

    ans = [0, 0]
    
    for num in arr:
    
        # If bit is not set, it 
        # belongs to first set. (FILTERS FOR THE TARGET ELEMENT WITH 0 AT DIFFERENT BITS)
        if (num & xorVal) == 0:
            ans[0] ^= num
            
        # If bit is set, it 
        # belongs to 2nd set.
        else: # (FILTERS FOR THE TARGET ELEMENT WITH 1 AT DIFFERENT BITS)
            ans[1] ^= num
    
    # Return in decreasing order
    if ans[0] < ans[1]:
        ans[0], ans[1] = ans[1], ans[0]
    
    return ans

if __name__ == "__main__":
    arr = [12, 23, 34, 12, 12, 23, 12, 45]
    ans = twoOddNum(arr)
    print(ans[0], ans[1])
```
</details>

#### Code implementation

```python
def findTwoElement(arr):
    n = len(arr)
    xorVal = 0  

    # get the xor of all array elements
    # And numbers from 1 to n
    for i in range(n):
        xorVal ^= arr[i]
        xorVal ^= (i + 1)  # 1 to n numbers -- Cancels out one-occurrence elements 
                            #               -- Keeps the duplicate and missing element
                            # at the end, xorVal = duplicate-element ^ missing-element

    # get the rightmost set bit in xorVal -- One of the bits that sets duplicate-element and missing-element apart
    #                                     -- Then group the array into the "duplicate" side and the "missing" side
    setBitIndex = xorVal & ~(xorVal - 1)
    
    x, y = 0, 0

    # now divide elements into two sets 
    # by comparing rightmost set bit
    for i in range(n):
      
        # decide whether arr[i] is in first set 
        # or second
        # Doesn't which group takes "same" or "different"
        if arr[i] & setBitIndex: 
            x ^= arr[i] 
        else: 
            y ^= arr[i]
      
        # decide whether (i+1) is in first set 
        # or second
        # CANCELS ONE-OCCURRENCE ELEMENT; KEEPS ONLY MISSING / DUPLICATE ELEMENT
        if (i + 1) & setBitIndex: 
            x ^= (i + 1) 
        else: 
            y ^= (i + 1)

    # x and y are the repeating and missing values.
    # to know which one is what, traverse the array 
    xCnt = sum(1 for num in arr if num == x) # `1 for num in arr if num == x` generates an 1 whenever num == x is met
    # If count is 0, then x is the missing element 
    # If count is 2, then x is the duplicate element 
    
    if xCnt == 0:
        missing, repeating = x, y
    else:
        missing, repeating = y, x

    return [repeating, missing]

if __name__ == "__main__":
    arr = [3, 1, 3]
    ans = findTwoElement(arr)

    print(ans[0], ans[1])
```

</details>

### ▶️ [Find the Duplicate One From 1 To n-1](https://www.geeksforgeeks.org/dsa/find-repetitive-element-1-n-1/)

---

<details>
<summary>[Expected Approach 4] Floyd's Cycle Detection - O(n) Time and O(1) Space</summary>

```python
# Python program to find the 
# duplicate element

# Function to find the duplicate
# element in an array
def findDuplicate(arr):

    # slow pointer
    slow = arr[0] 

    # fast pointer
    fast = arr[0] 

    while True:

        # moves one step
        slow = arr[slow]  

        # moves two steps
        fast = arr[arr[fast]]     
        if slow == fast:
            break

    # reinitialize fast to the start
    fast = arr[0] 
  
    # Loop until both pointers meet at the duplicate
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
  
    # Return duplicate number
    return slow
    
if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(findDuplicate(arr))
```

</details>

<details>
<summary>[Expected Approach 3] Using Elements as Indexes - O(n) Time and O(1) Space</summary>

```python
# Function to find the duplicate
# element in an array
def findDuplicate(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] < 0:
            return abs(arr[i])
        arr[abs(arr[i])] = -arr[abs(arr[i])]
    return -1
    
if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(findDuplicate(arr))
```

</details>

<details>
<summary>[Expected Approach 2] Using XOR - O(n) Time and O(1) Space</summary>

```python
# Python program to find the 
# duplicate element

# Function to find the duplicate
# element in an array
def findDuplicate(arr):
    n = len(arr)
    res = 0

    # XOR all numbers from 1 to n-1 and 
    # elements in the array
    for i in range(n - 1):
        res = res ^ (i + 1) ^ arr[i]
    
    # XOR the last element in the array
    res = res ^ arr[n - 1]
    
    return res

if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(findDuplicate(arr))
```

</details>

<details>
<summary>[Expected Approach 1] Sum Formula - O(n) Time and O(1) Space</summary>

```python
# Python program to find the duplicate element

def findDuplicate(arr):
    n = len(arr)
  
    # Find the sum of elements in the array
    # and subtract the sum of the first n-1 
    # natural numbers to find the repeating element.
    totalSum = sum(arr)
    duplicate = totalSum - ((n - 1) * n // 2)
    return duplicate

if __name__ == "__main__":
    arr = [1, 3, 2, 3, 4]
    print(findDuplicate(arr))
```

</details>


### ▶️ Sorted subsequence of size 3

---

存在有一组，不需要全部找到，只需要一个元素一个元素的判断，并存储最近一次的数据

**Recursive approach--generate subsequences**

[YouTube explaination video on Backtracking - Backtracking (Think Like a Programmer) by V. Anton Spraul](https://youtu.be/gBC_Fd8EE8A?si=rSyPf0LYjaIor6gk)

Key idea: **binary decision tree**

At each index, you have exactly two choices:

1. Do not take arr[index]
1. Take arr[index]

This forms a binary decision tree of depth n.

Example for [1, 2, 3]:
```css
                          []
                   /                \
               skip 1              take 1
                []                   [1]
            /         \          /           \
        skip 2       take 2   skip 2         take 2
         []           [2]      [1]           [1,2]
       /    \        /    \    /    \         /    \
     ...    ...    ...    ...  ...   ...     ...    ...

```
Each leaf node corresponds to one subsequence.


```python
# subsequences (not subarrays)
def subsequences(arr, index=0, current=None, result=None):
    if current is None:
        current = []
    if result is None:
        result = []

    if index == len(arr):
        result.append(current[:])
        return

    subsequences(arr, index + 1, current, result)
    current.append(arr[index])
    subsequences(arr, index + 1, current, result)
    current.pop() # pop current是真的function全局来说的，为平行*中在等待的其他recursive call清理current数组
```

<details>
<summary>Naive Approach - O(n) Time and O(n) Space</summary>

```python
# Python program to fund a sorted
# sub-sequence of size 3

def find3numbers(arr):
    n = len(arr)

# Index of maximum element from right side
    max = n-1

# Index of minimum element from left side 
    min = 0

    # 存每个位，左边，最近的满足比自己更小的元素的位置
    smaller = [-1] * n
    for i in range(1, n):
        if (arr[i] <= arr[min]):
            min = i
        else:
            smaller[i] = min

    # 存每个位，右边，最近的满足比自己更大的元素的位置
    greater = [-1]*n
    for i in range(n-2, -1, -1):
        if (arr[i] >= arr[max]):
            max = i
            greater[i] = -1

        else:
            greater[i] = max

    # 若同一位置，两边都有满足条件的元素，则为题目所求的解
    for i in range(n):
        if smaller[i] != -1 and greater[i] != -1:
            print arr[smaller[i]], arr[i], arr[greater[i]]
            return

    # If we reach here, then there are no such 3 numbers
    print "No triplet found"
    return

# Driver function to test above function
arr = [12, 11, 10, 5, 6, 2, 30]
find3numbers(arr)
```

</details>

<details>
<summary>[Expected Approach 1] Sum Formula - O(n) Time and O(1) Space</summary>

```python
def find3Numbers(nums):
    first = float('inf')
    second = float('inf')

    for x in nums:
        if x <= first:
            first = x
        elif x <= second:
            second = x
        else:
            print(f"Triplet: {first}, {second}, {x}")
            return

    print("No such triplet exists")
```

</details>

### ▶️ Maximum Subarray Sum - Kadane's Algorithm

---

<details>
<summary>[Naive Approach] By iterating over all subarrays - O(n^2) Time and O(1) Space</summary>

Use the naive solution from [Sum of all Subarrays](#️-sum-of-all-subarrays)

```python
def maxSubarraySum(arr):
    res = arr[0]
  
    # Outer loop for starting point of subarray
    for i in range(len(arr)):
        currSum = 0
      
        # Inner loop for ending point of subarray
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
          
            # Update res if currSum is greater than res
            res = max(res, currSum)
          
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))
```

</details>

<details>
<summary>[Expected Approach] Using Kadane's Algorithm - O(n) Time and O(1) Space</summary>

```python
def maxSubarraySum(arr):
    
    # Stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        
        # Either extend the previous subarray or start 
        # new from current element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update result if the new subarray sum is larger
        res = max(res, maxEnding)
    
    return res

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))
```

</details>

### ▶️ Equilibrium Index

---

<details>
<summary>[Naive Approach] Using Nested Loop - O(n^2) Time and O(1) Space</summary>

```python
# Python program to find equilibrium index of an array
# using nested loop

def findEquilibrium(arr):
    
    # Check for indexes one by one until
    # an equilibrium index is found 
    for i in range(len(arr)):
        # Get left sum
        leftSum = sum(arr[:i])

        # Get right sum
        rightSum = sum(arr[i + 1:])

        # If leftsum and rightsum are same, then 
        # index i is an equilibrium index
        if leftSum == rightSum:
            return i

    # If equilibrium index doesn't exist
    return -1
  
if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(findEquilibrium(arr))
```

</details>


<details>
<summary>[Better Approach] Prefix Sum and Suffix Sum Array - O(n) Time and O(n) Space</summary>

```python
# Python program to find equilibrium index of an array
# using prefix sum and suffix sum arrays

def findEquilibrium(arr):
    n = len(arr)

    pref = [0] * n
    suff = [0] * n

    # Initialize the ends of prefix and suffix array
    pref[0] = arr[0]
    suff[n - 1] = arr[n - 1]

    # Calculate prefix sum for all indices
    for i in range(1, n):
        pref[i] = pref[i - 1] + arr[i]

    # Calculating suffix sum for all indices
    for i in range(n - 2, -1, -1):
        suff[i] = suff[i + 1] + arr[i]

    # Checking if prefix sum is equal to suffix sum
    for i in range(n):
        if pref[i] == suff[i]:
            return i

    # if equilibrium index doesn't exist
    return -1
  
if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(findEquilibrium(arr))
```

</details>

<details>
<summary>[Expected Approach] Running Prefix Sum and Suffix Sum - O(n) Time and O(1) Space</summary>

Don't skip index 0 because:

Index 0 can be an equilibrium point if: 元素都是0

```
sum(arr[1:]) == 0
```

```python
# Python program to find equilibrium index of an array
# using nested loop

def equilibriumPoint_v1(arr):
    if not arr:
        return -1

    prefix = 0
    suffix = sum(arr)

    for i in range(len(arr)):
        suffix -= arr[i]     # now suffix is right sum

        if prefix == suffix:
            return i

        prefix += arr[i]

    return -1

def equilibriumPoint_v2(arr):
    if len(arr) == 0:
        return -1

    prefix = 0
    suffix = sum(arr[1:])

    if prefix == suffix:
        return 0

    for i in range(1, len(arr)):
        prefix += arr[i - 1]
        suffix -= arr[i]

        if prefix == suffix:
            return i

    return -1
  
if __name__ == '__main__':
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(equilibriumPoint_v2(arr))
```

</details>


### ▶️ [Two Sum](https://www.geeksforgeeks.org/dsa/2sum/)

---

#### 👬 Pair with given Sum

<details>
<summary>[Expected Approach] Using Hash Set - O(n) time and O(n) space</summary>
<br />Step By Step Implementations:

<br />

- Create an empty Hash Set or Unordered Set \
- Iterate through the array and for each number in the array: \
- => Calculate the complement (target - current number). \
- => Check if the complement exists in the set:
    - If it is, then pair found.
    - If it isn’t, add the current number to the set.
- If the loop completes without finding a pair, return that no pair exists.


```python
def twoSum(arr, target):

    # Create a set to store the elements
    s = set()

    for num in arr:
      
        # Calculate the complement that added to
        # num, equals the target
        complement = target - num

        # Check if the complement exists in the set
        if complement in s:
            return True

        # Add the current element to the set
        s.add(num)

    # If no pair is found
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    if twoSum(arr, target):
        print("true")
    else:
        print("false")
```

</details>

<details>
<summary>[Better Approach 1] Sorting and Binary Search - O(n × log(n)) time and O(1) space</summary>

```python
# Function to perform binary search
def binarySearch(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def twoSum(arr, target):
    arr.sort()

    for i in range(len(arr)):
        complement = target - arr[i]

        # Use binary search to find the complement
        if binarySearch(arr, i + 1,
                    len(arr) - 1, complement):
            return True
            
    # If no pair is found
    return False
  	
if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    if twoSum(arr, target):
        print("true")
    else:
        print("false")
```

</details>

<details>
<summary>[Better Approach 2] Sorting and Two-Pointer Technique - O(n × log(n)) time and O(1) space</summary>

```python
def twoSum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    # Iterate while left pointer is less than right
    while left < right:
        sum = arr[left] + arr[right]

        # Check if the sum matches the target
        if sum == target:
            return True
        elif sum < target:
            
            # Move left pointer to the right
            left += 1
        else:
            
            # Move right pointer to the left
            right -= 1

    # If no pair is found
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2
    if twoSum(arr, target):
        print("true")
    else:
        print("false")
```

</details>

<details>
<summary>[Naive Approach] Generating all Possible Pairs - O(n^2) time and O(1) space</summary>

```python
def twoSum(arr, target):
    n = len(arr)

    for i in range(n):
      
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
          
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                return True
              
    # If no pair is found after checking
    # all possibilities
    return False

if __name__ == "__main__":
    arr = [0, -1, 2, -3, 1]
    target = -2

    if twoSum(arr, target):
        print("true")
    else:
        print("false")
```

</details>

#### 👬 Pair Closest to 0

翻译：找两个元素绝对值最小的一对儿

<details>
<summary>[Expected Approach] Using Sorting + Two Pointer - O(nlog(n)) Time and O(1) Space</summary>

```python
# Python Code for Two Sum - Closest Pair
# Using Two Pointer
def minAbsSumPair(arr):
  
    # Sorting the array in ascending order
    arr.sort()

    i, j = 0, len(arr) - 1

    # Initializing sum with the first and last elements
    sum_val = arr[i] + arr[j]

    # Initializing the result with the absolute value
    # of the initial sum
    diff = abs(sum_val)

    while i < j:
      
        # If we have zero sum, there's no result
        # better. Hence, we return 0.
        if arr[i] + arr[j] == 0:
            return 0

        # If we get a better result, we update the
        # difference
        if abs(arr[i] + arr[j]) < abs(diff):
            diff = arr[i] + arr[j]
            sum_val = arr[i] + arr[j]
        elif abs(arr[i] + arr[j]) == abs(diff):
          
            # If there are multiple pairs with the same
            # minimum absolute difference, return the
            # pair with the larger sum
            sum_val = max(sum_val, arr[i] + arr[j])

        # If the current sum is greater than zero, we
        # search for a smaller sum
        if arr[i] + arr[j] > 0:
            j -= 1
        # Else, we search for a larger sum
        else:
            i += 1

    return sum_val


# Driver Code
arr = [0, -8, -6, 3]
print(minAbsSumPair(arr))
```

</details>

<details>
<summary>[Better Approach] Using Sorting + Binary Search - O(nlog(n)) Time and O(1) Space</summary>

```python
# Python Code for Two Sum - Closest Pair
# Using Binary Search

# Function to find the minimum absolute sum pair
def minAbsSumPair(arr):

    arr.sort()

    n = len(arr)

    # Variable to store the closest sum
    res = float('inf')

    # Iterate over the array
    for i in range(n):

        # Consider current element as first 
        # element of the pair and find the
        # other element using binary search
        x = arr[i]

        left, right = i + 1, n - 1

        while left <= right:
            mid = (left + right) // 2

            curr = arr[mid] + x

            # If exact pair is found
            if curr == 0:
                return 0

            # Update res if the current pair is closer
            if abs(curr) < abs(res):
                res = curr

            elif abs(curr) == abs(res):
                res = max(res, curr)

            # If current is smaller than 0,
            # go to right side. Else on the
            # left side.
            if curr < 0:
                left = mid + 1
            else:
                right = mid - 1

    return res

if __name__ == "__main__":
    arr = [0, -8, -6, 3]
    print(minAbsSumPair(arr))
```

</details>

### ▶️ Split array into three equal sum segments

---

<details>
<summary>[Expected Approach] Finding first two segments- O(n) Time and O(1) Space</summary>

```python
# Python program to find if the array can be divided into
# three segments by finding first two segments

# function to return the index pair of equal sum segments
def findSplit(arr):
    res = []
    total = sum(arr)

    # If the total sum is not divisible by 3,
    # it's impossible to split the array
    if total % 3 != 0:
        res = [-1, -1]
        return res

    # Keep track of the sum of current segment
    currSum = 0

    for i in range(len(arr)):
        currSum += arr[i]

        # If the valid segment is found, store its index
        # and reset current sum to zero
        if currSum == total / 3:
            currSum = 0
            res.append(i)

            # If two valid segments are found and third non
            # empty segment is possible, return the index pair
            if len(res) == 2 and i < len(arr) - 1:
                return resa

    # If no index pair is possible
    res = [-1, -1]
    return res

if __name__ == "__main__":
    arr = [1, 3, 4, 0, 4]
    res = findSplit(arr)

    print(res[0], res[1])
```

</details>

### ▶️ Maximum Consecutive Ones After Flipping Zeroes

---

<details>
<summary>[Expected Approach] Using Sliding Window Technique - O(n) Time and O(1) Space</summary>

```python
def maxOnes(arr, k):
    res = 0

    # Start and end pointer of the window
    start = 0
    end = 0

    # Counter to keep track of zeros in current window
    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1

        # Shrink the window from left if no. 
        # of zeroes are greater than k
        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))

        # Increment the end pointer 
        # to expand the window
        end += 1

    return res

if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes(arr, k))
```

</details>
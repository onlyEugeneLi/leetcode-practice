# Array

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

2. Copy (Creates a New List)
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

3. List slicing

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
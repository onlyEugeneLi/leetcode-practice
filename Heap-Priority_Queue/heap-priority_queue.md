# Heap

A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap) or largest (max-heap) element. 

A heap is typically implemented as a **binary tree**, where each parent node's value is smaller (for a min-heap) or larger (for a max-heap) than its children. 

However, in *Python*, heaps are usually implemented as *min-heaps* which means the smallest element is always at the root of the tree (index 0), making it easy to access.

## Python implementation -- `Heapq`

```
import heapq

# Creating an initial heap
h = [10, 20, 15, 30, 40]
heapq.heapify(h)

# Appending an element
heapq.heappush(h, 5)

# Pop the smallest element from the heap
min = heapq.heappop(h)

print(h)

print("Smallest:", min)
print(h)
```

Output:
```
[10, 20, 15, 30, 40]
Smallest: 5
[10, 20, 15, 30, 40]
```
# Graph

## Basics

### Graph representation

- Adjacency matrix 
- Adjacency linked list

### BFS (Breadth First Search)

逐个扫描每个选项然后再到下一层，level by level，一直到终点

Main function: for loop one-by-one Traversal

Fully connected graph: Run BFS once from the source node

Direction matrix (up, down, left, right)

Boundary detection before checking

While loop and Queue to store nodes to visit at each cycle 

Disconnected graph: Run BFS over all nodes (multi-source shortest path problem)


### DFS (Depth First Search)

Main function: for loop one-by-one Traversal

Direction matrix (up, down, left, right)

Boundary detection before checking 

Recursion works on one direction to the end

Increment in the map to mark progress

## BFS & DFS

### Rotten oranges

Multi-source shortest path problem

<details>
<summary>[Naive Approach] - Using Iteration - O((n x m) ^ 2) Time and O(1) Space</summary>

```python
def isSafe(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def orangesRot(mat):
    n = len(mat)
    m = len(mat[0])

    # to check if any changes are made
    changed = False

    # counter of elapsed time
    elapsedTime = 0

    # all four directions
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # iterate until changes are there
    while True:
        for i in range(n):
            for j in range(m):

                # check if the cell was marked in last iteration
                if mat[i][j] == elapsedTime + 2:

                    # change 4-directionally connected cells
                    for dir in directions:
                        x = i + dir[0]
                        y = j + dir[1]

                        # if cell is in the matrix and
                        # the orange is fresh
                        if isSafe(x, y, n, m) and mat[x][y] == 1:
                            mat[x][y] = mat[i][j] + 1 # 原rotten点叠加新次数，可以引用之前的结果，一圈一圈的叠加传播次数，结果存在adjacent orange上
                            changed = True

        # if no changes are done
        if not changed:
            break
        changed = False
        elapsedTime += 1

    for i in range(n):
        for j in range(m):

            # if any orange is found
            # not rotten, return -1
            if mat[i][j] == 1:
                return -1

    return elapsedTime

if __name__ == "__main__":
    mat =  [ [2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1] ]
    
    print(orangesRot(mat))
```

</details>


<details>
<summary>[Better Approach] - Using Depth First Search - O(n x m) Time and O(1) Space</summary>
<br>
Elapsedtime not updated during DFS propagation 

`Elapsedtime = max(elapsedTime, mat[i][j] - 2)` takes care of 

3 conditions:

- Every fresh orange that can rot has been reached

- No fresh orange remains (1 is absent)

- The grid contains at least one rotten orange initially

```python
def isSafe(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

# function to perform dfs and find fresh orange
def dfs(mat, i, j, time):
    n = len(mat)
    m = len(mat[0])

    # update minimum time / rotten tomatoes 
    mat[i][j] = time

    # all four directions
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # change 4-directionally connected cells
    for dir in directions:
        x = i + dir[0]
        y = j + dir[1]

        # if cell is in the matrix and
        # the orange is fresh
        if isSafe(x, y, n, m) and (mat[x][y] == 1 or mat[x][y] > time + 1): # time + 1 保证fresh oranges也能记录传播次数 propagate these values; 不用再把1转换成2
            dfs(mat, x, y, time + 1) # 计数从0代rotten oranges走到这里要多少步


def orangesRot(mat):
    n = len(mat)
    m = len(mat[0])

    # counter of elapsed time
    elapsedTime = 0

    # iterate through all the cells
    for i in range(n):
        for j in range(m):

            # if orange is initially rotten
            if mat[i][j] == 2:
                dfs(mat, i, j, 2)

    # iterate through all the cells
    for i in range(n):
        for j in range(m):

            # if orange is fresh
            if mat[i][j] == 1:
                return -1

            # update the maximum time
            elapsedTime = max(elapsedTime, mat[i][j] - 2) ## HOW DOES THIS WORK OUT Correct result? ?

    return    elapsedTime


if __name__ == "__main__":
    mat = [[2, 1, 0, 2, 1],
          [1, 0, 1, 2, 1],
          [1, 0, 0, 2, 1]]

    print(orangesRot(mat))
```
</details>

### Number of Islands

<details>
<summary>[Approach 3] Using Disjoint Set - O(n*m) time and O(n*m) space</summary>

```python
class DisjointSet:
    # Initialize DSU with each node as its own parent
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find operation with path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union operation by rank
    def unite(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1


def countIslands(grid):
    n = len(grid)
    m = len(grid[0])
    ds = DisjointSet(n * m)

    # Directions for 8-connected neighbors
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    # Perform union for all connected 'L' (land) cells
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'L':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 'L':
                        ds.unite(r * m + c, nr * m + nc)

    # Use a set to count unique root parents representing islands
    uniqueIslands = set()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'L':
                uniqueIslands.add(ds.find(r * m + c))

    return len(uniqueIslands)


if __name__ == "__main__":
    grid = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]
    print(countIslands(grid))
```


</details>

### Check for Bipartite

Optimisation methods Lecture 5 Maximum bipartite matching

Method: Colour a node, and colour its neighbours with the other colour. If there's edge between same colour nodes, it is not a bipartite. 

<details>
<summary>Using Breadth-First Search (BFS) - Time Complexity: O(V + E), Space O(V)</summary>

```python
from collections import deque

# Function to construct the adjacency list from edges
def constructadj(V, edges):
    adj = [[] for _ in range(V)]
    for edge in edges:
        u, v = edge
        adj[u].append(v)
        adj[v].append(u)  
    return adj

# Function to check if the graph is Bipartite using BFS
def isBipartite(V, adj):
    # Initialize all as uncolored
    color = [-1] * V  
    
    # create adjacency list
    adj = constructadj(V,edges)
    
    for i in range(V):
        if color[i] == -1:
            color[i] = 0 # After visiting all nodes, start from a new source '0' colour node 
            q = deque([i])

            while q:
                u = q.popleft()

                for v in adj[u]:
                    if color[v] == -1: # Unvisited neighbours
                        color[v] = 1 - color[u] # Colour neighbours 1-0=1
                        q.append(v) # Append neighbours
                    elif color[v] == color[u]: # If they are both 0 or 1 --> Not bipartite
                        return False  # Conflict found

     # No conflict, graph is bipartite
    return True 

if __name__ == "__main__":
    V = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    print("true" if isBipartite(V, edges) else "false")
```

</details>


<details>
<summary>Depth-First Search - O(V+E) Time and O(V) Space</summary>

```python

# Function to construct the adjacency list from edges
def constructadj(V, edges):
    adj = [[] for _ in range(V)]
    for edge in edges:
        u, v = edge
        adj[u].append(v)
        adj[v].append(u)  
    return adj


def dfs(u, color, colors, adj):
    # Assign color to the current u
    colors[u] = color

    # Iterate through all adjacent vertices
    for v in adj[u]:
        if colors[v] == -1:
            # Assign alternate color to the adjacent u
            if not dfs(v, 1 - color, colors, adj):
                return False
        elif colors[v] == color:
            # If the adjacent u has the same color, it's not bipartite
            return False
    return True

def isBipartite(V, edges):
    # Initialize all vertices as uncolored
    colors = [-1] * V
    
    # create adjacency list
    adj = constructadj(V,edges)
    
    # Check each component of the graph
    for i in range(V):
        # If the vertex is uncolored
        if colors[i] == -1:
            # If DFS fails, the graph is not bipartite
            if not dfs(i, 0, colors, adj):
                return False

    # All vertices can be colored bipartitely
    return True

if __name__ == "__main__":
    
    V = 4
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    print("true" if isBipartite(V, edges) else "false")

```

</details>

### Word ladder

<details>
<summary>[Naive Approach]: Using backtracking, explore all possible path--Time Complexity: O(N⋅26^L), Space Complexity: O(N)</summary>


```python
# Recursive function to find the shortest transformation chain
def minWordTransform(start, target, mp):
    # If start word is the same as target, no transformation is needed
    if start == target:
        return 1 # The target is the first (end) point on the chain

    mini = float('inf')

    # Mark current word as visited
    mp[start] = 1

    # Try changing each character of the word
    for i in range(len(start)):
        original_char = start[i]

        # Try all possible lowercase letters at position i
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            new_word = start[:i] + ch + start[i+1:]

            # If the new word exists in dictionary and is not visited
            if new_word in mp and mp[new_word] == 0:
                # Recursive call for next transformation
                mini = min(mini, 1 + minWordTransform(new_word, target, mp))

    # 回溯到上一层再判断另一条路 Mark current word as unvisited (backtracking)
    mp[start] = 0

    return mini

# Wrapper function to prepare the map and call recursive function
def wordLadder(start, target, arr):
    mp = {word: 0 for word in arr}

    result = minWordTransform(start, target, mp)
    if(result == float('inf')):
        result = 0
    return result

# Driver code
arr = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
start = "toon"
target = "plea"

print(wordLadder(start, target, arr))
```

</details>


<details>
<summary>Breadth First Search--Time Complexity: O(26 * n * m * m) = O(n * m * m), Space Complexity: O(n * m)</summary>


```python
# Python program to find length of the shortest
# chain transformation from start to target
from collections import deque

def wordLadder(start, target, arr):
    
    if (start == target):
        return 0
    # set to keep track of unvisited words
    st = set(arr)
    
    # store the current chain length
    res = 0
    m = len(start)
    
    # queue to store words to visit
    words = deque()
    words.append(start)
    
    while words:
        res+=1
        length = len(words)
        
        # iterate through all words at same level
        for _ in range(length):
            word = words.popleft()
            
            # For every character of the word
            for j in range(m):
                # Retain the original character
                # at the current position
                ch = word[j]
                
                # Replace the current character with
                # every possible lowercase alphabet
                for c in range(ord('a'), ord('z') + 1):
                    word = word[:j] + chr(c) + word[j+1:]
                    
                    # Not matched: skip the word if already added to the chain
                    # or not present in the word map
                    if word not in st:
                        continue
                    
                    # If target word is found
                    if word == target:
                        return res + 1
                    
                    # Matched: word exists in set, added to the chain -- remove the word from set, to prevent revisit
                    st.remove(word)
                    
                    # And push the newly generated word
                    # which will be a part of the chain
                    words.append(word)
                
                # Restore the original character
                # at the current position
                word = word[:j] + ch + word[j+1:]
        
    return 0

if __name__ == "__main__":
    arr = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
    start = "toon"
    target = "plea"
    print(wordLadder(start, target, arr))
```

</details>

### Snake and ladder problem 

How to model snake and ladder nodes to decide next node

<details>
<summary>Approach 1: Breadth-First Search - O(n) Time and O(n) Space</summary>

```python
from collections import deque

def getMinDiceThrows(snake_ladder_map):
    n = len(snake_ladder_map)
    visited = [False] * n
    q = deque()

    visited[0] = True

    # Start from cell 0 with 0 moves [cell index, no. of throws]
    q.append([0, 0])

    while q:
        curr = q[0]
        v = curr[0]
        throws = curr[1]

        if v == n - 1:
            return throws
        
        q.popleft()

        # Try all possible dice throws from current cell
        for dice in range(v + 1, min(v + 7, n)):
            # Not visited before
            if not visited[dice]:
                visited[dice] = True # Mark node as visited

                # Move to destination cell if there's a ladder/snake
                next_node = snake_ladder_map[dice] if snake_ladder_map[dice] != -1 else dice
                q.append([next_node, throws + 1])
    
    return -1

if __name__ == "__main__":
    n = 30
    snake_ladder_map = [-1] * n

    # Ladders
    snake_ladder_map[2] = 21
    snake_ladder_map[4] = 7
    snake_ladder_map[10] = 25
    snake_ladder_map[19] = 28

    # Snakes
    snake_ladder_map[26] = 0
    snake_ladder_map[20] = 8
    snake_ladder_map[16] = 3
    snake_ladder_map[18] = 6

    print(getMinDiceThrows(snake_ladder_map))
```

</details>

<details>
<summary>Approach 2: Depth-First Search - O(n) Time and O(n) Space</summary>

```python
import sys

def dfs(currPos, throws, move, visited, n, res):
    # Don't proceed if we have already found a better solution
    if throws >= res[0] or (currPos in visited and throws >= visited[currPos]):
        return
    
    # Base case: reached the target
    if currPos == n - 1:
        res[0] = throws
        return
    
    # Throws taken to reach currPos
    visited[currPos] = throws

    # Roll the dice: 1 to 6
    for i in range(1, 7):
        if currPos + i < n: # Safety range check
            # Move the next position
            nextPos = currPos + i
            # Check for snake, ladder or normal move
            dest = move[nextPos] if move[nextPos] != -1 else nextPos
            # Prepare for next dice throw
            dfs(dest, throws + 1, move, visited, n, res)

def getMinDiceThrows(move):
    n = len(move)
    visited = {} # Visited array and store throws taken to reach each position
    res = [sys.maxsize]

    dfs(0, 0, move, visited, n, res)

    return -1 if res[0] == sys.maxsize else res[0]

if __name__ == "__main__":
    n = 30
    moves = [-1] * n

    # Ladders
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28

    # Snakes
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    print(getMinDiceThrows(moves))
```

</details>

## Cycles

### Detect Cycle in a Directed Graph
<br>
Methods:

- Back-Edge Detection 
    - recursion stack + visited array
    - unvisited-processing-processed colouring

<details>
<summary>DFS - O(V + E) Time and O(V) Space</summary>

```python
def isCyclicUtil(adj, u, visited, recStack):

    if recStack[u]:
        return True # Cycle found

    if visited[u]:
        return False

    visited[u] = True
    recStack[u] = True

    for v in adj[u]:
        if isCyclicUtil(adj, v, visited, recStack):
            return True
        
    recStack[u] = False # Backtracking to parent

    return False

def isCyclic(adj):
    V = len(adj)
    visited = [False] * V
    recStack = [False] * V

    # Multi-source
    for i in range(V):
        if not visited[i] and isCyclicUtil(adj, i, visited, recStack):
            return True
    
    return False
```

</details>

<br>

Topological sort: 满足条件的线性序列 dependency order 

| Method                | Graph Type | Space | Time   | Notes             |
| --------------------- | ---------- | ----- | ------ | ----------------- |
| DFS + Recursion Stack | Directed   | O(V)  | O(V+E) | Most common       |
| DFS + Parent          | Undirected | O(V)  | O(V+E) | Simple            |
| BFS + Parent          | Undirected | O(V)  | O(V+E) | Iterative         |
| Union-Find            | Undirected | O(V)  | ~O(E)  | Edge-based        |
| Topological Sort      | Directed   | O(V)  | O(V+E) | Also orders nodes |
| Floyd’s Algorithm     | Functional | O(1)  | O(n)   | Specialized       |


<details>
<summary>Topological Sorting (Kahn's Algorithm) - O(V + E) Time and O(V) Space</summary>

[Reference - Kahn's algorithm](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/)

Degree-based (iterative) 

环中的node必会都剩下至少1个入度无法消除

```python

def isCyclic(adj):
    V = max(max(sub) if sub else 0 for sub in adj) + 1

    inDegree = [0] * V
    q = deque()

    visited = 0

    for u in range(V):
        for v in adj[u]:
            inDegree[v] += 1

    for u in range(V):
        if inDegree[u] == 0:
            q.append(u)

    while q: 
        u = q.popleft()

```

</details>

<br>

Floyd's Cycle Detection:

Detect cycles in functional graphs (each node has exactly one outgoing edge).

Use when
- Linked lists
- Functional graphs
- Constant space

<br>

<u>Why does marking a node fully explored guarantee a visited node cannot form a cycle with other unvisited nodes? </u>

>*Theorem*: A cycle exists if and only if there is a back edge—an edge that points from a node to one of its ancestors still in the current recursion stack

- **Paths are Exhausted**: Marking a node as Black (fully explored) means that the algorithm has already visited all neighbors and followed every possible path originating from that node. If any of those paths had led back to an ancestor, a cycle would have been detected while that node was still in the "visiting" (Gray) state
- **Cycles Require "Active" Ancestors**: A cycle is only confirmed when you encounter a Gray node. If a path from an unvisited (White) node eventually reaches a Black node, it is essentially hitting a "dead end" or a "safe branch" that has already been cleared of cycles
- **One-Way Logic**: In a directed graph, just because an unvisited node can reach a fully explored node does not mean the fully explored node can reach back to that unvisited node. If there were a path from the Black node back to the White node, the White node would have been discovered and processed while the Black node was still Gray

<details>
<summary>Colouring - O(V+E) Time and O(V) Space</summary>

Colouring scheme -- *Status*:

- white = 0 --> unvisited
- grey = 1 --> visited in recursion
- black = 2 --> fully processed (no need to visit in the future search)

```python
def constructadj(V, edges):
    adj = [[] for _ in rnage(V)]
    for u, v in edges: 
        adj[u].append(v)
    return adj

def dfsutil(u, adj, colour):
    grey = 1
    black = 2

    colour[u] = grey

    for v in adj[u]: 
        if colour[v] == grey: # Cycle detected
            return True
        if colour[v] == 0 and dfsutil(v, adj, colour): # Conitnue search on unvisited neighbour
            return True
    
    colour[u] = black
    return False

def isCyclic(V, edges):
    colour = [0] * V
    adj = constructadj(V, edges)
    for i in range(V):
        if colour[i] == 0:
            if dfsutil(i, adj, colour):
                return True
    
    return False

if __name__ == '__main__':
    V = 4
    edges = [[0, 1], [0, 2], [1, 2],
            [2, 0], [2, 3], [3, 3]]

    print("true" if isCyclic(V, edges) else "false")
```

</details>

### Detect Cycle in Undirected Graph

<br>

Method: **Parent tracker**

Track parents of each node `visited[v] and v != parent[u]` 

To distinguish a different visited node from the node you just came from

<details>
<summary>Breadth First Search - O(V+E) Time and O(V) Space</summary>

```python
from collections import deque

# Function to perform BFS from node 'start' to detect cycle
def bfs(start, adj, visited):
    
    # Queue stores [current node, parent node]
    q = deque()
     
     # Start node has no parent
    q.append([start, -1])
    visited[start] = True

    while q:
        node = q[0][0]
        parent = q[0][1]
        q.popleft()

        # Traverse all neighbors of current node
        for neighbor in adj[node]:

            # If neighbor is not visited, mark it visited and push to queue
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append([neighbor, node])
            # If neighbor is visited and not parent, a cycle is detected
            elif neighbor != parent:
                return True
    
    # No cycle found starting from this node
    return False

# Function to check if the undirected graph contains a cycle
def isCycle(adj):
    
    V = len(adj)
    
    # Keep track of visited vertices
    visited = [False] * V

    # Perform BFS from every unvisited node
    for i in range(V):
        if not visited[i]:
            
            # If BFS finds a cycle
            if bfs(i, adj, visited):
                return True
    
    # If no cycle is found in any component
    return False


#Driver Code Starts

if __name__ == "__main__":
    adj = [[1, 2],[0, 2],[0, 1, 3],[2]]
    
    print("true" if isCycle(adj) else "false")
```

</details>


<details>
<summary>Depth First Search - O(V+E) Time and O(V) Space</summary>

```python
def dfs(v, adj, visited, parent):
    
    # Mark the current node as visited
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    for neighbor in adj[v]:
        
        # If an adjacent vertex is not visited, 
        # then recur for that adjacent
        if not visited[neighbor]:
            if dfs(neighbor, adj, visited, v):
                return True
                
        # If an adjacent vertex is visited and is not
        # parent of current vertex,
        # then there exists a cycle in the graph.
        elif neighbor != parent:
            return True

    return False

# Returns true if the graph contains a cycle, else false.
def isCycle(adj):
    V = len(adj)
    # Mark all the vertices as not visited
    visited = [False] * V

    for u in range(V):
        if not visited[u]:
            if dfs(u, adj, visited, -1):
                return True

    return False

#Driver Code Starts
if __name__ == "__main__":
    adj = [[1, 2],[0, 2],[0, 1, 3],[2]]

    print("true" if isCycle(adj) else "false")
```

</details>


### Cycles of length n in an undirected and connected graph

>Why is starting DFS from only V - (n - 1) vertices sufficient?
>
>The last $(n - 1)$ vertices alone cannot form such a cycle. Therefore, every length-n cycle must include at least one of the first $V - (n - 1)$ verticesd

*Logic*: we check if this path ends with the vertex it started with, if yes then we count this as the cycle of length n. 

Notice that we looked for path of length (n-1) because the nth edge will be the closing edge of cycle.

<details>
<summary>BFS - decreasing length and compute count</summary>
<br>
Analogy: Think of it like building a necklace with exactly n beads. You pick a starting bead and string together n−1 more beads in a line. To turn that line into a necklace (a cycle), you simply check if the very last bead you added can be clipped back onto the very first bead you picked. If it can, you’ve successfully made a necklace of length n.

```python
V = 5

def DFS(graph, marked, length, vertex, start, count):

    marked[vertex] = True

    # The begin of a new search
    if length == 0:
        marked[vertex] = False # Mark as unvisited

        '''
        The Verification: To form a cycle of length n, there must be an edge connecting the final vertex (vert) back to the original starting vertex (start). The check if (graph[vert][start]) verifies if this n-th "closing edge" exists
        '''
        if graph[vertex][start] == 1:
            return count + 1
        else: 
            return count
    
    # DFS
    for i in range(V):
        # Choose one unvisited neighbour to dive in deeper
        if marked[i] == False and graph[vertex][i] == 1:
            count = DFS(graph, marked, length - 1, i, start, count)

    marked[vertex] = False

    return count

def countCycles(graph, length):

    marked[False] * V

    count = 0

    for i in rnage(V - (length - 1)):
        count = DFS(graph, marked, length - 1, i, i, count)

        marked[i] = True
    
    return int(count / 2)

# Main
if __name__ == '__main__':
    graph = [[0, 1, 0, 1, 0],
            [1 ,0 ,1 ,0, 1],
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0]]
            
    n = 4
    print("Total cycles of length ",n," are ",countCycles(graph, n))
```
</details>

<details>
<summary>BFS - accumulating cycle length and count</summary>

```python
def DFS(graph, marked, current_len, vert, start, n):
    """
    Utility function for DFS traversal that returns the count of paths.
    Uses 'incrementing logic' for current_len.
    """
    # Mark the current node as being part of the active path
    marked[vert] = True
    count = 0

    # Base Case: If the path length (current_len) reaches n-1 [3]
    if current_len == n - 1:
        # Before returning, unmark to allow this node in other paths
        marked[vert] = False
        
        # Check if the nth edge connects the current vertex back to start [3, 4]
        if graph[vert][start] == 1:
            return 1
        else:
            return 0

    # For searching every possible path of length (n-1) [1]
    for i in range(V):
        if not marked[i] and graph[vert][i] == 1:
            # Accumulate count from recursive calls using incrementing logic
            count += DFS(graph, marked, current_len + 1, i, start, n)

    # Backtracking: unmarking the vertex to make it usable again [2, 4]
    marked[vert] = False
    return count

def countCycles(graph, n):
    """
    Counts simple cycles of length n in an undirected graph.
    """
    # All vertices are marked un-visited initially
    marked = [False] * V
    total_cycles = 0

    # Only need to search using V - (n - 1) vertices [5, 6]
    for i in range(V - (n - 1)):
        # Start path building from current vertex i with length 0
        total_cycles += DFS(graph, marked, 0, i, i, n)
        
        # Once all cycles through vertex i are found, mark it permanently 
        # to avoid re-counting them in subsequent loops [2, 6]
        marked[i] = True

    # Every cycle is found twice (one for each direction), so divide by 2 [2, 7]
    return total_cycles // 2

# Driver Code
if __name__ == "__main__":
    # Example graph from source: Adjacency matrix representation
    graph = [
        [8]
    ]
    
    n = 4
    result = countCycles(graph, n)
    print(f"Total cycles of length {n} are {result}")
```

</details>

### [Disjoint set (Union-Find data structure)](https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/)
find relationship of a node and another -- direct or indirect 

[YouTube Tutorial with diagram](https://www.youtube.com/watch?v=ayW5B2W9hfo)

[Example problem and solution -- Number of Islands approach 3](#number-of-islands)

- `parent[]`: array that stores parent of the node (multi-dimension array can be represented in )
- `find(node)`: returns the meta parent of the node 
- `unionset()`
    - Path compression: flatten all child nodes under the root node (grouping nodes)
    - Union by rank: merge lower rank node to higher rank 

### Bellman-Ford algorithm--Detect a negative cycle in a Graph

<br>

> **Bellman-Ford algorithm** is used to compute <us>ingle source shortest path</u>. 

<br>

> 🐛 Negative weight cycle
>
> a cycle in a graph, whose sum of edge weights is negative

> 💡 Why Relaxing Edges (V - 1) times gives us Single Source Shortest Path?
>
> *A shortest path between two vertices can have at most (V - 1) edges.* It is not possible to have a simple path with more than (V - 1) edges (otherwise it would form a cycle). Therefore, repeating the relaxation process (V - 1) times ensures that all possible paths between source and any other node have been covered.

> 💡 Why Bellman-Ford works on Detection of a Negative Weight Cycle?
>
> As discussed, after (V - 1) relaxations of all the edges, we have single source shortest path in the graph.
>
> If one additional relaxation (Vth) for any edge is possible, it indicates that some edges with overall negative weight has been traversed once more. This indicates the presence of a negative weight cycle in the graph.

Seudo-code:
1. Initialisation
1. Relaxation for all edges for $V - 1$ times
1. To detect negative cycle, Relax for the $V$ -th time

<details>
<summary>Algorithm to Find Negative Cycle in a Directed Weighted Graph Using Bellman-Ford</summary>

```python
import math

class Edge: 
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph: 
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

def bellman_ford_detects_negative_cycle(graph, source, dist):
    """
    Runs Bellman-Ford from a given source.
    Returns True if a negative-weight cycle is reachable.
    """
    V = graph.V

    # Step 1: Initialize distances
    for i in range(V):
        dist[i] = math.inf
    dist[source] = 0

    # Step 2: Relaxation on all edges V - 1 times
    for _ in range(V - 1):
        for edge in graph.edges:
            u, v, w = edge.src, edge.dest, edge.weight

            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 3: Check for negative cycle
    for edge in graph.edges:
        u, v, w = edge.src, edge.dest, edge.weight

        if dist[u] != math.inf and dist[u] + w < dist[v]:
            return True # Negative cycle found
    
def has_negative_cycle_disconnected(graph):
    """
    Detects negative cycles even if the graph is disconnected.
    """
    V = graph.V
    visited = [False] * V
    dist = [math.inf] * V

    for i in range(V):
        if not visited[i]:
            if bellman_ford_detects_negative_cycle(graph, i, dist):
                return True
            
            # Mark all reachable vertices as visited
            for j in range(V):
                if dist[j] != math.inf:
                    visited[j] = True
    
    return False

if __name__ == '__main__':
    graph = Graph(5)

    graph.edges.append(Edge(0, 1, -1))
    graph.edges.append(Edge(0, 2, 4))
    graph.edges.append(Edge(1, 2, 3))
    graph.edges.append(Edge(1, 3, 2))
    graph.edges.append(Edge(1, 4, 2))
    graph.edges.append(Edge(3, 2, 5))
    graph.edges.append(Edge(3, 1, 1))
    graph.edges.append(Edge(4, 3, -3))

    print("Yes" if has_negative_cycle_disconnected(graph) else "No")
```

</details>

### Clone a Directed Acyclic Graph

<details>
<summary>Clone a Directed Acyclic Graph</summary>

```python
# define graph 
class Node():
    def __init__(self, key = None, neighbour = None):
        self.key = key 
        self.neighbour = neighbour


def printGraph(startNode: Node) -> None:
    visited_list = set()

    def dfs(node):
        visited_list.add(startNode) # Mark node visited
        for n in node.neighbour:
            print("edge %s-%s: %s-%s" %(hex(id(node)), hex(id(n)), node.key, n.key))

            # neighbour not visited, continue DFS to print the graph
            if n not in visited_list:
                dfs(n, visited_list)
    
    dfs(startNode)

# Version 3: ChatGPT
def cloneGraph(oldNode: Node) -> Node:
    visited_map = dict()

    def inner_method(node: Node) -> Node:
        # If node already cloned, add it to current node neighbour, without marking it visited again
        if node in visited_map:
            return visited_map[node]

        # Initiate a new node first
        clone = Node(node.key, [])
        visited_map[node] = clone # {originalNode: clonedNode} -- same but different in memory 

        # DFS
        for neighbor in node.neighbour:
            cloned_neighbor = inner_method(neighbor)
            clone.neighbour.append(cloned_neighbor)

        return clone
    
    return inner_method(oldNode)

# --- Initialisation in Main ---
# Instead of [False] * 5, use a dictionary to store the clones
n0, n1, n2 = Node(0, []), Node(1, []), Node(2, [])
n3, n4 = Node(3, []), Node(4)
n0.adj.append(n1)
n0.adj.append(n2)
n1.adj.append(n2)
n1.adj.append(n3)
n1.adj.append(n4)
n2.adj.append(n3)
n3.adj.append(n4)

new_root = cloneGraph(n0, visited)
printGraph(n0)
printGraph(new_root)
```

</details>

## Shortest Path

### Dijkstra's Algorithm

<details>
<summary>Implementation</summary>

```python



```


<details>

## Minimum Spanning Tree


## Topological Sorting

## Connectivity in Graph


## Maximum Flow in Graph


## Classic problems 




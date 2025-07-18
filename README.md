# Leetcode practice log

This is to track my progress in practicing Leetcode coding problems. It also serves as a documentation of my thoughts when cracking the problems.

This space saves coding problem encountered from any coding assessment for learning purpose only.

# Tips for Live Coding Interviews

## Common clarifications:

- How big is the size of the input?
- How big is the range of values?
- What kind of values are there? Are there negative numbers? Floating points? Will there be empty inputs? Is it string? 
- Are there duplicates within the input?
- What are some extreme cases of the input?
- How is the input stored? If you are given a dictionary of words, is it a list of strings or a trie?

## Steps:

1. Read the problem. Think about edge cases. Ask for clarifications
1. How you plan to solve it at a high level
1. Focus on solving! \
    Keep the conversation going, solicit feedback:
    - I have a feeling I could get the performance better here, I’d like to get this working first and circle back to it at the end with time permitting
    - For some reason I have a suspicion there might be edge cases that could bite us at this point, but I can’t put my finger on one…do you have any thoughts?
    - I had hoped that I could keep this in a single loop for performance, but at this point am not seeing a way around adding a second. If I have time at the end, I would definitely come back and tighten up some things, just as I would with real code before submitting a PR
1. Keep the code clean, use built-in function. 
1. Analyse time and space complexity before the interivewer asks you 
1. Test your code (dry run)

# Complexity Analysis

Runtime improvement
1. Less new variable creation
1. Ealry exit on invalid input
1. More specific `if` logic paths
1. Avoid unnecessary checks

# Algorithms

## Dynamic Programming

### When to Use Dynamic Programming (DP)?

#### Optimal Substructure

Optimal substructure means that we use the optimal results of subproblems to achieve the optimal result of the bigger problem. The solution to the larger problem (finding the minimum cost path from the source node to the destination node) can be constructed from the solutions to these smaller subproblems.

Consider the problem of finding the minimum cost path in a weighted graph from a source node to a destination node. We can break this problem down into smaller subproblems:

- Find the minimum cost path from the source node to each intermediate node.
- Find the minimum cost path from each intermediate node to the destination node.


#### Overlapping Subproblems

The same subproblems are solved repeatedly in different parts of the problem

Consider the problem of computing the Fibonacci series. To compute the Fibonacci number at index n, we need to compute the Fibonacci numbers at indices n-1 and n-2. 

### Approaches of Dynamic Programming (DP)

#### Top-Down Approach (Memoization)

keep the solution recursive and add a memoization table to avoid repeated calls of same subproblems

```python
# Python program to find
# fibonacci number using memoization.
def fibRec(n, memo):
  
    # Base case
    if n <= 1:
        return n

    # To check if output already exists
    if memo[n] != -1:
        return memo[n]

    # Calculate and save output for future use
    memo[n] = fibRec(n - 1, memo) + \
              fibRec(n - 2, memo)
    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)

n = 5
print(fib(n))
# Console output: 5
```

#### Bottom-Up Approach (Tabulation):

we start with the smallest subproblems and gradually build up to the final solution

- We write an **iterative** solution (avoid recursion overhead) and build the solution in bottom-up manner.
- We use a **dp table** where we first fill the solution for **base cases** and then fill the remaining entries of the table using recursive formula.
- We only use recursive formula on table entries and do not make recursive calls.

```python
# Python program to find
# fibonacci number using tabulation.
def fibo(n):
    dp = [0] * (n + 1)

    # Storing the independent values in dp
    dp[0] = 0
    dp[1] = 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 5
print(fibo(n))
# Console output: 5
```

## Hash Map

`zip(*grid)`: transpose 2D-array -- combine i-th elements of every row into the same tuple

# Data Structures

Basic operations: Add, Delete, Search, Modify

## Stack

LIFO array

### ✅ When to Use a Stack

| Category                           | Example Problems                                                                                                                            | Why Stack Works                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Balanced Symbols / Parentheses** | - Valid Parentheses (`"(()[]){}"`)<br>- HTML/XML tag matching                                                                               | Track opening symbols and match them in reverse order |
| **String Manipulation**            | - Remove adjacent duplicates<br>- Decode strings (e.g., `"3[a2[c]]"` → `"accaccacc"`)<br>- Backspace string comparison (`"ab#c"`, `"ad#c"`) | Undo-like operations or structure preservation        |
| **Backtracking**                   | - Maze / path traversal<br>- Undo operations                                                                                                | Stack holds states to backtrack to                    |
| **Evaluation of Expressions**      | - Infix to postfix conversion<br>- Evaluate RPN (Reverse Polish Notation)                                                                   | Operators and operands are managed in LIFO order      |
| **Tree/Graph Traversal**           | - Iterative DFS (Depth-First Search)<br>- Postorder traversal (without recursion)                                                           | Simulate recursion using a stack                      |
| **History Tracking**               | - Browser back button<br>- Undo in text editor                                                                                              | Keep track of previous states                         |
| **Monotonic Stack Problems**       | - Next Greater Element<br>- Stock Span<br>- Largest Rectangle in Histogram                                                                  | Maintain a stack of increasing/decreasing elements    |
| **Recursive Simulation**           | - Convert recursive functions into iterative ones                                                                                           | Explicitly manage the call stack                      |
| **Parsing Problems**               | - Parsing nested expressions or serialized structures                                                                                       | Manage nesting levels cleanly                         |


### Monotonic stack

## Graph

Reference: [Stack Overflow - Representing graphs (data structure) in Python](https://stackoverflow.com/a/30747003)

The most useful and efficient for graphs in Python: **a dict of sets**

```python
[('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
```

```python
import pprint
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
```


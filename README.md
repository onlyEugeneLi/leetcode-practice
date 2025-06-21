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
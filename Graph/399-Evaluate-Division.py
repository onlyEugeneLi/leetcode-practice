from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        defaultdict(data_type)

        Sets default value or empty data structure for each key

        For example: 
        - int: 0
        - list: []
        '''
        graph = defaultdict(list)
        num_of_values = len(values)

        '''
        Building the graph based on equaitons and values 

        equations = [["a","b"],["b","c"]], values = [2.0,3.0]

        Directed Graph:
        {
            a: [(b, 2), ]
            b: [(a, 1 / 2), (c, 3)]
            c: [(b, 1 / 3)]
        }
        '''
        for i in range(num_of_values):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        '''
        Construct DFS helper method

        <source> is where your search starts for each query

        <destination> is the target node you want to reach, but it does not change during the search for a single query. It is fixed for each query, so you can reference it directly from the enclosing scope (for-loop).
        '''
        def dfs(node, value):

            nonlocal answer
            visited.add(node)

            # When the target node is found, terminate the depth-first search
            if node == destination:
                answer = value
                return 
            
            # Look for target node down in each neighbour's direction
            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, value * weight) # Trace down the path and update the equation result
        
        '''
        Traverse queries
        '''
        query_result = []

        for source, destination in queries:
            # Invalid search (node does not exist), enter -1
            if source not in graph or destination not in graph:
                query_result.append(-1)
                continue
            
            # Start DFS
            visited = set()
            answer = -1 # Set default answer to -1 if query not found
            dfs(source, 1)

            query_result.append(answer)
        
        return query_result

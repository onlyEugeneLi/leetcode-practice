from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        num_of_values = len(values)
        # Graph
        # How to represent graph and adjacency in dict
        for i in range(num_of_values):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

        def dfs(node, value):
            nonlocal answer
            visited.add(node)
            if node == destination:
                answer = value
                return
            
            for neighbour, weight in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, value * weight)
            
        enquiry_result = []

        for source, destination in queries:
            if source not in graph or destination not in graph:
                enquiry_result.append(-1)
                continue
            
            visited = set()
            answer = -1
            dfs(source, 1)

            enquiry_result.append(answer)
        
        return enquiry_result

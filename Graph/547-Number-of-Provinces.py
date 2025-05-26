from typing import List
from collections import deque

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # Base case
        if not isConnected:
            return 0
        
        # Initialise variables
        num_of_cities = len(isConnected)
        visited_cities = [False] * num_of_cities
        num_of_provinces = 0 # stores the result

        # Depth first search
        def dfs(node):
            for next_city in range(num_of_cities): # Check connectivity for each city
                # Check connectivity and visited status
                if isConnected[node][next_city] and not visited_cities[next_city]:
                    visited_cities[next_city] = True
                    dfs(next_city) # Keep exploring cities until no more cities can be reached

        # Traverse each province from each city
        for city in range(num_of_cities):
            if not visited_cities[city]: # if the city was not visited, then start exploring
                num_of_provinces += 1
                visited_cities[city] = True
                # DFS
                dfs(city)

        return num_of_provinces

    def findCircleNum_exceed_time_limit_attempt(self, isConnected: List[List[int]]) -> int:

        # Initialise variables
        visited_cities = set([0])
        next_stops = deque([0]) # stack: append(), pop()
        num_of_provinces = 0 # stores the result

        # Go to 1st city --> collect reachable cities (add into the queue)
        while len(visited_cities) < len(isConnected):

            while next_stops:
                city = next_stops.popleft()
                for i in range(len(isConnected[city])):
                    if isConnected[city][i]:
                        next_stops.append(i)
            # When all cities in a province are traversed, count +1 province, and look for next yet-to-vist city

            for i in range(len(isConnected)):
                if i not in visited_cities:
                    next_stops.append(i)
                    break

            num_of_provinces += 1

        return num_of_provinces
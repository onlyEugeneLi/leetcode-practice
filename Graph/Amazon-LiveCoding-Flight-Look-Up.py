# Amazon Live Coding - Flight Look Up
# Date: 2025-06-23

# Problem
# Assume the dataset is a list of direct flights between cities, like:
# 
# Seattle <-> Houston
# Seattle <-> Dallas
# Houston <-> New York City

# Question:
# 1. Does a direct flight from A to B exist?
# - How would you model the dataset?
#   Answer: graph, implemented as a dictionary where keys are source cities
#           and values are lists of destination cities.
# 
# - How would you implement the solution?

# Data structure to represent the flight connections

# 1. Adjacency List (Hash Map → List / Set)
# 2. Adjacency Matrix
# 3. Edge List
# 4. Graph with Weighted Edges
# 6. Multi-Index Graph (Advanced / Production)

# Interview guidance:

# Interview Recommendation (Very Important)
# Say this:

# “I’ll start with an adjacency list using a dictionary of sets.
# It’s optimal for sparse graphs and supports fast lookups and BFS-style queries.”

# Then mention extensibility:

# “If costs or constraints are needed, I’ll store metadata on edges.”

# generalize this to exactly k stops

# return shortest one-stop route

# handle undirected flights

# add cycle prevention

# refactor your code to production-grade

# add k-stop path enumeration

# show Dijkstra on flights

# simulate airline pricing

flights = {
    "Seattle": ["Houston", "Dallas"],
    "Houston": ["New York City"],
    "Dallas": ["New York City"],
    "New York City": [],
}

def has_direct_flight(source, destination):
    """
    Check if there is a direct flight from source to destination.
    
    :param source: Source city
    :param destination: Destination city
    :return: True if direct flight exists, False otherwise
    """
    return destination in flights.get(source, [])
# Time complexity: O(1) on average, O(n) in the worst case (if we have to check all destinations)

# 2. Can I get from city A to B within k max stops?

from collections import deque

def can_reach_within_k_stops(start, end, k):
    queue = deque([(start, 0)])  # (city, stops)
    visited = set()

    while queue:
        city, stops = queue.popleft()
        if city == end:
            return True
        if stops == k:
            continue
        for neighbor in flights[city]:
            if (neighbor, stops + 1) not in visited:
                visited.add((neighbor, stops + 1))
                queue.append((neighbor, stops + 1))
    
    return False

# Post interview study:

# 3. “Return one-stop routes only if no direct flight exists”

def routes_via_one_city(start, end):
    # If direct flight exists, return nothing
    if end in flights.get(start, []):
        return []

    routes = []
    for intermediate in flights.get(start, []):
        if end in flights.get(intermediate, []):
            routes.append([start, intermediate, end])

    return routes


# Interview Recommendation (Very Important)
# Say this:

# “I’ll start with an adjacency list using a dictionary of sets.
# It’s optimal for sparse graphs and supports fast lookups and BFS-style queries.”

# Then mention extensibility:

# “If costs or constraints are needed, I’ll store metadata on edges.”





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
        for neighbor in graph[city]:
            if (neighbor, stops + 1) not in visited:
                visited.add((neighbor, stops + 1))
                queue.append((neighbor, stops + 1))
    
    return False



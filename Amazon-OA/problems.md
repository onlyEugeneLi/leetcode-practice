Coding interviews
---

## Problem 1

Given: A list of flight paths, where each path is a tuple (origin, destination).

Task: 

Find all direct flights from a given origin airport A to a destination airport B.

Find all connecting flights from airport A to airport B that stop at exactly one intermediate airport C.

```python
from collections import defaultdict

def find_flights(flights, start_airport, end_airport):
    # 1. Build the graph (adjacency list)
    # The graph is a dictionary where keys are airports and values are lists of destination airports
    graph = defaultdict(list)
    for origin, destination in flights:
        graph[origin].append(destination)
    
    # 2. Find direct flights
    direct_flights = []
    if end_airport in graph.get(start_airport, []):
        direct_flights.append([start_airport, end_airport])
    
    # 3. Find connecting flights via a third airport
    connecting_flights = []
    # Check all possible intermediate airports (C) that A flies to
    for intermediate_airport in graph.get(start_airport, []):
        # Ensure the intermediate airport is not the destination (to avoid miscounting direct flights)
        if intermediate_airport != end_airport:
            # Check if there is a flight from the intermediate airport (C) to the final destination (B)
            if end_airport in graph.get(intermediate_airport, []):
                connecting_flights.append([start_airport, intermediate_airport, end_airport])

    return direct_flights, connecting_flights

# Example Usage:
flights_list = [
    ("JFK", "LAX"),
    ("JFK", "MIA"),
    ("MIA", "LAX"),
    ("LAX", "ORD"),
    ("JFK", "ORD"),
    ("ORD", "MIA"),
    ("MIA", "JFK"),
    ("LAX", "JFK")
]

origin_A = "JFK"
destination_B = "LAX"

direct, connecting = find_flights(flights_list, origin_A, destination_B)

print(f"Direct flights from {origin_A} to {destination_B}:")
for route in direct:
    print(f"- {route[0]} -> {route[1]}")

print(f"\nConnecting flights from {origin_A} to {destination_B} (one stop):")
for route in connecting:
    print(f"- {route[0]} -> {route[1]} -> {route[2]}")

# Example 2
origin_C = "JFK"
destination_D = "ORD"
direct_2, connecting_2 = find_flights(flights_list, origin_C, destination_D)
print(f"\nDirect flights from {origin_C} to {destination_D}:")
for route in direct_2:
    print(f"- {route[0]} -> {route[1]}")
print(f"\nConnecting flights from {origin_C} to {destination_D} (one stop):")
for route in connecting_2:
    print(f"- {route[0]} -> {route[1]} -> {route[2]}")
```
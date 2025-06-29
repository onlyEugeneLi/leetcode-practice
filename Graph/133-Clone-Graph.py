"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base case: When no graph exists
        if not node: 
            return node
        
        # Queue: to store neighbours to visit
        new_neighbours = deque([node])

        # Visited note (value - unique): so we don't revisit nodes  // Dict can ensure no repetition 
        # Clone variable -- node table for retrieval: 
            # key - label(index)
            # value - the node instance reference
        clones = {node.val: Node(node.val)}

        # BFS: copy original graph
        while new_neighbours:
            # Travel to a new node
            curr_node = new_neighbours.popleft()
            # Prepare the empty clone vessel to copy neighbour information 
            curr_clone = clones[curr_node.val]

            # Explore neighbours
            for n in curr_node.neighbors:
                if n.val not in clones: # Check to avoid repetition
                    # Add new nodes: Create a key for new neighbours
                    clones[n.val] = Node(n.val)
                    # Next to explore: Add current node's neighbours to the BFS search list 
                    new_neighbours.append(n)
                
                # Populate the neighbour list for current clone node
                curr_clone.neighbors.append(clones[n.val])
        
        # Return the cloned input node: using key as a reference because they're unique to each node
        return clones[node.val]
    
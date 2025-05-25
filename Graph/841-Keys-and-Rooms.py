from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        Runtime: 70ms (Beats 5.17%)
        Memory: 18.24MB (Beats 47.56%)
        '''
        # Total number of room -- total number of nodes in the graph
        total_room_number = len(rooms)
        visited_rooms = deque([0])
        next_rooms = deque(rooms[0]) # Go to room 0 and get the keys
        # Traverse the graph with BFS
        while next_rooms:
            room = next_rooms.popleft()
            # Check if the room has been visited before
            if room not in visited_rooms:
                visited_rooms.append(room)
            # Visit the room and get new keys
            if rooms[room]:
                for i in range(len(rooms[room])):
                    if rooms[room][i] not in visited_rooms:
                        next_rooms.append(rooms[room][i])
            if len(visited_rooms) == len(rooms):
                return True

        return False

    def canVisitAllRooms_solution(self, rooms: List[List[int]]) -> bool:
        '''
        Runtime: 0ms (Beats 100%)
        Memory: 18.29MB (Beats 47.56%)
        '''
        visited_rooms = set()
        next_rooms = [0] # Go to room 0 and get the keys
        # Traverse the graph with BFS
        while next_rooms:
            room = next_rooms.pop()
            visited_rooms.add(room)
            # Visit the room and get new keys
            for key in rooms[room]:
                if key not in visited_rooms:
                    next_rooms.append(key)

        return len(visited_rooms) == len(rooms)
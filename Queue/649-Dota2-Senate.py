from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Enumerate --> (index, element)
        _rad = deque([i for i, s in enumerate(senate) if s =='R'])
        _dir = deque([i for i, s in enumerate(senate) if s =='D'])

        next_position = len(senate)
        while _rad and _dir:
            if _rad[0] < _dir[0]:
                _rad.append(next_position)
            else:
                _dir.append(next_position)
            _rad.popleft()
            _dir.popleft()
            next_position += 1
        return 'Radiant' if _rad else 'Dire'
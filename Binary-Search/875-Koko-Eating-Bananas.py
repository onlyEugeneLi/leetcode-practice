from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k -- range(min, max + 1) of piles
        # finish all bananas in h hours

        # h and length(piles)
        # if h == length(piles) ==> k = max(piles)

        '''
        Intuition
        Process of eating all bananas:
        while elasped_time < h:
            while piles:
                if piles[i] >= k:
                    piles[i] -= k
                elif piles[i] < k:
                    piles.pop(i)


            elasped_time += 1

        -----------------------------------
        Doesn't work
        -----------------------------------
        '''

        '''
        Use total time that will take Koko to eat all bananas at rate of k as a measure

        (not specify that the time has to be exact h hours)

        And left < right pointer

        '''

        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2
            
            ''' ceil(p / mid) = (p + mid - 1) // mid '''
            time_to_eat_all = sum((p + mid - 1) // mid for p in piles)

            if time_to_eat_all <= h: # Eating to fast, try and slow down
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k
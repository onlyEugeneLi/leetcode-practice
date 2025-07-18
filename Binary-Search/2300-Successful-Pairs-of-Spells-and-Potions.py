from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        Objective: a count of valid potion for each spell
        Valid -- spell * potion >= success 

        Intuition:
        nested for loops
        for spell :
            for potion:
                count
                update answer List

        Improvement:

        Binary search -- O(log(n))
        >> sort potion
        >> spell * mid potion
        >> if ...: first half ? second half
        >> answer = length - index 
        '''
        
        potions.sort() # sorting potions in ascending order
        pairs = [] # empyt pairs array

        for spell in spells:
            low, high = 0, len(potions) # low & high pointers
            while low < high: 
                mid = (low + high) // 2 # floor dvision -- round down to nearest integer

                # Look for the smallest number's index that meets the requirement
                if potions[mid] * spell >= success:
                    high = mid # move high pointer to mid
                else:
                    low = mid + 1
            # Low index found, save correct number of valid potions
            pairs.append(len(potions) - low) # Number of valid potions

        return pairs
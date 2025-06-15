from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # Store temperatures index
        answer = [0] * len(temperatures)  # Counters to next warmer day for each day

        for curr_temp_index, curr_temp in enumerate(temperatures):

            '''
            Looking for next warmer day
            but track __decreasing__ temperatures to count days elasped until the next warmer day
            '''

            # Maintain a monotonic stack: temperatures in the stack are always in decreasing order
            # Detect temperature increase: latest temperature > previous temperature (top of the stack)
            # When temperature increases, the top higher temperature record immediately gets deleted to manintain the __decreasing__ order
            # until it finds a temperature that is higher than the current temperature
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_low_temp_index = stack.pop() 
                # Trace back to the previous lower temperature to compute the days elapsed until the next warmer day
                answer[prev_low_temp_index] = curr_temp_index - prev_low_temp_index

            # If temperature keeps dropping, keep adding lower temperature record
            stack.append(curr_temp_index) # Update the stack with lower temperature index when no previous lower temperature day is found in the stack

        return answer

from math import floor
from math import ceil
class Solution():
    def calcMaxQualityScore(impactFactor, ratings):
        # Method 1 brute force
        maxScore = float("-inf")
        n = len(ratings)
        for i in range(n):
            for j in range(i, n):
                amp_sum = 0
                adj_sum = 0
                for k in range(i, j+ 1):
                    if ratings[k] >= 0:
                        amp_sum += ratings[k] * impactFactor
                        adj_sum += floor(ratings[k] / impactFactor)
                    else:
                        amp_sum += ratings[k]
                        adj_sum += ceil(ratings[k] / impactFactor)
                maxScore = max(maxScore, max(amp_sum, adj_sum))

        return maxScore

# Perform unit test on the method
import unittest
class testCalcMaxQualityScore(unittest.TestCase):
    def test_basic_case(self):
        impactFactor = 2
        ratings = [1, -2, 3, -4]
        result = Solution().calcMaxQualityScore(impactFactor, ratings)
        self.assertEqual(result, 3) # self.assertEqual(result, expected output)

# Tescases

# # Testcase 1
# impactFactor = 2
# ratings = [4, -5, 5, -7, 1]
# ans = 11

# Testcase 2
impactFactor = 3
ratings = [5, -3, -3, 2, 4]
ans = 11
print(
    f"{'Impact Factor:':<20}{impactFactor:>20}",
    f"{'Ratings:':<20}{str(ratings).replace('[', '').replace(']', ''):>20}",
    f"{'Expected output:':<20}{ans:>20}",
    f"{'My output:':<20}{Solution().calcMaxQualityScore(impactFactor, ratings):>20}",
    sep="\n"
)
class Solution:
    def numTilings(self, n: int) -> int:
        # Base case
        # if n == 1:
        #     return 1
        
        # n = 1 --> 1
        # n = 2 --> 
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i - 1] * 2 + dp[i - 3]) % (10e9 + 7)
        return int(dp[n - 1])

print(Solution().numTilings(1))
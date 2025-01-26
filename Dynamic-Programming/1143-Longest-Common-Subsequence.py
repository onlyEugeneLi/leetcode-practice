class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D dp
        # Bottom up dynamic programming approach
        # Traverse array 
        m, n = len(text1), len(text2)
        # dp = [[0] * (n + 1) ] * (m + 1)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        '''
        dp table
            a b c d e
          0 0 0 0 0 0
        a 0 1 1 1 1 1
        c 0 1 1 2 2 2
        e 0 1 1 2 2 3

        '''
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    # Matched! Last top-left diagonal element + 1
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    # Not matched. Whichever is bigger, left or top element 
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        
        return dp[m][n]

'''
Test
'''
# t1 = "ace"
t2 = "abcba"
# t2 = "abcde"
t1 = "abcbcba"
print(Solution().longestCommonSubsequence(t1, t2))
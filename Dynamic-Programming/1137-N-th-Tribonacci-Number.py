class Solution_brute_force:
    def tribonacci(self, n: int) -> int:
        i = 0
        T_0 = 0
        T_1 = 1
        T_2 = 1
        T_3 = 0 # Declare T_3 in wider scope, instead of local variabla in while loop
        print(f"\nT_{i} = {T_0}, T_{i+1} = {T_1}, T_{i+2} = {T_2}")
        if n == 0:
            return T_0
        if n == 1:
            return T_1
        if n == 2:
            return T_2
        while(i < n - 2):
            # T_3 = T_0 + T_1 + T_2
            # T_0, T_1, T_2 = T_1, T_2, T_3
            T_0, T_1, T_2 = T_1, T_2, T_0 + T_1 + T_2
            print(f"T_{i} = {T_0}, T_{i+1} = {T_1}, T_{i+2}={T_2} || T_{i+3} = {T_3}")
            i += 1
        return T_3

'''
Time complexity: O(3^n) for brute force recursive solution
Space compleixity for brute force recursive solution: O(n) due to recursion stack
'''
class Solution_brute_force_recursive_TLE:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

class Solution_dynamic_programming_bottom_up:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
    
class Solution_dynamic_programming_top_down:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            
            memo[n] = helper(n - 1) + helper(n - 2) + helper(n - 3)
            return memo[n]

        return helper(n)
        
s = Solution_brute_force().tribonacci
n = int(input("\nEnter a number: "))
print(f"\nAnswer:\n" 
      f"T_{n} = {s(n)}\n")
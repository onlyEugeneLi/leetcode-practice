class Solution:
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
            T_3 = T_0 + T_1 + T_2
            T_0, T_1, T_2 = T_1, T_2, T_3
            print(f"T_{i} = {T_0}, T_{i+1} = {T_1}, T_{i+2}={T_2} || T_{i+3} = {T_3}")
            i += 1
        return T_3
    

s = Solution().tribonacci
n = int(input("\nEnter a number: "))
print(f"\nAnswer:\n" 
      f"T_{n} = {s(n)}\n")
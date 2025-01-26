class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab, xor, ans = a | b, (a | b) ^ c, 0
        # Intuition:
        # 1. 初始的a | b结果跟c对比，看哪里不同
        # 2. 想把a | b跟c不同的位改成c，a | b要改的话，看回去a和b的对应的位要怎么变
        # 3. 基本就四种情况 1 | 1 = 1, 1 | 0 = 1, 0 | 1 = 1, 0 | 0 = 0
        # 4. 知道a和b的位是哪种组合，再看要改成输出什么样，就知道要改多少位
        # 5. 最终发现：0 | 0 和 1 | 0 只用改一次，1 | 1 改为0要改2次
        # xor若为0，则为相同，否则有不同之处变为1
        # mask? 怎么按位迭代更新
        # Iterate through 30 bits
        for i in range(31): # 2^30 > 10^9 题目限制数最大值10^9
            mask = 1 << i
            if xor & mask > 0: # 看xor和mask是否相同
                # 对比后发现如果a和b该位相同，则两个位都要改
                # 否则只有一个位要改
                ans += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
            
            return ans
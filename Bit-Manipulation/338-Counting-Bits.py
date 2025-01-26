class Solution:
    def countBits(self, n: int) -> list[int]:
        counter = [0]
        # 解题思路
        # 二进制从0开始，"1"的个数为0. 增长1变成数字1.
        # 数字1的二进制中，"1"的个数为1。然后偶数不变，奇数加1.
        for i in range(1, n + 1):
            # Bitwise operator >> and <<
            # Bitwise "and": &
            # Complement of x: ~x
            # Bitwise xor (exclusive or): x ^ y
            counter.append(counter[i >> 1] + i % 2)
            # 2(0010) * 2 -> 4(0100)
            # >> right bit shifting = dividing by 2.
            # 奇数 = 偶数 + 1
            # 偶数的二进制1的个数都一样，x2不过增加0的个数而已

            # 想要知道任意一个数二进制的1的个数，从1开始递加
            # 每个数回溯到前一个数，然后作增加或不变
            # 奇数 + 1，偶数 + 0
            # i % 2: odd number -> 1, even number -> 0
        return counter

    # # Brute force
    # def countBits(self, n: int) -> list[int]:
    #     ans = []
    #     # Decial -> Binary conversion
    #     for i in range(n + 1):
    #         ans.append(bin(i).count("1")) # bin() returns binary form in a string
    #                                       # count the number of 1 in the string
    #     return ans
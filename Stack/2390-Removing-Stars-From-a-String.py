class Solution:
    def removeStars(self, s: str) -> str:
        # Method 1 Stack - list: 
        # 如果不是*就是堆字母，
        # 如果下一个是*，就把上一次堆上去的字母弹出（如果堆里还有字母的话）
        ans = []
        for i in s:
            if i != '*':
                ans.append(i)
            elif ans:
                ans.pop()
        
        return ''.join(ans)
    
        # # Method 2 Stack - string
        # a = ''
        # for char in s:
        #     if char == '*':
        #         a = a[1:]
        #     else:
        #         # 反向加字母
        #         a = char + a
        # return a[::-1]
    
print(Solution().removeStars("leet**cod*e"))
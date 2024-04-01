# 2810. 故障键盘
# https://leetcode.cn/problems/faulty-keyboard/description
class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res = res + s[i] if s[i] != 'i' else ''.join(reversed(res))
        return res


solution = Solution()
s = 'string'
print(solution.finalString(s))

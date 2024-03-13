# 2864. 最大二进制奇数
# https://leetcode.cn/problems/maximum-odd-binary-number/description
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = [0] * 2
        for c in s:
            count[ord(c) - ord('0')] += 1
        count[ord('1') - ord('0')] -= 1
        res = ''
        for i in range(0, count[1]):
            res += '1'
        for i in range(0, count[0]):
            res += '0'
        res += '1'
        return res


solution = Solution()
res = solution.maximumOddBinaryNumber('0101')
print(res)

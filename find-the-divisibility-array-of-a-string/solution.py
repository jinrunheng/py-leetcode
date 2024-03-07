# 2575. 找出字符串的可整除数组
# https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/description/
from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        r = 0
        for w in word:
            if (r * 10 + int(w)) % m == 0:
                res.append(1)
            else:
                res.append(0)
            r = (r * 10 + int(w)) % m
        return res


solution = Solution()
word = '998244353'
m = 3
arr = solution.divisibilityArray(word, m)
for i in arr:
    print(i)

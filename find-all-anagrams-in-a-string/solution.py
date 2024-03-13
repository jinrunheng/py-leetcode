# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 超出时间限制
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        plen = len(p)
        slen = len(s)
        pCount = self.getCount(p)
        for i in range(slen - plen + 1):
            if self.getCount(s[i:i + plen]) == pCount:
                res.append(i)
        return res

    def getCount(self, s: str) -> List[int]:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        return count

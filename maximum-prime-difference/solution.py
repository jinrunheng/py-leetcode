# https://leetcode.cn/problems/maximum-prime-difference/
# 3115. 质数的最大距离
import math
from typing import List


class Solution:

    def isPrime(self, num: int) -> bool:
        if num in [2, 3, 5, 7, 11,
                   13, 17, 19, 23, 29,
                   31, 37, 41, 43, 47,
                   53, 59, 61, 67, 71,
                   73, 79, 83, 89, 97]:
            return True
        else:
            return False

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l = -1
        r = -1
        for i in range(0, len(nums)):
            if l == -1 and self.isPrime(nums[i]):
                l = i
            if self.isPrime(nums[i]):
                r = i
        return r - l

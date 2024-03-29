# 2908. 元素和最小的山形三元组 I
# https://leetcode.cn/problems/minimum-sum-of-mountain-triplets-i/description
from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = 1000
        for i in range(1, len(nums) - 1):
            leftMin = self.getMin(nums, 0, i - 1)
            rightMin = self.getMin(nums, i + 1, len(nums) - 1)
            if leftMin < nums[i] > rightMin:
                res = min(res, (leftMin + rightMin + nums[i]))
        return res if res != 1000 else -1

    def getMin(self, nums: List[int], i: int, j: int) -> int:
        res = 1000
        if i == j:
            return nums[i]
        else:
            for k in range(i, j + 1):
                res = min(res, (nums[k]))
        return res


solution = Solution()
nums = [5, 4, 8, 7, 10, 2]
res = solution.minimumSum(nums)
print(res)

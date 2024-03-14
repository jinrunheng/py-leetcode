from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums_len = len(nums)
        res = nums[nums_len - 1]
        for i in range(nums_len - 2, -1, -1):
            if res >= nums[i]:
                res += nums[i]
            else:
                res = nums[i]
        return res

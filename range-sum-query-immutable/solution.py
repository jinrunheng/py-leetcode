from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.pre_sum[i + 1] = self.pre_sum[i] + nums[i]

    # [-2, 0, 3, -5, 2, -1]
    # [0, -2,-2, 1, -4,-2, -3]
    #  2-5 --> -1
    #  0-2 --> 1
    # pre[6] - pre[2] = -1
    # pre[3] - pre[0] = 1
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))

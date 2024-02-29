# 2673. 使二叉树所有路径值相等的最小代价
# https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/description/
from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        # 整除
        lastNonChildNodeIdx = n // 2 - 1
        for i in range(lastNonChildNodeIdx, -1, -1):
            res += abs(cost[i * 2 + 1] - cost[i * 2 + 2])
            cost[i] += max(cost[i * 2 + 1], cost[i * 2 + 2])
        return res


n = 7
cost = [1, 5, 2, 2, 3, 3, 1]
solution = Solution()
res = solution.minIncrements(n, cost)
print(res)

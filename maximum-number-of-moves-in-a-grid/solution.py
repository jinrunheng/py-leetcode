# 2684. 矩阵中移动的最大次数
# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/description
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        res = 0
        dp: List[List[int]] = [[0] * len(grid[0]) for _ in range(len(grid))]
        for j in range(len(grid[0]) - 2, -1, -1):
            for i in range(0, len(grid), 1):
                dp[i][j] = self.process(grid, dp, i, j)
        for i in range(0, len(grid)):
            res = max(res, dp[i][0])
        return res

    def process(self, grid: List[List[int]], dp: List[List[int]], i: int, j: int) -> int:
        res1, res2, res3 = 0, 0, 0
        row = len(grid)
        if i - 1 >= 0 and grid[i - 1][j + 1] > grid[i][j]:
            res1 = dp[i - 1][j + 1] + 1
        if grid[i][j + 1] > grid[i][j]:
            res2 = dp[i][j + 1] + 1
        if i + 1 < row and grid[i + 1][j + 1] > grid[i][j]:
            res3 = dp[i + 1][j + 1] + 1
        return max(res1, res2, res3)


solution = Solution()
grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
print(solution.maxMoves(grid))

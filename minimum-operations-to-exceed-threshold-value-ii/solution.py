# 3066. 超过阈值的最少操作数 II
# https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/description/
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
        res = 0
        while minHeap and len(minHeap) >= 2:
            if minHeap[0] >= k:
                break
            else:
                x = heapq.heappop(minHeap)
                y = heapq.heappop(minHeap)
                combined = min(x, y) * 2 + max(x, y)
                heapq.heappush(minHeap, combined)
                res += 1
        return res

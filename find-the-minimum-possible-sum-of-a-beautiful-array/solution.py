# 2834. 找出美丽数组的最小和
# https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/description
# 超出内存限制
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        a_set = set()
        t = 1
        res = 0
        for i in range(0, n):
            if len(a_set) == 0:
                a_set.add(t)
                a_set.add(target - t)
                res += t
                t += 1
            else:
                while target - t in a_set:
                    t += 1
                a_set.add(t)
                a_set.add(target - t)
                res += t
                t += 1
        return res % (10 ** 9 + 7)


solution = Solution()
n = 2
target = 3
res = solution.minimumPossibleSum(n, 3)
print(res)

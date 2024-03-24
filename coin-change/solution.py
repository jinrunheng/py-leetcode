# 322. 零钱兑换
# https://leetcode.cn/problems/coin-change/description
from typing import List


class Solution:
    '''
    sort coins
    [5,2,1]

    '''

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        coins.sort(reverse=True)
        for coin in coins:
            if amount < coin:
                continue
            else:
                res += amount // coin
                amount %= coin
        if amount != 0:
            return -1
        else:
            return res


s = Solution()
amount = 3
coins = [2]
print(s.coinChange(coins, amount))

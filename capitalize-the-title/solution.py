# 2129. 将标题首字母大写
# https://leetcode.cn/problems/capitalize-the-title/description
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        split = title.split(' ')
        res = []
        for s in split:
            if len(s) > 2:
                res.append(s.title())
            else:
                res.append(s.lower())
        return ' '.join(res)


solution = Solution()
title = "capiTalIze tHe titLe"
res = solution.capitalizeTitle(title)
print(res)

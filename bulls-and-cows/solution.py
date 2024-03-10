# 299. 猜数字游戏
# https://leetcode.cn/problems/bulls-and-cows
# secret
# 1 -> 1
# 8 -> 1
# 0 -> 1
# 7 -> 1

# guess
# 7 -> 1
# 8 -> 1
# 1 -> 1
# 0 -> 1
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_left = []
        guess_left = []
        len_secret = len(secret)

        for i in range(len_secret):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_left.append(secret[i])
                guess_left.append(guess[i])

        secret_dict = {}
        guess_dict = {}

        for char in secret_left:
            if char in secret_dict:
                secret_dict[char] += 1
            else:
                secret_dict[char] = 1
            if char in guess_dict:
                guess_dict[char] += 1
            else:
                guess_dict[char] = 1

        for char in guess_left:
            if char in secret_dict and secret_dict[char] > 0:
                cows += 1
                secret_dict[char] -= 1

        return str(bulls) + "A" + str(cows) + "B"


solution = Solution()
secret = "1123"
guess = "0111"
res = solution.getHint(secret, guess)
print(res)

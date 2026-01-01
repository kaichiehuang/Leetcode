#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i+j] += digit
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10

        res = res[::-1]
        beginning = 0
        while beginning < len(res) and res[beginning] == 0:
            beginning += 1

        res = map(str, res[beginning:])
        return "".join(res)


# @lc code=end


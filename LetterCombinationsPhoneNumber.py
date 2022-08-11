# https://www.youtube.com/watch?v=0snEunUacZY&ab_channel=NeetCode


class Solution(object):
    def letterCombinations(self, digits):
        result = []
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, current_str):
            if len(current_str) == len(digits):
                result.append(current_str)
                return
            for char in digitsToChar[digits[i]]:
                backtrack(i+1, current_str + char)

        if digits:
            backtrack(0, "")

        return result


if __name__ == '__main__':
    digits = ""
    obj1 = Solution()
    print(obj1.letterCombinations(digits))

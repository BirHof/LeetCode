# 13. Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0

        for i, elem in enumerate(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]

        return sum

"""
"LVIII" = ['L','V','I','I','I'] = 58
"MCMXCIV" = ['M','C','M','X','C','I','V'] = 1994
"""
obj = Solution()
str1 = ['M','C','M','X','C','I','V']
out1 = obj.romanToInt(str1)
print(out1)

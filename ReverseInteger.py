import sys
# 7. Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            str1 = str(x)
            int_r = int(str1[::-1])
        else:
            str1 = str(-x)
            int_r = int('-' + str1[::-1])

        if not (-2 ** 31 <= int_r <= (2 ** 31 - 1)):
            return 0

        return int_r


if __name__ == '__main__':
    x = -129
    obj1 = Solution()
    ans = obj1.reverse(x)
    print(f"Input int: {x}")
    print(f"Reversed int: {ans}")

# https://www.youtube.com/watch?v=Fi5INvcmDos&ab_channel=QuinstonPimenta
# 5. Longest Palindromic Substring
class Solution1(object):
    def goBothWays(self, s, i_left, i_right):
        L = len(s)
        if i_left < 0 or i_right > L - 1 or s[i_left] != s[i_right]:
            return 0
        else:
            return 2 + self.goBothWays(s, i_left - 1, i_right + 1)

    def longestPalindrome(self, s):
        loc_odd = [0]*len(s)
        loc_even = [0] * len(s)

        for i in range(len(s)):
            loc_odd[i] = 1 + self.goBothWays(s, i-1, i+1)
        #print(f"Odd: {loc_odd}")

        for i in range(len(s)):
            loc_even[i] = self.goBothWays(s, i, i+1)
        #print(f"Even: {loc_even}")

        odd_max = max(loc_odd)
        odd_max_idx = loc_odd.index(odd_max)
        even_max = max(loc_even)
        even_max_idx = loc_even.index(even_max)

        #print(f"odd_max_idx: {odd_max_idx}, even_max_idx: {even_max_idx}")

        if odd_max > even_max:
            step = odd_max // 2
            i_L = odd_max_idx - step
            i_R = odd_max_idx + step
        else:
            step = int(even_max / 2)
            i_L = even_max_idx - step + 1
            i_R = even_max_idx + step

        return s[i_L:i_R+1]


# Using table
class Solution2(object):
    def __init__(self):
        self.s = None
        self.L = 0
        self.h_table = None

    def print_table(self):
        for i in range(self.L):
            print(self.h_table[i])

    def longestPalindrome(self, s):
        self.s = s
        self.L = len(s)
        self.h_table = [[None] * self.L for _ in range(self.L)]
        for i in range(self.L):
            self.h_table[i][i] = True
        self.best_idx = [0, 0]

        # second diagonal
        for i in range(self.L-1):
            j = i + 1
            if s[i] == s[j]:
                self.h_table[i][j] = True
                self.best_idx = i, j
            else:
                self.h_table[i][i + 1] = False

        #self.print_table()

        for k in range(2, self.L):
            i = -1
            for j in range(k, self.L):
                i += 1
                #print(f"index: {i},{j}")
                if s[i] == s[j] and self.h_table[i+1][j-1]:
                    self.h_table[i][j] = True
                    self.best_idx = i, j

                else:
                    self.h_table[i][j] = False

        #self.print_table()
        #print(self.best_idx[0], self.best_idx[1])
        return self.s[self.best_idx[0]:self.best_idx[1]+1]

if __name__ == "__main__":
    s = "babad"
    s = "cbbd"
    s = "gftdoabccba"
    s = "gcbabcs"

    print(s)
    obj1 = Solution1()
    print(obj1.longestPalindrome(s))

    obj2 = Solution2()
    print(obj2.longestPalindrome(s))


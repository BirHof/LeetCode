# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        my_set = set()
        pointer_rear = 0
        max_window = 0
        #print(s)
        for pointer_front in range(len(s)):
            #print("letter: " + s[pointer_front])
            while s[pointer_front] in my_set:
                my_set.remove(s[pointer_rear])
                pointer_rear += 1
            #print(pointer_rear, "  ", pointer_front)
            my_set.add(s[pointer_front])
            max_window = max(max_window, pointer_front - pointer_rear + 1)

        return max_window



odj1 = Solution()
if __name__ == '__main__':
    s = "pwwkew"
    s = "aabbccddabcd"
    ans = odj1.lengthOfLongestSubstring(s)
    print(f"Input string: {s}")
    print(f"max length: {ans}")

"""
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
"""


"""
set1 = {"tiger", "amir", "biro"}
namelist = ["ruth", "dan"]

print(set1)
set1.add("yona")
print(set1)
set1.update(namelist)
print(set1)

# set1.remove("sami")
# print(set1)
set1.discard("sami")
print(f"discard sami: {set1}")
"""

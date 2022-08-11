# https://www.youtube.com/watch?v=fMSJSS7eO1w&ab_channel=NeetCode
# 48. Rotate Image

class Solution(object):
    def rotate(self, matrix):
        left = 0
        right = len(matrix)-1
        
        while left < right:
            top = left
            bottom = right
            for i in range(right-left):
                temp_top_left = matrix[top][left+i]
        
                # top-left <-- bottom-left:
                matrix[top][left+i] = matrix[bottom-i][left]
        
                # bottom-left <-- bottom-right:
                matrix[bottom-i][left] = matrix[bottom][right-i]
        
                # bottom-right <-- top-right:
                matrix[bottom][right-i] = matrix[top+i][right]
        
                # top-right <-- top-left:
                matrix[top+i][right] = temp_top_left

            left += 1
            right -= 1

        return matrix


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(f"Input:      {matrix}")

output = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
print(f"Expected::  {output}")

obj1 = Solution()
ans = obj1.rotate(matrix)
print(f"Ans:        {ans}")
print(f"Input:      {matrix}")

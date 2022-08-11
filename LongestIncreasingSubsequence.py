

# O(n^2):
class Solution(object):
    def lengthOfLIS(self, nums):
        L = len(nums)
        list_depth = [1]*L

        for i in reversed(range(L-1)):
            for j in range(i+1, L):
                if nums[i] < nums[j] and list_depth[i] < list_depth[j] + 1:
                    list_depth[i] = list_depth[j] + 1

        print(list_depth)
        return max(list_depth)


nums = [0, 1, 0, 3, 2, 3]
print(nums)
obj1 = Solution()
print(obj1.lengthOfLIS(nums))


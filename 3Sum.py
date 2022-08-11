# https://www.youtube.com/watch?v=erEHQO0xljc&ab_channel=GiuseppePicciano

class Solution(object):
    def threeSum(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            nums.sort()
            print(nums)
            triplets = []
            L3 = len(nums)
            triplets = []
            for i in range(L3-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                j = i + 1
                k = L3 - 1

                while j < k:
                    current_sum = nums[i] + nums[j] + nums[k]
                    if current_sum == 0:
                        triplets.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1
                    elif current_sum < 0:
                        j += 1
                    else:
                        k -= 1

            return triplets


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, 2, -1, -4, 1, 1, -3, -2]
    # nums = [-4, -3, -2, -1, -1, 0, 1, 1, 1, 2, 2]
    nums = [0,1,1]
    obj1 = Solution()
    ans = obj1.threeSum(nums)
    print(f"Input array: {nums}")
    print(f"Triplets : {ans}")

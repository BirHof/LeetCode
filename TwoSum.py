# 1. Two Sum

nums1 = [2, 7, 11, 15]
target1 = 9
# Output: [0,1]

nums2 = [3, 2, 4]
target2 = 6
# Output: [1,2]


def two_sum(nums, target):
    dic = {}
    for i, element in enumerate(nums):
        complement = target - element
        if complement in dic:
            return [dic[complement], i]
        dic[element] = i
    return []


list1 = two_sum(nums1, target1)
print(list1)
list2 = two_sum(nums2, target2)
print(list2)



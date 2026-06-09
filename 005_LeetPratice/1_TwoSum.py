class Solution:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        for index, num in enumerate(nums):
            searched_num = target - num
            if searched_num in nums:
                if not index == nums.index(searched_num):
                    return [index, nums.index(searched_num)]


solution = Solution()
print(solution.twoSum([2, 11, 7, 15], 9))
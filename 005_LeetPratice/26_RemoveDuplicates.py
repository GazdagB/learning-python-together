class Solution:
    def removeDuplicates(self, nums) -> int:

        for index, num in enumerate(nums):
            notGreater = True

            while notGreater:
                if index +1 >= len(nums):
                    notGreater = False
                    continue
                nextNum = nums[index + 1]
                if nextNum == num:
                    nums.pop(index + 1)
                elif nextNum > num:
                    notGreater = False
        return len(nums)

solution = Solution()
k = solution.removeDuplicates([1,1,2]) # Expect 2
k2 = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) # Expect 5
print(k)
print(k2)
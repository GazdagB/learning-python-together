class Solution(object):
    def plusOne(self, digits):
        lastIndex = (len(digits) - 1)

        not_solved = True

        while not_solved:
            if digits[lastIndex] + 1 < 10:
                digits[lastIndex] += 1
                return digits
            if digits[lastIndex] + 1 == 10:
                digits[lastIndex] = 0
                lastIndex -= 1
                if lastIndex == -1:
                    digits.insert(0,1)
                    return digits


    #Loop through digits from the back
    #If number +1 is 10 increment index -1 with on if that is 10 increment the next
    #If current index is 0 add a 1 to the first place of the array

solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)

        reversed_str = num_str[::-1]

        if reversed_str == num_str:
            return True

        return False


solution = Solution()
print(solution.isPalindrome(121)) # True
print(solution.isPalindrome(121222)) # False
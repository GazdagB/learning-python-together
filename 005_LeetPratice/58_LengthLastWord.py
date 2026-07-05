class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])

solution = Solution()

print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))
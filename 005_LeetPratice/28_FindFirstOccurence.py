class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for start_index in range(len(haystack) - len(needle) + 1):
            if haystack[start_index:start_index + len(needle)] == needle:
                return start_index

        return -1



solution = Solution()

print(solution.strStr("mississippi", "issip"))

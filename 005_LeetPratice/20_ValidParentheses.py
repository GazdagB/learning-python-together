CLOSING_PAIRS = {
    ")" : "(",
    "]" : "[",
    "}" : "{"
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets= ["[","(","{"]
        closing_brackets = [")","]","}"]

        for char in s:
            if len(stack) == 0 and char in closing_brackets:
                return False
            if char in opening_brackets:
                stack.append(char)
            if  char in closing_brackets:
                if stack[-1] == CLOSING_PAIRS.get(char):
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True


solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("]"))

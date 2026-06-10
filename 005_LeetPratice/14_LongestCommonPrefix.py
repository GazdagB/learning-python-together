class Solution:
    def longestCommonPrefix(self, strs):
        first_word = strs[0]
        output = ""
        match = True
        for first_i, char in enumerate(first_word):

            print(char)

            for word in strs:

                if len(word) <= first_i:
                    match = False
                    break

                if word[first_i] == char:
                    match = True

                else:
                    match = False
                    break

            if match:
                output += char
            else:
                break
        return output








sol = Solution()
sol.longestCommonPrefix(["flower", "f", "float", "flat"])
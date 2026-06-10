ROMAN_DICTIONARY = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


class Solution:
    def __init__(self):
        self.result = 0

    def romanToInt(self, s: str) -> int:
        reversed_str = s[::-1]
        str_array = list(reversed_str)

        index = 0

        while index < len(str_array):
           if self.is_next_lower(index, index + 1, str_array):
               edge_str = f"{str_array[index+ 1]}{str_array[index]}"
               self.result += ROMAN_DICTIONARY[edge_str]
               index += 2
           else:
               self.result += ROMAN_DICTIONARY[str_array[index]]
               index += 1

        result = self.result
        self.result = 0
        return result


    def is_next_lower(self, curr , next_el , str_array) -> bool:
        if not next_el == len(str_array):
            if ROMAN_DICTIONARY[str_array[curr]] > ROMAN_DICTIONARY[str_array[next_el]]:
                return True
        return False

# Reverse the input string
# Start a loop
# For each check if the next value is a smaller value
# If yes concetanate the string
# Look up the value and ad it to the result
# If it isn't smaller just add the value to the result

sol = Solution()
print(sol.romanToInt("III")) # Expected: 3
print(sol.romanToInt("LVIII")) # Expected: 58
print(sol.romanToInt("MCMXCIV")) # Expected: 1994
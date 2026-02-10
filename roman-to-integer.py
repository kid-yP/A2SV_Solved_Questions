class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_to_integer[s[i]]

            if i + 1 < n and roman_to_integer[s[i + 1]] > current_value:
                total -= current_value
            else:
                total += current_value
        
        return total

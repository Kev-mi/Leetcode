class Solution:
    def subtraction(self, value_1, value_2):
        return value_2-value_1

    def romanToInt(self, s: str) -> int:
        summation = 0
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        string = [char for char in s]
        if len(string) > 1:
            char = 0
            while char < len(string) -1:
                if values[string[char]] < values[string[char + 1]]:
                    value_to_add = Solution().subtraction(values[string[char]], values[string[char + 1]])
                    char += 2
                    summation += value_to_add
                else:
                    summation += values[string[char]]
                    char += 1
            if values[string[-1]] <= values[string[-2]]:
                char +=1
                summation += values[string[-1]]
        else:
            summation += values[string[0]]
        return summation



print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))
print(Solution().romanToInt("MCMXCIV"))

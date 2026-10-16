class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        digits = "0123456789abcdef"
        res = ""
        while num:
            res = digits[num & 15] + res
            num >>= 4
        return res
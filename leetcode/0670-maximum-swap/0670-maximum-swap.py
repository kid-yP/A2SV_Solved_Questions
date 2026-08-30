class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        
        last = {d: -1 for d in range(10)}
        for i, ch in enumerate(digits):
            last[int(ch)] = i
        
        for i, ch in enumerate(digits):
            d = int(ch)
            for larger in range(9, d, -1):
                if last[larger] > i:
                    digits[i], digits[last[larger]] = digits[last[larger]], digits[i]
                    return int(''.join(digits))
        
        return num
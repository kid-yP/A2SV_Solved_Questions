class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))

        while i <= j:
            s_sum = i ** 2 + j ** 2
            if s_sum > c:
                j -= 1
            elif s_sum < c:
                i += 1
            else:
                return True
        return False

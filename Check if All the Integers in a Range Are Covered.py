class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for x in range(left, right + 1):
            flag = False

            for start, end in ranges:
                if start <= x <= end:
                    flag = True
                    break

            if not flag:
                return False

        return True

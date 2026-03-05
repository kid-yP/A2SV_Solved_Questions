class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.p = [0] * (n + 1)
        for i in range(n):
            self.p[i + 1] = self.p[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right + 1] - self.p[left]
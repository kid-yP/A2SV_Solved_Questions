import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.pos[target]
        return indices[random.randrange(len(indices))]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
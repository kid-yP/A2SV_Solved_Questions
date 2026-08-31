class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        dp = {0: {0}}

        for stone in stones:
            for k in dp.get(stone, set()):
                for step in (k - 1, k, k + 1):
                    if step > 0:
                        next_pos = stone + step
                        if next_pos in stone_set:
                            dp.setdefault(next_pos, set()).add(step)

        return bool(dp.get(stones[-1], set()))
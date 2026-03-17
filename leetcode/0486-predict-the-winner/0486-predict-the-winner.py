class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def choose(l: int, r: int) -> int:
            if l == r:
                return nums[l]

            left = nums[l] - choose(l + 1, r)
            right = nums[r] - choose(l, r - 1)

            return max(left, right)

        return choose(0, len(nums) - 1) >= 0
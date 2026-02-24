class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        tot_skill = skill[0] + skill[-1]
        chemistry = 0
        left, right = 0, n - 1
        while left < right:
            if skill[left] + skill[right] != tot_skill:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return chemistry

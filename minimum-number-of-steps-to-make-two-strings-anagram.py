class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(sorted(s))
        t_cnt = Counter(sorted(t))

        
        if s_cnt == t_cnt:
            return 0
        
        steps = 0

        for char in t_cnt:
            if s_cnt[char] < t_cnt[char]:
                steps += t_cnt[char] - s_cnt[char]
        
        return steps

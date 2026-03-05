class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        p = [0] * (n + 1)
        
        for start, end, direction in shifts:
            if direction == 1:
                p[start] += 1
                p[end + 1] -= 1
            else:
                p[start] -= 1
                p[end + 1] += 1

        for i in range(1, n):
            p[i] += p[i - 1]

        result = []
        for i in range(n):
            curr_pos = ord(s[i]) - ord('a')
            new_pos = (curr_pos + p[i]) % 26
            result.append(chr(new_pos + ord('a')))
        return "".join(result)
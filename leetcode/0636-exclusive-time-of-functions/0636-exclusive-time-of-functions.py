class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func_id, typ, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)

            if typ == "start":
                if stack:
                    ans[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                ans[stack[-1]] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1

        return ans
from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1

        if len(self.queue) > self.k:
            removed = self.queue.popleft()
            if removed == self.value:
                self.count -= 1

        return len(self.queue) == self.k and self.count == self.k
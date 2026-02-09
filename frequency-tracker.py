class FrequencyTracker:
    def __init__(self):
        self.num_freq = {}
        self.freq_count = {}

    def add(self, number: int) -> None:
        old_freq = self.num_freq.get(number, 0)
        new_freq = old_freq + 1
        self.num_freq[number] = new_freq

        if old_freq > 0:
            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

        self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1

    def deleteOne(self, number: int) -> None:
        if number not in self.num_freq:
            return

        old_freq = self.num_freq[number]
        new_freq = old_freq - 1

        self.freq_count[old_freq] -= 1
        if self.freq_count[old_freq] == 0:
            del self.freq_count[old_freq]

        if new_freq > 0:
            self.num_freq[number] = new_freq
            self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1
        else:
            del self.num_freq[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count

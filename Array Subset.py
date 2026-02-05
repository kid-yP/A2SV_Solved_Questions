from collections import Counter
class Solution:
    def isSubset(self, a, b):
        freq_a = Counter(a)
        freq_b = Counter(b)
        
        for key in freq_b: 
            if freq_b[key] > freq_a.get(key, 0): 
                return False 
        
        return True

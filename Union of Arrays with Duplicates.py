class Solution:    
    def findUnion(self, a, b):
        aset = set(a)
        bset = set(b)
        union_set = aset.union(bset)
        return union_set

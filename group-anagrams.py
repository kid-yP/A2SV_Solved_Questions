class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram[sorted_str].append(s)
        
        return list(anagram.values())

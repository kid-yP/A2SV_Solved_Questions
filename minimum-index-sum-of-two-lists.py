class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tot = defaultdict(int)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    tot[list1[i]] += i + j
        
        ans = []
        x = min(tot.values())
        for key, values in tot.items():
            if values == x:
                ans.append(key)
        
        return ans

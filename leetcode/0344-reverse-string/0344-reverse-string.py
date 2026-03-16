class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #Recursion
        def recursion(left: int, right: int) -> list:
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]

            return recursion(left + 1, right - 1)
            
        return recursion(0, len(s) - 1) 
        
        # left, right = 0, len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1


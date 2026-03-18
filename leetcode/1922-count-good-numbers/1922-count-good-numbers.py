class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 1
        even_pos = (n+1)//2 
        odd_pos = n//2
        return ((pow(5,even_pos,mod) * pow(4,odd_pos,mod)) %mod)
#       return (pow(4, n//2,  pow(10, 9)+7) * pow(5, ceil(n/2),  pow(10, 9)+7)) % (10**9 + 7)

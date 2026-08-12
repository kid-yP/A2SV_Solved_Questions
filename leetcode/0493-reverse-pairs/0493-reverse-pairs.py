class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def merge_sort(lo: int, hi: int) -> int:
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid
            
            temp = []
            i, j = lo, mid
            while i < mid and j < hi:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            if i < mid:
                temp.extend(nums[i:mid])
            if j < hi:
                temp.extend(nums[j:hi])
            nums[lo:hi] = temp
            
            return count
        
        return merge_sort(0, len(nums))
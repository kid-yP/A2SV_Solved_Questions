class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))

        def merge_sort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []
            i, j = left, mid + 1
            right_counter = 0
            while i <= mid and j <= right:
                if nums[indices[j]] < nums[indices[i]]:
                    temp.append(indices[j])
                    right_counter += 1
                    j += 1
                else:
                    temp.append(indices[i])
                    counts[indices[i]] += right_counter
                    i += 1
            while i <= mid:
                temp.append(indices[i])
                counts[indices[i]] += right_counter
                i += 1
            while j <= right:
                temp.append(indices[j])
                j += 1
            for k in range(left, right + 1):
                indices[k] = temp[k - left]

        merge_sort(0, n - 1)
        return counts

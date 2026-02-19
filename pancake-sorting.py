class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        sorted_arr = sorted(arr)
        n = len(arr)

        def flip(k):
            arr[:k] = arr[:k][::-1]

        for i in range(n - 1, -1, -1):

            correct_value = sorted_arr[i]
            curr_index = arr.index(correct_value)

            if curr_index == i:
                continue

            if curr_index != 0:
                flip(curr_index + 1)
                res.append(curr_index + 1)

            flip(i + 1)
            res.append(i + 1)

        return res

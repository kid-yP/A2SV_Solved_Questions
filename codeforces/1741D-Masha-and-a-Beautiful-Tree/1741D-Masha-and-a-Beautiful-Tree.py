def dfs(l, r):
            if l == r:
                return 0, p[l], p[l]
            mid = (l + r) // 2
            left_swaps, left_min, left_max = dfs(l, mid)
            right_swaps, right_min, right_max = dfs(mid+1, r)
            if left_swaps == -1 or right_swaps == -1:
                return -1, 0, 0
            if left_max < right_min:
                return left_swaps + right_swaps, left_min, right_max
            elif right_max < left_min:
                return left_swaps + right_swaps + 1, right_min, left_max
            else:
                return -1, 0, 0
        
    ans, _, _ = dfs(0, m-1)
    print(ans)
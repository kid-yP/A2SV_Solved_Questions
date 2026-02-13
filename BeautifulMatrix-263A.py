matrix = [list(map(int, input().split()))for _ in range(5)]

for row_idx in range(5):
    for col_idx in range(5):
        if matrix[row_idx][col_idx] == 1:
            print(abs(2 - row_idx) + abs(2 - col_idx))
            

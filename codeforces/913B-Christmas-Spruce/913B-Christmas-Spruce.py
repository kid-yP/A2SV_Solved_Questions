def is_leaf(node):
    return len(children[node]) == 0

for node in range(1, n + 1):
    if not is_leaf(node):
        leaf_count = 0
        
        for child in children[node]:
            if is_leaf(child):
                leaf_count += 1
        
        if leaf_count < 3:
            print("No")
            exit()

print("Yes")
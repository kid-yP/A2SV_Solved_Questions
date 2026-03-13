s = input()

stack = [-1]
max_len = 0
count = 0

for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            longest = i - stack[-1]
            if longest > max_len:
                max_len = longest
                count = 1
            elif longest == max_len:
                count += 1

if max_len == 0:
    print(0, 1)
else:
    print(max_len, count)
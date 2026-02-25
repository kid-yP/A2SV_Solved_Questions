from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()
    ts = input().strip()

    freq_s = Counter(s)
    freq_ts = Counter(ts)

    possible = True
    for ch in freq_s:
        if freq_s[ch] > freq_ts[ch]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue

    remaining = []
    for ch in freq_ts:
        leftover = freq_ts[ch] - freq_s[ch]
        if leftover > 0:
            remaining.extend([ch] * leftover)
    remaining.sort()

    i, j = 0, 0
    result = []
    s_sorted = list(s)

    while i < len(remaining) and j < len(s_sorted):
        if remaining[i] < s_sorted[j]:
            result.append(remaining[i])
            i += 1
        else:
            result.append(s_sorted[j])
            j += 1

    result.extend(remaining[i:])
    result.extend(s_sorted[j:])

    print("".join(result))

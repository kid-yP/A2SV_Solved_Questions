class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def str_add(a: str, b: str) -> str:
            i, j, carry = len(a) - 1, len(b) - 1, 0
            res = []
            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0
                s = x + y + carry
                res.append(str(s % 10))
                carry = s // 10
                i -= 1
                j -= 1
            return ''.join(res[::-1])

        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue

                k = j
                while k < n:
                    third = str_add(first, second)
                    if not num.startswith(third, k):
                        break
                    k += len(third)
                    first, second = second, third
                if k == n:
                    return True
        return False

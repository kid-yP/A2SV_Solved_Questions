class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        is_negative = (numerator < 0) ^ (denominator < 0)
        num = abs(numerator)
        den = abs(denominator)

        integer = num // den
        remainder = num % den
        if remainder == 0:
            return "-" + str(integer) if is_negative else str(integer)

        frac_digits = []
        rem_map = {}
        pos = 0
        while remainder != 0 and remainder not in rem_map:
            rem_map[remainder] = pos
            remainder *= 10
            frac_digits.append(str(remainder // den))
            remainder %= den
            pos += 1

        if remainder in rem_map:
            start = rem_map[remainder]
            frac_digits.insert(start, '(')
            frac_digits.append(')')

        frac_str = ''.join(frac_digits)
        result = str(integer) + "." + frac_str
        return "-" + result if is_negative else result
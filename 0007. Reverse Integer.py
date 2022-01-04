class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        intMax, intMin = 2**31 - 1, -2**31
        while x != 0:
            pop = int(math.fmod(x, 10))
            x = int(x / 10)
            if rev > intMax // 10 or (rev == intMax // 10 and pop > 7):
                return 0
            if rev < int(intMin / 10) or (rev == int(intMin / 10) and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev

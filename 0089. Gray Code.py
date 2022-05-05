class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        # there are 2 ^ n numbers in the Gray code sequence.
        sequenceLength = 1 << n
        for i in range(0, sequenceLength):
            num = i ^ i >> 1
            result.append(num)
        return result

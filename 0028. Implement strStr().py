class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        needleArr = self._createNeedleSuffixArr(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = needleArr[j-1]
            else:
                i += 1
        return i - j if j == len(needle) else -1
    
    def _createNeedleSuffixArr(self, needle):
        result = [0]*len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                result[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = result[j-1]
            else:
                i += 1
        return result

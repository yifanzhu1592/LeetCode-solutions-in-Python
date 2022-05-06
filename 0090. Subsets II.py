class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        currentSubset = []

        self.subsetsWithDupHelper(subsets, currentSubset, nums, 0)
        return subsets

    def subsetsWithDupHelper(self, subsets: List[List[int]], currentSubset: List[int], nums: List[int], index: int):
        # Add the subset formed so far to the subsets list.
        subsets.append(currentSubset[:])

        for i in range(index, len(nums)):
            # If the current element is a duplicate, ignore.
            if (i != index and nums[i] == nums[i - 1]):
                continue
            currentSubset.append(nums[i])
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i + 1)
            currentSubset.pop()

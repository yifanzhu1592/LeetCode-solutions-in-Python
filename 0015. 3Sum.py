class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add(tuple(sorted([nums[i], nums[j], complement])))
            seen.add(nums[j])
            j += 1

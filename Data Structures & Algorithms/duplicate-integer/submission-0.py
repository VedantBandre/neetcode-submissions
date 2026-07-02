class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        # print(setNums)
        if len(setNums) == len(nums):
            return False
        else:
            return True
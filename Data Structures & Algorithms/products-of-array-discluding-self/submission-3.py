class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make res array the size of input nums array
        res = [1] * len(nums)
        
        # 1st pass: store multiplication to left of index in prefix array
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref = pref * nums[i]
        
        # 2nd pass: and the right in the suffix array
        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suff
            suff = suff * nums[i]
        return res
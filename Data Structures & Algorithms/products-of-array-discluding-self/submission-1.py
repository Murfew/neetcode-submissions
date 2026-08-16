from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = {}
        suff = {}

        for i in range(len(nums)):
            if i == 0:
                pref[i] = 1
                suff[len(nums) - 1 - i] = 1
            else:
                pref[i] = nums[i - 1] * pref[i - 1] 
                suff[len(nums) - 1 - i] = nums[len(nums) - i] * suff[len(nums) - i]


        return [suff[i] * pref[i] for i in range(len(nums))]
        

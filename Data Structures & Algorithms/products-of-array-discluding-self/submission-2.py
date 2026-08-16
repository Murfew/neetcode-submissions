from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = {}
        suff = {}
        n = len(nums)

        for i in range(n):
            if i == 0:
                pref[i] = 1
                suff[n - 1 - i] = 1
            else:
                pref[i] = nums[i - 1] * pref[i - 1] 
                suff[n - 1 - i] = nums[n - i] * suff[n - i]


        return [suff[i] * pref[i] for i in range(n)]
        

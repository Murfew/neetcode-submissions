class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return [list(t) for t in res]
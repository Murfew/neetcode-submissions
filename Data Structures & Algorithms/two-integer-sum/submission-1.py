class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in differences:
                return [min(i, differences[difference]), max(i, differences[difference])]
            
            differences[nums[i]] = i


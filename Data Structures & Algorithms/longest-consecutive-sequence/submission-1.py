class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_count = 0
        cur_count = 0

        if not nums:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            
            if nums[i + 1] - nums[i] != 1:
                max_count = max(max_count, cur_count)
                cur_count = 0

                continue

            cur_count += 1

        max_count = max(max_count, cur_count)
        return max_count + 1
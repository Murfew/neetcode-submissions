class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m

            # in the left sorted part
            if nums[m] >= nums[r]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                elif target >= nums[l]:
                    r = m - 1

            # in the right sorted part
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m -  1
                elif target <= nums[r]:
                    l = m + 1


        return -1
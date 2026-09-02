class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        
        for i, n in enumerate(nums):
            j, k = i + 1, len(nums) - 1

            while j < k:
                currSum = nums[j] + nums[k]

                if currSum == -n:
                    triplets.add((n, nums[j], nums[k]))
                    j += 1
                    continue

                if currSum > -n:
                    k -= 1
                    continue

                if currSum < -n:
                    j += 1
                    continue

        return [list(t) for t in triplets]


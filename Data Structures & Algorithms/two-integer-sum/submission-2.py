class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the list
        # Check the difference of the current with the target
        # If that difference is in the hash map, then return
        # If not, add the current to the hash map

        indices = {} # number -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return [indices.get(diff), i]
            else:
                indices[n] = i

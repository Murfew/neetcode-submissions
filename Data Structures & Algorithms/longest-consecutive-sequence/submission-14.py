class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for n in nums:
            if n - 1 in nums_set:
                continue

            curr = 0
            while n + curr in nums_set:
                curr += 1

            longest = max(curr, longest)

        return longest
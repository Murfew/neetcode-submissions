class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 in numsSet:
                continue

            length = 1
            while True:
                if n + length in numsSet:
                    length += 1
                
                else:
                    break
            
            longest = max(longest, length)
        
        return longest
            
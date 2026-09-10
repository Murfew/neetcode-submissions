class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]

            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]

                total = a + b + c

                if total == 0:
                    res.append([a, b, c])
                    while l < r and b == nums[l]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return res
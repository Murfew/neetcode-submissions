class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            freq[count - 1].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            res.extend(freq[i])
            
            if len(res) == k:
                break

        return res
            


import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq = [[] for _ in range(len(nums))]

        for n in counts:
            freq[counts[n] - 1].append(n)

        non_empty = list(filter(None, freq))

        res = []
        i = -1
        while len(res) < k:
            res += non_empty[i]

            i -= 1
        
        return res
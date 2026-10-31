import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        heap = []
        for n in frequencies:
            heapq.heappush(heap, (-frequencies[n], n))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

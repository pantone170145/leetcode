class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        items = sorted(d.items(), reverse=True, key=lambda x: x[1])
        return list(map(lambda x: x[0], items))[:k]

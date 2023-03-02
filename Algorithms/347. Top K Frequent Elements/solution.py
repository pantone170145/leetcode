class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(Counter(nums))
        items = dict(sorted(d.items(), reverse=True, key=lambda x: x[1]))
        return list(items.keys())[:k]

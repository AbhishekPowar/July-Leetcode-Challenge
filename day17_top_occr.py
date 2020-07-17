class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        hmap = Counter(nums)
        return sorted(hmap, key=lambda x: hmap[x], reverse=True)[:k]

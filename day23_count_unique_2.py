class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        hmap = Counter(nums)
        a, b = hmap.most_common()[-2:]
        return [a[0], b[0]]

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        hmap = Counter(nums)
        a, b = hmap.most_common()[-2:]
        return [a[0], b[0]]

        # better solution
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return s

class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        for idx in range(N-1):
            if nums[idx] > nums[idx+1]:
                return nums[idx+1]
        return nums[0]

        # return min(nums)

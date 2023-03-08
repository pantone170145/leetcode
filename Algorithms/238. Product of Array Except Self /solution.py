class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        # 1で初期化
        left = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            left[i] *= right
            right *= nums[i]

        return left

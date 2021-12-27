class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1
        left, middle, right = 0, len(nums) // 2, len(nums) - 1
        for _ in range(len(nums)):
            if target > nums[middle]:
                left = middle
                middle += max((right - left) // 2, 1)
            elif target < nums[middle]:
                right = middle
                middle -= max((right - left) // 2, 1)
            elif target == nums[middle]:
                return middle

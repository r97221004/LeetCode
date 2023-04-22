# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def search(self, nums, target):
        for i, val in enumerate(nums):
            if val == target:
                return i

        return -1


p = Solution()
print(p.search([-1, 0, 3, 5, 9, 12], 9))


# Binary search
# 時間複雜度: O(log(n))
# 空間複雜度: O(1)
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


p = Solution()
print(p.search([-1, 0, 3, 5, 9, 12], 9))

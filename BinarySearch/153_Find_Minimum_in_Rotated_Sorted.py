# 時間複雜度： O(log(n))
# 空間複雜度: O(1)
class Solution:
    def findMin(self, nums):
        # 1234567
        # 6712345
        # 3456712

        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return res


p = Solution()
print(p.findMin([3, 4, 5, 1, 2]))

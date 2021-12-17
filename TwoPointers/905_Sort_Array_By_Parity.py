# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def sortArrayByParity(self, nums):
        return [i for i in nums if i%2 == 0] + [i for i in nums if i%2 == 1]

p = Solution()
print(p.sortArrayByParity([3, 1, 2, 4]))

# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def sortArrayByParity(self, nums):
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i]%2 == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        
        return nums

p = Solution()
print(p.sortArrayByParity([3, 1, 2, 4]))


# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution(object):
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
            
        while left < right:
            while left < right and nums[left]%2 == 0:
                left += 1
            while left < right and nums[right]%2 == 1:
                right -= 1
                
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
        return nums

p = Solution()
print(p.sortArrayByParity([3, 1, 2, 4]))
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
        start = 0
        end = len(nums)
        
        while start < end:
            mid = (start + end)//2
            
            if nums[mid] >= target:
                end = mid              
            else:
                start = mid + 1
                
        return start if start < len(nums) and nums[start] == target else -1

p = Solution()
print(p.search([-1, 0, 3, 5, 9, 12], 9))

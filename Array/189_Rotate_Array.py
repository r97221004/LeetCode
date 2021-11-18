# 時間複雜度:O(n)
# 空間複雜度:O(n)
class Solution:
    def rotate(self, nums, k):
        k = k%len(nums)
        
        nums[:] = nums[len(nums) - k:] + nums[0 : len(nums) - k] 


# 時間複雜度:O(n)
# 空間複雜度:O(1)
class Solution:
    def rotate(self, nums, k):
        k = k%len(nums)
              
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        reverse(nums, 0, len(nums) - k - 1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)
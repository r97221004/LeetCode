# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)

p = Solution()
print(p.searchInsert([1, 3 ,5, 6], 5))  


# Binary search  
# 時間複雜度 O(log(n)):
# 空間複雜度: O(1)
class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)
        
        while start < end:
            mid = (start + end)//2
            
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1
                
        return start
        
p = Solution()
print(p.searchInsert([1, 3, 5, 6], 4))  







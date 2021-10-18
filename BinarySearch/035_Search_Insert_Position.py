# 時間複雜度: O(n)
# class Solution:
#     def searchInsert(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
            
#         return len(nums)

# p = Solution()
# print(p.searchInsert([1,3,5,6], 5))  


# Classical binary search  
# 時間複雜度 O(log(n)):
class Solution:
    def searchInsert(self, nums, target):
        beg, end = 0, len(nums) # beg 會是我們最終要插入的位置  
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg


p = Solution()
print(p.searchInsert([1,3,5,6], 4))  
print(p.searchInsert([1,3,5,6], 5)) 
print(p.searchInsert([0,0,0,0], 2))






# 時間複雜度: 使用 python 內建列表方法，所以不看時間複雜度
# class Solution:
#     def removeElement(self, nums, val):
#         while nums.count(val):
#             nums.remove(val)
#         return len(nums)

# p = Solution()
# print(p.removeElement([3, 2, 2, 3], 3))   


# 時間複雜度: O(n)
class Solution:
    def removeElement(self, nums, val):
        start = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start
    
p = Solution()
print(p.removeElement([0,1,2,2,3,0,4,2], 2))  
            

            


    
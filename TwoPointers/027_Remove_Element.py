# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def removeElement(self, nums, val):
        start = 0
        
        for i in nums:
            if i != val:
                nums[start] = i
                start += 1
        
        return start
    
p = Solution()
print(p.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  
 
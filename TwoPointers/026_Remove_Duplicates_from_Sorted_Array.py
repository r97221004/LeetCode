# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def removeDuplicates(self, nums):
        start = 0
        
        for i, val in enumerate(nums):
            if val != nums[start]:
                nums[start + 1] = val
                start += 1
        
        return start + 1
     
p = Solution()
print(p.removeDuplicates([1, 1, 2, 3, 4]))

        
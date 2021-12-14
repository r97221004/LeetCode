# 時間複雜度: O(n^2)
# 空間複雜度: O(n)
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                self.TwoSum(res, nums, i)
            
        return res
                
    
    def TwoSum(self, res, nums, i):
        low = i + 1
        hig = len(nums) - 1
        
        while low < hig:
            total = nums[i] + nums[low] + nums[hig]
            if total > 0:
                hig -= 1
            elif total < 0:
                low += 1
            else:
                res.append([nums[i], nums[low], nums[hig]])
                low += 1
                hig -= 1
                while low < hig and nums[low - 1] == nums[low]:
                    low += 1
                    
p = Solution()
print(p.threeSum([-1, 0, 1, 2, -1, -4]))

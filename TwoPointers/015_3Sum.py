# 時間複雜度: O(n^2)
# 空間複雜度: O(n)
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0 :
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i , res)
        return res
          
    def twoSum(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo - 1] == nums[lo]:
                    lo += 1
p = Solution()
print(p.threeSum([-1,0,1,2,-1,-4]))

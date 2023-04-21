# 時間複雜度: O(n^2)
# 空間複雜度: O(n)
class Solution:
    def threeSum(self, nums):
        res = []   
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(res, nums, i)
        
        return res
                
    def twoSum(self, res, nums, i):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1       
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
                    
p = Solution()
print(p.threeSum([-1, 0, 1, 2, -1, -4]))


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for index, val in enumerate(nums):
            if index > 0 and nums[index - 1] == nums[index]:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:    
                        left += 1
        return res

                    
p = Solution()
print(p.threeSum([-1, 0, 1, 2, -1, -4]))

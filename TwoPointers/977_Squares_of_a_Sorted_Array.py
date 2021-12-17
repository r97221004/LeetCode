# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def sortedSquares(self, nums):
        result = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right]**2
                right -= 1
            else:
                result[i] = nums[left]**2
                left += 1
        return result

p = Solution()
print(p.sortedSquares([-4, -1, 0, 3, 10]))

# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def sortedSquares(self, nums):
        res = [0]*len(nums)
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                res[right - left] = nums[left]**2
                left += 1
                
            else:
                res[right -left] = nums[right]**2 
                right -= 1
                  
        return res

p = Solution()
print(p.sortedSquares([-4, -1, 0, 3, 10]))

# 時間複雜度: O(n*log(n))
# 空間複雜度: O(n)
class Solution:
    def sortedSquares(self, nums):
        nums = [ num**2 for num in nums]
        nums.sort()
        return nums

p = Solution()
print(p.sortedSquares([-4, -1, 0, 3, 10]))
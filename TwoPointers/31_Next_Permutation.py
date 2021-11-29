# 時間複雜度: O(n)
# 空間複雜度: O(1)
# 解釋: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums [i]:
            i -= 1
            
        if i == 0:  # nums are in descending order
            nums.reverse()
            return
        
        k = i - 1 # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        
        nums[k], nums[j] = nums[j], nums[k]
        left, right = k + 1, len(nums) - 1  # reverse the second part
        while left < right:
            nums[left], nums[right]  = nums[right], nums[left]
            left += 1
            right -= 1

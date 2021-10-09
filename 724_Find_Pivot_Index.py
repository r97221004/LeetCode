# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        
        for i, val in enumerate(nums):
            if leftsum == S - leftsum - val:
                return i
            leftsum += val
        
        return -1

p = Solution()
print(p.pivotIndex([1,7,3,6,5,6]))
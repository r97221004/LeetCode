# 注意 Python 的 .sort() 方法的時間複雜度是 O(nlog(n))，空間複雜度是 O(log(n))
# 時間複雜度: O(nlog(n))
# 空間複雜度: O(log(n))
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

p = Solution()
print(p.maximumProduct([1,2,3,4]))



# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def maximumProduct(self, nums):
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')
        
        for i in nums:
            if i >= max1:
                max1, max2, max3 = i, max1, max2
            elif i >= max2:
                max2, max3 = i, max2
            elif i >= max3:
                max3 = i
                
            if i <= min1:
                min1, min2 = i, min1            
            elif i <= min2:
                min2 = i
            
        return max( max1*max2*max3, max1*min1*min2)

p = Solution()
print(p.maximumProduct([1,2,3,4]))
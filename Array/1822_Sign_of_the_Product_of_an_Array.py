# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def arraySign(self, nums):
        result = 1
        for i in nums:
            result *= i
        
        if result > 0 : return 1
        elif result < 0: return -1
        else: return 0
    
p = Solution()
print(p.arraySign([-1, -2, -3, -4, 3, 2, 1]))

# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution(object):
    def arraySign(self, nums):
        res = 0
        
        for i in nums:
            if i == 0: return 0
            elif i < 0: res += 1
                
        return  1 if res%2 == 0 else -1

p = Solution()
print(p.arraySign([-1, -2, -3, -4, 3, 2, 1]))
        
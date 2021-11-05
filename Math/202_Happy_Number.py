# 時間複雜度: O(log(n))
# 空間複雜度: O(log(n))
class Solution:
    def isHappy(self, n):
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = sum( int(i)**2 for i in str(n))
            
        return n == 1

p = Solution()
print(p.isHappy(19))
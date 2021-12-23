# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def plusOne(self, digits):        
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        return [1] + digits

p = Solution()
print(p.plusOne([1, 2, 3, 9]))

# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def plusOne(self, digits):        
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            digits[i] = carry%10
            carry //= 10
            
        if carry: return [carry] + digits

p = Solution()
print(p.plusOne([1, 2, 3, 9]))
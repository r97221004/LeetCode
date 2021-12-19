# 時間複雜度: O(max(n, m)), n = len(num1) and m = len(num2)
# 空間複雜度: O(max(n, m))
class Solution:
    def addStrings(self, num1, num2):
        a = list(num1)
        b = list(num2)
        carry = 0
        result = ''
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
                
            if b:
                carry += int(b.pop())
            
            result = str(carry%10) + result
            carry //= 10
        
        return result 

p = Solution()
print(p.addStrings("11", "123"))
        
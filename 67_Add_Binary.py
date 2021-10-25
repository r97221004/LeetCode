# 時間複雜度: O(max(n, m)), n = len(a) and m = len(b)
# 空間複雜度: O(max(n, m))
class Solution:
    def addBinary(self, a, b):
        carry = 0
        result = ''
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            result += str(carry%2)
            carry //= 2
            
        return result[::-1]

p = Solution()
print(p.addBinary("1010", b = "1011"))
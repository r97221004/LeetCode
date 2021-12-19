# 時間複雜度: O(max(n, m)), n = len(a) and m = len(b)
# 空間複雜度: O(max(n, m))
class Solution:
    def addBinary(self, a, b):
        res = ""
        carry = 0
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
                
            if b:
                carry += int(b.pop())
                
            res = str(carry%2) + res
            carry //= 2
        
        
        return res

p = Solution()
print(p.addBinary("1010", b = "1011"))  
     
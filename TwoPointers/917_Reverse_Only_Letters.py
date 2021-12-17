# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def reverseOnlyLetters(self, s):
        left = 0
        right = len(s) - 1
        s = list(s)
        
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
                
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
            
        return "".join(s)

p = Solution()
print(p.reverseOnlyLetters("a-bC-dEf-ghIj"))
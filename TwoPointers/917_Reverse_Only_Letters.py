# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        start, end = 0, len(s) - 1
        
        while start < end:
            while start < end and not s[start].isalpha():
                start += 1
            while  start < end  and not s[end].isalpha() :
                end -= 1
                
            
            s[start], s[end] = s[end], s[start] # start 與 end 在上面 while 的保護下都不會超出
                
            start += 1
            end -= 1
        
        return ''.join(s)

p = Solution()
print(p.reverseOnlyLetters("a-bC-dEf-ghIj"))
# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
    
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
                
            while start < end and not s[end].isalnum():
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True

p = Solution()
print(p.isPalindrome("A man, a plan, a canal: Panama"))
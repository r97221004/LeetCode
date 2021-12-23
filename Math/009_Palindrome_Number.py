# 時間複雜度: O(n), n = len(x)
# 空間複雜度: O(n)
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

p = Solution()
print(p.isPalindrome(x = 121))


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        start = 0
        end = len(x) - 1
        
        while start < end:
            if x[start] == x[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True

p = Solution()
print(p.isPalindrome(x = 121))

# 時間複雜度: O(n)
# 空間複雜度: O(n)
# 沒有轉成字串
class Solution:
    def isPalindrome(self, x):
        if x < 0: return False
        
        res = []
 
        while x:
            x, r = x//10, x%10
            res = [r] + res
            
        return res == res[::-1] 

p = Solution()
print(p.isPalindrome(x = 121))
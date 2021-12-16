# 時間複雜度: O(n)
# 空間複雜度: O(n) ?
class Solution:
    def expressiveWords(self, s: str, words):
        return sum( self.check(s, word) for word in words)
               
    def check(self, s, word):
        i = j = 0
        
        for i in range(len(s)):
            if j < len(word) and s[i] == word[j]: j += 1
            elif s[i - 1:i + 2] != s[i]*3 != s[i - 2: i + 1]: return False
            
        return j == len(word)    

p = Solution()
print(p.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
        
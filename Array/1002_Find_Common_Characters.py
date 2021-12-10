# Let N be the number of words in the list and M be the maximum length of a single word.
# 時間複雜度: O(M*(*N*M + N)) -> O(M*N*M ) 
# 空間複雜度: O(max(N,M))
class Solution:
    def commonChars(self, words):
        chars = set(words[0])
        res = []
        
        for char in chars:
            count = min([word.count(char) for word in words])
            res += [char]*count
            
        return res

p = Solution()
print(p.commonChars(["bella", "label", "roller"]))





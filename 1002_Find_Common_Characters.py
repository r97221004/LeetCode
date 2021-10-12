# Let N be the number of words in the list and M be the maximum length of a single word.
# 時間複雜度: O(M*N*M)
# 空間複雜度: O(M)
class Solution:
    def commonChars(self, words):
        result = []
        first = set(words[0])
        
        for i in first:
            count = []
            for word in words:
                count.append(word.count(i))
            result += [i]*min(count)
        
        return result

p = Solution()
print(p.commonChars(["bella","label","roller"]))





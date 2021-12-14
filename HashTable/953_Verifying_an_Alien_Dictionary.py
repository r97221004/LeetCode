# Let N be the length of order, and M be the total number of characters in words.
# 時間複雜度: O(M), 因為英文字母只有 26 個字, 所以 N 會固定在 26
# 空間複雜度: O(1), 因為 N 會固定在 26
class Solution:
    def isAlienSorted(self, words, order):
        orderDict = {}
        
        for i, val in enumerate(order):
            orderDict[val] = i
                
        for w1, w2 in zip(words, words[1:]):
            for i in range(len(w1)):
                if i <= len(w2) - 1 and orderDict[w1[i]] < orderDict[w2[i]]:
                    break
                elif i <= len(w2) - 1 and orderDict[w1[i]] > orderDict[w2[i]]:
                    return False
                elif i > len(w2) - 1:
                    return False
        return True

p = Solution()
print(p.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

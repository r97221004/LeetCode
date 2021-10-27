# 時間複雜度: O(n)
# 空間複雜度: O(1), 因為英文單字最多 26 個
class Solution:
    def isAnagram(self, s, t):
        data1 = {}
        data2 = {}
        for i in s:
            data1[i] = data1.get(i, 0) + 1
        
        for i in t:
            data2[i] = data2.get(i, 0) + 1
        
        return data1 == data2

p = Solution()
print(p.isAnagram(s = "rat", t = "car"))
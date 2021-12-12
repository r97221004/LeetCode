# 時間複雜度: O(n)
# 空間複雜度: O(1), 因為英文單字最多 26 個
class Solution:
    def isAnagram(self, s, t):
        return self.count(s) == self.count(t)
        
    def count(self, s):
        data = {}
        for i in s:
            data[i] = data.get(i, 0) + 1
        return data

p = Solution()
print(p.isAnagram(s = "rat", t = "car"))


# 時間複雜度: O(n*logn)
# 空間複雜度: O(n)
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

p = Solution()
print(p.isAnagram(s = "rat", t = "car"))
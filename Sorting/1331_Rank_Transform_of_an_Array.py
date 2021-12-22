# 時間複雜度: O(nlogn)
# 空間複雜度: O(n)

class Solution:
    def arrayRankTransform(self, arr):
        ans = sorted(arr) # .sort() 方法是 in-place, 而 sorted() 函式不是
        data = {}
        rank = 1
        
        for i in ans:
            if i not in data: 
                data[i] = rank
                rank += 1
        
        ans = [data[i] for i in arr]
        return ans   

p = Solution()
print(p.arrayRankTransform([40, 10, 20, 30]))
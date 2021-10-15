# 時間複雜度: O(nlogn)
# 空間複雜度: O(n)

class Solution:
    def arrayRankTransform(self, arr):
        data = {}
        arrSorted = sorted(arr)  # .sort() 方法是 in-place, 而 sorted() 函式不是 
        rank = 1
        
        for i in arrSorted:
            if i not in data:
                data[i] = rank
                rank += 1
        
        for i, val in enumerate(arr):
            arr[i] = data[val]
            
        
        return arr

p = Solution()
print(p.arrayRankTransform([40,10,20,30]))
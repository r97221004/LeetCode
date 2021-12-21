# 時間複雜度: O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def highFive(self, items):
        items.sort()
        items = items[::-1]
        res = []
        
        for k, [i, val] in enumerate(items):
            if not res or i != res[-1][0]:
                res.append([i, sum( items[i][1] for i in range(k, k + 5))//5])
            
        return res[::-1]
        
p = Solution()
print(p.highFive( [[1,91], [1,92], [2,93], [2,97], [1,60], [2,77], [1,65], [1,87], [1,100], [2,100], [2,76], [2,10]]))
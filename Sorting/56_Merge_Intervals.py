# 時間複雜度:O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def merge(self, intervals):    
        intervals.sort(key=lambda x: x[0])
        res = []
        
        for i, val in enumerate(intervals):
            if not res or res[-1][1] < val[0]:
                res.append(val)
            
            else:
                res[-1][1] = max(res[-1][1], val[1])
                        
        return res

p = Solution()
print(p.merge([[1,3], [2,6], [8,10], [15,18]]))
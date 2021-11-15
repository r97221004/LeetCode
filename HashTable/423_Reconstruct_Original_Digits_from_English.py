# 時間複雜度: O(n)
# 空間複雜度: O(1), count 有限多個英文字母, res 只有 10 個
class Solution:
    def originalDigits(self, s):
        count = {}
        res = {}
        
        for i in s:
            count[i] = count.get(i, 0) + 1
            
        res['0'] = count.get('z', 0)
        res['2'] = count.get('w', 0)
        res['4'] = count.get('u', 0)
        res['6'] = count.get('x', 0)
        res['8'] = count.get('g', 0)
        res['3'] = count.get('h', 0) - res['8']
        res['5'] = count.get('f', 0) - res['4']
        res['7'] = count.get('v', 0) - res['5']
        res['9'] = count.get('i', 0) - res['5'] - res['6'] - res['8']
        res['1'] = count.get('o', 0) - res['2'] - res['4'] -res['0']
                                    
                                    
        res = [ i*res[i] for i in sorted(res.keys()) ]
         
        return "".join(res)     

p = Solution()
print(p.originalDigits("owoztneoer"))
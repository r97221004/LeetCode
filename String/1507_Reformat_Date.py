# 時間複雜度: O(1)
# 時間複雜度: O(1)
class Solution:
    def reformatDate(self, date):     
        date = date.split(' ')[::-1]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date[1] = f'{month.index(date[1]) + 1:0>2}'
        date[2] = f'{date[2][0:len(date[2])-2]:0>2}'
           
        return '-'.join(date)

p = Solution()
print(p.reformatDate("20th Oct 2052"))

# 時間複雜度: O(1)
# 時間複雜度: O(1)
class Solution:
    def reformatDate(self, date):     
        date = date.split(" ")[::-1]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date[1] = "{:0>2}".format(month.index(date[1]) + 1)
        date[2] = "{:0>2}".format(date[2][:len(date[2])-2])
        
        return "-".join(date)

p = Solution()
print(p.reformatDate("20th Oct 2052"))


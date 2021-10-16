# 注意列表的 .sort() 方法是 O(nlog(n))
# 時間複雜度: O(nlog(n))
# 空間複雜度: O(1)

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
p = Solution()
print(p.canAttendMeetings( [[0,30],[5,10],[15,20]]))

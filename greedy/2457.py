'''
1월 -> 31 
2월 -> 28 59
3월 -> 31 90
4월 -> 30 120
5월 -> 31 151
6월 -> 30 181
7월 -> 31 212
8월 -> 31 243
9월 -> 30 273
10월 -> 31 304
11월 -> 30 334
12월 -> 31 365

3월 1일: 60
11월 30일: 334
'''
def convert(month, date):
    if month == 1:
        return date
    elif month == 2:
        return 31 + date
    elif month == 3:
        return 59 + date
    elif month == 4:
        return 90 + date
    elif month == 5:
        return 120 + date
    elif month == 6:
        return 151 + date
    elif month == 7:
        return 181 + date
    elif month == 8:
        return 212 + date
    elif month == 9:
        return 243 + date
    elif month == 10:
        return 273 + date
    elif month == 11:
        return 304 + date
    elif month == 12:
        return 334 + date

def get_start(flowers):
    end = 0
    res = -1
    for i in range(len(flowers)):
        if flowers[i][0] <= 60:
            if flowers[i][1] >= end:
                end = flowers[i][1]
                res = i

    return res 

def get_next(s_idx, cur_end, flowers):
    res = -1
    next_end = cur_end
    for i in range(s_idx+1, len(flowers)):
        if flowers[i][0] <= cur_end:
            if flowers[i][1] >= next_end:
                next_end = flowers[i][1]
                res = i
    
    return res

def solve(flowers):
    n = len(flowers)
    start = get_start(flowers)
    if start == -1:
        return 0
    
    cur_end = flowers[start][1]
    ans = 1
    while start < n and cur_end <= 334:
        start = get_next(start, cur_end, flowers)
        cur_end = flowers[start][1]
        ans += 1
        if start == -1:
            return 0
    return ans

n = int(input())
flowers = []
for _ in range(n):
    s_month, s_date, e_month, e_date = map(int, input().split())
    start = convert(s_month, s_date)
    end = convert(e_month, e_date)
    if end < 60 or start > 334:
        continue
    flowers.append((start, end))

flowers.sort(key=lambda x: (x[0], x[1]))

print(solve(flowers))
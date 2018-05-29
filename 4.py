#题目：输入某年某月某日，判断这一天是这一年的第几天？

#程序分析：以3月5日为例，应该把前两个月的加起来，然后再加上5天就是本年的第几天，特殊情况，闰年

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日："))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month-1]
else:
    print("日期错误")
sum += day
leap = 0
if (year % 4 ==0 and year % 100 !=0 ) or (year % 400 == 0):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print("%d年%d月%d日是这一年的第%d天"%(year,month,day,sum))


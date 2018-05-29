#题目：输入三个整数，请阿布这三个整数由小到大输出
'''
#1.接受输入
num1 = int(input("第一个数："))
num2 = int(input("第二个数："))
num3 = int(input("第三个数："))

#2.进行比较
if num1 > num2:
    num1,num2 = num2,num1
if num1 > num3:
    num1,num3 = num3,num1
if num2 > num3:
    num2,num3 = num3,num2

#3.打印输出
print("由小到大：%d,%d,%d"%(num1,num2,num3))
'''

#方法二：
nums = []
for i in range(3):
    num = int(input("请输入数："))
    nums.append(num)
nums.sort()
print(nums)
    



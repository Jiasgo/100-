#从键盘随机获取四个数字，a,b,c,d,计算组合成的不同的四位数
import random
#1.获取用户输入的四个数字
a = int(input("输入的第一个数字："))
b = int(input("输入的第二个数字："))
c = int(input("输入的第三个数字："))
d = int(input("输入的第四个数字："))
#组合四个数字
if (a != b and a != c and a != d and b != c and b != d and c != d):
    print(a,b,c,d)
    n = str(a+b+c+d)
while True:
    num = random.randint(0,10)
    result = n * num
print(result)

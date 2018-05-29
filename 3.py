#题目：
#一个整数，它加上100后是一个完全平方数，在加上168又是一个完全平方数，请问该数是多少？
#程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足以下条件，就是结果
'''
include"math.h"
main()
{
long int i,x,y,z;
for(i=1;i<100000;i++)
    {
        x=sqrt(i+100);
        y=sqrt(i+268);
        if(x*x==i+100&&y*y==i+268)
        printf("\n%1d\n",i)
        }
        }
'''

import math
for i in range(100000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)


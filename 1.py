#计算1,2,3,4四个数字一共能生成多少个不同的三位数
print("猜一猜1，2，3，4四个数字一共能生成多少个不同的三位数呢：\n")
count = 0
for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
            if (i != j and j != k and i != k):
                print("%s%s%s"%(i,j,k),end=" ")
                count += 1
print("\n一共有%s个"%count)

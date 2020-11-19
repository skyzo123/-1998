软件1班 郭宇天 2020012054
import random
print("欢迎使用算术自测程序，测试开始:")
count=[]
L=[]
def q():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("请问",a,"+",b,"=?")
    s=int(input())
    if s==a+b:
        L.append("第%d题正确,你的结果为%d+%d=%s"%(i,a,b,a+b) )
        count.append(10)
    else:
        L.append("第%d题错误，你的结果为%d+%d=%s,正确结果为%d+%d=%d"%(i,a,b,s,a,b,a+b))
    return count,L
def w():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("请问",a,"-",b,"=?")
    s=int(input())
    if s==a-b:
        L.append("第%d题正确,你的结果为%d-%d=%s"%(i,a,b,a-b) )
        count.append(10)
    else:
        L.append("第%d题错误，你的结果为%d-%d=%s,正确结果为%d-%d=%d"%(i,a,b,s,a,b,a-b))
    return count,L
def e():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("请问",a,"*",b,"=?")
    s=float(input())
    if s==a*b:
        L.append("第%d题正确,你的结果为%d*%d=%s"%(i,a,b,a*b) )
        count.append(10)
    else:
        L.append("第%d题错误，你的结果为%d*%d=%s,正确结果为%d*%d=%d"%(i,a,b,s,a,b,a*b))
    return count,L
def r():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("请问",a,"//",b,"=?")
    s=float(input())
    if s==a//b:
        L.append("第%d题正确,你的结果为%d//%d=%s"%(i,a,b,a//b) )
        count.append(10)
    else:
        L.append("第%d题错误，你的结果为%d//%d=%s,正确结果为%d//%d=%d"%(i,a,b,s,a,b,a//b))
    return count,L
for i in range(1,11):
    print("第%d题"%i)
    k=random.randint(1,4)
    #随机调用一个函数
    if k==1:
        q()
    if k==2:
        w()
    if k==3:
        e()
    if k==4:
        r()
for j in range(0,10):
    print(L[j])
print("您最终的分数是%d"%sum(count))

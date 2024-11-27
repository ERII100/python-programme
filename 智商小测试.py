#智商测试
IQ=0
print("现在是智商测试时间！")
answer1=int(input("1+1="))
if answer1 == 2:
    IQ+=1
else:
    IQ+=0
answer2=int(input("9+6="))
if answer2 == 15:
    IQ+=1
else:
    IQ+=0
if IQ<1:
 print("您的IQ为",IQ)
 print("您是猪吗？")
else:
 print("您的IQ为",IQ)
 print("您是人！")
   

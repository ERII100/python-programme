n=0
while True:
    try:
     height=float(input("请输入身高（m）："))
     weight=float(input("请输入体重（kg）"))
     if height>0 and weight>0:
        BMI=weight/height**2
        if 0<=BMI<18.5:
         print("细狗")
        elif BMI<=24.9:
         print("人")
        else:
         print("猪")
        break
     elif height<=0 or weight<=0:
         print("你是猪吗，数字都输不明白？")

      
    except ValueError:
        n+=1
        if n<5:
         print("请输入数字！")
        else:
         print("是不是有毛病？")
     

       

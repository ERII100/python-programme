sg=eval(input("请输入您的身高(m)："))
tz=eval(input("请输入您的体重(kg)："))
bmi=tz/sg**2
if bmi<18.5:
    print("您是细狗")
elif bmi<=24.9:
    print("您是人")
else:
    print("您是猪")

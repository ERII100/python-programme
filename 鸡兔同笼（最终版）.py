def chicken_rabbit_problem(total_heads, total_feet):
    chickens = 2 * total_heads - total_feet/2
    rabbits = total_feet/2 - total_heads
    return int(chickens), int(rabbits)
while True:
    try:
        total_heads=int(input("请输入总的头数："))
        break
    except ValueError:
        print("请输入一个整数值的头数！")
while True:
    try:
        total_feet=int(input("请输入总的脚数："))
        break
    except ValueError:
        print("请输入一个整数值的脚数！")
if total_feet % 2!= 0:
    print("脚的数量应该为偶数，请重新输入!")
    chickens = "错误!请重新输入!"
    rabbits = "错误!请重新输入!"
elif total_feet < 2 * total_heads or total_feet > 4 * total_heads:
    print("输入的脚数不符合鸡兔同笼的逻辑，请重新输入!")
    chickens = "错误!请重新输入!"
    rabbits = "错误!请重新输入!"
else:
    chickens, rabbits = chicken_rabbit_problem(total_heads, total_feet)
if not isinstance(chickens, str) or not isinstance(rabbits, str):
    print("鸡的数量:", chickens)
    print("兔的数量:", rabbits)
   

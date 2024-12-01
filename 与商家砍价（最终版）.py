import time
import random
print("注意！商家存在耐心，耐心耗尽交易失败。每次耐心随机。")
patience=random.randint(1,10)
price=random.randint(800,8000)
print("商家的原价为：",price)
print("商家的耐心为：",patience)
while  True:
     deal_done = False
     try:
       while patience>0:
        bid=float(input("请输入你的报价（如果过低商家将会失去耐心）："))
        if  0.85*price<=bid<=price:
              if bid==int(bid):
               print(f"成交!成交价格为：{int(bid)}")
               deal_done=True
               break
              else:
               print("成交！成交价格为：",bid)
               deal_done=True
               break
        elif bid>price:
             print("反向砍价？人傻钱多是吧，成交!")
             deal_done=True
             break
        else:
             patience-=1
             print("\r商家耐心剩余：{}".format(patience))
             time.sleep(0.8)
             
       if patience==0:
             print("\r交易失败，商家耐心已耗尽")
             break
       if deal_done:
             break
     except ValueError:
             print("请输入数字")






#  @Author  :RG
#  @Time    :2020-04-18 上午 10:46
#  @Note    :

with open("items.txt","r",encoding="utf-8") as f,open("items2.txt","r",encoding="utf-8") as f2:
    for line in f:
        print("f:",line)
    for line in f2:
        print("f2:",line)

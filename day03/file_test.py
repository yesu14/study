#  @Author  :RG
#  @Time    :2020-04-17 下午 22:49
#  @Note    :

f = open("items.txt","r",encoding="utf-8")
# for line in f:
# #     print(line)
print(f.tell())    # 光标位置
print(f.readline())
# print(f.read(2))
print("第一行结束:",f.tell())
# print(f.readline())  123\n
# print("第二行:",f.tell())
# print(f.readline())
# print("第三行：",f.tell())
# print(f.seek(0)) # 光标回到0位置
# print(f.readline())
# print("最后",f.tell())

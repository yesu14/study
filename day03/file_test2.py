#  @Author  :RG
#  @Time    :2020-04-17 下午 23:51
#  @Note    :

f = open("items.txt","w")
f.write("hello 1\n")
f.flush()  # 将缓存写入硬盘，不写flush 代码执行完后一次性写入硬盘，不写容易死机

f.write("hello 2\n")
f.flush()
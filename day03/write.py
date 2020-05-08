#  @Author  :RG
#  @Time    :2020-04-18 上午 10:25
#  @Note    :
f = open("items.txt","r",encoding="utf-8")
f_new = open("items2.txt","w",encoding="utf-8")

for line in f:
    if "国破山河在" in line:
        line = line.replace("国破山河在","12345")
    f_new.write(line)
    f_new.flush()
f.close()
f_new.close()

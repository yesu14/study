#  @Author  :RG
#  @Time    :2020-04-13 下午 23:08
#  @Note    :

item = [("samsung",6000),[2,"iphone",5000],[3,"huawei",4000],[4,"xiaomi",3000]]
for d,jinmeiyan in enumerate(item):
    print("\033[4;34;47m%s\033[0m %s" %(d,jinmeiyan))
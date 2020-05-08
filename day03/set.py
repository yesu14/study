#  @Author  :RG
#  @Time    :2020-04-17 下午 16:08
#  @Note    :
list = [1,2,3,4,2,3,4]
list = set(list)

list.add("9")
print(list,type(list))
list.update(["6,",7,8,9])
list2 = set([5,6,7,8,1,2,3,4])
# 交集
print(list.intersection(list2))
print(list & list2)
# 并集
print(list.union(list2))
# 差集
print(list.difference(list2))
# 子集
print(list.issubset(list2))
# 父集
print(list.issuperset(list2))
# 去掉重复的
print(list.symmetric_difference(list2))
# list.isdisjoint()
print(list.isdisjoint(list2))


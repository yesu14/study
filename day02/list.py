#  @Author  :RG
#  @Time    :2020-04-13 上午 10:13
#  @Note    :
import copy

names = ["user01","user02","user03",["tom01","tom02"],"user04","#user05","!user06","2user07","user08","6user09"]

names2 = copy.deepcopy(names)
names[3][1] = "tom100"
print(names)
print(names2)
# names02 = names.copy()
# names[3][0]="tom03"
# print(names)
# print(names02)
# for name in names[::2]:
#     print(name)
# print(names[2:6:2])
# print(names[-1])
# print(names[-2])
# print(names[-3:])
#
# print(names[-4:-2:3])
# print(names[::-2])
#
# names.append("user10")
# names.insert(3,"user11")
# names[2] = "user12"
# print(names)
#
# names.remove("user10")
# print(names)
# del names[0]
# print(names)
# names.pop(3)
# print(names)
# print([1,2,3,]+[3,2,6])
#
# print(names.index("user02"))
#
# print(names.count("user01"))
# names.reverse()
# print(names)
# names.sort()
# print(names)
#
# names2 = [1,2,3,4,5]
# names.extend(names2)
# del names2
# print(names)

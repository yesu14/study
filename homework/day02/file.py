#  @Author  :RG
#  @Time    :2020-04-17 下午 15:21
#  @Note    :

# list = ["a","b","c"]
# a = "abc"
# print(a+str(list))
list = ["a","b","c","d"]

print("a"+str(list).replace("[","").replace("]","").replace("'",""))

print("\033[41;1mItem delete completed!", "Delete -->Item:", "order_list[2]", "Price:", "order_list[3]","\033[0m")
with open("test.txt", "w", encoding="utf-8") as items_file:
    count = 0
    for line in range(10):
        count += 1
        items_file.write(str(count)+"5")
        items_file.flush()
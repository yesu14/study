#  @Author  :RG
#  @Time    :2020-04-17 下午 15:21
#  @Note    :

with open("test.txt", "w", encoding="utf-8") as items_file:
    count = 0
    for line in range(10):
        count += 1
        items_file.write(str(count)+"5")
        items_file.flush()
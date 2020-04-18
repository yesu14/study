#  @Author  :RG
#  @Time    :2020-04-15 下午 15:51
#  @Note    :

print("\033[32;1mExecution completed!")
new_file = ""
with open("shopping_list.txt","r",encoding="utf-8") as f:
    for line in f.readlines():
        _line = line.strip("\n").split(",",1)
        print("_line:",_line)
        list = (_line[1].strip("\n").strip("[").strip("]")).split(",")
        list.append("ip7")
        new_file= str(list)
        print(new_file)
        # f.write(list)
print("new_file:",new_file)

# with open("items.txt","a+",encoding="utf-8") as f:
#     for index,line in enumerate(f.readlines()):
#         print(line)
#         if index == 1:
#             line = "s2,222"
#     # item_file_content = ""
#     # print(type(f.readlines()))
#     f.write("\n"+"s1,111")
#     # s.append(["s1","1111"])
#     # f.write(str(s))
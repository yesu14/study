#-*- coding:utf-8 -*-
# @Author: Meiyan Jin
# @Time: 2020/4/30 15:52
# @File: xml处理.py01
# @Software: PyCharm

import xml.etree.ElementTree as ET
tree = ET.parse("user.xml")
root = tree.getroot()
print(root.tag)


#修改
for node in root.iter("password"):
    new_str = node.text+"haha"
    node.text = new_str
    node.set("u","yes")

tree.write("user.xml")

#查询
# for node in root.iter('age'):
#     print(node.tag,node.text)

# for child in root:
#     print("子节点:",child.tag,child.attrib)
#     for i in child:
#         print("子节点属性：",i.tag,i.attrib,i.text)
#         for j in i:
#             print("子--------子节点属性：",j.tag,j.text)
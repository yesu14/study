# -*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-06 上午 2:43
#  @Note    :

import pickle

def merge_dict(dict1, dict2):
    return {**dict1, **dict2}


def create_school(self, name, addr):
    if self.info.get("学校"):
        self.info["学校"] = self.merge_dict(self.info["学校"], {name, addr})


json = [{
        "北京": "地址1",
        "班级": "班级1",
        "学生": [
            {
                "姓名": "学生1",
                "学号": "1001",
                "性别": "男",
                "年龄": 15
            },
            {
                "姓名": "学生2",
                "学号": "1002",
                "性别": "男",
                "年龄": 20
            }
        ],
        "老师": [
            {
                "姓名": "老师1",
                "职工编号": "2001",
                "性别": "男",
                "年龄": 30
            },
            {
                "姓名": "老师2",
                "职工编号": "2002",
                "性别": "男",
                "年龄": 40
            }
        ]
    },
    {
        "上海": "地址1",
        "班级": "班级1",
        "学生": [
            {
                "姓名": "学生5",
                "学号": "1005",
                "性别": "男",
                "年龄": 15
            },
            {
                "姓名": "学生6",
                "学号": "1006",
                "性别": "男",
                "年龄": 20
            }
        ],
        "老师": [
            {
                "姓名": "老师5",
                "职工编号": "2005",
                "性别": "男",
                "年龄": 30
            },
            {
                "姓名": "老师6",
                "职工编号": "2006",
                "性别": "男",
                "年龄": 40
            }
        ]
    }]

print(type(json))
with open("../db/school","wb") as file:
    pickle.dump(json,file)

with open("../db/school","rb") as file:
    txt = pickle.load(file)
    txt.append({"学校3":"地址3"})
    # print(txt["学生"])
    print(txt)


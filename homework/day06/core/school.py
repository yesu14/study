# -*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-06 上午 1:49
#  @Note    :

import pickle

DB_PATH = "../db/"
F_STUDENT = "student"  # 学生数据
F_SCHOOL = "school"  # 学校文件
F_TEACHER = "teacher"  # 老师文件
str_create_school_msg = "创建学校：\033[33m [名称:%s] [地址:%s]\033[0m 成功"
str_create_grade_msg = "创建班级：\033[33m [%s]学校 [%s] [周期:%s]\033[0m 成功"
str_c_grade_teacher_msg = "%s班里添加老师：\033[33m [%s] \033[0m 成功"
str_c_grade_student_msg = "%s班里添加学生：\033[33m [%s] \033[0m 成功"

str_query_s_info = "学校信息：\033[33m [%s] \033[0m 成功"
str_x_msg_no_school = "\033[31m [%s]学校不存在 \033[0m"


# 获取pickle数据
def get_data(f_name):
    with open(f_name, "rb") as f:
        data = pickle.load(f)
        return data


# 用pickle写文件
def write_data(f_name, data):
    with open(f_name, "wb") as f:
        pickle.dump(data, f)


# 合并字典
def merge_dict(dict1, dict2):
    return {**dict1, **dict2}


class Manager(object):
    def __init__(self):
        self.info = {}
        self.grade = []  # 班级
        self.students = []  # 学生
        self.teachers = []  # 老师
        # 初始化学校
        self.s_info = get_data(DB_PATH + F_SCHOOL)
        print(str_query_s_info % self.s_info)

    def create_school(self, name, addr):
        self.info = self.s_info.append({name, addr})
        write_data(DB_PATH + F_SCHOOL, self.s_info)
        print(str_create_school_msg % (name, addr))

    # 创建班级(班级名称，生命周期)
    def create_grade(self, school, grade, lifecycle):
        is_completed = False
        for i, school in enumerate(self.s_info):
            if school[i].get(school):
                school[i].append({grade: lifecycle})
                is_completed = True
                break
        if is_completed:
            write_data(DB_PATH + F_SCHOOL)
            print(str_create_grade_msg % (school, grade, lifecycle))
        else:
            print(str_x_msg_no_school % school)

    # 添加老师(老师信息，班级)
    def set_teacher(self, school, grade, teacher):

        print(str_c_grade_teacher_msg % (teacher, grade))

    # 添加学生(学生信息，班级)
    def set_student(self, student, grade):
        print(str_c_grade_student_msg % (student, grade))
        self.students.append(student)

    def __del__(self):
        pass


class User(object):
    def __init__(self, name, age, sex, id, grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.id = id
        self.grade = grade

    def reg(obj):
        obj.reg()


class Teacher(User):

    def reg(self):
        dic = {"姓名": self.name, "年龄": self.age, "性别": self.sex, "id": self.id}
        write_data(DB_PATH + F_STUDENT, dic)
        s_info = get_data(DB_PATH + F_STUDENT)
        print("老师[%s]注册成功\n基本信息：%s" % (s_info["姓名"], s_info))

    def get_grade_info(self):
        pass


class Student(User):

    def reg(self):
        dic = {"姓名": self.name, "年龄": self.age, "性别": self.sex, "id": self.id}
        write_data(DB_PATH + F_STUDENT, dic)
        s_info = get_data(DB_PATH + F_STUDENT)
        print("学生[%s]注册成功\n基本信息：%s" % (s_info["姓名"],s_info))

    def pay_tuition(self, tuition):
        print("学生%s交学费[%s]成功" % (self.name, tuition))
        dic = {"姓名": self.name, "年龄": self.age, "性别": self.sex, "id": self.id, "学费": tuition}
        write_data(DB_PATH + F_STUDENT, dic)
        s_info = get_data(DB_PATH + F_STUDENT)
        print(s_info)
        print(s_info["姓名"])


# s = Student("学生01",25,"M","1001","班级2")
# s.reg()
# s.pay_tuition(3000)
# s = Manager()
# s.create_school("北京100","地址300")

# print(get_data(DB_PATH+F_SCHOOL))
# s.create_grade("python","6周")
# s.create_grade("linux","8周")


# pickle数据格式
json = [{
    "学校": "北京",
    "地址": "地址1",
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
        "学校": "上海",
        "地址": "地址1",
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

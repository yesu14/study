#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-05 下午 23:42
#  @Note    :

# 学校 名字，地址
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
    def enroll(self,stu_obj):
        print("为%s 办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣了老师：%s" % staff_obj.name)
        self.staffs.append(staff_obj)
        # print("雇佣了老师：%s"%self.staffs[0].name)
class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
               --------- 学生信息 %s --------
               name:%s
               age:%s
               sex:%s
               stu_id:%s
               grade:%s
           ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print("%s交学费 $%s" %(self.name,amount))

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
            --------- 老师信息 %s --------
            name:%s
            age:%s
            sex:%s
            salary:%s
            course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("授课功能",self.name)

school = School("老男孩IT","北京")
t1 = Teacher("老师1",55,"M",2000,"Linux")
t2 = Teacher("Alex",22,"M",3000,"PYTHON")

school.hire(t1)
# school.enroll(t1)

school.staffs[0].teach()

s1 = Student("学生1",21,"M",110,"PYTHON")
s2 = Student("学生2",15,"M",122,"Linux")

school.enroll(s1)
school.enroll(s2)

for student in school.students:
    print("在校学生：",student.name)
    student.pay_tuition(5000)

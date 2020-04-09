#  @Author  :RG
#  @Time    :2020-04-07 下午 16:35
#  @Note    :

name="RG"
print("my name is"+name)

name1 = '''
123
456
789
'''
print(name1)

name = input("您的姓名是？")
age = int(input("您的年龄是？"))
print(type(age))
age = str(age)
print(type(age))
job = input("您的职业是？")

# info = '''
# --------- 您的信息 -----------
# name = %s
# age  = %d
# job  = %s
# '''%(name,age,job)
# print(info)


info2 = '''
name = {_name}
age  = {_age}
job  = {_job} 
'''.format(_name = name,_age=age,_job=job)
print(info2)
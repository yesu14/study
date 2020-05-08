#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-05-02 下午 16:56
#  @Note    :没有处理负数

import re

formula = r"2*((60-30+(40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(4*3)/(16-3*2))"
#TODO 没有处理负数
'''
1.先判断左括号
(*)
'''

# 删除字符
# email = "tony@tiremove_thisger.net"
# m = re.search("remove_this", email)
# print(email[:m.start()] + email[m.end():])



#进行加减乘除运算
def calculate(symbol,x,y):
    if symbol == "+":
        return int(int(x) + int(y))
    elif symbol == "-":
        return int(int(x) - int(y))
    elif symbol == "*":
        return int(int(x) * int(y))
    elif symbol == "/":
        return int(int(x) / int(y))

def handle_formula(formula):
    formula = formula.strip("(").strip(")")
    print("公式：",formula)
    if re.search(r"[*/]",formula):
        arr_f = re.split(r'[*/]',formula)   #['64-7', '8', '8']
        arr_j = re.split(r'[+-]', arr_f[0]) #['64','7']
        arry_k = re.split(r'[+-]', arr_f[1])
        symbol = formula.replace(arr_f[0],"")[0]
        print("%s %s %s" %(arr_j[-1],symbol,arry_k[0]))
        result = calculate(symbol,arr_j[-1],arry_k[0])
        print("result:",result)
        formula = formula.replace((arr_j[-1]+symbol+arry_k[0]),str(result))
        return handle_formula(formula)
    elif re.search(r'[+-]',formula):
        arr = re.split(r'[+-]',formula)
        if len(arr)>0:
            symbol = formula.replace(arr[0],"")[0]
            result = calculate(symbol,arr[0],arr[1])
            formula = formula.replace((arr[0]+symbol+arr[1]),str(result))
            return handle_formula(formula)
    return formula

def brackets(formula):
    print("原始公式：",formula)
    if re.search(r'\([^()]+\)', formula):
        x = re.search(r'\([^()]+\)', formula).group()
        print("x:",x)
        result = handle_formula(x)
        new_formula = formula.replace(x,str(result))
        print("新公式:",new_formula)
        return brackets(new_formula)
    else:
        print("formula中没有括号：",formula)
        sum = handle_formula(formula)
        print("运算结果：",sum)




brackets(formula)

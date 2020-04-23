#-*- coding:utf-8 -*-
#  @Author  :RG
#  @Time    :2020-04-23 下午 22:42
#  @Note    :
from PIL import Image
import numpy as np

#为了便于文件的导入，可以使用相对路径，将文件和程序放在同一个文件夹下

vec_el=np.pi/2.2
vec_az=np.pi/4.
depth=10.
im=Image.open("35.jpg").convert('L')
a=np.asarray(im).astype('float')
grad=np.gradient(a)
grad_x,grad_y=grad
grad_x=grad_x*depth/100.
grad_y=grad_y*depth/100.
dx=np.cos(vec_el)*np.cos(vec_az)
dy=np.cos(vec_el)*np.sin(vec_az)
dz=np.sin(vec_el)
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1./A
a2=255*(dx*uni_x+dy*uni_y+dz*uni_z)
a2=a2.clip(0,255)
im2=Image.fromarray(a2.astype('uint8'))
im2.save('356.jpg')
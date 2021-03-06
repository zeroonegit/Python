#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: number4.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 20:19:39
############################

'''
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。

例如1^3 + 5^3 + 3^3 = 153。
1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
'''

# Python 检测用户输入的数字是否为阿姆斯特朗数


#=======================================================================

## 获取用户输入的数字
#num = int(input('请输入一个数字： '))
#
## 初始化变量 sum
#sum = 0
#
## 指数
#n = len(str(num))
#
## 检测
#temp = num
#while temp > 0:
#    digit = temp % 10
#    sum += digit ** n
#    temp //= 10
#
## 输出结果
#if num == sum:
#    print(num, '是阿姆斯特朗数')
#else:
#    print(num, '不是阿姆斯特朗数')


#=======================================================================

## 获取用户输入的数字
##num = int(input('请输入一个数字： '))
#
#def amstl_number(num):
#    # 初始化变量 sum
#    sum = 0
#
#    # 指数
#    n = len(str(num))
#
#    # 检测
#    temp = num
#    while temp > 0:
#        digit = temp % 10
#        sum += digit ** n
#        temp //= 10
#
#    # 输出结果
#    if num == sum:
#        print(num, '是阿姆斯特朗数')
#    #else:
#    #    print(num, '不是阿姆斯特朗数')
#
#for i in range(1000):
#    amstl_number(i)


#=======================================================================

# 获取用户输入的数字
lower = int(input('最小值： '))
upper = int(input('最大值： '))

for num in range(lower, upper + 1):
    # 初始化变量 sum
    sum = 0

    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    # 输出结果
    if num == sum:
        print(num, '是阿姆斯特朗数')

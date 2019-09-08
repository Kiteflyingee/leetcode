# -*- coding:UTF-8 -*-
#! /usr/bin/python3

import random

v = []

def display(v):
        '''显示界面

        '''
        print(v[0][0], v[0][1], v[0][2], v[0][3])
        print(v[1][0], v[1][1], v[1][2], v[1][3])
        print(v[2][0], v[2][1], v[2][2], v[2][3])
        print(v[3][0], v[3][1], v[3][2], v[3][3])


def align(vList, direction):
        '''对齐非零的数字

        direction == 'left'：向左对齐，例如[8,0,0,2]左对齐后[8,2,0,0]
        direction == 'right'：向右对齐，例如[8,0,0,2]右对齐后[0,0,8,2]
        '''

        # 移除列表中的0
        for i in range(vList.count(0)):
                vList.remove(0)
        # 被移除的0
        zeros = [0 for x in range(4 - len(vList))]
        # 在非0数字的一侧补充0
        if direction == 'left':
                vList.extend(zeros)
        else:
                vList[:0] = zeros
        
def addSame(vList, direction):
        '''在列表查找相同且相邻的数字相加, 找到符合条件的返回True，否则返回False,同时还返回增加的分数
        
        direction == 'left':从右向左查找，找到相同且相邻的两个数字，左侧数字翻倍，右侧数字置0
        direction == 'right':从左向右查找，找到相同且相邻的两个数字，右侧数字翻倍，左侧数字置0
        '''
        if direction == 'left':
                for i in [0, 1, 2]:
                        if vList[i] == vList[i+1] != 0: 
                                vList[i] *= 2
                                vList[i+1] = 0
                                return {'bool':True}
        else:
                for i in [3, 2, 1]:
                        if vList[i] == vList[i-1] != 0:
                                vList[i-1] *= 2
                                vList[i] = 0
                                return {'bool':True}
        return {'bool':False}

def handle(vList, direction):
        '''处理一行（列）中的数据，得到最终的该行（列）的数字状态值, 返回得分

        vList: 列表结构，存储了一行（列）中的数据
        direction: 移动方向,向上和向左都使用方向'left'，向右和向下都使用'right'
        '''
        totalScore = 0
        align(vList, direction)
        result = addSame(vList, direction)
        while result['bool'] == True:
                align(vList, direction)
                result = addSame(vList, direction)
        return totalScore
        

def operation(v, op):
        '''根据移动方向重新计算矩阵状态值，并记录得分
        '''
        totalScore = 0
        gameOver = False
        direction = 'left'
        if op in ['3']:    # 向左移动
                direction = 'left'
                for row in range(4):
                        totalScore += handle(v[row], direction)
        elif op in ['4']:  # 向右移动
                direction = 'right'
                for row in range(4):
                        totalScore += handle(v[row], direction)
        elif op in ['1']:  # 向上移动
                direction = 'left'
                for col in range(4):
                        # 将矩阵中一列复制到一个列表中然后处理
                        vList = [v[row][col] for row in range(4)]
                        totalScore += handle(vList, direction)
                        # 从处理后的列表中的数字覆盖原来矩阵中的值
                        for row in range(4):
                                v[row][col] = vList[row]
        elif op in ['2']:  # 向下移动
                direction = 'right'
                for col in range(4):
                        # 同上
                        vList = [v[row][col] for row in range(4)]
                        totalScore += handle(vList, direction)
                        for row in range(4):
                                v[row][col] = vList[row]

fx = input()

for _ in range(4):
    v_row = list(map(int, input().split()))
    v.append(v_row)

result = operation(v, fx)
display(v)

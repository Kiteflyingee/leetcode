# -*- coding: UTF-8 -*-

class Parent(object):        # 定义父类
   def myMethod(self):
      print 'father'
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print 'son'
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法

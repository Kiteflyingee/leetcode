# conda环境配置

## 使用conda来维护多个python环境
创建一个虚拟环境：conda create -n 环境名 python=version（新环境的python版本）  

激活对应环境：activate 环境名 （如果提示命令无效可以在前面加conda activate 环境名）  

tips:在conda的虚拟环境中可以使用pip安装模块包也可以通过conda来安装对应的包，推荐使用conda安装，会帮助安装一些依赖包，如果用conda命令搜索不到需要的包，可以在anaconda cloud查找需要的包：不同channels会有人提供一些非官方的包
https://anaconda.org

## 在pycharm中配置conda环境
在不同环境下维护对应的python包，各环境下包版本互不影响。  
在pycharm添加一个conda虚拟环境  
https://www.cnblogs.com/fanzhongjie/p/11439103.html

## jupyter添加conda其他环境内核
https://blog.csdn.net/BigBossZjz/article/details/79985082

## canda常用命令
https://www.jianshu.com/p/7ebe1df808ba
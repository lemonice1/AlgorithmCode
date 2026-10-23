# -*- coding: utf-8 -*-
# Python 3 算法实现；中文题意、算法说明与原课程顺序对应。
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 收集累加和等于aim的所有路径
# 测试链接 : https://leetcode.cn/problems/path-sum-ii/
class Code03_PathSumII:
    __java_fields__ = {}
    # 不提交这个类
    class TreeNode:
        __java_fields__ = {'val': 'val', 'left': 'left', 'right': 'right'}
        # val：实例字段，在构造函数中初始化。
        # left：实例字段，在构造函数中初始化。
        # right：实例字段，在构造函数中初始化。
        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.left = None
            self.right = None
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 提交如下的方法
    @staticmethod
    def pathSum(root, aim):
        aim = jcast('int', aim)
        ans = jnew('ArrayList')
        if (root != None):
            path = jnew('ArrayList')
            Code03_PathSumII.f(root, aim, 0, path, ans)
        return ans

    @staticmethod
    def f(cur, aim, sum, path, ans):
        aim = jcast('int', aim)
        sum = jcast('int', sum)
        if ((jget(cur, 'left') == None) and (jget(cur, 'right') == None)):
            # 叶节点
            if (jcast('int', jadd(jget(cur, 'val'), sum)) == aim):
                jcall(path, 'add', jget(cur, 'val'))
                Code03_PathSumII.copy(path, ans)
                jcall(path, 'remove', jcast('int', (jcall(path, 'size') - 1)))
        else:
            # 不是叶节点
            jcall(path, 'add', jget(cur, 'val'))
            if (jget(cur, 'left') != None):
                Code03_PathSumII.f(jget(cur, 'left'), aim, jcast('int', jadd(sum, jget(cur, 'val'))), path, ans)
            if (jget(cur, 'right') != None):
                Code03_PathSumII.f(jget(cur, 'right'), aim, jcast('int', jadd(sum, jget(cur, 'val'))), path, ans)
            jcall(path, 'remove', jcast('int', (jcall(path, 'size') - 1)))

    @staticmethod
    def copy(path, ans):
        copy = jnew('ArrayList')
        for num in path:
            jcall(copy, 'add', num)
        jcall(ans, 'add', copy)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



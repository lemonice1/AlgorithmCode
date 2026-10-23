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

# 字符串的全部子序列
# 子序列本身是可以有重复的，只是这个题目要求去重
# 测试链接 : https://www.nowcoder.com/practice/92e6247998294f2c933906fdedbc6e6a
class Code01_Subsequences:
    __java_fields__ = {}
    @staticmethod
    def generatePermutation1(str):
        s = jcall(str, 'toCharArray')
        set = jnew('HashSet')
        Code01_Subsequences.f1(s, 0, jnew('StringBuilder'), set)
        m = jcast('int', jcall(set, 'size'))
        ans = jarray('String', [m])
        i = jcast('int', 0)
        for cur in set:
            jset(ans, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], cur)
        return ans

    # s[i...]，之前决定的路径path，set收集结果时去重
    @staticmethod
    def f1(s, i, path, set):
        i = jcast('int', i)
        if (i == jget(s, 'length')):
            jcall(set, 'add', jcall(path, 'toString'))
        else:
            # 加到路径中去
            jcall(path, 'append', s[i])
            Code01_Subsequences.f1(s, jcast('int', jadd(i, 1)), path, set)
            # 从路径中移除
            jcall(path, 'deleteCharAt', jcast('int', (jcall(path, 'length') - 1)))
            Code01_Subsequences.f1(s, jcast('int', jadd(i, 1)), path, set)

    @staticmethod
    def generatePermutation2(str):
        s = jcall(str, 'toCharArray')
        set = jnew('HashSet')
        Code01_Subsequences.f2(s, 0, jarray('char', [jget(s, 'length')]), 0, set)
        m = jcast('int', jcall(set, 'size'))
        ans = jarray('String', [m])
        i = jcast('int', 0)
        for cur in set:
            jset(ans, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], cur)
        return ans

    @staticmethod
    def f2(s, i, path, size, set):
        i = jcast('int', i)
        size = jcast('int', size)
        if (i == jget(s, 'length')):
            jcall(set, 'add', jstatic('String', 'valueOf', path, 0, size))
        else:
            path[size] = jcast('char', s[i])
            Code01_Subsequences.f2(s, jcast('int', jadd(i, 1)), path, jcast('int', jadd(size, 1)), set)
            Code01_Subsequences.f2(s, jcast('int', jadd(i, 1)), path, size, set)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



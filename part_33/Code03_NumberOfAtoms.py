# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 含有嵌套的分子式求原子数量
# 测试链接 : https://leetcode.cn/problems/number-of-atoms/
class Code03_NumberOfAtoms:
    __java_fields__ = {'where': 'where'}
    @staticmethod
    def countOfAtoms(str):
        Code03_NumberOfAtoms.where = jcast('int', 0)
        map = Code03_NumberOfAtoms.f(jcall(str, 'toCharArray'), 0)
        ans = jnew('StringBuilder')
        for key in jcall(map, 'keySet'):
            jcall(ans, 'append', key)
            cnt = jcast('int', jcall(map, 'get', key))
            if (cnt > 1):
                jcall(ans, 'append', cnt)
        return jcall(ans, 'toString')

    where = 0
    # s[i....]开始计算，遇到字符串终止 或者 遇到 ) 停止
    # 返回 : 自己负责的这一段字符串的结果，有序表！
    # 返回之间，更新全局变量where，为了上游函数知道从哪继续！
    @staticmethod
    def f(s, i):
        i = jcast('int', i)
        # ans是总表
        ans = jnew('TreeMap')
        # 之前收集到的名字，历史一部分
        name = jnew('StringBuilder')
        # 之前收集到的有序表，历史一部分
        pre = None
        # 历史翻几倍
        cnt = jcast('int', 0)
        while ((i < jget(s, 'length')) and (s[i] != jchar(')'))):
            if (((s[i] >= jchar('A')) and (s[i] <= jchar('Z'))) or (s[i] == jchar('('))):
                Code03_NumberOfAtoms.fill(ans, name, pre, cnt)
                jcall(name, 'setLength', 0)
                pre = None
                cnt = jcast('int', 0)
                if ((s[i] >= jchar('A')) and (s[i] <= jchar('Z'))):
                    jcall(name, 'append', s[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]])
                else:
                    # 遇到 (
                    pre = Code03_NumberOfAtoms.f(s, jcast('int', jadd(i, 1)))
                    i = jcast('int', jcast('int', jadd(Code03_NumberOfAtoms.where, 1)))
            else:
                if ((s[i] >= jchar('a')) and (s[i] <= jchar('z'))):
                    jcall(name, 'append', s[((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2]])
                else:
                    cnt = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (cnt * 10)), s[((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2]])) - jchar('0'))))
        Code03_NumberOfAtoms.fill(ans, name, pre, cnt)
        Code03_NumberOfAtoms.where = jcast('int', i)
        return ans

    @staticmethod
    def fill(ans, name, pre, cnt):
        cnt = jcast('int', cnt)
        if ((jcall(name, 'length') > 0) or (pre != None)):
            cnt = jcast('int', (1 if (cnt == 0) else cnt))
            if (jcall(name, 'length') > 0):
                key = jcall(name, 'toString')
                jcall(ans, 'put', key, jadd(jcall(ans, 'getOrDefault', key, 0), cnt))
            else:
                for key in jcall(pre, 'keySet'):
                    jcall(ans, 'put', key, jadd(jcall(ans, 'getOrDefault', key, 0), (jcall(pre, 'get', key) * cnt)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_NumberOfAtoms.where = jcast('int', 0)

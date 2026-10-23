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

# 除法求值
# 所有变量都用字符串表示，并且给定若干组等式
# 比如等式
# ["ab", "ef"] = 8，代表ab / ef = 8
# ["ct", "ef"] = 2，代表ct / ef = 2
# 所有等式都是正确的并且可以进行推断，给定所有等式之后，会给你若干条查询
# 比如查询，["ab", "ct"]，根据上面的等式推断，ab / ct = 4
# 如果某条查询中的变量，从来没在等式中出现过，认为答案是-1.0
# 如果某条查询的答案根本推断不出来，认为答案是-1.0
# 返回所有查询的答案
# 测试链接 : https://leetcode.cn/problems/evaluate-division/
class Code05_EvaluateDivision:
    __java_fields__ = {'father': 'father', 'dist': 'dist'}
    @staticmethod
    def calcEquation(equations, values, queries):
        Code05_EvaluateDivision.prepare(equations)
        i = jcast('int', 0)
        while (i < jget(values, 'length')):
            Code05_EvaluateDivision.union(jcall(jcall(equations, 'get', i), 'get', 0), jcall(jcall(equations, 'get', i), 'get', 1), values[i])
            i = jcast('int', (i + 1))
        ans = jarray('double', [jcall(queries, 'size')])
        i = jcast('int', 0)
        while (i < jcall(queries, 'size')):
            jset(ans, i, Code05_EvaluateDivision.query(jcall(jcall(queries, 'get', i), 'get', 0), jcall(jcall(queries, 'get', i), 'get', 1)))
            i = jcast('int', (i + 1))
        return ans

    father = None
    dist = None
    @staticmethod
    def prepare(equations):
        jcall(Code05_EvaluateDivision.father, 'clear')
        jcall(Code05_EvaluateDivision.dist, 'clear')
        for list in equations:
            for key in list:
                jcall(Code05_EvaluateDivision.father, 'put', key, key)
                jcall(Code05_EvaluateDivision.dist, 'put', key, 1.0)

    @staticmethod
    def find(x):
        if (not jcall(Code05_EvaluateDivision.father, 'containsKey', x)):
            return None
        tmp = None
        fa = x
        if (not jcall(x, 'equals', jcall(Code05_EvaluateDivision.father, 'get', x))):
            tmp = jcall(Code05_EvaluateDivision.father, 'get', x)
            fa = Code05_EvaluateDivision.find(tmp)
            jcall(Code05_EvaluateDivision.dist, 'put', x, (jcall(Code05_EvaluateDivision.dist, 'get', x) * jcall(Code05_EvaluateDivision.dist, 'get', tmp)))
            jcall(Code05_EvaluateDivision.father, 'put', x, fa)
        return fa

    @staticmethod
    def union(l, r, v):
        v = jcast('double', v)
        lf = Code05_EvaluateDivision.find(l)
        rf = Code05_EvaluateDivision.find(r)
        if (not jcall(lf, 'equals', rf)):
            jcall(Code05_EvaluateDivision.father, 'put', lf, rf)
            jcall(Code05_EvaluateDivision.dist, 'put', lf, (jdiv(jcall(Code05_EvaluateDivision.dist, 'get', r), jcall(Code05_EvaluateDivision.dist, 'get', l)) * v))

    @staticmethod
    def query(l, r):
        lf = Code05_EvaluateDivision.find(l)
        rf = Code05_EvaluateDivision.find(r)
        if (((lf == None) or (rf == None)) or (not jcall(lf, 'equals', rf))):
            return jcast('double', (-1.0))
        return jcast('double', jdiv(jcall(Code05_EvaluateDivision.dist, 'get', l), jcall(Code05_EvaluateDivision.dist, 'get', r)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_EvaluateDivision.father = jnew('HashMap')
Code05_EvaluateDivision.dist = jnew('HashMap')

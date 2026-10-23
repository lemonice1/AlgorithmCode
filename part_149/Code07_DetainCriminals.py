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

# 关押罪犯
# 一共有n个犯人，编号1 ~ n，一共有两个监狱，你可以决定每个犯人去哪个监狱
# 给定m条记录，每条记录 l r v，表示l号犯人和r号犯人的仇恨值
# 每个监狱的暴力值 = 该监狱中仇恨最深的犯人之间的仇恨值
# 冲突值 = max(第一座监狱的暴力值，第二座监狱的暴力值)
# 犯人的分配方案需要让这个冲突值最小，返回最小能是多少
# 1 <= n <= 20000    1 <= m <= 100000    1 <= 仇恨值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1525
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_DetainCriminals:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'father': 'father', 'enemy': 'enemy', 'arr': 'arr'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    father = None
    enemy = None
    arr = None
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code07_DetainCriminals.n):
            Code07_DetainCriminals.father[i] = jcast('int', i)
            Code07_DetainCriminals.enemy[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code07_DetainCriminals.father, i, (i if (Code07_DetainCriminals.father[i] == i) else Code07_DetainCriminals.find(Code07_DetainCriminals.father[i])))
        return jcast('int', Code07_DetainCriminals.father[i])

    @staticmethod
    def union(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        jset(Code07_DetainCriminals.father, Code07_DetainCriminals.find(l), Code07_DetainCriminals.find(r))

    @staticmethod
    def same(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('boolean', (Code07_DetainCriminals.find(l) == Code07_DetainCriminals.find(r)))

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code07_DetainCriminals.arr, 1, jcast('int', jadd(Code07_DetainCriminals.m, 1)), (lambda a, b: (b[2] - a[2])))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        l = 0
        r = 0
        v = 0
        while (i <= Code07_DetainCriminals.m):
            try:
                l = jcast('int', Code07_DetainCriminals.arr[i][0])
                r = jcast('int', Code07_DetainCriminals.arr[i][1])
                v = jcast('int', Code07_DetainCriminals.arr[i][2])
                if Code07_DetainCriminals.same(l, r):
                    ans = jcast('int', v)
                    raise JBreak(None)
                else:
                    if (Code07_DetainCriminals.enemy[l] == 0):
                        Code07_DetainCriminals.enemy[l] = jcast('int', r)
                    else:
                        Code07_DetainCriminals.union(Code07_DetainCriminals.enemy[l], r)
                    if (Code07_DetainCriminals.enemy[r] == 0):
                        Code07_DetainCriminals.enemy[r] = jcast('int', l)
                    else:
                        Code07_DetainCriminals.union(l, Code07_DetainCriminals.enemy[r])
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code07_DetainCriminals.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code07_DetainCriminals.m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code07_DetainCriminals.prepare()
        i = jcast('int', 1)
        while (i <= Code07_DetainCriminals.m):
            jcall(in_, 'nextToken')
            jset(Code07_DetainCriminals.arr[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code07_DetainCriminals.arr[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code07_DetainCriminals.arr[i], 2, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code07_DetainCriminals.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_DetainCriminals.MAXN = jcast('int', 20002)
Code07_DetainCriminals.MAXM = jcast('int', 100001)
Code07_DetainCriminals.n = jcast('int', 0)
Code07_DetainCriminals.m = jcast('int', 0)
Code07_DetainCriminals.father = jarray('int', [Code07_DetainCriminals.MAXN])
Code07_DetainCriminals.enemy = jarray('int', [Code07_DetainCriminals.MAXN])
Code07_DetainCriminals.arr = jarray('int', [Code07_DetainCriminals.MAXM, 3])

if __name__ == '__main__':
    Code07_DetainCriminals.main([])

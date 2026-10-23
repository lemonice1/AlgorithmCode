# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 猴王，Python版
# 给定n只猴子的战斗力，一开始每个猴子都是独立的阵营
# 一共有m次冲突，每次冲突给定两只猴子的编号x、y
# 如果x和y在同一阵营，这次冲突停止，打印-1
# 如果x和y在不同阵营，x所在阵营的最强猴子会和y所在阵营的最强猴子进行打斗
# 打斗的结果是，两个各自阵营的最强猴子，战斗力都减半，向下取整，其他猴子战力不变
# 然后两个阵营合并，打印合并后的阵营最大战斗力
# 题目可能有多组数据，需要监控输入流直到结束
# 1 <= n, m <= 10^5
# 0 <= 猴子战斗力 <= 32768
# 测试链接 : https://www.luogu.com.cn/problem/P1456
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_MonkeyKing2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'num': 'num', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father'}
    MAXN = 0
    n = 0
    m = 0
    num = None
    left = None
    right = None
    dist = None
    father = None
    @staticmethod
    def prepare():
        Code03_MonkeyKing2.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code03_MonkeyKing2.n):
            jset(Code03_MonkeyKing2.left, i, jset(Code03_MonkeyKing2.right, i, jset(Code03_MonkeyKing2.dist, i, 0)))
            Code03_MonkeyKing2.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code03_MonkeyKing2.father, i, (i if (Code03_MonkeyKing2.father[i] == i) else Code03_MonkeyKing2.find(Code03_MonkeyKing2.father[i])))
        return jcast('int', Code03_MonkeyKing2.father[i])

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 维护大根堆
        if (Code03_MonkeyKing2.num[i] < Code03_MonkeyKing2.num[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code03_MonkeyKing2.right, i, Code03_MonkeyKing2.merge(Code03_MonkeyKing2.right[i], j))
        if (Code03_MonkeyKing2.dist[Code03_MonkeyKing2.left[i]] < Code03_MonkeyKing2.dist[Code03_MonkeyKing2.right[i]]):
            tmp = jcast('int', Code03_MonkeyKing2.left[i])
            Code03_MonkeyKing2.left[i] = jcast('int', Code03_MonkeyKing2.right[i])
            Code03_MonkeyKing2.right[i] = jcast('int', tmp)
        Code03_MonkeyKing2.dist[i] = jcast('int', jcast('int', jadd(Code03_MonkeyKing2.dist[Code03_MonkeyKing2.right[i]], 1)))
        jset(Code03_MonkeyKing2.father, Code03_MonkeyKing2.left[i], jset(Code03_MonkeyKing2.father, Code03_MonkeyKing2.right[i], i))
        return jcast('int', i)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        jset(Code03_MonkeyKing2.father, Code03_MonkeyKing2.left[i], Code03_MonkeyKing2.left[i])
        jset(Code03_MonkeyKing2.father, Code03_MonkeyKing2.right[i], Code03_MonkeyKing2.right[i])
        jset(Code03_MonkeyKing2.father, i, Code03_MonkeyKing2.merge(Code03_MonkeyKing2.left[i], Code03_MonkeyKing2.right[i]))
        jset(Code03_MonkeyKing2.left, i, jset(Code03_MonkeyKing2.right, i, jset(Code03_MonkeyKing2.dist, i, 0)))
        return jcast('int', Code03_MonkeyKing2.father[i])

    @staticmethod
    def fight(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        a = jcast('int', Code03_MonkeyKing2.find(x))
        b = jcast('int', Code03_MonkeyKing2.find(y))
        if (a == b):
            return jcast('int', jcast('int', (-1)))
        l = jcast('int', Code03_MonkeyKing2.pop(a))
        r = jcast('int', Code03_MonkeyKing2.pop(b))
        Code03_MonkeyKing2.num[a] = jcast('int', jcast('int', jdiv(Code03_MonkeyKing2.num[a], 2)))
        Code03_MonkeyKing2.num[b] = jcast('int', jcast('int', jdiv(Code03_MonkeyKing2.num[b], 2)))
        jset(Code03_MonkeyKing2.father, a, jset(Code03_MonkeyKing2.father, b, jset(Code03_MonkeyKing2.father, l, jset(Code03_MonkeyKing2.father, r, Code03_MonkeyKing2.merge(Code03_MonkeyKing2.merge(l, a), Code03_MonkeyKing2.merge(r, b))))))
        return jcast('int', Code03_MonkeyKing2.num[Code03_MonkeyKing2.father[a]])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_MonkeyKing2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_MonkeyKing2.prepare()
            i = jcast('int', 1)
            while (i <= Code03_MonkeyKing2.n):
                jcall(in_, 'nextToken')
                Code03_MonkeyKing2.num[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(in_, 'nextToken')
            Code03_MonkeyKing2.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            x = 0
            y = 0
            while (i <= Code03_MonkeyKing2.m):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code03_MonkeyKing2.fight(x, y))
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MonkeyKing2.MAXN = jcast('int', 100001)
Code03_MonkeyKing2.n = jcast('int', 0)
Code03_MonkeyKing2.m = jcast('int', 0)
Code03_MonkeyKing2.num = jarray('int', [Code03_MonkeyKing2.MAXN])
Code03_MonkeyKing2.left = jarray('int', [Code03_MonkeyKing2.MAXN])
Code03_MonkeyKing2.right = jarray('int', [Code03_MonkeyKing2.MAXN])
Code03_MonkeyKing2.dist = jarray('int', [Code03_MonkeyKing2.MAXN])
Code03_MonkeyKing2.father = jarray('int', [Code03_MonkeyKing2.MAXN])

if __name__ == '__main__':
    Code03_MonkeyKing2.main([])

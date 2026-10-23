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

# Splay树的实现，不用词频压缩，Python版
# 实现一种结构，支持如下操作，要求单次调用的时间复杂度O(log n)
# 1，增加x，重复加入算多个词频
# 2，删除x，如果有多个，只删掉一个
# 3，查询x的排名，x的排名为，比x小的数的个数+1
# 4，查询数据中排名为x的数
# 5，查询x的前驱，x的前驱为，小于x的数中最大的数，不存在返回整数最小值
# 6，查询x的后继，x的后继为，大于x的数中最小的数，不存在返回整数最大值
# 所有操作的次数 <= 10^5
# -10^7 <= x <= +10^7
# 测试链接 : https://www.luogu.com.cn/problem/P3369
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Splay1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size'}
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    father = None
    left = None
    right = None
    size = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_Splay1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_Splay1.size[Code01_Splay1.left[i]], Code01_Splay1.size[Code01_Splay1.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (Code01_Splay1.right[Code01_Splay1.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', Code01_Splay1.father[i])
        g = jcast('int', Code01_Splay1.father[f])
        soni = jcast('int', Code01_Splay1.lr(i))
        sonf = jcast('int', Code01_Splay1.lr(f))
        if (soni == 1):
            Code01_Splay1.right[f] = jcast('int', Code01_Splay1.left[i])
            if (Code01_Splay1.right[f] != 0):
                jset(Code01_Splay1.father, Code01_Splay1.right[f], f)
            Code01_Splay1.left[i] = jcast('int', f)
        else:
            Code01_Splay1.left[f] = jcast('int', Code01_Splay1.right[i])
            if (Code01_Splay1.left[f] != 0):
                jset(Code01_Splay1.father, Code01_Splay1.left[f], f)
            Code01_Splay1.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                Code01_Splay1.right[g] = jcast('int', i)
            else:
                Code01_Splay1.left[g] = jcast('int', i)
        Code01_Splay1.father[f] = jcast('int', i)
        Code01_Splay1.father[i] = jcast('int', g)
        Code01_Splay1.up(f)
        Code01_Splay1.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', Code01_Splay1.father[i])
        g = jcast('int', Code01_Splay1.father[f])
        while (f != goal):
            if (g != goal):
                if (Code01_Splay1.lr(i) == Code01_Splay1.lr(f)):
                    Code01_Splay1.rotate(f)
                else:
                    Code01_Splay1.rotate(i)
            Code01_Splay1.rotate(i)
            f = jcast('int', Code01_Splay1.father[i])
            g = jcast('int', Code01_Splay1.father[f])
        if (goal == 0):
            Code01_Splay1.head = jcast('int', i)

    # 整棵树上找到中序排名为rank的节点，返回节点编号
    # 这个方法不是题目要求的查询操作，作为内部方法使用
    # 为什么该方法不进行提根操作？
    # 因为remove方法使用该方法时，要求find不能提根！
    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', Code01_Splay1.head)
        while (i != 0):
            if (jcast('int', jadd(Code01_Splay1.size[Code01_Splay1.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (Code01_Splay1.size[Code01_Splay1.left[i]] >= rank):
                    i = jcast('int', Code01_Splay1.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(Code01_Splay1.size[Code01_Splay1.left[i]], 1)))))
                    i = jcast('int', Code01_Splay1.right[i])
        return jcast('int', 0)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        jset(Code01_Splay1.key, ((_java_obj_1 := Code01_Splay1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        Code01_Splay1.size[Code01_Splay1.cnt] = jcast('int', 1)
        if (Code01_Splay1.head == 0):
            Code01_Splay1.head = jcast('int', Code01_Splay1.cnt)
        else:
            f = jcast('int', 0)
            i = jcast('int', Code01_Splay1.head)
            son = jcast('int', 0)
            while (i != 0):
                f = jcast('int', i)
                if (Code01_Splay1.key[i] <= num):
                    son = jcast('int', 1)
                    i = jcast('int', Code01_Splay1.right[i])
                else:
                    son = jcast('int', 0)
                    i = jcast('int', Code01_Splay1.left[i])
            if (son == 1):
                Code01_Splay1.right[f] = jcast('int', Code01_Splay1.cnt)
            else:
                Code01_Splay1.left[f] = jcast('int', Code01_Splay1.cnt)
            Code01_Splay1.father[Code01_Splay1.cnt] = jcast('int', f)
            Code01_Splay1.splay(Code01_Splay1.cnt, 0)

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        i = jcast('int', Code01_Splay1.head)
        last = jcast('int', Code01_Splay1.head)
        ans = jcast('int', 0)
        while (i != 0):
            last = jcast('int', i)
            if (Code01_Splay1.key[i] >= num):
                i = jcast('int', Code01_Splay1.left[i])
            else:
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(Code01_Splay1.size[Code01_Splay1.left[i]], 1)))))
                i = jcast('int', Code01_Splay1.right[i])
        Code01_Splay1.splay(last, 0)
        return jcast('int', jcast('int', jadd(ans, 1)))

    @staticmethod
    def index(x):
        x = jcast('int', x)
        i = jcast('int', Code01_Splay1.find(x))
        Code01_Splay1.splay(i, 0)
        return jcast('int', Code01_Splay1.key[i])

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        i = jcast('int', Code01_Splay1.head)
        last = jcast('int', Code01_Splay1.head)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (Code01_Splay1.key[i] >= num):
                i = jcast('int', Code01_Splay1.left[i])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, Code01_Splay1.key[i]))
                i = jcast('int', Code01_Splay1.right[i])
        Code01_Splay1.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def post(num):
        num = jcast('int', num)
        i = jcast('int', Code01_Splay1.head)
        last = jcast('int', Code01_Splay1.head)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (Code01_Splay1.key[i] <= num):
                i = jcast('int', Code01_Splay1.right[i])
            else:
                ans = jcast('int', jstatic('Math', 'min', ans, Code01_Splay1.key[i]))
                i = jcast('int', Code01_Splay1.left[i])
        Code01_Splay1.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        kth = jcast('int', Code01_Splay1.rank(num))
        if (kth != Code01_Splay1.rank(jcast('int', jadd(num, 1)))):
            i = jcast('int', Code01_Splay1.find(kth))
            Code01_Splay1.splay(i, 0)
            if (Code01_Splay1.left[i] == 0):
                Code01_Splay1.head = jcast('int', Code01_Splay1.right[i])
            else:
                if (Code01_Splay1.right[i] == 0):
                    Code01_Splay1.head = jcast('int', Code01_Splay1.left[i])
                else:
                    j = jcast('int', Code01_Splay1.find(jcast('int', jadd(kth, 1))))
                    Code01_Splay1.splay(j, i)
                    Code01_Splay1.left[j] = jcast('int', Code01_Splay1.left[i])
                    jset(Code01_Splay1.father, Code01_Splay1.left[j], j)
                    Code01_Splay1.up(j)
                    Code01_Splay1.head = jcast('int', j)
            Code01_Splay1.father[Code01_Splay1.head] = jcast('int', 0)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                Code01_Splay1.add(x)
            else:
                if (op == 2):
                    Code01_Splay1.remove(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code01_Splay1.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code01_Splay1.index(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code01_Splay1.pre(x))
                            else:
                                jcall(out, 'println', Code01_Splay1.post(x))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Splay1.MAXN = jcast('int', 100001)
Code01_Splay1.head = jcast('int', 0)
Code01_Splay1.cnt = jcast('int', 0)
Code01_Splay1.key = jarray('int', [Code01_Splay1.MAXN])
Code01_Splay1.father = jarray('int', [Code01_Splay1.MAXN])
Code01_Splay1.left = jarray('int', [Code01_Splay1.MAXN])
Code01_Splay1.right = jarray('int', [Code01_Splay1.MAXN])
Code01_Splay1.size = jarray('int', [Code01_Splay1.MAXN])

if __name__ == '__main__':
    Code01_Splay1.main([])

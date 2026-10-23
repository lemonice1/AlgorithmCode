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

# Splay树实现普通有序表，不用词频压缩，数据加强的测试，Python版
# 这个文件课上没有讲，测试数据加强了，而且有强制在线的要求
# 基本功能要求都是不变的，可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P6136
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp1:
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
        FollowUp1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], FollowUp1.size[FollowUp1.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (FollowUp1.right[FollowUp1.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', FollowUp1.father[i])
        g = jcast('int', FollowUp1.father[f])
        soni = jcast('int', FollowUp1.lr(i))
        sonf = jcast('int', FollowUp1.lr(f))
        if (soni == 1):
            FollowUp1.right[f] = jcast('int', FollowUp1.left[i])
            if (FollowUp1.right[f] != 0):
                jset(FollowUp1.father, FollowUp1.right[f], f)
            FollowUp1.left[i] = jcast('int', f)
        else:
            FollowUp1.left[f] = jcast('int', FollowUp1.right[i])
            if (FollowUp1.left[f] != 0):
                jset(FollowUp1.father, FollowUp1.left[f], f)
            FollowUp1.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                FollowUp1.right[g] = jcast('int', i)
            else:
                FollowUp1.left[g] = jcast('int', i)
        FollowUp1.father[f] = jcast('int', i)
        FollowUp1.father[i] = jcast('int', g)
        FollowUp1.up(f)
        FollowUp1.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', FollowUp1.father[i])
        g = jcast('int', FollowUp1.father[f])
        while (f != goal):
            if (g != goal):
                if (FollowUp1.lr(i) == FollowUp1.lr(f)):
                    FollowUp1.rotate(f)
                else:
                    FollowUp1.rotate(i)
            FollowUp1.rotate(i)
            f = jcast('int', FollowUp1.father[i])
            g = jcast('int', FollowUp1.father[f])
        if (goal == 0):
            FollowUp1.head = jcast('int', i)

    # 整棵树上找到中序排名为rank的节点，返回节点编号
    # 这个方法不是题目要求的查询操作，作为内部方法使用
    # 为什么该方法不进行提根操作？
    # 因为remove方法使用该方法时，要求find不能提根！
    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', FollowUp1.head)
        while (i != 0):
            if (jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (FollowUp1.size[FollowUp1.left[i]] >= rank):
                    i = jcast('int', FollowUp1.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], 1)))))
                    i = jcast('int', FollowUp1.right[i])
        return jcast('int', 0)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        jset(FollowUp1.key, ((_java_obj_1 := FollowUp1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        FollowUp1.size[FollowUp1.cnt] = jcast('int', 1)
        if (FollowUp1.head == 0):
            FollowUp1.head = jcast('int', FollowUp1.cnt)
        else:
            f = jcast('int', 0)
            i = jcast('int', FollowUp1.head)
            son = jcast('int', 0)
            while (i != 0):
                f = jcast('int', i)
                if (FollowUp1.key[i] <= num):
                    son = jcast('int', 1)
                    i = jcast('int', FollowUp1.right[i])
                else:
                    son = jcast('int', 0)
                    i = jcast('int', FollowUp1.left[i])
            if (son == 1):
                FollowUp1.right[f] = jcast('int', FollowUp1.cnt)
            else:
                FollowUp1.left[f] = jcast('int', FollowUp1.cnt)
            FollowUp1.father[FollowUp1.cnt] = jcast('int', f)
            FollowUp1.splay(FollowUp1.cnt, 0)

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp1.head)
        last = jcast('int', FollowUp1.head)
        ans = jcast('int', 0)
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp1.key[i] >= num):
                i = jcast('int', FollowUp1.left[i])
            else:
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], 1)))))
                i = jcast('int', FollowUp1.right[i])
        FollowUp1.splay(last, 0)
        return jcast('int', jcast('int', jadd(ans, 1)))

    @staticmethod
    def index(x):
        x = jcast('int', x)
        i = jcast('int', FollowUp1.find(x))
        FollowUp1.splay(i, 0)
        return jcast('int', FollowUp1.key[i])

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp1.head)
        last = jcast('int', FollowUp1.head)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp1.key[i] >= num):
                i = jcast('int', FollowUp1.left[i])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, FollowUp1.key[i]))
                i = jcast('int', FollowUp1.right[i])
        FollowUp1.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def post(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp1.head)
        last = jcast('int', FollowUp1.head)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp1.key[i] <= num):
                i = jcast('int', FollowUp1.right[i])
            else:
                ans = jcast('int', jstatic('Math', 'min', ans, FollowUp1.key[i]))
                i = jcast('int', FollowUp1.left[i])
        FollowUp1.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        kth = jcast('int', FollowUp1.rank(num))
        if (kth != FollowUp1.rank(jcast('int', jadd(num, 1)))):
            i = jcast('int', FollowUp1.find(kth))
            FollowUp1.splay(i, 0)
            if (FollowUp1.left[i] == 0):
                FollowUp1.head = jcast('int', FollowUp1.right[i])
            else:
                if (FollowUp1.right[i] == 0):
                    FollowUp1.head = jcast('int', FollowUp1.left[i])
                else:
                    j = jcast('int', FollowUp1.find(jcast('int', jadd(kth, 1))))
                    FollowUp1.splay(j, i)
                    FollowUp1.left[j] = jcast('int', FollowUp1.left[i])
                    jset(FollowUp1.father, FollowUp1.left[j], j)
                    FollowUp1.up(j)
                    FollowUp1.head = jcast('int', j)
            FollowUp1.father[FollowUp1.head] = jcast('int', 0)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        num = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            num = jcast('int', jcast('int', jget(in_, 'nval')))
            FollowUp1.add(num)
            i = jcast('int', (i + 1))
        lastAns = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', (jcast('int', jget(in_, 'nval')) ^ lastAns)))
            if (op == 1):
                FollowUp1.add(x)
            else:
                if (op == 2):
                    FollowUp1.remove(x)
                else:
                    if (op == 3):
                        lastAns = jcast('int', FollowUp1.rank(x))
                        ans = jcast('int', jcast('int', (ans ^ lastAns)))
                    else:
                        if (op == 4):
                            lastAns = jcast('int', FollowUp1.index(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', FollowUp1.pre(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', FollowUp1.post(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUp1.MAXN = jcast('int', 2000001)
FollowUp1.head = jcast('int', 0)
FollowUp1.cnt = jcast('int', 0)
FollowUp1.key = jarray('int', [FollowUp1.MAXN])
FollowUp1.father = jarray('int', [FollowUp1.MAXN])
FollowUp1.left = jarray('int', [FollowUp1.MAXN])
FollowUp1.right = jarray('int', [FollowUp1.MAXN])
FollowUp1.size = jarray('int', [FollowUp1.MAXN])

if __name__ == '__main__':
    FollowUp1.main([])

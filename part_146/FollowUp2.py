# -*- coding: utf-8 -*-
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
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp2:
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
        FollowUp2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], FollowUp2.size[FollowUp2.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (FollowUp2.right[FollowUp2.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', FollowUp2.father[i])
        g = jcast('int', FollowUp2.father[f])
        soni = jcast('int', FollowUp2.lr(i))
        sonf = jcast('int', FollowUp2.lr(f))
        if (soni == 1):
            FollowUp2.right[f] = jcast('int', FollowUp2.left[i])
            if (FollowUp2.right[f] != 0):
                jset(FollowUp2.father, FollowUp2.right[f], f)
            FollowUp2.left[i] = jcast('int', f)
        else:
            FollowUp2.left[f] = jcast('int', FollowUp2.right[i])
            if (FollowUp2.left[f] != 0):
                jset(FollowUp2.father, FollowUp2.left[f], f)
            FollowUp2.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                FollowUp2.right[g] = jcast('int', i)
            else:
                FollowUp2.left[g] = jcast('int', i)
        FollowUp2.father[f] = jcast('int', i)
        FollowUp2.father[i] = jcast('int', g)
        FollowUp2.up(f)
        FollowUp2.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', FollowUp2.father[i])
        g = jcast('int', FollowUp2.father[f])
        while (f != goal):
            if (g != goal):
                if (FollowUp2.lr(i) == FollowUp2.lr(f)):
                    FollowUp2.rotate(f)
                else:
                    FollowUp2.rotate(i)
            FollowUp2.rotate(i)
            f = jcast('int', FollowUp2.father[i])
            g = jcast('int', FollowUp2.father[f])
        if (goal == 0):
            FollowUp2.head = jcast('int', i)

    # 整棵树上找到中序排名为rank的节点，返回节点编号
    # 这个方法不是题目要求的查询操作，作为内部方法使用
    # 为什么该方法不进行提根操作？
    # 因为remove方法使用该方法时，要求find不能提根！
    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', FollowUp2.head)
        while (i != 0):
            if (jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (FollowUp2.size[FollowUp2.left[i]] >= rank):
                    i = jcast('int', FollowUp2.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], 1)))))
                    i = jcast('int', FollowUp2.right[i])
        return jcast('int', 0)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        jset(FollowUp2.key, ((_java_obj_1 := FollowUp2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        FollowUp2.size[FollowUp2.cnt] = jcast('int', 1)
        if (FollowUp2.head == 0):
            FollowUp2.head = jcast('int', FollowUp2.cnt)
        else:
            f = jcast('int', 0)
            i = jcast('int', FollowUp2.head)
            son = jcast('int', 0)
            while (i != 0):
                f = jcast('int', i)
                if (FollowUp2.key[i] <= num):
                    son = jcast('int', 1)
                    i = jcast('int', FollowUp2.right[i])
                else:
                    son = jcast('int', 0)
                    i = jcast('int', FollowUp2.left[i])
            if (son == 1):
                FollowUp2.right[f] = jcast('int', FollowUp2.cnt)
            else:
                FollowUp2.left[f] = jcast('int', FollowUp2.cnt)
            FollowUp2.father[FollowUp2.cnt] = jcast('int', f)
            FollowUp2.splay(FollowUp2.cnt, 0)

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp2.head)
        last = jcast('int', FollowUp2.head)
        ans = jcast('int', 0)
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp2.key[i] >= num):
                i = jcast('int', FollowUp2.left[i])
            else:
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], 1)))))
                i = jcast('int', FollowUp2.right[i])
        FollowUp2.splay(last, 0)
        return jcast('int', jcast('int', jadd(ans, 1)))

    @staticmethod
    def index(x):
        x = jcast('int', x)
        i = jcast('int', FollowUp2.find(x))
        FollowUp2.splay(i, 0)
        return jcast('int', FollowUp2.key[i])

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp2.head)
        last = jcast('int', FollowUp2.head)
        ans = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp2.key[i] >= num):
                i = jcast('int', FollowUp2.left[i])
            else:
                ans = jcast('int', jstatic('Math', 'max', ans, FollowUp2.key[i]))
                i = jcast('int', FollowUp2.right[i])
        FollowUp2.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def post(num):
        num = jcast('int', num)
        i = jcast('int', FollowUp2.head)
        last = jcast('int', FollowUp2.head)
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        while (i != 0):
            last = jcast('int', i)
            if (FollowUp2.key[i] <= num):
                i = jcast('int', FollowUp2.right[i])
            else:
                ans = jcast('int', jstatic('Math', 'min', ans, FollowUp2.key[i]))
                i = jcast('int', FollowUp2.left[i])
        FollowUp2.splay(last, 0)
        return jcast('int', ans)

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        kth = jcast('int', FollowUp2.rank(num))
        if (kth != FollowUp2.rank(jcast('int', jadd(num, 1)))):
            i = jcast('int', FollowUp2.find(kth))
            FollowUp2.splay(i, 0)
            if (FollowUp2.left[i] == 0):
                FollowUp2.head = jcast('int', FollowUp2.right[i])
            else:
                if (FollowUp2.right[i] == 0):
                    FollowUp2.head = jcast('int', FollowUp2.left[i])
                else:
                    j = jcast('int', FollowUp2.find(jcast('int', jadd(kth, 1))))
                    FollowUp2.splay(j, i)
                    FollowUp2.left[j] = jcast('int', FollowUp2.left[i])
                    jset(FollowUp2.father, FollowUp2.left[j], j)
                    FollowUp2.up(j)
                    FollowUp2.head = jcast('int', j)
            FollowUp2.father[FollowUp2.head] = jcast('int', 0)

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
            FollowUp2.add(num)
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
                FollowUp2.add(x)
            else:
                if (op == 2):
                    FollowUp2.remove(x)
                else:
                    if (op == 3):
                        lastAns = jcast('int', FollowUp2.rank(x))
                        ans = jcast('int', jcast('int', (ans ^ lastAns)))
                    else:
                        if (op == 4):
                            lastAns = jcast('int', FollowUp2.index(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', FollowUp2.pre(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', FollowUp2.post(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUp2.MAXN = jcast('int', 2000001)
FollowUp2.head = jcast('int', 0)
FollowUp2.cnt = jcast('int', 0)
FollowUp2.key = jarray('int', [FollowUp2.MAXN])
FollowUp2.father = jarray('int', [FollowUp2.MAXN])
FollowUp2.left = jarray('int', [FollowUp2.MAXN])
FollowUp2.right = jarray('int', [FollowUp2.MAXN])
FollowUp2.size = jarray('int', [FollowUp2.MAXN])

if __name__ == '__main__':
    FollowUp2.main([])

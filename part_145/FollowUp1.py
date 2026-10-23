# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# FHQ-Treap实现普通有序表，不用词频压缩，数据加强的测试，Python版
# 这个文件课上没有讲，测试数据加强了，而且有强制在线的要求
# 基本功能要求都是不变的，可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P6136
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority'}
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    left = None
    right = None
    size = None
    priority = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        FollowUp1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], FollowUp1.size[FollowUp1.right[i]])), 1)))

    @staticmethod
    def split(l, r, i, num):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(FollowUp1.right, l, jset(FollowUp1.left, r, 0))
        else:
            if (FollowUp1.key[i] <= num):
                FollowUp1.right[l] = jcast('int', i)
                FollowUp1.split(i, r, FollowUp1.right[i], num)
            else:
                FollowUp1.left[r] = jcast('int', i)
                FollowUp1.split(l, i, FollowUp1.left[i], num)
            FollowUp1.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (FollowUp1.priority[l] >= FollowUp1.priority[r]):
            jset(FollowUp1.right, l, FollowUp1.merge(FollowUp1.right[l], r))
            FollowUp1.up(l)
            return jcast('int', l)
        else:
            jset(FollowUp1.left, r, FollowUp1.merge(l, FollowUp1.left[r]))
            FollowUp1.up(r)
            return jcast('int', r)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        FollowUp1.split(0, 0, FollowUp1.head, num)
        jset(FollowUp1.key, ((_java_obj_1 := FollowUp1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        FollowUp1.size[FollowUp1.cnt] = jcast('int', 1)
        jset(FollowUp1.priority, FollowUp1.cnt, jstatic('Math', 'random'))
        FollowUp1.head = jcast('int', FollowUp1.merge(FollowUp1.merge(FollowUp1.right[0], FollowUp1.cnt), FollowUp1.left[0]))

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        FollowUp1.split(0, 0, FollowUp1.head, num)
        lm = jcast('int', FollowUp1.right[0])
        r = jcast('int', FollowUp1.left[0])
        FollowUp1.split(0, 0, lm, jcast('int', (num - 1)))
        l = jcast('int', FollowUp1.right[0])
        m = jcast('int', FollowUp1.left[0])
        FollowUp1.head = jcast('int', FollowUp1.merge(FollowUp1.merge(l, FollowUp1.merge(FollowUp1.left[m], FollowUp1.right[m])), r))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        FollowUp1.split(0, 0, FollowUp1.head, jcast('int', (num - 1)))
        ans = jcast('int', jcast('int', jadd(FollowUp1.size[FollowUp1.right[0]], 1)))
        FollowUp1.head = jcast('int', FollowUp1.merge(FollowUp1.right[0], FollowUp1.left[0]))
        return jcast('int', ans)

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (FollowUp1.size[FollowUp1.left[i]] >= x):
            return jcast('int', FollowUp1._java_index_0(FollowUp1.left[i], x))
        else:
            if (jcast('int', jadd(FollowUp1.size[FollowUp1.left[i]], 1)) < x):
                return jcast('int', FollowUp1._java_index_0(FollowUp1.right[i], jcast('int', (jcast('int', (x - FollowUp1.size[FollowUp1.left[i]])) - 1))))
            else:
                return jcast('int', FollowUp1.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', FollowUp1._java_index_0(FollowUp1.head, x))

    @staticmethod
    def _java_pre_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (FollowUp1.key[i] >= num):
            return jcast('int', FollowUp1._java_pre_0(FollowUp1.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', FollowUp1.key[i], FollowUp1._java_pre_0(FollowUp1.right[i], num)))

    @staticmethod
    def _java_pre_1(num):
        num = jcast('int', num)
        return jcast('int', FollowUp1._java_pre_0(FollowUp1.head, num))

    @staticmethod
    def _java_post_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (FollowUp1.key[i] <= num):
            return jcast('int', FollowUp1._java_post_0(FollowUp1.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', FollowUp1.key[i], FollowUp1._java_post_0(FollowUp1.left[i], num)))

    @staticmethod
    def _java_post_1(num):
        num = jcast('int', num)
        return jcast('int', FollowUp1._java_post_0(FollowUp1.head, num))

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
                            lastAns = jcast('int', FollowUp1._java_index_1(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', FollowUp1._java_pre_1(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', FollowUp1._java_post_1(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_index_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_index_1(*args)
        raise TypeError("No matching overload for FollowUp1.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_pre_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_pre_1(*args)
        raise TypeError("No matching overload for FollowUp1.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return FollowUp1._java_post_0(*args)
        if _java_choice == 1:
            return FollowUp1._java_post_1(*args)
        raise TypeError("No matching overload for FollowUp1.post")


FollowUp1.MAXN = jcast('int', 2000001)
FollowUp1.head = jcast('int', 0)
FollowUp1.cnt = jcast('int', 0)
FollowUp1.key = jarray('int', [FollowUp1.MAXN])
FollowUp1.left = jarray('int', [FollowUp1.MAXN])
FollowUp1.right = jarray('int', [FollowUp1.MAXN])
FollowUp1.size = jarray('int', [FollowUp1.MAXN])
FollowUp1.priority = jarray('double', [FollowUp1.MAXN])

if __name__ == '__main__':
    FollowUp1.main([])

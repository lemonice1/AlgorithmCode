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
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp2:
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
        FollowUp2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], FollowUp2.size[FollowUp2.right[i]])), 1)))

    @staticmethod
    def split(l, r, i, num):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(FollowUp2.right, l, jset(FollowUp2.left, r, 0))
        else:
            if (FollowUp2.key[i] <= num):
                FollowUp2.right[l] = jcast('int', i)
                FollowUp2.split(i, r, FollowUp2.right[i], num)
            else:
                FollowUp2.left[r] = jcast('int', i)
                FollowUp2.split(l, i, FollowUp2.left[i], num)
            FollowUp2.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (FollowUp2.priority[l] >= FollowUp2.priority[r]):
            jset(FollowUp2.right, l, FollowUp2.merge(FollowUp2.right[l], r))
            FollowUp2.up(l)
            return jcast('int', l)
        else:
            jset(FollowUp2.left, r, FollowUp2.merge(l, FollowUp2.left[r]))
            FollowUp2.up(r)
            return jcast('int', r)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        FollowUp2.split(0, 0, FollowUp2.head, num)
        jset(FollowUp2.key, ((_java_obj_1 := FollowUp2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        FollowUp2.size[FollowUp2.cnt] = jcast('int', 1)
        jset(FollowUp2.priority, FollowUp2.cnt, jstatic('Math', 'random'))
        FollowUp2.head = jcast('int', FollowUp2.merge(FollowUp2.merge(FollowUp2.right[0], FollowUp2.cnt), FollowUp2.left[0]))

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        FollowUp2.split(0, 0, FollowUp2.head, num)
        lm = jcast('int', FollowUp2.right[0])
        r = jcast('int', FollowUp2.left[0])
        FollowUp2.split(0, 0, lm, jcast('int', (num - 1)))
        l = jcast('int', FollowUp2.right[0])
        m = jcast('int', FollowUp2.left[0])
        FollowUp2.head = jcast('int', FollowUp2.merge(FollowUp2.merge(l, FollowUp2.merge(FollowUp2.left[m], FollowUp2.right[m])), r))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        FollowUp2.split(0, 0, FollowUp2.head, jcast('int', (num - 1)))
        ans = jcast('int', jcast('int', jadd(FollowUp2.size[FollowUp2.right[0]], 1)))
        FollowUp2.head = jcast('int', FollowUp2.merge(FollowUp2.right[0], FollowUp2.left[0]))
        return jcast('int', ans)

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (FollowUp2.size[FollowUp2.left[i]] >= x):
            return jcast('int', FollowUp2._java_index_0(FollowUp2.left[i], x))
        else:
            if (jcast('int', jadd(FollowUp2.size[FollowUp2.left[i]], 1)) < x):
                return jcast('int', FollowUp2._java_index_0(FollowUp2.right[i], jcast('int', (jcast('int', (x - FollowUp2.size[FollowUp2.left[i]])) - 1))))
            else:
                return jcast('int', FollowUp2.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', FollowUp2._java_index_0(FollowUp2.head, x))

    @staticmethod
    def _java_pre_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (FollowUp2.key[i] >= num):
            return jcast('int', FollowUp2._java_pre_0(FollowUp2.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', FollowUp2.key[i], FollowUp2._java_pre_0(FollowUp2.right[i], num)))

    @staticmethod
    def _java_pre_1(num):
        num = jcast('int', num)
        return jcast('int', FollowUp2._java_pre_0(FollowUp2.head, num))

    @staticmethod
    def _java_post_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (FollowUp2.key[i] <= num):
            return jcast('int', FollowUp2._java_post_0(FollowUp2.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', FollowUp2.key[i], FollowUp2._java_post_0(FollowUp2.left[i], num)))

    @staticmethod
    def _java_post_1(num):
        num = jcast('int', num)
        return jcast('int', FollowUp2._java_post_0(FollowUp2.head, num))

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
                            lastAns = jcast('int', FollowUp2._java_index_1(x))
                            ans = jcast('int', jcast('int', (ans ^ lastAns)))
                        else:
                            if (op == 5):
                                lastAns = jcast('int', FollowUp2._java_pre_1(x))
                                ans = jcast('int', jcast('int', (ans ^ lastAns)))
                            else:
                                lastAns = jcast('int', FollowUp2._java_post_1(x))
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
            return FollowUp2._java_index_0(*args)
        if _java_choice == 1:
            return FollowUp2._java_index_1(*args)
        raise TypeError("No matching overload for FollowUp2.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return FollowUp2._java_pre_0(*args)
        if _java_choice == 1:
            return FollowUp2._java_pre_1(*args)
        raise TypeError("No matching overload for FollowUp2.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return FollowUp2._java_post_0(*args)
        if _java_choice == 1:
            return FollowUp2._java_post_1(*args)
        raise TypeError("No matching overload for FollowUp2.post")


FollowUp2.MAXN = jcast('int', 2000001)
FollowUp2.head = jcast('int', 0)
FollowUp2.cnt = jcast('int', 0)
FollowUp2.key = jarray('int', [FollowUp2.MAXN])
FollowUp2.left = jarray('int', [FollowUp2.MAXN])
FollowUp2.right = jarray('int', [FollowUp2.MAXN])
FollowUp2.size = jarray('int', [FollowUp2.MAXN])
FollowUp2.priority = jarray('double', [FollowUp2.MAXN])

if __name__ == '__main__':
    FollowUp2.main([])

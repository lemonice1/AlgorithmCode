# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# FHQ-Treap，不用词频压缩，FHQ-Treap最常规的实现，Python版
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
class Code02_FHQTreapWithoutCount1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority'}
    MAXN = 0
    # 整棵树的头节点编号
    head = 0
    # 空间使用计数
    cnt = 0
    # 节点的key值
    key = None
    # 左孩子
    left = None
    # 右孩子
    right = None
    # 节点总数
    size = None
    # 节点优先级
    priority = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_FHQTreapWithoutCount1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.left[i]], Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.right[i]])), 1)))

    @staticmethod
    def split(l, r, i, num):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(Code02_FHQTreapWithoutCount1.right, l, jset(Code02_FHQTreapWithoutCount1.left, r, 0))
        else:
            if (Code02_FHQTreapWithoutCount1.key[i] <= num):
                Code02_FHQTreapWithoutCount1.right[l] = jcast('int', i)
                Code02_FHQTreapWithoutCount1.split(i, r, Code02_FHQTreapWithoutCount1.right[i], num)
            else:
                Code02_FHQTreapWithoutCount1.left[r] = jcast('int', i)
                Code02_FHQTreapWithoutCount1.split(l, i, Code02_FHQTreapWithoutCount1.left[i], num)
            Code02_FHQTreapWithoutCount1.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code02_FHQTreapWithoutCount1.priority[l] >= Code02_FHQTreapWithoutCount1.priority[r]):
            jset(Code02_FHQTreapWithoutCount1.right, l, Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.right[l], r))
            Code02_FHQTreapWithoutCount1.up(l)
            return jcast('int', l)
        else:
            jset(Code02_FHQTreapWithoutCount1.left, r, Code02_FHQTreapWithoutCount1.merge(l, Code02_FHQTreapWithoutCount1.left[r]))
            Code02_FHQTreapWithoutCount1.up(r)
            return jcast('int', r)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        Code02_FHQTreapWithoutCount1.split(0, 0, Code02_FHQTreapWithoutCount1.head, num)
        jset(Code02_FHQTreapWithoutCount1.key, ((_java_obj_1 := Code02_FHQTreapWithoutCount1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.cnt] = jcast('int', 1)
        jset(Code02_FHQTreapWithoutCount1.priority, Code02_FHQTreapWithoutCount1.cnt, jstatic('Math', 'random'))
        Code02_FHQTreapWithoutCount1.head = jcast('int', Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.right[0], Code02_FHQTreapWithoutCount1.cnt), Code02_FHQTreapWithoutCount1.left[0]))

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        Code02_FHQTreapWithoutCount1.split(0, 0, Code02_FHQTreapWithoutCount1.head, num)
        lm = jcast('int', Code02_FHQTreapWithoutCount1.right[0])
        r = jcast('int', Code02_FHQTreapWithoutCount1.left[0])
        Code02_FHQTreapWithoutCount1.split(0, 0, lm, jcast('int', (num - 1)))
        l = jcast('int', Code02_FHQTreapWithoutCount1.right[0])
        m = jcast('int', Code02_FHQTreapWithoutCount1.left[0])
        Code02_FHQTreapWithoutCount1.head = jcast('int', Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.merge(l, Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.left[m], Code02_FHQTreapWithoutCount1.right[m])), r))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        Code02_FHQTreapWithoutCount1.split(0, 0, Code02_FHQTreapWithoutCount1.head, jcast('int', (num - 1)))
        ans = jcast('int', jcast('int', jadd(Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.right[0]], 1)))
        Code02_FHQTreapWithoutCount1.head = jcast('int', Code02_FHQTreapWithoutCount1.merge(Code02_FHQTreapWithoutCount1.right[0], Code02_FHQTreapWithoutCount1.left[0]))
        return jcast('int', ans)

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.left[i]] >= x):
            return jcast('int', Code02_FHQTreapWithoutCount1._java_index_0(Code02_FHQTreapWithoutCount1.left[i], x))
        else:
            if (jcast('int', jadd(Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.left[i]], 1)) < x):
                return jcast('int', Code02_FHQTreapWithoutCount1._java_index_0(Code02_FHQTreapWithoutCount1.right[i], jcast('int', (jcast('int', (x - Code02_FHQTreapWithoutCount1.size[Code02_FHQTreapWithoutCount1.left[i]])) - 1))))
            else:
                return jcast('int', Code02_FHQTreapWithoutCount1.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', Code02_FHQTreapWithoutCount1._java_index_0(Code02_FHQTreapWithoutCount1.head, x))

    @staticmethod
    def _java_pre_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (Code02_FHQTreapWithoutCount1.key[i] >= num):
            return jcast('int', Code02_FHQTreapWithoutCount1._java_pre_0(Code02_FHQTreapWithoutCount1.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', Code02_FHQTreapWithoutCount1.key[i], Code02_FHQTreapWithoutCount1._java_pre_0(Code02_FHQTreapWithoutCount1.right[i], num)))

    @staticmethod
    def _java_pre_1(num):
        num = jcast('int', num)
        return jcast('int', Code02_FHQTreapWithoutCount1._java_pre_0(Code02_FHQTreapWithoutCount1.head, num))

    @staticmethod
    def _java_post_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (Code02_FHQTreapWithoutCount1.key[i] <= num):
            return jcast('int', Code02_FHQTreapWithoutCount1._java_post_0(Code02_FHQTreapWithoutCount1.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', Code02_FHQTreapWithoutCount1.key[i], Code02_FHQTreapWithoutCount1._java_post_0(Code02_FHQTreapWithoutCount1.left[i], num)))

    @staticmethod
    def _java_post_1(num):
        num = jcast('int', num)
        return jcast('int', Code02_FHQTreapWithoutCount1._java_post_0(Code02_FHQTreapWithoutCount1.head, num))

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
                Code02_FHQTreapWithoutCount1.add(x)
            else:
                if (op == 2):
                    Code02_FHQTreapWithoutCount1.remove(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code02_FHQTreapWithoutCount1.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code02_FHQTreapWithoutCount1._java_index_1(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code02_FHQTreapWithoutCount1._java_pre_1(x))
                            else:
                                jcall(out, 'println', Code02_FHQTreapWithoutCount1._java_post_1(x))
            i = jcast('int', (i + 1))
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
            return Code02_FHQTreapWithoutCount1._java_index_0(*args)
        if _java_choice == 1:
            return Code02_FHQTreapWithoutCount1._java_index_1(*args)
        raise TypeError("No matching overload for Code02_FHQTreapWithoutCount1.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_FHQTreapWithoutCount1._java_pre_0(*args)
        if _java_choice == 1:
            return Code02_FHQTreapWithoutCount1._java_pre_1(*args)
        raise TypeError("No matching overload for Code02_FHQTreapWithoutCount1.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_FHQTreapWithoutCount1._java_post_0(*args)
        if _java_choice == 1:
            return Code02_FHQTreapWithoutCount1._java_post_1(*args)
        raise TypeError("No matching overload for Code02_FHQTreapWithoutCount1.post")


Code02_FHQTreapWithoutCount1.MAXN = jcast('int', 100001)
Code02_FHQTreapWithoutCount1.head = jcast('int', 0)
Code02_FHQTreapWithoutCount1.cnt = jcast('int', 0)
Code02_FHQTreapWithoutCount1.key = jarray('int', [Code02_FHQTreapWithoutCount1.MAXN])
Code02_FHQTreapWithoutCount1.left = jarray('int', [Code02_FHQTreapWithoutCount1.MAXN])
Code02_FHQTreapWithoutCount1.right = jarray('int', [Code02_FHQTreapWithoutCount1.MAXN])
Code02_FHQTreapWithoutCount1.size = jarray('int', [Code02_FHQTreapWithoutCount1.MAXN])
Code02_FHQTreapWithoutCount1.priority = jarray('double', [Code02_FHQTreapWithoutCount1.MAXN])

if __name__ == '__main__':
    Code02_FHQTreapWithoutCount1.main([])

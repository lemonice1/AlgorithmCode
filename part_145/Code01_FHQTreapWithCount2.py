# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# FHQ-Treap，使用词频压缩，Python版
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
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_FHQTreapWithCount2:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'count': 'count', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority'}
    MAXN = 0
    # 整棵树的头节点编号
    head = 0
    # 空间使用计数
    cnt = 0
    # 节点的key值
    key = None
    # 节点key的计数
    count = None
    # 左孩子
    left = None
    # 右孩子
    right = None
    # 数字总数
    size = None
    # 节点优先级
    priority = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_FHQTreapWithCount2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.left[i]], Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.right[i]])), Code01_FHQTreapWithCount2.count[i])))

    @staticmethod
    def split(l, r, i, num):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            jset(Code01_FHQTreapWithCount2.right, l, jset(Code01_FHQTreapWithCount2.left, r, 0))
        else:
            if (Code01_FHQTreapWithCount2.key[i] <= num):
                Code01_FHQTreapWithCount2.right[l] = jcast('int', i)
                Code01_FHQTreapWithCount2.split(i, r, Code01_FHQTreapWithCount2.right[i], num)
            else:
                Code01_FHQTreapWithCount2.left[r] = jcast('int', i)
                Code01_FHQTreapWithCount2.split(l, i, Code01_FHQTreapWithCount2.left[i], num)
            Code01_FHQTreapWithCount2.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code01_FHQTreapWithCount2.priority[l] >= Code01_FHQTreapWithCount2.priority[r]):
            jset(Code01_FHQTreapWithCount2.right, l, Code01_FHQTreapWithCount2.merge(Code01_FHQTreapWithCount2.right[l], r))
            Code01_FHQTreapWithCount2.up(l)
            return jcast('int', l)
        else:
            jset(Code01_FHQTreapWithCount2.left, r, Code01_FHQTreapWithCount2.merge(l, Code01_FHQTreapWithCount2.left[r]))
            Code01_FHQTreapWithCount2.up(r)
            return jcast('int', r)

    @staticmethod
    def find(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code01_FHQTreapWithCount2.key[i] == num):
            return jcast('int', i)
        else:
            if (Code01_FHQTreapWithCount2.key[i] > num):
                return jcast('int', Code01_FHQTreapWithCount2.find(Code01_FHQTreapWithCount2.left[i], num))
            else:
                return jcast('int', Code01_FHQTreapWithCount2.find(Code01_FHQTreapWithCount2.right[i], num))

    @staticmethod
    def changeCount(i, num, change):
        i = jcast('int', i)
        num = jcast('int', num)
        change = jcast('int', change)
        if (Code01_FHQTreapWithCount2.key[i] == num):
            Code01_FHQTreapWithCount2.count[i] = jcast('int', jcast('int', jadd(Code01_FHQTreapWithCount2.count[i], change)))
        else:
            if (Code01_FHQTreapWithCount2.key[i] > num):
                Code01_FHQTreapWithCount2.changeCount(Code01_FHQTreapWithCount2.left[i], num, change)
            else:
                Code01_FHQTreapWithCount2.changeCount(Code01_FHQTreapWithCount2.right[i], num, change)
        Code01_FHQTreapWithCount2.up(i)

    @staticmethod
    def add(num):
        num = jcast('int', num)
        if (Code01_FHQTreapWithCount2.find(Code01_FHQTreapWithCount2.head, num) != 0):
            Code01_FHQTreapWithCount2.changeCount(Code01_FHQTreapWithCount2.head, num, 1)
        else:
            Code01_FHQTreapWithCount2.split(0, 0, Code01_FHQTreapWithCount2.head, num)
            jset(Code01_FHQTreapWithCount2.key, ((_java_obj_1 := Code01_FHQTreapWithCount2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            jset(Code01_FHQTreapWithCount2.count, Code01_FHQTreapWithCount2.cnt, jset(Code01_FHQTreapWithCount2.size, Code01_FHQTreapWithCount2.cnt, 1))
            jset(Code01_FHQTreapWithCount2.priority, Code01_FHQTreapWithCount2.cnt, jstatic('Math', 'random'))
            Code01_FHQTreapWithCount2.head = jcast('int', Code01_FHQTreapWithCount2.merge(Code01_FHQTreapWithCount2.merge(Code01_FHQTreapWithCount2.right[0], Code01_FHQTreapWithCount2.cnt), Code01_FHQTreapWithCount2.left[0]))

    @staticmethod
    def remove(num):
        num = jcast('int', num)
        i = jcast('int', Code01_FHQTreapWithCount2.find(Code01_FHQTreapWithCount2.head, num))
        if (i != 0):
            if (Code01_FHQTreapWithCount2.count[i] > 1):
                Code01_FHQTreapWithCount2.changeCount(Code01_FHQTreapWithCount2.head, num, jcast('int', (-1)))
            else:
                Code01_FHQTreapWithCount2.split(0, 0, Code01_FHQTreapWithCount2.head, num)
                lm = jcast('int', Code01_FHQTreapWithCount2.right[0])
                r = jcast('int', Code01_FHQTreapWithCount2.left[0])
                Code01_FHQTreapWithCount2.split(0, 0, lm, jcast('int', (num - 1)))
                l = jcast('int', Code01_FHQTreapWithCount2.right[0])
                Code01_FHQTreapWithCount2.head = jcast('int', Code01_FHQTreapWithCount2.merge(l, r))

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code01_FHQTreapWithCount2.key[i] >= num):
            return jcast('int', Code01_FHQTreapWithCount2.small(Code01_FHQTreapWithCount2.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.left[i]], Code01_FHQTreapWithCount2.count[i])), Code01_FHQTreapWithCount2.small(Code01_FHQTreapWithCount2.right[i], num))))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Code01_FHQTreapWithCount2.small(Code01_FHQTreapWithCount2.head, num), 1)))

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.left[i]] >= x):
            return jcast('int', Code01_FHQTreapWithCount2._java_index_0(Code01_FHQTreapWithCount2.left[i], x))
        else:
            if (jcast('int', jadd(Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.left[i]], Code01_FHQTreapWithCount2.count[i])) < x):
                return jcast('int', Code01_FHQTreapWithCount2._java_index_0(Code01_FHQTreapWithCount2.right[i], jcast('int', (jcast('int', (x - Code01_FHQTreapWithCount2.size[Code01_FHQTreapWithCount2.left[i]])) - Code01_FHQTreapWithCount2.count[i]))))
        return jcast('int', Code01_FHQTreapWithCount2.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', Code01_FHQTreapWithCount2._java_index_0(Code01_FHQTreapWithCount2.head, x))

    @staticmethod
    def _java_pre_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        if (Code01_FHQTreapWithCount2.key[i] >= num):
            return jcast('int', Code01_FHQTreapWithCount2._java_pre_0(Code01_FHQTreapWithCount2.left[i], num))
        else:
            return jcast('int', jstatic('Math', 'max', Code01_FHQTreapWithCount2.key[i], Code01_FHQTreapWithCount2._java_pre_0(Code01_FHQTreapWithCount2.right[i], num)))

    @staticmethod
    def _java_pre_1(num):
        num = jcast('int', num)
        return jcast('int', Code01_FHQTreapWithCount2._java_pre_0(Code01_FHQTreapWithCount2.head, num))

    @staticmethod
    def _java_post_0(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        if (Code01_FHQTreapWithCount2.key[i] <= num):
            return jcast('int', Code01_FHQTreapWithCount2._java_post_0(Code01_FHQTreapWithCount2.right[i], num))
        else:
            return jcast('int', jstatic('Math', 'min', Code01_FHQTreapWithCount2.key[i], Code01_FHQTreapWithCount2._java_post_0(Code01_FHQTreapWithCount2.left[i], num)))

    @staticmethod
    def _java_post_1(num):
        num = jcast('int', num)
        return jcast('int', Code01_FHQTreapWithCount2._java_post_0(Code01_FHQTreapWithCount2.head, num))

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
                Code01_FHQTreapWithCount2.add(x)
            else:
                if (op == 2):
                    Code01_FHQTreapWithCount2.remove(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code01_FHQTreapWithCount2.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code01_FHQTreapWithCount2._java_index_1(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code01_FHQTreapWithCount2._java_pre_1(x))
                            else:
                                jcall(out, 'println', Code01_FHQTreapWithCount2._java_post_1(x))
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
            return Code01_FHQTreapWithCount2._java_index_0(*args)
        if _java_choice == 1:
            return Code01_FHQTreapWithCount2._java_index_1(*args)
        raise TypeError("No matching overload for Code01_FHQTreapWithCount2.index")

    @staticmethod
    def pre(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_FHQTreapWithCount2._java_pre_0(*args)
        if _java_choice == 1:
            return Code01_FHQTreapWithCount2._java_pre_1(*args)
        raise TypeError("No matching overload for Code01_FHQTreapWithCount2.pre")

    @staticmethod
    def post(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_FHQTreapWithCount2._java_post_0(*args)
        if _java_choice == 1:
            return Code01_FHQTreapWithCount2._java_post_1(*args)
        raise TypeError("No matching overload for Code01_FHQTreapWithCount2.post")


Code01_FHQTreapWithCount2.MAXN = jcast('int', 100001)
Code01_FHQTreapWithCount2.head = jcast('int', 0)
Code01_FHQTreapWithCount2.cnt = jcast('int', 0)
Code01_FHQTreapWithCount2.key = jarray('int', [Code01_FHQTreapWithCount2.MAXN])
Code01_FHQTreapWithCount2.count = jarray('int', [Code01_FHQTreapWithCount2.MAXN])
Code01_FHQTreapWithCount2.left = jarray('int', [Code01_FHQTreapWithCount2.MAXN])
Code01_FHQTreapWithCount2.right = jarray('int', [Code01_FHQTreapWithCount2.MAXN])
Code01_FHQTreapWithCount2.size = jarray('int', [Code01_FHQTreapWithCount2.MAXN])
Code01_FHQTreapWithCount2.priority = jarray('double', [Code01_FHQTreapWithCount2.MAXN])

if __name__ == '__main__':
    Code01_FHQTreapWithCount2.main([])

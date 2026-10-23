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

# 平衡因子影响替罪羊树的实验
# 一旦，max(左树节点数，右树节点数) > 平衡因子 * 整树节点数，就会发生重构
# 平衡因子范围是(0.5, 1.0)，否则无意义
# 平衡因子等于0.5时，树高很小，查询效率高，但是重构发生很频繁
# 平衡因子等于1.0时，重构完全不发生，但是树高很大，查询效率低
# 保证查询效率、同时保证重构的节点总数不多，0.7为最常用的平衡因子
# 这保证了查询效率，因为树高几乎是O(log n)
# 同时重构触发的时机合适，单次调整的均摊代价为O(log n)
class Code01_ShowDetails:
    __java_fields__ = {'max': 'max', 'cost': 'cost', 'ALPHA': 'ALPHA', 'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'count': 'count', 'left': 'left', 'right': 'right', 'size': 'size', 'diff': 'diff', 'collect': 'collect', 'ci': 'ci', 'top': 'top', 'father': 'father', 'side': 'side'}
    @staticmethod
    def main(args):
        # 设置平衡因子
        Code01_ShowDetails.ALPHA = jcast('double', 0.7)
        # 设置插入范围
        Code01_ShowDetails.max = jcast('int', 10000)
        jprint('测试开始', newline=True)
        # 清空重构节点计数
        Code01_ShowDetails.cost = jcast('int', 0)
        num = jcast('int', 1)
        while (num <= Code01_ShowDetails.max):
            Code01_ShowDetails._java_add_1(num)
            num = jcast('int', (num + 1))
        jprint(jadd(jadd('插入数字 : ', '1~'), Code01_ShowDetails.max), newline=True)
        jprint(jadd('平衡因子 : ', Code01_ShowDetails.ALPHA), newline=True)
        jprint(jadd('树的高度 : ', Code01_ShowDetails.deep(Code01_ShowDetails.head)), newline=True)
        jprint(jadd('重构节点 : ', Code01_ShowDetails.cost), newline=True)
        jprint('测试结束', newline=True)
        Code01_ShowDetails.clear()

    # 统计树高
    @staticmethod
    def deep(i):
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        return jcast('int', jcast('int', jadd(jstatic('Math', 'max', Code01_ShowDetails.deep(Code01_ShowDetails.left[i]), Code01_ShowDetails.deep(Code01_ShowDetails.right[i])), 1)))

    max = 0
    cost = 0
    ALPHA = 0.0
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    count = None
    left = None
    right = None
    size = None
    diff = None
    collect = None
    ci = 0
    top = 0
    father = 0
    side = 0
    @staticmethod
    def init(num):
        num = jcast('int', num)
        jset(Code01_ShowDetails.key, ((_java_obj_1 := Code01_ShowDetails), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        jset(Code01_ShowDetails.left, Code01_ShowDetails.cnt, jset(Code01_ShowDetails.right, Code01_ShowDetails.cnt, 0))
        jset(Code01_ShowDetails.count, Code01_ShowDetails.cnt, jset(Code01_ShowDetails.size, Code01_ShowDetails.cnt, jset(Code01_ShowDetails.diff, Code01_ShowDetails.cnt, 1)))
        return jcast('int', Code01_ShowDetails.cnt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_ShowDetails.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_ShowDetails.size[Code01_ShowDetails.left[i]], Code01_ShowDetails.size[Code01_ShowDetails.right[i]])), Code01_ShowDetails.count[i])))
        Code01_ShowDetails.diff[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_ShowDetails.diff[Code01_ShowDetails.left[i]], Code01_ShowDetails.diff[Code01_ShowDetails.right[i]])), (1 if (Code01_ShowDetails.count[i] > 0) else 0))))

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if (i != 0):
            Code01_ShowDetails.inorder(Code01_ShowDetails.left[i])
            if (Code01_ShowDetails.count[i] > 0):
                jset(Code01_ShowDetails.collect, ((_java_obj_4 := Code01_ShowDetails), (_java_key_5 := 'ci'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Code01_ShowDetails.inorder(Code01_ShowDetails.right[i])

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        h = jcast('int', Code01_ShowDetails.collect[m])
        jset(Code01_ShowDetails.left, h, Code01_ShowDetails.build(l, jcast('int', (m - 1))))
        jset(Code01_ShowDetails.right, h, Code01_ShowDetails.build(jcast('int', jadd(m, 1)), r))
        Code01_ShowDetails.up(h)
        return jcast('int', h)

    @staticmethod
    def rebuild():
        if (Code01_ShowDetails.top != 0):
            Code01_ShowDetails.ci = jcast('int', 0)
            Code01_ShowDetails.inorder(Code01_ShowDetails.top)
            if (Code01_ShowDetails.ci > 0):
                # 统计重构节点数
                Code01_ShowDetails.cost = jcast('int', jcast('int', jadd(Code01_ShowDetails.cost, Code01_ShowDetails.ci)))
                if (Code01_ShowDetails.father == 0):
                    Code01_ShowDetails.head = jcast('int', Code01_ShowDetails.build(1, Code01_ShowDetails.ci))
                else:
                    if (Code01_ShowDetails.side == 1):
                        jset(Code01_ShowDetails.left, Code01_ShowDetails.father, Code01_ShowDetails.build(1, Code01_ShowDetails.ci))
                    else:
                        jset(Code01_ShowDetails.right, Code01_ShowDetails.father, Code01_ShowDetails.build(1, Code01_ShowDetails.ci))

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code01_ShowDetails.ALPHA * Code01_ShowDetails.diff[i]) >= jstatic('Math', 'max', Code01_ShowDetails.diff[Code01_ShowDetails.left[i]], Code01_ShowDetails.diff[Code01_ShowDetails.right[i]])))

    @staticmethod
    def _java_add_0(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        if (i == 0):
            if (f == 0):
                Code01_ShowDetails.head = jcast('int', Code01_ShowDetails.init(num))
            else:
                if (s == 1):
                    jset(Code01_ShowDetails.left, f, Code01_ShowDetails.init(num))
                else:
                    jset(Code01_ShowDetails.right, f, Code01_ShowDetails.init(num))
        else:
            if (Code01_ShowDetails.key[i] == num):
                Code01_ShowDetails.count[i] = jcast('int', (Code01_ShowDetails.count[i] + 1))
            else:
                if (Code01_ShowDetails.key[i] > num):
                    Code01_ShowDetails._java_add_0(Code01_ShowDetails.left[i], i, 1, num)
                else:
                    Code01_ShowDetails._java_add_0(Code01_ShowDetails.right[i], i, 2, num)
            Code01_ShowDetails.up(i)
            if (not Code01_ShowDetails.balance(i)):
                Code01_ShowDetails.top = jcast('int', i)
                Code01_ShowDetails.father = jcast('int', f)
                Code01_ShowDetails.side = jcast('int', s)

    @staticmethod
    def _java_add_1(num):
        num = jcast('int', num)
        Code01_ShowDetails.top = jcast('int', jset(Code01_ShowDetails, 'father', jset(Code01_ShowDetails, 'side', 0)))
        Code01_ShowDetails._java_add_0(Code01_ShowDetails.head, 0, 0, num)
        Code01_ShowDetails.rebuild()

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code01_ShowDetails.key[i] >= num):
            return jcast('int', Code01_ShowDetails.small(Code01_ShowDetails.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code01_ShowDetails.size[Code01_ShowDetails.left[i]], Code01_ShowDetails.count[i])), Code01_ShowDetails.small(Code01_ShowDetails.right[i], num))))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Code01_ShowDetails.small(Code01_ShowDetails.head, num), 1)))

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code01_ShowDetails.size[Code01_ShowDetails.left[i]] >= x):
            return jcast('int', Code01_ShowDetails._java_index_0(Code01_ShowDetails.left[i], x))
        else:
            if (jcast('int', jadd(Code01_ShowDetails.size[Code01_ShowDetails.left[i]], Code01_ShowDetails.count[i])) < x):
                return jcast('int', Code01_ShowDetails._java_index_0(Code01_ShowDetails.right[i], jcast('int', (jcast('int', (x - Code01_ShowDetails.size[Code01_ShowDetails.left[i]])) - Code01_ShowDetails.count[i]))))
        return jcast('int', Code01_ShowDetails.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', Code01_ShowDetails._java_index_0(Code01_ShowDetails.head, x))

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        kth = jcast('int', Code01_ShowDetails.rank(num))
        if (kth == 1):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        else:
            return jcast('int', Code01_ShowDetails._java_index_1(jcast('int', (kth - 1))))

    @staticmethod
    def post(num):
        num = jcast('int', num)
        kth = jcast('int', Code01_ShowDetails.rank(jcast('int', jadd(num, 1))))
        if (kth == jcast('int', jadd(Code01_ShowDetails.size[Code01_ShowDetails.head], 1))):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        else:
            return jcast('int', Code01_ShowDetails._java_index_1(kth))

    @staticmethod
    def _java_remove_0(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        if (Code01_ShowDetails.key[i] == num):
            Code01_ShowDetails.count[i] = jcast('int', (Code01_ShowDetails.count[i] - 1))
        else:
            if (Code01_ShowDetails.key[i] > num):
                Code01_ShowDetails._java_remove_0(Code01_ShowDetails.left[i], i, 1, num)
            else:
                Code01_ShowDetails._java_remove_0(Code01_ShowDetails.right[i], i, 2, num)
        Code01_ShowDetails.up(i)
        if (not Code01_ShowDetails.balance(i)):
            Code01_ShowDetails.top = jcast('int', i)
            Code01_ShowDetails.father = jcast('int', f)
            Code01_ShowDetails.side = jcast('int', s)

    @staticmethod
    def _java_remove_1(num):
        num = jcast('int', num)
        if (Code01_ShowDetails.rank(num) != Code01_ShowDetails.rank(jcast('int', jadd(num, 1)))):
            Code01_ShowDetails.top = jcast('int', jset(Code01_ShowDetails, 'father', jset(Code01_ShowDetails, 'side', 0)))
            Code01_ShowDetails._java_remove_0(Code01_ShowDetails.head, 0, 0, num)
            Code01_ShowDetails.rebuild()

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code01_ShowDetails.key, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_ShowDetails.count, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_ShowDetails.left, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_ShowDetails.right, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_ShowDetails.size, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_ShowDetails.diff, 1, jcast('int', jadd(Code01_ShowDetails.cnt, 1)), 0)
        Code01_ShowDetails.cnt = jcast('int', 0)
        Code01_ShowDetails.head = jcast('int', 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_ShowDetails._java_add_0(*args)
        if _java_choice == 1:
            return Code01_ShowDetails._java_add_1(*args)
        raise TypeError("No matching overload for Code01_ShowDetails.add")

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_ShowDetails._java_index_0(*args)
        if _java_choice == 1:
            return Code01_ShowDetails._java_index_1(*args)
        raise TypeError("No matching overload for Code01_ShowDetails.index")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_ShowDetails._java_remove_0(*args)
        if _java_choice == 1:
            return Code01_ShowDetails._java_remove_1(*args)
        raise TypeError("No matching overload for Code01_ShowDetails.remove")


Code01_ShowDetails.max = jcast('int', 0)
Code01_ShowDetails.cost = jcast('int', 0)
Code01_ShowDetails.ALPHA = jcast('double', 0.7)
Code01_ShowDetails.MAXN = jcast('int', 100001)
Code01_ShowDetails.head = jcast('int', 0)
Code01_ShowDetails.cnt = jcast('int', 0)
Code01_ShowDetails.key = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.count = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.left = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.right = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.size = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.diff = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.collect = jarray('int', [Code01_ShowDetails.MAXN])
Code01_ShowDetails.ci = jcast('int', 0)
Code01_ShowDetails.top = jcast('int', 0)
Code01_ShowDetails.father = jcast('int', 0)
Code01_ShowDetails.side = jcast('int', 0)

if __name__ == '__main__':
    Code01_ShowDetails.main([])

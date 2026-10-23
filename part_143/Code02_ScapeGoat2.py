# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 替罪羊树的实现(Python版)
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
class Code02_ScapeGoat2:
    __java_fields__ = {'ALPHA': 'ALPHA', 'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'count': 'count', 'left': 'left', 'right': 'right', 'size': 'size', 'diff': 'diff', 'collect': 'collect', 'ci': 'ci', 'top': 'top', 'father': 'father', 'side': 'side'}
    # 平衡因子
    ALPHA = 0.0
    # 空间的最大使用量
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
    # 节点总数
    diff = None
    # 中序收集节点的数组
    collect = None
    # 中序收集节点的计数
    ci = 0
    # 最上方的不平衡节点
    top = 0
    # top的父节点
    father = 0
    # top是父节点的什么孩子，1代表左孩子，2代表右孩子
    side = 0
    @staticmethod
    def init(num):
        num = jcast('int', num)
        jset(Code02_ScapeGoat2.key, ((_java_obj_1 := Code02_ScapeGoat2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        jset(Code02_ScapeGoat2.left, Code02_ScapeGoat2.cnt, jset(Code02_ScapeGoat2.right, Code02_ScapeGoat2.cnt, 0))
        jset(Code02_ScapeGoat2.count, Code02_ScapeGoat2.cnt, jset(Code02_ScapeGoat2.size, Code02_ScapeGoat2.cnt, jset(Code02_ScapeGoat2.diff, Code02_ScapeGoat2.cnt, 1)))
        return jcast('int', Code02_ScapeGoat2.cnt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_ScapeGoat2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_ScapeGoat2.size[Code02_ScapeGoat2.left[i]], Code02_ScapeGoat2.size[Code02_ScapeGoat2.right[i]])), Code02_ScapeGoat2.count[i])))
        Code02_ScapeGoat2.diff[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_ScapeGoat2.diff[Code02_ScapeGoat2.left[i]], Code02_ScapeGoat2.diff[Code02_ScapeGoat2.right[i]])), (1 if (Code02_ScapeGoat2.count[i] > 0) else 0))))

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if (i != 0):
            Code02_ScapeGoat2.inorder(Code02_ScapeGoat2.left[i])
            if (Code02_ScapeGoat2.count[i] > 0):
                jset(Code02_ScapeGoat2.collect, ((_java_obj_4 := Code02_ScapeGoat2), (_java_key_5 := 'ci'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Code02_ScapeGoat2.inorder(Code02_ScapeGoat2.right[i])

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        h = jcast('int', Code02_ScapeGoat2.collect[m])
        jset(Code02_ScapeGoat2.left, h, Code02_ScapeGoat2.build(l, jcast('int', (m - 1))))
        jset(Code02_ScapeGoat2.right, h, Code02_ScapeGoat2.build(jcast('int', jadd(m, 1)), r))
        Code02_ScapeGoat2.up(h)
        return jcast('int', h)

    @staticmethod
    def rebuild():
        if (Code02_ScapeGoat2.top != 0):
            Code02_ScapeGoat2.ci = jcast('int', 0)
            Code02_ScapeGoat2.inorder(Code02_ScapeGoat2.top)
            if (Code02_ScapeGoat2.ci > 0):
                if (Code02_ScapeGoat2.father == 0):
                    Code02_ScapeGoat2.head = jcast('int', Code02_ScapeGoat2.build(1, Code02_ScapeGoat2.ci))
                else:
                    if (Code02_ScapeGoat2.side == 1):
                        jset(Code02_ScapeGoat2.left, Code02_ScapeGoat2.father, Code02_ScapeGoat2.build(1, Code02_ScapeGoat2.ci))
                    else:
                        jset(Code02_ScapeGoat2.right, Code02_ScapeGoat2.father, Code02_ScapeGoat2.build(1, Code02_ScapeGoat2.ci))

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code02_ScapeGoat2.ALPHA * Code02_ScapeGoat2.diff[i]) >= jstatic('Math', 'max', Code02_ScapeGoat2.diff[Code02_ScapeGoat2.left[i]], Code02_ScapeGoat2.diff[Code02_ScapeGoat2.right[i]])))

    @staticmethod
    def _java_add_0(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        if (i == 0):
            if (f == 0):
                Code02_ScapeGoat2.head = jcast('int', Code02_ScapeGoat2.init(num))
            else:
                if (s == 1):
                    jset(Code02_ScapeGoat2.left, f, Code02_ScapeGoat2.init(num))
                else:
                    jset(Code02_ScapeGoat2.right, f, Code02_ScapeGoat2.init(num))
        else:
            if (Code02_ScapeGoat2.key[i] == num):
                Code02_ScapeGoat2.count[i] = jcast('int', (Code02_ScapeGoat2.count[i] + 1))
            else:
                if (Code02_ScapeGoat2.key[i] > num):
                    Code02_ScapeGoat2._java_add_0(Code02_ScapeGoat2.left[i], i, 1, num)
                else:
                    Code02_ScapeGoat2._java_add_0(Code02_ScapeGoat2.right[i], i, 2, num)
            Code02_ScapeGoat2.up(i)
            if (not Code02_ScapeGoat2.balance(i)):
                Code02_ScapeGoat2.top = jcast('int', i)
                Code02_ScapeGoat2.father = jcast('int', f)
                Code02_ScapeGoat2.side = jcast('int', s)

    @staticmethod
    def _java_add_1(num):
        num = jcast('int', num)
        Code02_ScapeGoat2.top = jcast('int', jset(Code02_ScapeGoat2, 'father', jset(Code02_ScapeGoat2, 'side', 0)))
        Code02_ScapeGoat2._java_add_0(Code02_ScapeGoat2.head, 0, 0, num)
        Code02_ScapeGoat2.rebuild()

    @staticmethod
    def small(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if (i == 0):
            return jcast('int', 0)
        if (Code02_ScapeGoat2.key[i] >= num):
            return jcast('int', Code02_ScapeGoat2.small(Code02_ScapeGoat2.left[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_ScapeGoat2.size[Code02_ScapeGoat2.left[i]], Code02_ScapeGoat2.count[i])), Code02_ScapeGoat2.small(Code02_ScapeGoat2.right[i], num))))

    @staticmethod
    def rank(num):
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Code02_ScapeGoat2.small(Code02_ScapeGoat2.head, num), 1)))

    @staticmethod
    def _java_index_0(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (Code02_ScapeGoat2.size[Code02_ScapeGoat2.left[i]] >= x):
            return jcast('int', Code02_ScapeGoat2._java_index_0(Code02_ScapeGoat2.left[i], x))
        else:
            if (jcast('int', jadd(Code02_ScapeGoat2.size[Code02_ScapeGoat2.left[i]], Code02_ScapeGoat2.count[i])) < x):
                return jcast('int', Code02_ScapeGoat2._java_index_0(Code02_ScapeGoat2.right[i], jcast('int', (jcast('int', (x - Code02_ScapeGoat2.size[Code02_ScapeGoat2.left[i]])) - Code02_ScapeGoat2.count[i]))))
        return jcast('int', Code02_ScapeGoat2.key[i])

    @staticmethod
    def _java_index_1(x):
        x = jcast('int', x)
        return jcast('int', Code02_ScapeGoat2._java_index_0(Code02_ScapeGoat2.head, x))

    @staticmethod
    def pre(num):
        num = jcast('int', num)
        kth = jcast('int', Code02_ScapeGoat2.rank(num))
        if (kth == 1):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        else:
            return jcast('int', Code02_ScapeGoat2._java_index_1(jcast('int', (kth - 1))))

    @staticmethod
    def post(num):
        num = jcast('int', num)
        kth = jcast('int', Code02_ScapeGoat2.rank(jcast('int', jadd(num, 1))))
        if (kth == jcast('int', jadd(Code02_ScapeGoat2.size[Code02_ScapeGoat2.head], 1))):
            return jcast('int', jget(Integer, 'MAX_VALUE'))
        else:
            return jcast('int', Code02_ScapeGoat2._java_index_1(kth))

    @staticmethod
    def _java_remove_0(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        if (Code02_ScapeGoat2.key[i] == num):
            Code02_ScapeGoat2.count[i] = jcast('int', (Code02_ScapeGoat2.count[i] - 1))
        else:
            if (Code02_ScapeGoat2.key[i] > num):
                Code02_ScapeGoat2._java_remove_0(Code02_ScapeGoat2.left[i], i, 1, num)
            else:
                Code02_ScapeGoat2._java_remove_0(Code02_ScapeGoat2.right[i], i, 2, num)
        Code02_ScapeGoat2.up(i)
        if (not Code02_ScapeGoat2.balance(i)):
            Code02_ScapeGoat2.top = jcast('int', i)
            Code02_ScapeGoat2.father = jcast('int', f)
            Code02_ScapeGoat2.side = jcast('int', s)

    @staticmethod
    def _java_remove_1(num):
        num = jcast('int', num)
        if (Code02_ScapeGoat2.rank(num) != Code02_ScapeGoat2.rank(jcast('int', jadd(num, 1)))):
            Code02_ScapeGoat2.top = jcast('int', jset(Code02_ScapeGoat2, 'father', jset(Code02_ScapeGoat2, 'side', 0)))
            Code02_ScapeGoat2._java_remove_0(Code02_ScapeGoat2.head, 0, 0, num)
            Code02_ScapeGoat2.rebuild()

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.key, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.count, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.left, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.right, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.size, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ScapeGoat2.diff, 1, jcast('int', jadd(Code02_ScapeGoat2.cnt, 1)), 0)
        Code02_ScapeGoat2.cnt = jcast('int', 0)
        Code02_ScapeGoat2.head = jcast('int', 0)

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
                Code02_ScapeGoat2._java_add_1(x)
            else:
                if (op == 2):
                    Code02_ScapeGoat2._java_remove_1(x)
                else:
                    if (op == 3):
                        jcall(out, 'println', Code02_ScapeGoat2.rank(x))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code02_ScapeGoat2._java_index_1(x))
                        else:
                            if (op == 5):
                                jcall(out, 'println', Code02_ScapeGoat2.pre(x))
                            else:
                                jcall(out, 'println', Code02_ScapeGoat2.post(x))
            i = jcast('int', (i + 1))
        Code02_ScapeGoat2.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_ScapeGoat2._java_add_0(*args)
        if _java_choice == 1:
            return Code02_ScapeGoat2._java_add_1(*args)
        raise TypeError("No matching overload for Code02_ScapeGoat2.add")

    @staticmethod
    def index(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_ScapeGoat2._java_index_0(*args)
        if _java_choice == 1:
            return Code02_ScapeGoat2._java_index_1(*args)
        raise TypeError("No matching overload for Code02_ScapeGoat2.index")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_ScapeGoat2._java_remove_0(*args)
        if _java_choice == 1:
            return Code02_ScapeGoat2._java_remove_1(*args)
        raise TypeError("No matching overload for Code02_ScapeGoat2.remove")


Code02_ScapeGoat2.ALPHA = jcast('double', 0.7)
Code02_ScapeGoat2.MAXN = jcast('int', 100001)
Code02_ScapeGoat2.head = jcast('int', 0)
Code02_ScapeGoat2.cnt = jcast('int', 0)
Code02_ScapeGoat2.key = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.count = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.left = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.right = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.size = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.diff = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.collect = jarray('int', [Code02_ScapeGoat2.MAXN])
Code02_ScapeGoat2.ci = jcast('int', 0)
Code02_ScapeGoat2.top = jcast('int', 0)
Code02_ScapeGoat2.father = jcast('int', 0)
Code02_ScapeGoat2.side = jcast('int', 0)

if __name__ == '__main__':
    Code02_ScapeGoat2.main([])

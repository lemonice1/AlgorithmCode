# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 文艺平衡树，Splay实现范围翻转，Python版本
# 长度为n的序列，下标从1开始，一开始序列为1, 2, ..., n
# 接下来会有k个操作，每个操作给定l，r，表示从l到r范围上的所有数字翻转
# 做完k次操作后，从左到右打印所有数字
# 1 <= n, k <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3391
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_LiteraryTree2:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'num': 'num', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size', 'reverse': 'reverse_data', 'stack': 'stack', 'si': 'si', 'ans': 'ans', 'ai': 'ai'}
    MAXN = 0
    head = 0
    cnt = 0
    num = None
    father = None
    left = None
    right = None
    size = None
    reverse_data = None
    stack = None
    si = 0
    ans = None
    ai = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_LiteraryTree2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code03_LiteraryTree2.size[Code03_LiteraryTree2.left[i]], Code03_LiteraryTree2.size[Code03_LiteraryTree2.right[i]])), 1)))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (Code03_LiteraryTree2.right[Code03_LiteraryTree2.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', Code03_LiteraryTree2.father[i])
        g = jcast('int', Code03_LiteraryTree2.father[f])
        soni = jcast('int', Code03_LiteraryTree2.lr(i))
        sonf = jcast('int', Code03_LiteraryTree2.lr(f))
        if (soni == 1):
            Code03_LiteraryTree2.right[f] = jcast('int', Code03_LiteraryTree2.left[i])
            if (Code03_LiteraryTree2.right[f] != 0):
                jset(Code03_LiteraryTree2.father, Code03_LiteraryTree2.right[f], f)
            Code03_LiteraryTree2.left[i] = jcast('int', f)
        else:
            Code03_LiteraryTree2.left[f] = jcast('int', Code03_LiteraryTree2.right[i])
            if (Code03_LiteraryTree2.left[f] != 0):
                jset(Code03_LiteraryTree2.father, Code03_LiteraryTree2.left[f], f)
            Code03_LiteraryTree2.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                Code03_LiteraryTree2.right[g] = jcast('int', i)
            else:
                Code03_LiteraryTree2.left[g] = jcast('int', i)
        Code03_LiteraryTree2.father[f] = jcast('int', i)
        Code03_LiteraryTree2.father[i] = jcast('int', g)
        Code03_LiteraryTree2.up(f)
        Code03_LiteraryTree2.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', Code03_LiteraryTree2.father[i])
        g = jcast('int', Code03_LiteraryTree2.father[f])
        while (f != goal):
            if (g != goal):
                if (Code03_LiteraryTree2.lr(i) == Code03_LiteraryTree2.lr(f)):
                    Code03_LiteraryTree2.rotate(f)
                else:
                    Code03_LiteraryTree2.rotate(i)
            Code03_LiteraryTree2.rotate(i)
            f = jcast('int', Code03_LiteraryTree2.father[i])
            g = jcast('int', Code03_LiteraryTree2.father[f])
        if (goal == 0):
            Code03_LiteraryTree2.head = jcast('int', i)

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code03_LiteraryTree2.reverse_data[i]:
            jset(Code03_LiteraryTree2.reverse_data, Code03_LiteraryTree2.left[i], (not Code03_LiteraryTree2.reverse_data[Code03_LiteraryTree2.left[i]]))
            jset(Code03_LiteraryTree2.reverse_data, Code03_LiteraryTree2.right[i], (not Code03_LiteraryTree2.reverse_data[Code03_LiteraryTree2.right[i]]))
            tmp = jcast('int', Code03_LiteraryTree2.left[i])
            Code03_LiteraryTree2.left[i] = jcast('int', Code03_LiteraryTree2.right[i])
            Code03_LiteraryTree2.right[i] = jcast('int', tmp)
            Code03_LiteraryTree2.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', Code03_LiteraryTree2.head)
        while (i != 0):
            Code03_LiteraryTree2.down(i)
            if (jcast('int', jadd(Code03_LiteraryTree2.size[Code03_LiteraryTree2.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (Code03_LiteraryTree2.size[Code03_LiteraryTree2.left[i]] >= rank):
                    i = jcast('int', Code03_LiteraryTree2.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(Code03_LiteraryTree2.size[Code03_LiteraryTree2.left[i]], 1)))))
                    i = jcast('int', Code03_LiteraryTree2.right[i])
        return jcast('int', 0)

    @staticmethod
    def add(x):
        x = jcast('int', x)
        jset(Code03_LiteraryTree2.num, ((_java_obj_1 := Code03_LiteraryTree2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], x)
        Code03_LiteraryTree2.size[Code03_LiteraryTree2.cnt] = jcast('int', 1)
        Code03_LiteraryTree2.father[Code03_LiteraryTree2.cnt] = jcast('int', Code03_LiteraryTree2.head)
        Code03_LiteraryTree2.right[Code03_LiteraryTree2.head] = jcast('int', Code03_LiteraryTree2.cnt)
        Code03_LiteraryTree2.splay(Code03_LiteraryTree2.cnt, 0)

    # 注意l永远不会是最左位置，r永远不会是最右位置
    # 因为最左和最右位置提前加入了预备值，永远不会修改
    @staticmethod
    def reverse(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', Code03_LiteraryTree2.find(jcast('int', (l - 1))))
        j = jcast('int', Code03_LiteraryTree2.find(jcast('int', jadd(r, 1))))
        Code03_LiteraryTree2.splay(i, 0)
        Code03_LiteraryTree2.splay(j, i)
        jset(Code03_LiteraryTree2.reverse_data, Code03_LiteraryTree2.left[Code03_LiteraryTree2.right[Code03_LiteraryTree2.head]], (not Code03_LiteraryTree2.reverse_data[Code03_LiteraryTree2.left[Code03_LiteraryTree2.right[Code03_LiteraryTree2.head]]]))

    # 递归方式实现二叉树中序遍历
    # 对本题来说，递归不会爆栈，但其实是有风险的
    @staticmethod
    def _java_inorder_0(i):
        i = jcast('int', i)
        if (i != 0):
            Code03_LiteraryTree2.down(i)
            Code03_LiteraryTree2._java_inorder_0(Code03_LiteraryTree2.left[i])
            jset(Code03_LiteraryTree2.ans, ((_java_obj_4 := Code03_LiteraryTree2), (_java_key_5 := 'ai'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_LiteraryTree2.num[i])
            Code03_LiteraryTree2._java_inorder_0(Code03_LiteraryTree2.right[i])

    # 迭代方式实现二叉树中序遍历，防止递归爆栈
    # 不懂的话，看讲解018，迭代方式实现二叉树中序遍历
    # 遍历时候懒更新任务也要下发
    @staticmethod
    def _java_inorder_1():
        Code03_LiteraryTree2.si = jcast('int', 0)
        i = jcast('int', Code03_LiteraryTree2.head)
        while ((Code03_LiteraryTree2.si != 0) or (i != 0)):
            if (i != 0):
                Code03_LiteraryTree2.down(i)
                jset(Code03_LiteraryTree2.stack, ((_java_obj_7 := Code03_LiteraryTree2), (_java_key_8 := 'si'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], i)
                i = jcast('int', Code03_LiteraryTree2.left[i])
            else:
                i = jcast('int', Code03_LiteraryTree2.stack[((_java_obj_10 := Code03_LiteraryTree2), (_java_key_11 := 'si'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                jset(Code03_LiteraryTree2.ans, ((_java_obj_13 := Code03_LiteraryTree2), (_java_key_14 := 'ai'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code03_LiteraryTree2.num[i])
                i = jcast('int', Code03_LiteraryTree2.right[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code03_LiteraryTree2.add(0)
        i = jcast('int', 1)
        while (i <= n):
            Code03_LiteraryTree2.add(i)
            i = jcast('int', (i + 1))
        Code03_LiteraryTree2.add(0)
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y = jcast('int', jcast('int', jget(in_, 'nval')))
            Code03_LiteraryTree2.reverse(jcast('int', jadd(x, 1)), jcast('int', jadd(y, 1)))
            i = jcast('int', (i + 1))
        Code03_LiteraryTree2.ai = jcast('int', 0)
        # inorder(head);
        Code03_LiteraryTree2._java_inorder_1()
        i = jcast('int', 2)
        while (i < Code03_LiteraryTree2.ai):
            jcall(out, 'print', jadd(Code03_LiteraryTree2.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def inorder(*args):
        _java_choice = jselect(args, [['int'], []], [False, False])
        if _java_choice == 0:
            return Code03_LiteraryTree2._java_inorder_0(*args)
        if _java_choice == 1:
            return Code03_LiteraryTree2._java_inorder_1(*args)
        raise TypeError("No matching overload for Code03_LiteraryTree2.inorder")


Code03_LiteraryTree2.MAXN = jcast('int', 100005)
Code03_LiteraryTree2.head = jcast('int', 0)
Code03_LiteraryTree2.cnt = jcast('int', 0)
Code03_LiteraryTree2.num = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.father = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.left = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.right = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.size = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.reverse_data = jarray('boolean', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.stack = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.si = jcast('int', 0)
Code03_LiteraryTree2.ans = jarray('int', [Code03_LiteraryTree2.MAXN])
Code03_LiteraryTree2.ai = jcast('int', 0)

if __name__ == '__main__':
    Code03_LiteraryTree2.main([])

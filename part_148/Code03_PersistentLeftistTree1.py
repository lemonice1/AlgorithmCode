# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 如下 Python 实现保留对数器验证逻辑，可比较不同方法的计算结果
class Code03_PersistentLeftistTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXT': 'MAXT', 'rt': 'rt', 'num': 'num', 'left': 'left', 'right': 'right', 'dist': 'dist', 'size': 'size', 'cnt': 'cnt', 'verify': 'verify'}
    MAXN = 0
    MAXV = 0
    MAXT = 0
    rt = None
    num = None
    left = None
    right = None
    dist = None
    size = None
    cnt = 0
    @staticmethod
    def init(v):
        v = jcast('int', v)
        jset(Code03_PersistentLeftistTree1.num, ((_java_obj_1 := Code03_PersistentLeftistTree1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], v)
        jset(Code03_PersistentLeftistTree1.left, Code03_PersistentLeftistTree1.cnt, jset(Code03_PersistentLeftistTree1.right, Code03_PersistentLeftistTree1.cnt, jset(Code03_PersistentLeftistTree1.dist, Code03_PersistentLeftistTree1.cnt, 0)))
        return jcast('int', Code03_PersistentLeftistTree1.cnt)

    @staticmethod
    def clone(i):
        i = jcast('int', i)
        jset(Code03_PersistentLeftistTree1.num, ((_java_obj_4 := Code03_PersistentLeftistTree1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code03_PersistentLeftistTree1.num[i])
        Code03_PersistentLeftistTree1.left[Code03_PersistentLeftistTree1.cnt] = jcast('int', Code03_PersistentLeftistTree1.left[i])
        Code03_PersistentLeftistTree1.right[Code03_PersistentLeftistTree1.cnt] = jcast('int', Code03_PersistentLeftistTree1.right[i])
        Code03_PersistentLeftistTree1.dist[Code03_PersistentLeftistTree1.cnt] = jcast('int', Code03_PersistentLeftistTree1.dist[i])
        return jcast('int', Code03_PersistentLeftistTree1.cnt)

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        if (Code03_PersistentLeftistTree1.num[i] > Code03_PersistentLeftistTree1.num[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        h = jcast('int', Code03_PersistentLeftistTree1.clone(i))
        jset(Code03_PersistentLeftistTree1.right, h, Code03_PersistentLeftistTree1.merge(Code03_PersistentLeftistTree1.right[h], j))
        if (Code03_PersistentLeftistTree1.dist[Code03_PersistentLeftistTree1.left[h]] < Code03_PersistentLeftistTree1.dist[Code03_PersistentLeftistTree1.right[h]]):
            tmp = jcast('int', Code03_PersistentLeftistTree1.left[h])
            Code03_PersistentLeftistTree1.left[h] = jcast('int', Code03_PersistentLeftistTree1.right[h])
            Code03_PersistentLeftistTree1.right[h] = jcast('int', tmp)
        Code03_PersistentLeftistTree1.dist[h] = jcast('int', jcast('int', jadd(Code03_PersistentLeftistTree1.dist[Code03_PersistentLeftistTree1.right[h]], 1)))
        return jcast('int', h)

    @staticmethod
    def pop(i):
        i = jcast('int', i)
        if ((Code03_PersistentLeftistTree1.left[i] == 0) and (Code03_PersistentLeftistTree1.right[i] == 0)):
            return jcast('int', 0)
        if ((Code03_PersistentLeftistTree1.left[i] == 0) or (Code03_PersistentLeftistTree1.right[i] == 0)):
            return jcast('int', Code03_PersistentLeftistTree1.clone(jcast('int', jadd(Code03_PersistentLeftistTree1.left[i], Code03_PersistentLeftistTree1.right[i]))))
        return jcast('int', Code03_PersistentLeftistTree1.merge(Code03_PersistentLeftistTree1.left[i], Code03_PersistentLeftistTree1.right[i]))

    # 可持久化左偏树，x版本加入数字y，生成最新的i版本
    @staticmethod
    def treeAdd(x, y, i):
        x = jcast('int', x)
        y = jcast('int', y)
        i = jcast('int', i)
        jset(Code03_PersistentLeftistTree1.rt, i, Code03_PersistentLeftistTree1.merge(Code03_PersistentLeftistTree1.rt[x], Code03_PersistentLeftistTree1.init(y)))
        jset(Code03_PersistentLeftistTree1.size, Code03_PersistentLeftistTree1.rt[i], jcast('int', jadd(Code03_PersistentLeftistTree1.size[Code03_PersistentLeftistTree1.rt[x]], 1)))

    # 可持久化左偏树，x版本与y版本合并，生成最新的i版本
    @staticmethod
    def treeMerge(x, y, i):
        x = jcast('int', x)
        y = jcast('int', y)
        i = jcast('int', i)
        if ((Code03_PersistentLeftistTree1.rt[x] == 0) and (Code03_PersistentLeftistTree1.rt[y] == 0)):
            Code03_PersistentLeftistTree1.rt[i] = jcast('int', 0)
        else:
            if ((Code03_PersistentLeftistTree1.rt[x] == 0) or (Code03_PersistentLeftistTree1.rt[y] == 0)):
                jset(Code03_PersistentLeftistTree1.rt, i, Code03_PersistentLeftistTree1.clone(jcast('int', jadd(Code03_PersistentLeftistTree1.rt[x], Code03_PersistentLeftistTree1.rt[y]))))
            else:
                jset(Code03_PersistentLeftistTree1.rt, i, Code03_PersistentLeftistTree1.merge(Code03_PersistentLeftistTree1.rt[x], Code03_PersistentLeftistTree1.rt[y]))
        jset(Code03_PersistentLeftistTree1.size, Code03_PersistentLeftistTree1.rt[i], jcast('int', jadd(Code03_PersistentLeftistTree1.size[Code03_PersistentLeftistTree1.rt[x]], Code03_PersistentLeftistTree1.size[Code03_PersistentLeftistTree1.rt[y]])))

    # 可持久化左偏树，x版本弹出顶部，生成最新的i版本
    @staticmethod
    def treePop(x, i):
        x = jcast('int', x)
        i = jcast('int', i)
        if (Code03_PersistentLeftistTree1.size[Code03_PersistentLeftistTree1.rt[x]] == 0):
            Code03_PersistentLeftistTree1.rt[i] = jcast('int', 0)
        else:
            jset(Code03_PersistentLeftistTree1.rt, i, Code03_PersistentLeftistTree1.pop(Code03_PersistentLeftistTree1.rt[x]))
            jset(Code03_PersistentLeftistTree1.size, Code03_PersistentLeftistTree1.rt[i], jcast('int', (Code03_PersistentLeftistTree1.size[Code03_PersistentLeftistTree1.rt[x]] - 1)))

    # 验证结构
    verify = None
    # 验证结构，x版本加入数字y，生成最新版本
    @staticmethod
    def verifyAdd(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        pre = jcall(Code03_PersistentLeftistTree1.verify, 'get', x)
        tmp = jnew('ArrayList')
        while (not jcall(pre, 'isEmpty')):
            jcall(tmp, 'add', jcall(pre, 'poll'))
        cur = jnew('PriorityQueue')
        for number in tmp:
            jcall(pre, 'add', number)
            jcall(cur, 'add', number)
        jcall(cur, 'add', y)
        jcall(Code03_PersistentLeftistTree1.verify, 'add', cur)

    # 验证结构，x版本与y版本合并，生成最新版本
    @staticmethod
    def verifyMerge(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        h1 = jcall(Code03_PersistentLeftistTree1.verify, 'get', x)
        h2 = jcall(Code03_PersistentLeftistTree1.verify, 'get', y)
        tmp = jnew('ArrayList')
        cur = jnew('PriorityQueue')
        while (not jcall(h1, 'isEmpty')):
            number = jcast('int', jcall(h1, 'poll'))
            jcall(tmp, 'add', number)
            jcall(cur, 'add', number)
        for number in tmp:
            jcall(h1, 'add', number)
        jcall(tmp, 'clear')
        while (not jcall(h2, 'isEmpty')):
            number = jcast('int', jcall(h2, 'poll'))
            jcall(tmp, 'add', number)
            jcall(cur, 'add', number)
        for number in tmp:
            jcall(h2, 'add', number)
        jcall(Code03_PersistentLeftistTree1.verify, 'add', cur)

    # 验证结构，x版本弹出顶部，生成最新版本
    @staticmethod
    def verifyPop(x):
        x = jcast('int', x)
        pre = jcall(Code03_PersistentLeftistTree1.verify, 'get', x)
        cur = jnew('PriorityQueue')
        if (jcall(pre, 'size') == 0):
            jcall(Code03_PersistentLeftistTree1.verify, 'add', cur)
        else:
            top = jcast('int', jcall(pre, 'poll'))
            tmp = jnew('ArrayList')
            while (not jcall(pre, 'isEmpty')):
                jcall(tmp, 'add', jcall(pre, 'poll'))
            for number in tmp:
                jcall(pre, 'add', number)
                jcall(cur, 'add', number)
            jcall(pre, 'add', top)
            jcall(Code03_PersistentLeftistTree1.verify, 'add', cur)

    # 可持久化左偏树i版本的堆
    # 是否等于
    # 验证结构i版本的堆
    @staticmethod
    def check(i):
        i = jcast('int', i)
        h1 = jcast('int', Code03_PersistentLeftistTree1.rt[i])
        h2 = jcall(Code03_PersistentLeftistTree1.verify, 'get', i)
        if (Code03_PersistentLeftistTree1.size[h1] != jcall(h2, 'size')):
            return jcast('boolean', False)
        ans = jcast('boolean', True)
        tmp = jnew('ArrayList')
        while (not jcall(h2, 'isEmpty')):
            try:
                o1 = jcast('int', Code03_PersistentLeftistTree1.num[h1])
                h1 = jcast('int', Code03_PersistentLeftistTree1.pop(h1))
                o2 = jcast('int', jcall(h2, 'poll'))
                jcall(tmp, 'add', o2)
                if (o1 != o2):
                    ans = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
        for v in tmp:
            jcall(h2, 'add', v)
        return jcast('boolean', ans)

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        Code03_PersistentLeftistTree1.dist[0] = jcast('int', jcast('int', (-1)))
        # 可持久化左偏树生成0版本的堆
        jset(Code03_PersistentLeftistTree1.rt, 0, jset(Code03_PersistentLeftistTree1.size, 0, 0))
        # 验证结构生成0版本的堆
        jcall(Code03_PersistentLeftistTree1.verify, 'add', jnew('PriorityQueue'))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i < Code03_PersistentLeftistTree1.MAXN):
            # op == 1，x版本的堆里加入数字y，形成i号版本的堆
            # op == 2，x版本的堆和y版本的堆合并，形成i号版本的堆
            # op == 3，x版本的堆弹出堆顶，形成i号版本的堆
            op = jcast('int', (1 if (i == 1) else jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * 3)), 1))))
            x = jcast('int', jcast('int', (jstatic('Math', 'random') * i)))
            if (op == 1):
                y = jcast('int', jcast('int', (jstatic('Math', 'random') * Code03_PersistentLeftistTree1.MAXV)))
                Code03_PersistentLeftistTree1.treeAdd(x, y, i)
                Code03_PersistentLeftistTree1.verifyAdd(x, y)
            else:
                if (op == 2):
                    y = jcast('int', x)
                    while True:
                        y = jcast('int', jcast('int', (jstatic('Math', 'random') * i)))
                        if not ((y == x)):
                            break
                    # 保证x != y
                    Code03_PersistentLeftistTree1.treeMerge(x, y, i)
                    Code03_PersistentLeftistTree1.verifyMerge(x, y)
                else:
                    Code03_PersistentLeftistTree1.treePop(x, i)
                    Code03_PersistentLeftistTree1.verifyPop(x)
            # 检查最新版本的堆是否一样
            if (not Code03_PersistentLeftistTree1.check(i)):
                jprint('出错了！', newline=True)
            i = jcast('int', (i + 1))
        # 最后验证是否所有版本的堆都一样
        i = jcast('int', 1)
        while (i < Code03_PersistentLeftistTree1.MAXN):
            if (not Code03_PersistentLeftistTree1.check(i)):
                jprint('出错了！', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PersistentLeftistTree1.MAXN = jcast('int', 10000)
Code03_PersistentLeftistTree1.MAXV = jcast('int', 100000)
Code03_PersistentLeftistTree1.MAXT = jcast('int', 2000001)
Code03_PersistentLeftistTree1.rt = jarray('int', [Code03_PersistentLeftistTree1.MAXN])
Code03_PersistentLeftistTree1.num = jarray('int', [Code03_PersistentLeftistTree1.MAXT])
Code03_PersistentLeftistTree1.left = jarray('int', [Code03_PersistentLeftistTree1.MAXT])
Code03_PersistentLeftistTree1.right = jarray('int', [Code03_PersistentLeftistTree1.MAXT])
Code03_PersistentLeftistTree1.dist = jarray('int', [Code03_PersistentLeftistTree1.MAXT])
Code03_PersistentLeftistTree1.size = jarray('int', [Code03_PersistentLeftistTree1.MAXT])
Code03_PersistentLeftistTree1.cnt = jcast('int', 0)
Code03_PersistentLeftistTree1.verify = jnew('ArrayList')

if __name__ == '__main__':
    Code03_PersistentLeftistTree1.main([])

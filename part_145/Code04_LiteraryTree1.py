# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 文艺平衡树，FHQ-Treap实现范围翻转，Python版本
# 长度为n的序列，下标从1开始，一开始序列为1, 2, ..., n
# 接下来会有k个操作，每个操作给定l，r，表示从l到r范围上的所有数字翻转
# 做完k次操作后，从左到右打印所有数字
# 1 <= n, k <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3391
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LiteraryTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority', 'reverse': 'reverse', 'ans': 'ans', 'ansi': 'ansi'}
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    left = None
    right = None
    size = None
    priority = None
    reverse = None
    ans = None
    ansi = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_LiteraryTree1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code04_LiteraryTree1.size[Code04_LiteraryTree1.left[i]], Code04_LiteraryTree1.size[Code04_LiteraryTree1.right[i]])), 1)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code04_LiteraryTree1.reverse[i]:
            tmp = jcast('int', Code04_LiteraryTree1.left[i])
            Code04_LiteraryTree1.left[i] = jcast('int', Code04_LiteraryTree1.right[i])
            Code04_LiteraryTree1.right[i] = jcast('int', tmp)
            jset(Code04_LiteraryTree1.reverse, Code04_LiteraryTree1.left[i], (not Code04_LiteraryTree1.reverse[Code04_LiteraryTree1.left[i]]))
            jset(Code04_LiteraryTree1.reverse, Code04_LiteraryTree1.right[i], (not Code04_LiteraryTree1.reverse[Code04_LiteraryTree1.right[i]]))
            Code04_LiteraryTree1.reverse[i] = jcast('boolean', False)

    @staticmethod
    def split(l, r, i, rank):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rank = jcast('int', rank)
        if (i == 0):
            jset(Code04_LiteraryTree1.right, l, jset(Code04_LiteraryTree1.left, r, 0))
        else:
            Code04_LiteraryTree1.down(i)
            if (jcast('int', jadd(Code04_LiteraryTree1.size[Code04_LiteraryTree1.left[i]], 1)) <= rank):
                Code04_LiteraryTree1.right[l] = jcast('int', i)
                Code04_LiteraryTree1.split(i, r, Code04_LiteraryTree1.right[i], jcast('int', (jcast('int', (rank - Code04_LiteraryTree1.size[Code04_LiteraryTree1.left[i]])) - 1)))
            else:
                Code04_LiteraryTree1.left[r] = jcast('int', i)
                Code04_LiteraryTree1.split(l, i, Code04_LiteraryTree1.left[i], rank)
            Code04_LiteraryTree1.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code04_LiteraryTree1.priority[l] >= Code04_LiteraryTree1.priority[r]):
            Code04_LiteraryTree1.down(l)
            jset(Code04_LiteraryTree1.right, l, Code04_LiteraryTree1.merge(Code04_LiteraryTree1.right[l], r))
            Code04_LiteraryTree1.up(l)
            return jcast('int', l)
        else:
            Code04_LiteraryTree1.down(r)
            jset(Code04_LiteraryTree1.left, r, Code04_LiteraryTree1.merge(l, Code04_LiteraryTree1.left[r]))
            Code04_LiteraryTree1.up(r)
            return jcast('int', r)

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if (i != 0):
            Code04_LiteraryTree1.down(i)
            Code04_LiteraryTree1.inorder(Code04_LiteraryTree1.left[i])
            jset(Code04_LiteraryTree1.ans, ((_java_obj_1 := Code04_LiteraryTree1), (_java_key_2 := 'ansi'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_LiteraryTree1.key[i])
            Code04_LiteraryTree1.inorder(Code04_LiteraryTree1.right[i])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jset(Code04_LiteraryTree1.key, ((_java_obj_4 := Code04_LiteraryTree1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Code04_LiteraryTree1.size[Code04_LiteraryTree1.cnt] = jcast('int', 1)
            jset(Code04_LiteraryTree1.priority, Code04_LiteraryTree1.cnt, jstatic('Math', 'random'))
            Code04_LiteraryTree1.head = jcast('int', Code04_LiteraryTree1.merge(Code04_LiteraryTree1.head, Code04_LiteraryTree1.cnt))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        x = 0
        y = 0
        l = 0
        m = 0
        lm = 0
        r = 0
        while (i <= k):
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            y = jcast('int', jcast('int', jget(in_, 'nval')))
            Code04_LiteraryTree1.split(0, 0, Code04_LiteraryTree1.head, y)
            lm = jcast('int', Code04_LiteraryTree1.right[0])
            r = jcast('int', Code04_LiteraryTree1.left[0])
            Code04_LiteraryTree1.split(0, 0, lm, jcast('int', (x - 1)))
            l = jcast('int', Code04_LiteraryTree1.right[0])
            m = jcast('int', Code04_LiteraryTree1.left[0])
            Code04_LiteraryTree1.reverse[m] = jcast('boolean', (not Code04_LiteraryTree1.reverse[m]))
            Code04_LiteraryTree1.head = jcast('int', Code04_LiteraryTree1.merge(Code04_LiteraryTree1.merge(l, m), r))
            i = jcast('int', (i + 1))
        Code04_LiteraryTree1.ansi = jcast('int', 0)
        Code04_LiteraryTree1.inorder(Code04_LiteraryTree1.head)
        i = jcast('int', 1)
        while (i <= Code04_LiteraryTree1.ansi):
            jcall(out, 'print', jadd(Code04_LiteraryTree1.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LiteraryTree1.MAXN = jcast('int', 100001)
Code04_LiteraryTree1.head = jcast('int', 0)
Code04_LiteraryTree1.cnt = jcast('int', 0)
Code04_LiteraryTree1.key = jarray('int', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.left = jarray('int', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.right = jarray('int', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.size = jarray('int', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.priority = jarray('double', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.reverse = jarray('boolean', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.ans = jarray('int', [Code04_LiteraryTree1.MAXN])
Code04_LiteraryTree1.ansi = jcast('int', 0)

if __name__ == '__main__':
    Code04_LiteraryTree1.main([])

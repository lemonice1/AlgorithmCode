# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 可持久化文艺平衡树，FHQ-Treap实现，Python版
# 一开始序列为空，实现如下操作，操作一共发生n次
# v 1 x y : 基于v版本的序列，在第x个数后插入y，生成新版本的序列
# v 2 x   : 基于v版本的序列，删除第x个数，生成新版本的序列
# v 3 x y : 基于v版本的序列，范围[x,y]所有数字翻转，生成新版本的序列
# v 4 x y : 基于v版本的序列，查询范围[x,y]所有数字的和，生成新版本的序列状况=v版本状况
# 不管什么操作，都基于某个v版本，操作完成后得到新版本的序列，但v版本不会变化
# 每种操作给定的参数都是有效的，插入数字的范围[-10^6, +10^6]
# 1 <= n <= 2 * 10^5
# 本题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P5055
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_PersistentLiteraryTree2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'cnt': 'cnt', 'head': 'head', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'reverse': 'reverse', 'sum': 'sum', 'priority': 'priority'}
    MAXN = 0
    MAXM = 0
    cnt = 0
    head = None
    key = None
    left = None
    right = None
    size = None
    reverse = None
    sum = None
    priority = None
    @staticmethod
    def copy(i):
        i = jcast('int', i)
        jset(Code06_PersistentLiteraryTree2.key, ((_java_obj_1 := Code06_PersistentLiteraryTree2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_PersistentLiteraryTree2.key[i])
        Code06_PersistentLiteraryTree2.left[Code06_PersistentLiteraryTree2.cnt] = jcast('int', Code06_PersistentLiteraryTree2.left[i])
        Code06_PersistentLiteraryTree2.right[Code06_PersistentLiteraryTree2.cnt] = jcast('int', Code06_PersistentLiteraryTree2.right[i])
        Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.cnt] = jcast('int', Code06_PersistentLiteraryTree2.size[i])
        Code06_PersistentLiteraryTree2.reverse[Code06_PersistentLiteraryTree2.cnt] = jcast('boolean', Code06_PersistentLiteraryTree2.reverse[i])
        Code06_PersistentLiteraryTree2.sum[Code06_PersistentLiteraryTree2.cnt] = jcast('long', Code06_PersistentLiteraryTree2.sum[i])
        Code06_PersistentLiteraryTree2.priority[Code06_PersistentLiteraryTree2.cnt] = jcast('double', Code06_PersistentLiteraryTree2.priority[i])
        return jcast('int', Code06_PersistentLiteraryTree2.cnt)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code06_PersistentLiteraryTree2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.left[i]], Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.right[i]])), 1)))
        Code06_PersistentLiteraryTree2.sum[i] = jcast('long', jcast('long', jadd(jcast('long', jadd(Code06_PersistentLiteraryTree2.sum[Code06_PersistentLiteraryTree2.left[i]], Code06_PersistentLiteraryTree2.sum[Code06_PersistentLiteraryTree2.right[i]])), Code06_PersistentLiteraryTree2.key[i])))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code06_PersistentLiteraryTree2.reverse[i]:
            if (Code06_PersistentLiteraryTree2.left[i] != 0):
                jset(Code06_PersistentLiteraryTree2.left, i, Code06_PersistentLiteraryTree2.copy(Code06_PersistentLiteraryTree2.left[i]))
                jset(Code06_PersistentLiteraryTree2.reverse, Code06_PersistentLiteraryTree2.left[i], (not Code06_PersistentLiteraryTree2.reverse[Code06_PersistentLiteraryTree2.left[i]]))
            if (Code06_PersistentLiteraryTree2.right[i] != 0):
                jset(Code06_PersistentLiteraryTree2.right, i, Code06_PersistentLiteraryTree2.copy(Code06_PersistentLiteraryTree2.right[i]))
                jset(Code06_PersistentLiteraryTree2.reverse, Code06_PersistentLiteraryTree2.right[i], (not Code06_PersistentLiteraryTree2.reverse[Code06_PersistentLiteraryTree2.right[i]]))
            tmp = jcast('int', Code06_PersistentLiteraryTree2.left[i])
            Code06_PersistentLiteraryTree2.left[i] = jcast('int', Code06_PersistentLiteraryTree2.right[i])
            Code06_PersistentLiteraryTree2.right[i] = jcast('int', tmp)
            Code06_PersistentLiteraryTree2.reverse[i] = jcast('boolean', False)

    @staticmethod
    def split(l, r, i, rank):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rank = jcast('int', rank)
        if (i == 0):
            jset(Code06_PersistentLiteraryTree2.right, l, jset(Code06_PersistentLiteraryTree2.left, r, 0))
        else:
            i = jcast('int', Code06_PersistentLiteraryTree2.copy(i))
            Code06_PersistentLiteraryTree2.down(i)
            if (jcast('int', jadd(Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.left[i]], 1)) <= rank):
                Code06_PersistentLiteraryTree2.right[l] = jcast('int', i)
                Code06_PersistentLiteraryTree2.split(i, r, Code06_PersistentLiteraryTree2.right[i], jcast('int', (jcast('int', (rank - Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.left[i]])) - 1)))
            else:
                Code06_PersistentLiteraryTree2.left[r] = jcast('int', i)
                Code06_PersistentLiteraryTree2.split(l, i, Code06_PersistentLiteraryTree2.left[i], rank)
            Code06_PersistentLiteraryTree2.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code06_PersistentLiteraryTree2.priority[l] >= Code06_PersistentLiteraryTree2.priority[r]):
            l = jcast('int', Code06_PersistentLiteraryTree2.copy(l))
            Code06_PersistentLiteraryTree2.down(l)
            jset(Code06_PersistentLiteraryTree2.right, l, Code06_PersistentLiteraryTree2.merge(Code06_PersistentLiteraryTree2.right[l], r))
            Code06_PersistentLiteraryTree2.up(l)
            return jcast('int', l)
        else:
            r = jcast('int', Code06_PersistentLiteraryTree2.copy(r))
            Code06_PersistentLiteraryTree2.down(r)
            jset(Code06_PersistentLiteraryTree2.left, r, Code06_PersistentLiteraryTree2.merge(l, Code06_PersistentLiteraryTree2.left[r]))
            Code06_PersistentLiteraryTree2.up(r)
            return jcast('int', r)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        lastAns = jcast('long', 0)
        i = jcast('int', 1)
        version = 0
        op = 0
        x = jcast('int', 0)
        y = jcast('int', 0)
        l = 0
        m = 0
        lm = 0
        r = 0
        while (i <= n):
            jcall(in_, 'nextToken')
            version = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            # 强制在线的规则
            x = jcast('int', jcast('int', jcast('long', (jcast('long', jget(in_, 'nval')) ^ lastAns))))
            if (op != 2):
                jcall(in_, 'nextToken')
                # 强制在线的规则
                y = jcast('int', jcast('int', jcast('long', (jcast('long', jget(in_, 'nval')) ^ lastAns))))
            if (op == 1):
                Code06_PersistentLiteraryTree2.split(0, 0, Code06_PersistentLiteraryTree2.head[version], x)
                l = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                r = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                # 保证0版本始终是空树
                jset(Code06_PersistentLiteraryTree2.left, 0, jset(Code06_PersistentLiteraryTree2.right, 0, 0))
                jset(Code06_PersistentLiteraryTree2.key, ((_java_obj_4 := Code06_PersistentLiteraryTree2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], jcast('int', y))
                Code06_PersistentLiteraryTree2.size[Code06_PersistentLiteraryTree2.cnt] = jcast('int', 1)
                Code06_PersistentLiteraryTree2.sum[Code06_PersistentLiteraryTree2.cnt] = jcast('long', y)
                jset(Code06_PersistentLiteraryTree2.priority, Code06_PersistentLiteraryTree2.cnt, jstatic('Math', 'random'))
                jset(Code06_PersistentLiteraryTree2.head, i, Code06_PersistentLiteraryTree2.merge(Code06_PersistentLiteraryTree2.merge(l, Code06_PersistentLiteraryTree2.cnt), r))
            else:
                if (op == 2):
                    Code06_PersistentLiteraryTree2.split(0, 0, Code06_PersistentLiteraryTree2.head[version], x)
                    lm = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                    r = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                    Code06_PersistentLiteraryTree2.split(0, 0, lm, jcast('int', (x - 1)))
                    l = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                    m = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                    # 保证0版本始终是空树
                    jset(Code06_PersistentLiteraryTree2.left, 0, jset(Code06_PersistentLiteraryTree2.right, 0, 0))
                    jset(Code06_PersistentLiteraryTree2.head, i, Code06_PersistentLiteraryTree2.merge(l, r))
                else:
                    if (op == 3):
                        Code06_PersistentLiteraryTree2.split(0, 0, Code06_PersistentLiteraryTree2.head[version], y)
                        lm = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                        r = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                        Code06_PersistentLiteraryTree2.split(0, 0, lm, jcast('int', (x - 1)))
                        l = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                        m = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                        # 保证0版本始终是空树
                        jset(Code06_PersistentLiteraryTree2.left, 0, jset(Code06_PersistentLiteraryTree2.right, 0, 0))
                        Code06_PersistentLiteraryTree2.reverse[m] = jcast('boolean', (not Code06_PersistentLiteraryTree2.reverse[m]))
                        jset(Code06_PersistentLiteraryTree2.head, i, Code06_PersistentLiteraryTree2.merge(Code06_PersistentLiteraryTree2.merge(l, m), r))
                    else:
                        Code06_PersistentLiteraryTree2.split(0, 0, Code06_PersistentLiteraryTree2.head[version], y)
                        lm = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                        r = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                        Code06_PersistentLiteraryTree2.split(0, 0, lm, jcast('int', (x - 1)))
                        l = jcast('int', Code06_PersistentLiteraryTree2.right[0])
                        m = jcast('int', Code06_PersistentLiteraryTree2.left[0])
                        # 保证0版本始终是空树
                        jset(Code06_PersistentLiteraryTree2.left, 0, jset(Code06_PersistentLiteraryTree2.right, 0, 0))
                        lastAns = jcast('long', Code06_PersistentLiteraryTree2.sum[m])
                        jcall(out, 'println', lastAns)
                        jset(Code06_PersistentLiteraryTree2.head, i, Code06_PersistentLiteraryTree2.merge(Code06_PersistentLiteraryTree2.merge(l, m), r))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_PersistentLiteraryTree2.MAXN = jcast('int', 200001)
Code06_PersistentLiteraryTree2.MAXM = jcast('int', jcast('int', (Code06_PersistentLiteraryTree2.MAXN * 100)))
Code06_PersistentLiteraryTree2.cnt = jcast('int', 0)
Code06_PersistentLiteraryTree2.head = jarray('int', [Code06_PersistentLiteraryTree2.MAXN])
Code06_PersistentLiteraryTree2.key = jarray('int', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.left = jarray('int', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.right = jarray('int', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.size = jarray('int', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.reverse = jarray('boolean', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.sum = jarray('long', [Code06_PersistentLiteraryTree2.MAXM])
Code06_PersistentLiteraryTree2.priority = jarray('double', [Code06_PersistentLiteraryTree2.MAXM])

if __name__ == '__main__':
    Code06_PersistentLiteraryTree2.main([])

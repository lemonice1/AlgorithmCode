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

# 给你一棵树，Python版
# 一共有n个节点，给定n-1条边，所有节点连成一棵树
# 树的路径是指，从端点x到端点y的简单路径，k路径是指，路径的节点数正好为k
# 整棵树希望分解成尽量多的k路径，k路径的节点不能复用，所有k路径不要求包含所有点
# 打印k = 1, 2, 3..n时，k路径有最多有几条
# 测试链接 : https://www.luogu.com.cn/problem/CF1039D
# 测试链接 : https://codeforces.com/problemset/problem/1039/D
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_GivenTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'blen': 'blen', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'fa': 'fa', 'dfnOrder': 'dfnOrder', 'cntd': 'cntd', 'len': 'len', 'max1': 'max1', 'max2': 'max2', 'ans': 'ans'}
    MAXN = 0
    n = 0
    blen = 0
    head = None
    next = None
    to = None
    cntg = 0
    # fa[i]表示，i节点的父节点编号
    # dfnOrder是根据dfn序，依次收集上来的节点编号
    fa = None
    dfnOrder = None
    cntd = 0
    # len[i]表示，当前i号节点只能往下走，没分配成路径的最长链的长度
    # max1[i]表示，最大值 { len[a], len[b], len[c] ... }，其中a、b、c..是i的子节点
    # max2[i]表示，次大值 { len[a], len[b], len[c] ... }，其中a、b、c..是i的子节点
    len = None
    max1 = None
    max2 = None
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_GivenTree1.next, ((_java_obj_1 := Code07_GivenTree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_GivenTree1.head[u])
        Code07_GivenTree1.to[Code07_GivenTree1.cntg] = jcast('int', v)
        Code07_GivenTree1.head[u] = jcast('int', Code07_GivenTree1.cntg)

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code07_GivenTree1.fa[u] = jcast('int', f)
        jset(Code07_GivenTree1.dfnOrder, ((_java_obj_4 := Code07_GivenTree1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)
        e = jcast('int', Code07_GivenTree1.head[u])
        while (e > 0):
            if (Code07_GivenTree1.to[e] != f):
                Code07_GivenTree1.dfs(Code07_GivenTree1.to[e], u)
            e = jcast('int', Code07_GivenTree1.next[e])

    @staticmethod
    def query(k):
        k = jcast('int', k)
        cnt = jcast('int', 0)
        i = jcast('int', Code07_GivenTree1.n)
        cur = 0
        father = 0
        while (i >= 1):
            cur = jcast('int', Code07_GivenTree1.dfnOrder[i])
            father = jcast('int', Code07_GivenTree1.fa[cur])
            if (jcast('int', jadd(jcast('int', jadd(Code07_GivenTree1.max1[cur], Code07_GivenTree1.max2[cur])), 1)) >= k):
                cnt = jcast('int', (cnt + 1))
                Code07_GivenTree1.len[cur] = jcast('int', 0)
            else:
                Code07_GivenTree1.len[cur] = jcast('int', jcast('int', jadd(Code07_GivenTree1.max1[cur], 1)))
            if (Code07_GivenTree1.len[cur] > Code07_GivenTree1.max1[father]):
                Code07_GivenTree1.max2[father] = jcast('int', Code07_GivenTree1.max1[father])
                Code07_GivenTree1.max1[father] = jcast('int', Code07_GivenTree1.len[cur])
            else:
                if (Code07_GivenTree1.len[cur] > Code07_GivenTree1.max2[father]):
                    Code07_GivenTree1.max2[father] = jcast('int', Code07_GivenTree1.len[cur])
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= Code07_GivenTree1.n):
            jset(Code07_GivenTree1.len, i, jset(Code07_GivenTree1.max1, i, jset(Code07_GivenTree1.max2, i, 0)))
            i = jcast('int', (i + 1))
        return jcast('int', cnt)

    @staticmethod
    def jump(l, r, curAns):
        l = jcast('int', l)
        r = jcast('int', r)
        curAns = jcast('int', curAns)
        find = jcast('int', l)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            check = jcast('int', Code07_GivenTree1.query(mid))
            if (check < curAns):
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                if (check > curAns):
                    l = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    find = jcast('int', mid)
                    l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', jcast('int', jadd(find, 1)))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code07_GivenTree1.blen):
            jset(Code07_GivenTree1.ans, i, Code07_GivenTree1.query(i))
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', jadd(Code07_GivenTree1.blen, 1)))
        while (i <= Code07_GivenTree1.n):
            jset(Code07_GivenTree1.ans, i, Code07_GivenTree1.query(i))
            i = jcast('int', Code07_GivenTree1.jump(i, Code07_GivenTree1.n, Code07_GivenTree1.ans[i]))

    @staticmethod
    def prepare():
        log2n = jcast('int', 0)
        while (jcast('int', (1 << (log2n & 31))) <= jcast('int', (Code07_GivenTree1.n >> (1 & 31)))):
            log2n = jcast('int', (log2n + 1))
        Code07_GivenTree1.blen = jcast('int', jstatic('Math', 'max', 1, jcast('int', jstatic('Math', 'sqrt', jcast('int', (Code07_GivenTree1.n * log2n))))))
        jstatic('Arrays', 'fill', Code07_GivenTree1.ans, 1, jcast('int', jadd(Code07_GivenTree1.n, 1)), jcast('int', (-1)))

    @staticmethod
    def main(args):
        in_ = Code07_GivenTree1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jget(System, 'out'))
        Code07_GivenTree1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_GivenTree1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_GivenTree1.addEdge(u, v)
            Code07_GivenTree1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code07_GivenTree1.dfs(1, 0)
        Code07_GivenTree1.prepare()
        Code07_GivenTree1.compute()
        i = jcast('int', 1)
        while (i <= Code07_GivenTree1.n):
            if (Code07_GivenTree1.ans[i] == jcast('int', (-1))):
                Code07_GivenTree1.ans[i] = jcast('int', Code07_GivenTree1.ans[jcast('int', (i - 1))])
            jcall(out, 'println', Code07_GivenTree1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_GivenTree1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_GivenTree1.MAXN = jcast('int', 200001)
Code07_GivenTree1.n = jcast('int', 0)
Code07_GivenTree1.blen = jcast('int', 0)
Code07_GivenTree1.head = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.next = jarray('int', [jcast('int', (Code07_GivenTree1.MAXN << (1 & 31)))])
Code07_GivenTree1.to = jarray('int', [jcast('int', (Code07_GivenTree1.MAXN << (1 & 31)))])
Code07_GivenTree1.cntg = jcast('int', 0)
Code07_GivenTree1.fa = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.dfnOrder = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.cntd = jcast('int', 0)
Code07_GivenTree1.len = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.max1 = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.max2 = jarray('int', [Code07_GivenTree1.MAXN])
Code07_GivenTree1.ans = jarray('int', [Code07_GivenTree1.MAXN])

if __name__ == '__main__':
    Code07_GivenTree1.main([])

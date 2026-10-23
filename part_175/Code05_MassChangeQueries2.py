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

# 值全改的操作，Python版
# 给定一个长度为n的数组arr，接下来有q条操作，格式如下
# 操作 l r x y : arr[l..r]范围上，所有数字x改成数字y
# 所有操作做完之后，从左到右打印arr中的值
# 1 <= n、q <= 2 * 10^5
# 1 <= arr[i]、x、y <= 100
# 测试链接 : https://www.luogu.com.cn/problem/CF911G
# 测试链接 : https://codeforces.com/problemset/problem/911/G
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MassChangeQueries2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXV': 'MAXV', 'n': 'n', 'q': 'q', 'arr': 'arr', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'status': 'status', 'pool': 'pool', 'top': 'top', 'tree1': 'tree1', 'tree2': 'tree2'}
    MAXN = 0
    MAXT = 0
    MAXV = 0
    n = 0
    q = 0
    arr = None
    root = None
    ls = None
    rs = None
    status = None
    pool = None
    top = 0
    @staticmethod
    def prepare():
        Code05_MassChangeQueries2.top = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code05_MassChangeQueries2.MAXT):
            jset(Code05_MassChangeQueries2.pool, ((_java_obj_1 := Code05_MassChangeQueries2), (_java_key_2 := 'top'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], i)
            i = jcast('int', (i + 1))

    @staticmethod
    def newNode():
        return jcast('int', Code05_MassChangeQueries2.pool[((_java_obj_4 := Code05_MassChangeQueries2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]])

    @staticmethod
    def del_(i):
        i = jcast('int', i)
        jset(Code05_MassChangeQueries2.pool, ((_java_obj_7 := Code05_MassChangeQueries2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], i)
        Code05_MassChangeQueries2.ls[i] = jcast('int', 0)
        Code05_MassChangeQueries2.rs[i] = jcast('int', 0)
        Code05_MassChangeQueries2.status[i] = jcast('boolean', False)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code05_MassChangeQueries2.status[i] = jcast('boolean', (Code05_MassChangeQueries2.status[Code05_MassChangeQueries2.ls[i]] | Code05_MassChangeQueries2.status[Code05_MassChangeQueries2.rs[i]]))

    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', Code05_MassChangeQueries2.newNode())
        if (l == r):
            Code05_MassChangeQueries2.status[rt] = jcast('boolean', True)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code05_MassChangeQueries2.ls, rt, Code05_MassChangeQueries2.insert(jobi, l, mid, Code05_MassChangeQueries2.ls[rt]))
            else:
                jset(Code05_MassChangeQueries2.rs, rt, Code05_MassChangeQueries2.insert(jobi, jcast('int', jadd(mid, 1)), r, Code05_MassChangeQueries2.rs[rt]))
            Code05_MassChangeQueries2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def merge(l, r, t1, t2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        if ((t1 == 0) or (t2 == 0)):
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code05_MassChangeQueries2.status[t1] = jcast('boolean', (Code05_MassChangeQueries2.status[t1] | Code05_MassChangeQueries2.status[t2]))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code05_MassChangeQueries2.ls, t1, Code05_MassChangeQueries2.merge(l, mid, Code05_MassChangeQueries2.ls[t1], Code05_MassChangeQueries2.ls[t2]))
            jset(Code05_MassChangeQueries2.rs, t1, Code05_MassChangeQueries2.merge(jcast('int', jadd(mid, 1)), r, Code05_MassChangeQueries2.rs[t1], Code05_MassChangeQueries2.rs[t2]))
            Code05_MassChangeQueries2.up(t1)
        Code05_MassChangeQueries2.del_(t2)
        return jcast('int', t1)

    tree1 = 0
    tree2 = 0
    @staticmethod
    def split(jobl, jobr, l, r, t1):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        if (t1 == 0):
            Code05_MassChangeQueries2.tree1 = jcast('int', t1)
            Code05_MassChangeQueries2.tree2 = jcast('int', 0)
            return
        if ((jobl <= l) and (r <= jobr)):
            Code05_MassChangeQueries2.tree1 = jcast('int', 0)
            Code05_MassChangeQueries2.tree2 = jcast('int', t1)
            return
        t2 = jcast('int', Code05_MassChangeQueries2.newNode())
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobl <= mid):
            Code05_MassChangeQueries2.split(jobl, jobr, l, mid, Code05_MassChangeQueries2.ls[t1])
            Code05_MassChangeQueries2.ls[t1] = jcast('int', Code05_MassChangeQueries2.tree1)
            Code05_MassChangeQueries2.ls[t2] = jcast('int', Code05_MassChangeQueries2.tree2)
        if (jobr > mid):
            Code05_MassChangeQueries2.split(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code05_MassChangeQueries2.rs[t1])
            Code05_MassChangeQueries2.rs[t1] = jcast('int', Code05_MassChangeQueries2.tree1)
            Code05_MassChangeQueries2.rs[t2] = jcast('int', Code05_MassChangeQueries2.tree2)
        Code05_MassChangeQueries2.up(t1)
        Code05_MassChangeQueries2.up(t2)
        Code05_MassChangeQueries2.tree1 = jcast('int', t1)
        Code05_MassChangeQueries2.tree2 = jcast('int', t2)

    @staticmethod
    def dfs(val, l, r, i):
        val = jcast('int', val)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((i == 0) or (not Code05_MassChangeQueries2.status[i])):
            return
        if (l == r):
            Code05_MassChangeQueries2.arr[l] = jcast('int', val)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_MassChangeQueries2.dfs(val, l, mid, Code05_MassChangeQueries2.ls[i])
            Code05_MassChangeQueries2.dfs(val, jcast('int', jadd(mid, 1)), r, Code05_MassChangeQueries2.rs[i])

    @staticmethod
    def main(args):
        in_ = Code05_MassChangeQueries2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_MassChangeQueries2.prepare()
        Code05_MassChangeQueries2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_MassChangeQueries2.n):
            jset(Code05_MassChangeQueries2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_MassChangeQueries2.n):
            jset(Code05_MassChangeQueries2.root, Code05_MassChangeQueries2.arr[i], Code05_MassChangeQueries2.insert(i, 1, Code05_MassChangeQueries2.n, Code05_MassChangeQueries2.root[Code05_MassChangeQueries2.arr[i]]))
            i = jcast('int', (i + 1))
        Code05_MassChangeQueries2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        l = 0
        r = 0
        x = 0
        y = 0
        while (i <= Code05_MassChangeQueries2.q):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code05_MassChangeQueries2.split(l, r, 1, Code05_MassChangeQueries2.n, Code05_MassChangeQueries2.root[x])
            Code05_MassChangeQueries2.root[x] = jcast('int', Code05_MassChangeQueries2.tree1)
            jset(Code05_MassChangeQueries2.root, y, Code05_MassChangeQueries2.merge(1, Code05_MassChangeQueries2.n, Code05_MassChangeQueries2.root[y], Code05_MassChangeQueries2.tree2))
            i = jcast('int', (i + 1))
        v = jcast('int', 1)
        while (v <= Code05_MassChangeQueries2.MAXV):
            Code05_MassChangeQueries2.dfs(v, 1, Code05_MassChangeQueries2.n, Code05_MassChangeQueries2.root[v])
            v = jcast('int', (v + 1))
        i = jcast('int', 1)
        while (i <= Code05_MassChangeQueries2.n):
            jcall(out, 'print', jadd(Code05_MassChangeQueries2.arr[i], ' '))
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code05_MassChangeQueries2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MassChangeQueries2.MAXN = jcast('int', 200001)
Code05_MassChangeQueries2.MAXT = jcast('int', jcast('int', (Code05_MassChangeQueries2.MAXN * 10)))
Code05_MassChangeQueries2.MAXV = jcast('int', 100)
Code05_MassChangeQueries2.n = jcast('int', 0)
Code05_MassChangeQueries2.q = jcast('int', 0)
Code05_MassChangeQueries2.arr = jarray('int', [Code05_MassChangeQueries2.MAXN])
Code05_MassChangeQueries2.root = jarray('int', [jcast('int', jadd(Code05_MassChangeQueries2.MAXV, 1))])
Code05_MassChangeQueries2.ls = jarray('int', [Code05_MassChangeQueries2.MAXT])
Code05_MassChangeQueries2.rs = jarray('int', [Code05_MassChangeQueries2.MAXT])
Code05_MassChangeQueries2.status = jarray('boolean', [Code05_MassChangeQueries2.MAXT])
Code05_MassChangeQueries2.pool = jarray('int', [Code05_MassChangeQueries2.MAXT])
Code05_MassChangeQueries2.top = jcast('int', 0)
Code05_MassChangeQueries2.tree1 = jcast('int', 0)
Code05_MassChangeQueries2.tree2 = jcast('int', 0)

if __name__ == '__main__':
    Code05_MassChangeQueries2.main([])

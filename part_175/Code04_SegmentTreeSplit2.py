# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 线段树分裂，Python版
# 数字范围1~n，给定每种数字的个数，建立编号为1的可重集合，以后新集合的编号自增即可
# 接下来有m条操作，每条操作是如下五种类型中的一种
# 操作 0 x y z : x号集合中，取出[y, z]范围上的所有数字，生成新的集合
# 操作 1 x y   : x号集合与y号集合合并，以后y编号的集合不会使用了
# 操作 2 x y z : x号集合中，加入y个数字z
# 操作 3 x y z : x号集合中，查询[y, z]范围上的数字个数
# 操作 4 x y   : x号集合中，查询第y小的数字，不存在打印-1
# 1 <= 所有数据 <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5494
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_SegmentTreeSplit2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'version': 'version', 'pool': 'pool', 'top': 'top', 'tree1': 'tree1', 'tree2': 'tree2'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    root = None
    ls = None
    rs = None
    sum = None
    version = 0
    pool = None
    top = 0
    @staticmethod
    def prepare():
        Code04_SegmentTreeSplit2.top = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code04_SegmentTreeSplit2.MAXT):
            jset(Code04_SegmentTreeSplit2.pool, ((_java_obj_1 := Code04_SegmentTreeSplit2), (_java_key_2 := 'top'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], i)
            i = jcast('int', (i + 1))

    @staticmethod
    def newNode():
        return jcast('int', Code04_SegmentTreeSplit2.pool[((_java_obj_4 := Code04_SegmentTreeSplit2), (_java_key_5 := 'top'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]])

    @staticmethod
    def del_(i):
        i = jcast('int', i)
        jset(Code04_SegmentTreeSplit2.pool, ((_java_obj_7 := Code04_SegmentTreeSplit2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], i)
        Code04_SegmentTreeSplit2.ls[i] = jcast('int', 0)
        Code04_SegmentTreeSplit2.rs[i] = jcast('int', 0)
        Code04_SegmentTreeSplit2.sum[i] = jcast('long', 0)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_SegmentTreeSplit2.sum[i] = jcast('long', jcast('long', jadd(Code04_SegmentTreeSplit2.sum[Code04_SegmentTreeSplit2.ls[i]], Code04_SegmentTreeSplit2.sum[Code04_SegmentTreeSplit2.rs[i]])))

    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', Code04_SegmentTreeSplit2.newNode())
        if (l == r):
            Code04_SegmentTreeSplit2.sum[rt] = jcast('long', jcast('long', jadd(Code04_SegmentTreeSplit2.sum[rt], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code04_SegmentTreeSplit2.ls, rt, Code04_SegmentTreeSplit2.add(jobi, jobv, l, mid, Code04_SegmentTreeSplit2.ls[rt]))
            else:
                jset(Code04_SegmentTreeSplit2.rs, rt, Code04_SegmentTreeSplit2.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code04_SegmentTreeSplit2.rs[rt]))
            Code04_SegmentTreeSplit2.up(rt)
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code04_SegmentTreeSplit2.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_SegmentTreeSplit2.query(jobl, jobr, l, mid, Code04_SegmentTreeSplit2.ls[i]))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code04_SegmentTreeSplit2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code04_SegmentTreeSplit2.rs[i]))))
        return jcast('long', ans)

    @staticmethod
    def kth(jobk, l, r, i):
        jobk = jcast('long', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', jcast('int', (-1)))
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (Code04_SegmentTreeSplit2.sum[Code04_SegmentTreeSplit2.ls[i]] >= jobk):
            return jcast('int', Code04_SegmentTreeSplit2.kth(jobk, l, mid, Code04_SegmentTreeSplit2.ls[i]))
        else:
            return jcast('int', Code04_SegmentTreeSplit2.kth(jcast('long', (jobk - Code04_SegmentTreeSplit2.sum[Code04_SegmentTreeSplit2.ls[i]])), jcast('int', jadd(mid, 1)), r, Code04_SegmentTreeSplit2.rs[i]))

    @staticmethod
    def merge(l, r, t1, t2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        if ((t1 == 0) or (t2 == 0)):
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code04_SegmentTreeSplit2.sum[t1] = jcast('long', jcast('long', jadd(Code04_SegmentTreeSplit2.sum[t1], Code04_SegmentTreeSplit2.sum[t2])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code04_SegmentTreeSplit2.ls, t1, Code04_SegmentTreeSplit2.merge(l, mid, Code04_SegmentTreeSplit2.ls[t1], Code04_SegmentTreeSplit2.ls[t2]))
            jset(Code04_SegmentTreeSplit2.rs, t1, Code04_SegmentTreeSplit2.merge(jcast('int', jadd(mid, 1)), r, Code04_SegmentTreeSplit2.rs[t1], Code04_SegmentTreeSplit2.rs[t2]))
            Code04_SegmentTreeSplit2.up(t1)
        Code04_SegmentTreeSplit2.del_(t2)
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
            Code04_SegmentTreeSplit2.tree1 = jcast('int', t1)
            Code04_SegmentTreeSplit2.tree2 = jcast('int', 0)
            return
        if ((jobl <= l) and (r <= jobr)):
            Code04_SegmentTreeSplit2.tree1 = jcast('int', 0)
            Code04_SegmentTreeSplit2.tree2 = jcast('int', t1)
            return
        t2 = jcast('int', Code04_SegmentTreeSplit2.newNode())
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobl <= mid):
            Code04_SegmentTreeSplit2.split(jobl, jobr, l, mid, Code04_SegmentTreeSplit2.ls[t1])
            Code04_SegmentTreeSplit2.ls[t1] = jcast('int', Code04_SegmentTreeSplit2.tree1)
            Code04_SegmentTreeSplit2.ls[t2] = jcast('int', Code04_SegmentTreeSplit2.tree2)
        if (jobr > mid):
            Code04_SegmentTreeSplit2.split(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code04_SegmentTreeSplit2.rs[t1])
            Code04_SegmentTreeSplit2.rs[t1] = jcast('int', Code04_SegmentTreeSplit2.tree1)
            Code04_SegmentTreeSplit2.rs[t2] = jcast('int', Code04_SegmentTreeSplit2.tree2)
        Code04_SegmentTreeSplit2.up(t1)
        Code04_SegmentTreeSplit2.up(t2)
        Code04_SegmentTreeSplit2.tree1 = jcast('int', t1)
        Code04_SegmentTreeSplit2.tree2 = jcast('int', t2)

    @staticmethod
    def main(args):
        in_ = Code04_SegmentTreeSplit2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_SegmentTreeSplit2.prepare()
        Code04_SegmentTreeSplit2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_SegmentTreeSplit2.m = jcast('int', jcall(in_, 'nextInt'))
        Code04_SegmentTreeSplit2.version = jcast('int', 1)
        i = jcast('int', 1)
        x = 0
        while (i <= Code04_SegmentTreeSplit2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            jset(Code04_SegmentTreeSplit2.root, Code04_SegmentTreeSplit2.version, Code04_SegmentTreeSplit2.add(i, x, 1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[1]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code04_SegmentTreeSplit2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                z = jcast('int', jcall(in_, 'nextInt'))
                Code04_SegmentTreeSplit2.split(y, z, 1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[x])
                Code04_SegmentTreeSplit2.root[x] = jcast('int', Code04_SegmentTreeSplit2.tree1)
                jset(Code04_SegmentTreeSplit2.root, ((_java_obj_10 := Code04_SegmentTreeSplit2), (_java_key_11 := 'version'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code04_SegmentTreeSplit2.tree2)
            else:
                if (op == 1):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jset(Code04_SegmentTreeSplit2.root, x, Code04_SegmentTreeSplit2.merge(1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[x], Code04_SegmentTreeSplit2.root[y]))
                else:
                    if (op == 2):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        z = jcast('int', jcall(in_, 'nextInt'))
                        jset(Code04_SegmentTreeSplit2.root, x, Code04_SegmentTreeSplit2.add(z, y, 1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[x]))
                    else:
                        if (op == 3):
                            x = jcast('int', jcall(in_, 'nextInt'))
                            y = jcast('int', jcall(in_, 'nextInt'))
                            z = jcast('int', jcall(in_, 'nextInt'))
                            jcall(out, 'println', Code04_SegmentTreeSplit2.query(y, z, 1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[x]))
                        else:
                            x = jcast('int', jcall(in_, 'nextInt'))
                            y = jcast('int', jcall(in_, 'nextInt'))
                            jcall(out, 'println', Code04_SegmentTreeSplit2.kth(y, 1, Code04_SegmentTreeSplit2.n, Code04_SegmentTreeSplit2.root[x]))
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
            return jcast('int', self.buffer[((_java_obj_13 := self), (_java_key_14 := 'ptr'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]])

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
            raise TypeError("No matching overload for Code04_SegmentTreeSplit2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_SegmentTreeSplit2.MAXN = jcast('int', 200001)
Code04_SegmentTreeSplit2.MAXT = jcast('int', jcast('int', (Code04_SegmentTreeSplit2.MAXN * 10)))
Code04_SegmentTreeSplit2.n = jcast('int', 0)
Code04_SegmentTreeSplit2.m = jcast('int', 0)
Code04_SegmentTreeSplit2.root = jarray('int', [Code04_SegmentTreeSplit2.MAXN])
Code04_SegmentTreeSplit2.ls = jarray('int', [Code04_SegmentTreeSplit2.MAXT])
Code04_SegmentTreeSplit2.rs = jarray('int', [Code04_SegmentTreeSplit2.MAXT])
Code04_SegmentTreeSplit2.sum = jarray('long', [Code04_SegmentTreeSplit2.MAXT])
Code04_SegmentTreeSplit2.version = jcast('int', 0)
Code04_SegmentTreeSplit2.pool = jarray('int', [Code04_SegmentTreeSplit2.MAXT])
Code04_SegmentTreeSplit2.top = jcast('int', 0)
Code04_SegmentTreeSplit2.tree1 = jcast('int', 0)
Code04_SegmentTreeSplit2.tree2 = jcast('int', 0)

if __name__ == '__main__':
    Code04_SegmentTreeSplit2.main([])

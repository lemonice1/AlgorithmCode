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

# 领导集团问题，Python版
# 一共有n个节点，给定每个点的点权，所有节点组成一棵树
# 已知1号节点是整棵树的头，其他节点的父亲节点都会给出
# 如果你在树上选择了u、v两个节点，并且u是v的祖先节点的话
# 那么需要保证 u的点权 <= v的点权，除此之外就没有别的限制了
# 打印你最多能在树上选择几个点
# 1 <= n <= 2 * 10^5
# 1 <= 点权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4577
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LeadersGroup2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'arr': 'arr', 'sorted': 'sorted', 'cntv': 'cntv', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'maxv': 'maxv', 'addLazy': 'addLazy', 'cntt': 'cntt'}
    MAXN = 0
    MAXT = 0
    n = 0
    arr = None
    sorted = None
    cntv = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    root = None
    ls = None
    rs = None
    maxv = None
    addLazy = None
    cntt = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code01_LeadersGroup2.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code01_LeadersGroup2.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_LeadersGroup2.nxt, ((_java_obj_1 := Code01_LeadersGroup2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_LeadersGroup2.head[u])
        Code01_LeadersGroup2.to[Code01_LeadersGroup2.cntg] = jcast('int', v)
        Code01_LeadersGroup2.head[u] = jcast('int', Code01_LeadersGroup2.cntg)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code01_LeadersGroup2.maxv, i, jstatic('Math', 'max', Code01_LeadersGroup2.maxv[Code01_LeadersGroup2.ls[i]], Code01_LeadersGroup2.maxv[Code01_LeadersGroup2.rs[i]]))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (i != 0):
            Code01_LeadersGroup2.maxv[i] = jcast('int', jcast('int', jadd(Code01_LeadersGroup2.maxv[i], v)))
            Code01_LeadersGroup2.addLazy[i] = jcast('int', jcast('int', jadd(Code01_LeadersGroup2.addLazy[i], v)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code01_LeadersGroup2.addLazy[i] > 0):
            Code01_LeadersGroup2.lazy(Code01_LeadersGroup2.ls[i], Code01_LeadersGroup2.addLazy[i])
            Code01_LeadersGroup2.lazy(Code01_LeadersGroup2.rs[i], Code01_LeadersGroup2.addLazy[i])
            Code01_LeadersGroup2.addLazy[i] = jcast('int', 0)

    # jobi来了个新值jobv，如果比之前获得的值更大就更新，否则不更新
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_4 := Code01_LeadersGroup2), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        if (l == r):
            jset(Code01_LeadersGroup2.maxv, rt, jstatic('Math', 'max', Code01_LeadersGroup2.maxv[rt], jobv))
        else:
            Code01_LeadersGroup2.down(rt)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code01_LeadersGroup2.ls, rt, Code01_LeadersGroup2.update(jobi, jobv, l, mid, Code01_LeadersGroup2.ls[rt]))
            else:
                jset(Code01_LeadersGroup2.rs, rt, Code01_LeadersGroup2.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code01_LeadersGroup2.rs[rt]))
            Code01_LeadersGroup2.up(rt)
        return jcast('int', rt)

    # 查询[jobl..jobr]范围上的最大值
    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_LeadersGroup2.maxv[i])
        Code01_LeadersGroup2.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_LeadersGroup2.query(jobl, jobr, l, mid, Code01_LeadersGroup2.ls[i])))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_LeadersGroup2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code01_LeadersGroup2.rs[i])))
        return jcast('int', ans)

    # 线段树合并
    # max1代表dp[u][r+1...]的最大值，max2代表dp[v][r+1...]的最大值
    @staticmethod
    def merge(l, r, t1, t2, max1, max2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        max1 = jcast('int', max1)
        max2 = jcast('int', max2)
        if ((t1 == 0) or (t2 == 0)):
            if (t1 != 0):
                Code01_LeadersGroup2.lazy(t1, max2)
            if (t2 != 0):
                Code01_LeadersGroup2.lazy(t2, max1)
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            ((_java_obj_7 := Code01_LeadersGroup2.maxv), (_java_key_8 := t1), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), jstatic('Math', 'max', Code01_LeadersGroup2.maxv[t2], max2)))))[2]
        else:
            Code01_LeadersGroup2.down(t1)
            Code01_LeadersGroup2.down(t2)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code01_LeadersGroup2.ls, t1, Code01_LeadersGroup2.merge(l, mid, Code01_LeadersGroup2.ls[t1], Code01_LeadersGroup2.ls[t2], jstatic('Math', 'max', max1, Code01_LeadersGroup2.maxv[Code01_LeadersGroup2.rs[t1]]), jstatic('Math', 'max', max2, Code01_LeadersGroup2.maxv[Code01_LeadersGroup2.rs[t2]])))
            jset(Code01_LeadersGroup2.rs, t1, Code01_LeadersGroup2.merge(jcast('int', jadd(mid, 1)), r, Code01_LeadersGroup2.rs[t1], Code01_LeadersGroup2.rs[t2], max1, max2))
            Code01_LeadersGroup2.up(t1)
        return jcast('int', t1)

    @staticmethod
    def dp(u):
        u = jcast('int', u)
        sum = jcast('int', 0)
        e = jcast('int', Code01_LeadersGroup2.head[u])
        while (e > 0):
            v = jcast('int', Code01_LeadersGroup2.to[e])
            Code01_LeadersGroup2.dp(v)
            sum = jcast('int', jcast('int', jadd(sum, Code01_LeadersGroup2.query(Code01_LeadersGroup2.arr[u], Code01_LeadersGroup2.cntv, 1, Code01_LeadersGroup2.cntv, Code01_LeadersGroup2.root[v]))))
            # 不选u的情况，每棵子树合并一遍
            jset(Code01_LeadersGroup2.root, u, Code01_LeadersGroup2.merge(1, Code01_LeadersGroup2.cntv, Code01_LeadersGroup2.root[u], Code01_LeadersGroup2.root[v], 0, 0))
            e = jcast('int', Code01_LeadersGroup2.nxt[e])
        # 选u的情况，最后sum需要加1
        jset(Code01_LeadersGroup2.root, u, Code01_LeadersGroup2.update(Code01_LeadersGroup2.arr[u], jcast('int', jadd(sum, 1)), 1, Code01_LeadersGroup2.cntv, Code01_LeadersGroup2.root[u]))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code01_LeadersGroup2.n):
            jset(Code01_LeadersGroup2.sorted, ((_java_obj_9 := Code01_LeadersGroup2), (_java_key_10 := 'cntv'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], Code01_LeadersGroup2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_LeadersGroup2.sorted, 1, jcast('int', jadd(Code01_LeadersGroup2.cntv, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_LeadersGroup2.cntv):
            if (Code01_LeadersGroup2.sorted[len] != Code01_LeadersGroup2.sorted[i]):
                jset(Code01_LeadersGroup2.sorted, (len := jcast('int', (len + (1)))), Code01_LeadersGroup2.sorted[i])
            i = jcast('int', (i + 1))
        Code01_LeadersGroup2.cntv = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code01_LeadersGroup2.n):
            jset(Code01_LeadersGroup2.arr, i, Code01_LeadersGroup2.kth(Code01_LeadersGroup2.arr[i]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code01_LeadersGroup2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_LeadersGroup2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_LeadersGroup2.n):
            jset(Code01_LeadersGroup2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 2)
        fa = 0
        while (i <= Code01_LeadersGroup2.n):
            fa = jcast('int', jcall(in_, 'nextInt'))
            Code01_LeadersGroup2.addEdge(fa, i)
            i = jcast('int', (i + 1))
        Code01_LeadersGroup2.prepare()
        Code01_LeadersGroup2.dp(1)
        jcall(out, 'println', Code01_LeadersGroup2.query(1, Code01_LeadersGroup2.cntv, 1, Code01_LeadersGroup2.cntv, Code01_LeadersGroup2.root[1]))
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code01_LeadersGroup2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LeadersGroup2.MAXN = jcast('int', 200001)
Code01_LeadersGroup2.MAXT = jcast('int', jcast('int', (Code01_LeadersGroup2.MAXN * 20)))
Code01_LeadersGroup2.n = jcast('int', 0)
Code01_LeadersGroup2.arr = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.sorted = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.cntv = jcast('int', 0)
Code01_LeadersGroup2.head = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.nxt = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.to = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.cntg = jcast('int', 0)
Code01_LeadersGroup2.root = jarray('int', [Code01_LeadersGroup2.MAXN])
Code01_LeadersGroup2.ls = jarray('int', [Code01_LeadersGroup2.MAXT])
Code01_LeadersGroup2.rs = jarray('int', [Code01_LeadersGroup2.MAXT])
Code01_LeadersGroup2.maxv = jarray('int', [Code01_LeadersGroup2.MAXT])
Code01_LeadersGroup2.addLazy = jarray('int', [Code01_LeadersGroup2.MAXT])
Code01_LeadersGroup2.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code01_LeadersGroup2.main([])

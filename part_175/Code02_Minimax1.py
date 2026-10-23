# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 根节点的取值，Python版
# 一共有n个节点，1号节点是整棵树的头，所有节点组成一棵树
# 给定一个长度为n的数组arr，如果节点x是叶，那么arr[x]表示点权，所有叶节点的点权都不同
# 如果节点x不是叶，那么它最多有两个孩子，此时arr[x]代表概率，节点x按照以下规则取得点权
# 以arr[x]的概率是所有儿子的点权最大值，以1 - arr[x]的概率是所有儿子的点权最小值
# 表示概率时，arr[x]的范围是[1, 9999]，表示概率 0.0001 ~ 0.9999
# 假设1号结点的权值有m种可能性，第i小的权值是Vi，取得概率为Di
# 计算 i = 1..m 时，每一项 (i * Vi * Di * Di) 的累加和，答案对 998244353 取模
# 1 <= n <= 3 * 10^5    1 <= 叶节点权值 <= 10^9    1 <= 概率 <= 9999
# 测试链接 : https://www.luogu.com.cn/problem/P5298
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Minimax1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MOD': 'MOD', 'n': 'n', 'fa': 'fa', 'arr': 'arr', 'sorted': 'sorted', 'cntv': 'cntv', 'sonCnt': 'sonCnt', 'son': 'son', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'sum': 'sum', 'mulLazy': 'mulLazy', 'cntt': 'cntt', 'D': 'D'}
    MAXN = 0
    MAXT = 0
    MOD = 0
    n = 0
    fa = None
    arr = None
    sorted = None
    cntv = 0
    sonCnt = None
    son = None
    root = None
    ls = None
    rs = None
    sum = None
    mulLazy = None
    cntt = 0
    D = None
    @staticmethod
    def power(x, p):
        x = jcast('long', x)
        p = jcast('int', p)
        ans = jcast('long', 1)
        while (p != 0):
            if (jcast('int', (p & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * x)), Code02_Minimax1.MOD)))
            p = jcast('int', jcast('int', (p >> (1 & 31))))
            x = jcast('long', jcast('long', jmod(jcast('long', (x * x)), Code02_Minimax1.MOD)))
        return jcast('long', ans)

    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code02_Minimax1.cntv)
        mid = 0
        ret = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', (jcast('int', jadd(left, right)) >> (1 & 31))))
            if (Code02_Minimax1.sorted[mid] <= num):
                ret = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ret)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_Minimax1.sum[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code02_Minimax1.sum[Code02_Minimax1.ls[i]], Code02_Minimax1.sum[Code02_Minimax1.rs[i]])), Code02_Minimax1.MOD)))

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        if (i != 0):
            Code02_Minimax1.sum[i] = jcast('long', jcast('long', jmod(jcast('long', (Code02_Minimax1.sum[i] * v)), Code02_Minimax1.MOD)))
            Code02_Minimax1.mulLazy[i] = jcast('long', jcast('long', jmod(jcast('long', (Code02_Minimax1.mulLazy[i] * v)), Code02_Minimax1.MOD)))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code02_Minimax1.mulLazy[i] != 1):
            Code02_Minimax1.lazy(Code02_Minimax1.ls[i], Code02_Minimax1.mulLazy[i])
            Code02_Minimax1.lazy(Code02_Minimax1.rs[i], Code02_Minimax1.mulLazy[i])
            Code02_Minimax1.mulLazy[i] = jcast('long', 1)

    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', i)
        if (rt == 0):
            rt = jcast('int', ((_java_obj_1 := Code02_Minimax1), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            Code02_Minimax1.mulLazy[rt] = jcast('long', 1)
        if (l == r):
            Code02_Minimax1.sum[rt] = jcast('long', 1)
        else:
            Code02_Minimax1.down(rt)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code02_Minimax1.ls, rt, Code02_Minimax1.insert(jobi, l, mid, Code02_Minimax1.ls[rt]))
            else:
                jset(Code02_Minimax1.rs, rt, Code02_Minimax1.insert(jobi, jcast('int', jadd(mid, 1)), r, Code02_Minimax1.rs[rt]))
            Code02_Minimax1.up(rt)
        return jcast('int', rt)

    @staticmethod
    def merge(l, r, t1, t2, p, sum1, sum2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        p = jcast('int', p)
        sum1 = jcast('long', sum1)
        sum2 = jcast('long', sum2)
        if ((t1 == 0) or (t2 == 0)):
            if (t1 != 0):
                Code02_Minimax1.lazy(t1, sum2)
            if (t2 != 0):
                Code02_Minimax1.lazy(t2, sum1)
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code02_Minimax1.sum[t1] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(jcast('long', (Code02_Minimax1.sum[t1] * sum2)), Code02_Minimax1.MOD)), jcast('long', jmod(jcast('long', (Code02_Minimax1.sum[t2] * sum1)), Code02_Minimax1.MOD)))), Code02_Minimax1.MOD)))
        else:
            Code02_Minimax1.down(t1)
            Code02_Minimax1.down(t2)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            lsum1 = jcast('long', jcast('long', jmod(jcast('long', jadd(sum1, jcast('long', (Code02_Minimax1.sum[Code02_Minimax1.rs[t1]] * jcast('int', jadd(jcast('int', (1 - p)), Code02_Minimax1.MOD)))))), Code02_Minimax1.MOD)))
            lsum2 = jcast('long', jcast('long', jmod(jcast('long', jadd(sum2, jcast('long', (Code02_Minimax1.sum[Code02_Minimax1.rs[t2]] * jcast('int', jadd(jcast('int', (1 - p)), Code02_Minimax1.MOD)))))), Code02_Minimax1.MOD)))
            rsum1 = jcast('long', jcast('long', jmod(jcast('long', jadd(sum1, jcast('long', (Code02_Minimax1.sum[Code02_Minimax1.ls[t1]] * p)))), Code02_Minimax1.MOD)))
            rsum2 = jcast('long', jcast('long', jmod(jcast('long', jadd(sum2, jcast('long', (Code02_Minimax1.sum[Code02_Minimax1.ls[t2]] * p)))), Code02_Minimax1.MOD)))
            jset(Code02_Minimax1.ls, t1, Code02_Minimax1.merge(l, mid, Code02_Minimax1.ls[t1], Code02_Minimax1.ls[t2], p, lsum1, lsum2))
            jset(Code02_Minimax1.rs, t1, Code02_Minimax1.merge(jcast('int', jadd(mid, 1)), r, Code02_Minimax1.rs[t1], Code02_Minimax1.rs[t2], p, rsum1, rsum2))
            Code02_Minimax1.up(t1)
        return jcast('int', t1)

    # 迭代版：使用显式状态保存遍历进度，避免深层递归调用
    @staticmethod
    def dp1(u):
        u = jcast('int', u)
        if (Code02_Minimax1.sonCnt[u] == 0):
            jset(Code02_Minimax1.root, u, Code02_Minimax1.insert(Code02_Minimax1.arr[u], 1, Code02_Minimax1.cntv, Code02_Minimax1.root[u]))
        else:
            if (Code02_Minimax1.sonCnt[u] == 1):
                Code02_Minimax1.dp1(Code02_Minimax1.son[u][0])
                Code02_Minimax1.root[u] = jcast('int', Code02_Minimax1.root[Code02_Minimax1.son[u][0]])
            else:
                Code02_Minimax1.dp1(Code02_Minimax1.son[u][0])
                Code02_Minimax1.dp1(Code02_Minimax1.son[u][1])
                jset(Code02_Minimax1.root, u, Code02_Minimax1.merge(1, Code02_Minimax1.cntv, Code02_Minimax1.root[Code02_Minimax1.son[u][0]], Code02_Minimax1.root[Code02_Minimax1.son[u][1]], Code02_Minimax1.arr[u], 0, 0))

    # dp1改成迭代版
    @staticmethod
    def dp2():
        stack = jarray('int', [jcast('int', jadd(Code02_Minimax1.n, 1)), 2])
        siz = jcast('int', 0)
        jset(stack[(siz := jcast('int', (siz + (1))))], 0, 1)
        jset(stack[siz], 1, 0)
        while (siz > 0):
            u = jcast('int', stack[siz][0])
            s = jcast('int', stack[((_java_old_4 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_4)[2]][1])
            if (Code02_Minimax1.sonCnt[u] == 0):
                jset(Code02_Minimax1.root, u, Code02_Minimax1.insert(Code02_Minimax1.arr[u], 1, Code02_Minimax1.cntv, Code02_Minimax1.root[u]))
            else:
                if (Code02_Minimax1.sonCnt[u] == 1):
                    if (s == 0):
                        jset(stack[(siz := jcast('int', (siz + (1))))], 0, u)
                        jset(stack[siz], 1, 1)
                        jset(stack[(siz := jcast('int', (siz + (1))))], 0, Code02_Minimax1.son[u][0])
                        jset(stack[siz], 1, 0)
                    else:
                        Code02_Minimax1.root[u] = jcast('int', Code02_Minimax1.root[Code02_Minimax1.son[u][0]])
                else:
                    if (s == 0):
                        jset(stack[(siz := jcast('int', (siz + (1))))], 0, u)
                        jset(stack[siz], 1, 1)
                        jset(stack[(siz := jcast('int', (siz + (1))))], 0, Code02_Minimax1.son[u][1])
                        jset(stack[siz], 1, 0)
                        jset(stack[(siz := jcast('int', (siz + (1))))], 0, Code02_Minimax1.son[u][0])
                        jset(stack[siz], 1, 0)
                    else:
                        jset(Code02_Minimax1.root, u, Code02_Minimax1.merge(1, Code02_Minimax1.cntv, Code02_Minimax1.root[Code02_Minimax1.son[u][0]], Code02_Minimax1.root[Code02_Minimax1.son[u][1]], Code02_Minimax1.arr[u], 0, 0))

    @staticmethod
    def getd(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return
        if (l == r):
            Code02_Minimax1.D[l] = jcast('long', jcast('long', jmod(Code02_Minimax1.sum[i], Code02_Minimax1.MOD)))
        else:
            Code02_Minimax1.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_Minimax1.getd(l, mid, Code02_Minimax1.ls[i])
            Code02_Minimax1.getd(jcast('int', jadd(mid, 1)), r, Code02_Minimax1.rs[i])

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.n):
            if (Code02_Minimax1.fa[i] != 0):
                jset(Code02_Minimax1.son[Code02_Minimax1.fa[i]], ((_java_obj_5 := Code02_Minimax1.sonCnt), (_java_key_6 := Code02_Minimax1.fa[i]), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4], i)
            i = jcast('int', (i + 1))
        inv = jcast('long', Code02_Minimax1.power(10000, jcast('int', (Code02_Minimax1.MOD - 2))))
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.n):
            if (Code02_Minimax1.sonCnt[i] == 0):
                jset(Code02_Minimax1.sorted, ((_java_obj_8 := Code02_Minimax1), (_java_key_9 := 'cntv'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3], Code02_Minimax1.arr[i])
            else:
                Code02_Minimax1.arr[i] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (inv * Code02_Minimax1.arr[i])), Code02_Minimax1.MOD))))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_Minimax1.sorted, 1, jcast('int', jadd(Code02_Minimax1.cntv, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_Minimax1.cntv):
            if (Code02_Minimax1.sorted[len] != Code02_Minimax1.sorted[i]):
                jset(Code02_Minimax1.sorted, (len := jcast('int', (len + (1)))), Code02_Minimax1.sorted[i])
            i = jcast('int', (i + 1))
        Code02_Minimax1.cntv = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.n):
            if (Code02_Minimax1.sonCnt[i] == 0):
                jset(Code02_Minimax1.arr, i, Code02_Minimax1.kth(Code02_Minimax1.arr[i]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_Minimax1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Minimax1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.n):
            jset(Code02_Minimax1.fa, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.n):
            jset(Code02_Minimax1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_Minimax1.prepare()
        # dp1(1);
        Code02_Minimax1.dp2()
        Code02_Minimax1.getd(1, Code02_Minimax1.cntv, Code02_Minimax1.root[1])
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code02_Minimax1.cntv):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', jmod(jcast('long', (jcast('long', jmod(jcast('long', (jcast('long', (1 * i)) * Code02_Minimax1.sorted[i])), Code02_Minimax1.MOD)) * Code02_Minimax1.D[i])), Code02_Minimax1.MOD)) * Code02_Minimax1.D[i])))), Code02_Minimax1.MOD)))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code02_Minimax1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Minimax1.MAXN = jcast('int', 300001)
Code02_Minimax1.MAXT = jcast('int', jcast('int', (Code02_Minimax1.MAXN * 40)))
Code02_Minimax1.MOD = jcast('int', 998244353)
Code02_Minimax1.n = jcast('int', 0)
Code02_Minimax1.fa = jarray('int', [Code02_Minimax1.MAXN])
Code02_Minimax1.arr = jarray('int', [Code02_Minimax1.MAXN])
Code02_Minimax1.sorted = jarray('int', [Code02_Minimax1.MAXN])
Code02_Minimax1.cntv = jcast('int', 0)
Code02_Minimax1.sonCnt = jarray('int', [Code02_Minimax1.MAXN])
Code02_Minimax1.son = jarray('int', [Code02_Minimax1.MAXN, 2])
Code02_Minimax1.root = jarray('int', [Code02_Minimax1.MAXN])
Code02_Minimax1.ls = jarray('int', [Code02_Minimax1.MAXT])
Code02_Minimax1.rs = jarray('int', [Code02_Minimax1.MAXT])
Code02_Minimax1.sum = jarray('long', [Code02_Minimax1.MAXT])
Code02_Minimax1.mulLazy = jarray('long', [Code02_Minimax1.MAXT])
Code02_Minimax1.cntt = jcast('int', 0)
Code02_Minimax1.D = jarray('long', [Code02_Minimax1.MAXN])

if __name__ == '__main__':
    Code02_Minimax1.main([])

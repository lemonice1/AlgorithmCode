# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 互质，Python版
# 一共n张卡片，每张卡片给定两个待选数字，选择其中一个数字作为卡片的值
# 确定每张卡片的值之后，如果任意两张卡片的值都是互质的，那么算作成功
# 存在成功的选值方案打印"Yes"，不存在打印"No"
# 1 <= n <= 3 * 10^4
# 1 <= 待选数字 <= 2 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/AT_abc210_f
# 测试链接 : https://atcoder.jp/contests/abc210/tasks/abc210_f
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Coprime1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'MAXM': 'MAXM', 'n': 'n', 'cntt': 'cntt', 'maxv': 'maxv', 'ab': 'ab', 'vis': 'vis', 'prime': 'prime', 'minp': 'minp', 'cntp': 'cntp', 'arr': 'arr', 'cnta': 'cnta', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt'}
    MAXN = 0
    MAXV = 0
    MAXM = 0
    n = 0
    cntt = 0
    maxv = 0
    ab = None
    # 利用欧拉筛生成最小质因子表
    vis = None
    prime = None
    minp = None
    cntp = 0
    # 质因子、拥有这个质因子的数字编号
    # 排序后得到每个质因子的数字编号列表
    arr = None
    cnta = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Coprime1.nxt, ((_java_obj_1 := Code07_Coprime1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Coprime1.head[u])
        Code07_Coprime1.to[Code07_Coprime1.cntg] = jcast('int', v)
        Code07_Coprime1.head[u] = jcast('int', Code07_Coprime1.cntg)

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code07_Coprime1.n)) if (x <= Code07_Coprime1.n) else jcast('int', (x - Code07_Coprime1.n))))

    # 欧拉筛，讲解097
    # 利用欧拉筛的过程，生成最小质因子表
    @staticmethod
    def euler():
        i = jcast('int', 2)
        while (i <= Code07_Coprime1.maxv):
            try:
                if (not Code07_Coprime1.vis[i]):
                    jset(Code07_Coprime1.prime, ((_java_obj_5 := Code07_Coprime1), (_java_key_6 := 'cntp'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], i)
                    Code07_Coprime1.minp[i] = jcast('int', i)
                j = jcast('int', 1)
                p = 0
                v = 0
                while (j <= Code07_Coprime1.cntp):
                    try:
                        p = jcast('int', Code07_Coprime1.prime[j])
                        v = jcast('int', jcast('int', (i * p)))
                        if (v > Code07_Coprime1.maxv):
                            raise JBreak(None)
                        Code07_Coprime1.vis[v] = jcast('boolean', True)
                        Code07_Coprime1.minp[v] = jcast('int', p)
                        if (jcast('int', jmod(i, p)) == 0):
                            raise JBreak(None)
                    except JContinue as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                    except JBreak as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    # 质因子分解
    @staticmethod
    def decompose():
        i = jcast('int', 1)
        while (i <= jcast('int', (Code07_Coprime1.n << (1 & 31)))):
            v = jcast('int', Code07_Coprime1.ab[i])
            p = jcast('int', Code07_Coprime1.minp[v])
            while (v > 1):
                jset(Code07_Coprime1.arr[((_java_obj_9 := Code07_Coprime1), (_java_key_10 := 'cnta'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3]], 0, p)
                jset(Code07_Coprime1.arr[Code07_Coprime1.cnta], 1, i)
                while (jcast('int', jmod(v, p)) == 0):
                    v = jcast('int', jcast('int', jdiv(v, p)))
                p = jcast('int', Code07_Coprime1.minp[v])
            i = jcast('int', (i + 1))

    # 前后缀优化建图
    @staticmethod
    def link():
        jstatic('Arrays', 'sort', Code07_Coprime1.arr, 1, jcast('int', jadd(Code07_Coprime1.cnta, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code07_Coprime1.cnta):
            while ((jcast('int', jadd(r, 1)) <= Code07_Coprime1.cnta) and (Code07_Coprime1.arr[l][0] == Code07_Coprime1.arr[jcast('int', jadd(r, 1))][0])):
                r = jcast('int', (r + 1))
            Code07_Coprime1.cntt = jcast('int', (Code07_Coprime1.cntt + 1))
            Code07_Coprime1.addEdge(Code07_Coprime1.cntt, Code07_Coprime1.other(Code07_Coprime1.arr[l][1]))
            i = jcast('int', jcast('int', jadd(l, 1)))
            while (i <= r):
                Code07_Coprime1.cntt = jcast('int', (Code07_Coprime1.cntt + 1))
                Code07_Coprime1.addEdge(Code07_Coprime1.cntt, Code07_Coprime1.other(Code07_Coprime1.arr[i][1]))
                Code07_Coprime1.addEdge(Code07_Coprime1.arr[i][1], jcast('int', (Code07_Coprime1.cntt - 1)))
                Code07_Coprime1.addEdge(Code07_Coprime1.cntt, jcast('int', (Code07_Coprime1.cntt - 1)))
                i = jcast('int', (i + 1))
            Code07_Coprime1.cntt = jcast('int', (Code07_Coprime1.cntt + 1))
            Code07_Coprime1.addEdge(Code07_Coprime1.cntt, Code07_Coprime1.other(Code07_Coprime1.arr[r][1]))
            i = jcast('int', jcast('int', (r - 1)))
            while (i >= l):
                Code07_Coprime1.cntt = jcast('int', (Code07_Coprime1.cntt + 1))
                Code07_Coprime1.addEdge(Code07_Coprime1.cntt, Code07_Coprime1.other(Code07_Coprime1.arr[i][1]))
                Code07_Coprime1.addEdge(Code07_Coprime1.arr[i][1], jcast('int', (Code07_Coprime1.cntt - 1)))
                Code07_Coprime1.addEdge(Code07_Coprime1.cntt, jcast('int', (Code07_Coprime1.cntt - 1)))
                i = jcast('int', (i - 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code07_Coprime1.dfn, u, jset(Code07_Coprime1.low, u, ((_java_obj_12 := Code07_Coprime1), (_java_key_13 := 'cntd'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3]))
        jset(Code07_Coprime1.sta, ((_java_obj_15 := Code07_Coprime1), (_java_key_16 := 'top'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3], u)
        e = jcast('int', Code07_Coprime1.head[u])
        while (e > 0):
            v = jcast('int', Code07_Coprime1.to[e])
            if (Code07_Coprime1.dfn[v] == 0):
                Code07_Coprime1.tarjan(v)
                jset(Code07_Coprime1.low, u, jstatic('Math', 'min', Code07_Coprime1.low[u], Code07_Coprime1.low[v]))
            else:
                if (Code07_Coprime1.belong[v] == 0):
                    jset(Code07_Coprime1.low, u, jstatic('Math', 'min', Code07_Coprime1.low[u], Code07_Coprime1.dfn[v]))
            e = jcast('int', Code07_Coprime1.nxt[e])
        if (Code07_Coprime1.dfn[u] == Code07_Coprime1.low[u]):
            Code07_Coprime1.sccCnt = jcast('int', (Code07_Coprime1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code07_Coprime1.sta[((_java_obj_18 := Code07_Coprime1), (_java_key_19 := 'top'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (-1)))), _java_old_20)[4]])
                Code07_Coprime1.belong[pop] = jcast('int', Code07_Coprime1.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code07_Coprime1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Coprime1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Coprime1.cntt = jcast('int', jcast('int', (Code07_Coprime1.n << (1 & 31))))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code07_Coprime1.n):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            Code07_Coprime1.ab[i] = jcast('int', a)
            Code07_Coprime1.ab[jcast('int', jadd(i, Code07_Coprime1.n))] = jcast('int', b)
            Code07_Coprime1.maxv = jcast('int', jstatic('Math', 'max', Code07_Coprime1.maxv, jstatic('Math', 'max', a, b)))
            i = jcast('int', (i + 1))
        Code07_Coprime1.euler()
        Code07_Coprime1.decompose()
        Code07_Coprime1.link()
        i = jcast('int', 1)
        while (i <= Code07_Coprime1.cntt):
            if (Code07_Coprime1.dfn[i] == 0):
                Code07_Coprime1.tarjan(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code07_Coprime1.n):
            try:
                if (Code07_Coprime1.belong[i] == Code07_Coprime1.belong[jcast('int', jadd(i, Code07_Coprime1.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_21:
                if _java_control_21.label not in (None,):
                    raise
            except JBreak as _java_control_21:
                if _java_control_21.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jcall(out, 'println', ('Yes' if check else 'No'))
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code07_Coprime1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Coprime1.MAXN = jcast('int', 1000001)
Code07_Coprime1.MAXV = jcast('int', 2000001)
Code07_Coprime1.MAXM = jcast('int', 3000001)
Code07_Coprime1.n = jcast('int', 0)
Code07_Coprime1.cntt = jcast('int', 0)
Code07_Coprime1.maxv = jcast('int', 0)
Code07_Coprime1.ab = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.vis = jarray('boolean', [Code07_Coprime1.MAXV])
Code07_Coprime1.prime = jarray('int', [Code07_Coprime1.MAXV])
Code07_Coprime1.minp = jarray('int', [Code07_Coprime1.MAXV])
Code07_Coprime1.cntp = jcast('int', 0)
Code07_Coprime1.arr = jarray('int', [Code07_Coprime1.MAXN, 2])
Code07_Coprime1.cnta = jcast('int', 0)
Code07_Coprime1.head = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.nxt = jarray('int', [Code07_Coprime1.MAXM])
Code07_Coprime1.to = jarray('int', [Code07_Coprime1.MAXM])
Code07_Coprime1.cntg = jcast('int', 0)
Code07_Coprime1.dfn = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.low = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.cntd = jcast('int', 0)
Code07_Coprime1.sta = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.top = jcast('int', 0)
Code07_Coprime1.belong = jarray('int', [Code07_Coprime1.MAXN])
Code07_Coprime1.sccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code07_Coprime1.main([])

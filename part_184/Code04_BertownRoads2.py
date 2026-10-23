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

# 贝尔敦道路，Python版
# 给定一张无向图，一共n个点、m条边，保证所有点连通
# 每条无向边需要指定一个方向，变成有向边，还要保证任意两点互相可达
# 如果不存在方案打印0，如果存在方案，打印m条有向边
# 可以任意次序打印有向边，如果方案不只一种，打印其中一种即可
# 1 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF118E
# 测试链接 : https://codeforces.com/problemset/problem/118/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_BertownRoads2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'check': 'check', 'ans1': 'ans1', 'ans2': 'ans2', 'cnta': 'cnta'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    check = False
    ans1 = None
    ans2 = None
    cnta = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_BertownRoads2.nxt, ((_java_obj_1 := Code04_BertownRoads2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_BertownRoads2.head[u])
        Code04_BertownRoads2.to[Code04_BertownRoads2.cntg] = jcast('int', v)
        Code04_BertownRoads2.head[u] = jcast('int', Code04_BertownRoads2.cntg)

    @staticmethod
    def tarjan(u, preEdge):
        u = jcast('int', u)
        preEdge = jcast('int', preEdge)
        jset(Code04_BertownRoads2.dfn, u, jset(Code04_BertownRoads2.low, u, ((_java_obj_4 := Code04_BertownRoads2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        e = jcast('int', Code04_BertownRoads2.head[u])
        while (e > 0):
            try:
                if (jcast('int', (e ^ 1)) == preEdge):
                    raise JContinue(None)
                v = jcast('int', Code04_BertownRoads2.to[e])
                # 树边和回边需要处理，弃边不要处理
                if ((Code04_BertownRoads2.dfn[v] == 0) or (Code04_BertownRoads2.dfn[v] < Code04_BertownRoads2.dfn[u])):
                    Code04_BertownRoads2.cnta = jcast('int', (Code04_BertownRoads2.cnta + 1))
                    Code04_BertownRoads2.ans1[Code04_BertownRoads2.cnta] = jcast('int', u)
                    Code04_BertownRoads2.ans2[Code04_BertownRoads2.cnta] = jcast('int', v)
                if (Code04_BertownRoads2.dfn[v] == 0):
                    Code04_BertownRoads2.tarjan(v, e)
                    jset(Code04_BertownRoads2.low, u, jstatic('Math', 'min', Code04_BertownRoads2.low[u], Code04_BertownRoads2.low[v]))
                    if (Code04_BertownRoads2.low[v] > Code04_BertownRoads2.dfn[u]):
                        Code04_BertownRoads2.check = jcast('boolean', False)
                else:
                    jset(Code04_BertownRoads2.low, u, jstatic('Math', 'min', Code04_BertownRoads2.low[u], Code04_BertownRoads2.dfn[v]))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
            e = jcast('int', Code04_BertownRoads2.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code04_BertownRoads2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_BertownRoads2.cntg = jcast('int', 1)
        Code04_BertownRoads2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_BertownRoads2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code04_BertownRoads2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_BertownRoads2.addEdge(u, v)
            Code04_BertownRoads2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code04_BertownRoads2.check = jcast('boolean', True)
        Code04_BertownRoads2.tarjan(1, 0)
        if (not Code04_BertownRoads2.check):
            jcall(out, 'println', 0)
        else:
            i = jcast('int', 1)
            while (i <= Code04_BertownRoads2.m):
                jcall(out, 'println', jadd(jadd(Code04_BertownRoads2.ans1[i], ' '), Code04_BertownRoads2.ans2[i]))
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code04_BertownRoads2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_BertownRoads2.MAXN = jcast('int', 100001)
Code04_BertownRoads2.MAXM = jcast('int', 300001)
Code04_BertownRoads2.n = jcast('int', 0)
Code04_BertownRoads2.m = jcast('int', 0)
Code04_BertownRoads2.head = jarray('int', [Code04_BertownRoads2.MAXN])
Code04_BertownRoads2.nxt = jarray('int', [jcast('int', (Code04_BertownRoads2.MAXM << (1 & 31)))])
Code04_BertownRoads2.to = jarray('int', [jcast('int', (Code04_BertownRoads2.MAXM << (1 & 31)))])
Code04_BertownRoads2.cntg = jcast('int', 0)
Code04_BertownRoads2.dfn = jarray('int', [Code04_BertownRoads2.MAXN])
Code04_BertownRoads2.low = jarray('int', [Code04_BertownRoads2.MAXN])
Code04_BertownRoads2.cntd = jcast('int', 0)
Code04_BertownRoads2.check = jcast('boolean', False)
Code04_BertownRoads2.ans1 = jarray('int', [Code04_BertownRoads2.MAXM])
Code04_BertownRoads2.ans2 = jarray('int', [Code04_BertownRoads2.MAXM])
Code04_BertownRoads2.cnta = jcast('int', 0)

if __name__ == '__main__':
    Code04_BertownRoads2.main([])

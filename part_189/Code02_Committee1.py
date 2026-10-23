# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 和平委员会，Python版
# 一共n个团体，每个团体有两个代表，所以有2n个代表
# 第i号团体两个代表的编号为2i−1和2i，然后给定m个讨厌关系
# 格式 x y : 编号x和编号y这两个代表，相互讨厌，不可共事
# 现在要选出n个人组成委员会，每个团体的两个代表，有且仅有1人入选
# 同时要求选出的委员会中，没有相互讨厌的代表，如果做不到，打印"NIE"
# 如果能做到，按升序打印组成委员会的n个人的编号，任何一种方案都可以
# 1 <= n <= 8 * 10^3
# 0 <= m <= 2 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P5782
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Committee1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'stack': 'stack', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
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
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stack = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        jset(Code02_Committee1.stack[Code02_Committee1.stacksize], 0, u)
        jset(Code02_Committee1.stack[Code02_Committee1.stacksize], 1, status)
        jset(Code02_Committee1.stack[Code02_Committee1.stacksize], 2, e)
        Code02_Committee1.stacksize = jcast('int', (Code02_Committee1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_Committee1.stacksize = jcast('int', (Code02_Committee1.stacksize - 1))
        Code02_Committee1.u = jcast('int', Code02_Committee1.stack[Code02_Committee1.stacksize][0])
        Code02_Committee1.status = jcast('int', Code02_Committee1.stack[Code02_Committee1.stacksize][1])
        Code02_Committee1.e = jcast('int', Code02_Committee1.stack[Code02_Committee1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_Committee1.nxt, ((_java_obj_1 := Code02_Committee1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Committee1.head[u])
        Code02_Committee1.to[Code02_Committee1.cntg] = jcast('int', v)
        Code02_Committee1.head[u] = jcast('int', Code02_Committee1.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code02_Committee1.dfn, u, jset(Code02_Committee1.low, u, ((_java_obj_4 := Code02_Committee1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code02_Committee1.sta, ((_java_obj_7 := Code02_Committee1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code02_Committee1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Committee1.to[e])
            if (Code02_Committee1.dfn[v] == 0):
                Code02_Committee1.tarjan1(v)
                jset(Code02_Committee1.low, u, jstatic('Math', 'min', Code02_Committee1.low[u], Code02_Committee1.low[v]))
            else:
                if (Code02_Committee1.belong[v] == 0):
                    jset(Code02_Committee1.low, u, jstatic('Math', 'min', Code02_Committee1.low[u], Code02_Committee1.dfn[v]))
            e = jcast('int', Code02_Committee1.nxt[e])
        if (Code02_Committee1.dfn[u] == Code02_Committee1.low[u]):
            Code02_Committee1.sccCnt = jcast('int', (Code02_Committee1.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code02_Committee1.sta[((_java_obj_10 := Code02_Committee1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code02_Committee1.belong[pop] = jcast('int', Code02_Committee1.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code02_Committee1.stacksize = jcast('int', 0)
        Code02_Committee1.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code02_Committee1.stacksize > 0):
            Code02_Committee1.pop()
            if (Code02_Committee1.status == jcast('int', (-1))):
                jset(Code02_Committee1.dfn, Code02_Committee1.u, jset(Code02_Committee1.low, Code02_Committee1.u, ((_java_obj_13 := Code02_Committee1), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code02_Committee1.sta, ((_java_obj_16 := Code02_Committee1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code02_Committee1.u)
                Code02_Committee1.e = jcast('int', Code02_Committee1.head[Code02_Committee1.u])
            else:
                v = jcast('int', Code02_Committee1.to[Code02_Committee1.e])
                if (Code02_Committee1.status == 0):
                    jset(Code02_Committee1.low, Code02_Committee1.u, jstatic('Math', 'min', Code02_Committee1.low[Code02_Committee1.u], Code02_Committee1.low[v]))
                if ((Code02_Committee1.status == 1) and (Code02_Committee1.belong[v] == 0)):
                    jset(Code02_Committee1.low, Code02_Committee1.u, jstatic('Math', 'min', Code02_Committee1.low[Code02_Committee1.u], Code02_Committee1.dfn[v]))
                Code02_Committee1.e = jcast('int', Code02_Committee1.nxt[Code02_Committee1.e])
            if (Code02_Committee1.e != 0):
                v = jcast('int', Code02_Committee1.to[Code02_Committee1.e])
                if (Code02_Committee1.dfn[v] == 0):
                    Code02_Committee1.push(Code02_Committee1.u, 0, Code02_Committee1.e)
                    Code02_Committee1.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code02_Committee1.push(Code02_Committee1.u, 1, Code02_Committee1.e)
            else:
                if (Code02_Committee1.dfn[Code02_Committee1.u] == Code02_Committee1.low[Code02_Committee1.u]):
                    Code02_Committee1.sccCnt = jcast('int', (Code02_Committee1.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code02_Committee1.sta[((_java_obj_19 := Code02_Committee1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code02_Committee1.belong[pop] = jcast('int', Code02_Committee1.sccCnt)
                        if not ((pop != Code02_Committee1.u)):
                            break

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', (x - 1)) if (jcast('int', (x & 1)) == 0) else jcast('int', jadd(x, 1))))

    @staticmethod
    def main(args):
        in_ = Code02_Committee1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Committee1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Committee1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_Committee1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_Committee1.addEdge(u, Code02_Committee1.other(v))
            Code02_Committee1.addEdge(v, Code02_Committee1.other(u))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= jcast('int', (Code02_Committee1.n << (1 & 31)))):
            if (Code02_Committee1.dfn[i] == 0):
                # tarjan1(i);
                Code02_Committee1.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code02_Committee1.n):
            a = jcast('int', jcast('int', (i << (1 & 31))))
            b = jcast('int', jcast('int', (a - 1)))
            if (Code02_Committee1.belong[a] == Code02_Committee1.belong[b]):
                check = jcast('boolean', False)
            i = jcast('int', (i + 1))
        if check:
            i = jcast('int', 1)
            a = 0
            b = 0
            while (i <= Code02_Committee1.n):
                a = jcast('int', jcast('int', (i << (1 & 31))))
                b = jcast('int', jcast('int', (a - 1)))
                if (Code02_Committee1.belong[a] < Code02_Committee1.belong[b]):
                    jcall(out, 'println', a)
                else:
                    jcall(out, 'println', b)
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', 'NIE')
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
            raise TypeError("No matching overload for Code02_Committee1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Committee1.MAXN = jcast('int', 20001)
Code02_Committee1.MAXM = jcast('int', 50001)
Code02_Committee1.n = jcast('int', 0)
Code02_Committee1.m = jcast('int', 0)
Code02_Committee1.head = jarray('int', [Code02_Committee1.MAXN])
Code02_Committee1.nxt = jarray('int', [Code02_Committee1.MAXM])
Code02_Committee1.to = jarray('int', [Code02_Committee1.MAXM])
Code02_Committee1.cntg = jcast('int', 0)
Code02_Committee1.dfn = jarray('int', [Code02_Committee1.MAXN])
Code02_Committee1.low = jarray('int', [Code02_Committee1.MAXN])
Code02_Committee1.cntd = jcast('int', 0)
Code02_Committee1.sta = jarray('int', [Code02_Committee1.MAXN])
Code02_Committee1.top = jcast('int', 0)
Code02_Committee1.belong = jarray('int', [Code02_Committee1.MAXN])
Code02_Committee1.sccCnt = jcast('int', 0)
Code02_Committee1.stack = jarray('int', [Code02_Committee1.MAXN, 3])
Code02_Committee1.u = jcast('int', 0)
Code02_Committee1.status = jcast('int', 0)
Code02_Committee1.e = jcast('int', 0)
Code02_Committee1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_Committee1.main([])

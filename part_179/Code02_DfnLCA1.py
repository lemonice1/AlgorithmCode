# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# dfn序求LCA，Python版
# 一共有n个节点，给定n-1条边，所有节点组成一棵树，给定树头root
# 一共有m条查询，格式 u v : 打印u和v的最低公共祖先
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DfnLCA1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'root': 'root', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'dfn': 'dfn', 'lg2': 'lg2', 'rmq': 'rmq', 'cntDfn': 'cntDfn', 'stack': 'stack', 'u': 'u', 'f': 'f', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    root = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    dfn = None
    lg2 = None
    rmq = None
    cntDfn = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize], 0, u)
        jset(Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize], 1, f)
        jset(Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize], 2, e)
        Code02_DfnLCA1.stacksize = jcast('int', (Code02_DfnLCA1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_DfnLCA1.stacksize = jcast('int', (Code02_DfnLCA1.stacksize - 1))
        Code02_DfnLCA1.u = jcast('int', Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize][0])
        Code02_DfnLCA1.f = jcast('int', Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize][1])
        Code02_DfnLCA1.e = jcast('int', Code02_DfnLCA1.stack[Code02_DfnLCA1.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_DfnLCA1.nextg, ((_java_obj_1 := Code02_DfnLCA1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_DfnLCA1.headg[u])
        Code02_DfnLCA1.tog[Code02_DfnLCA1.cntg] = jcast('int', v)
        Code02_DfnLCA1.headg[u] = jcast('int', Code02_DfnLCA1.cntg)

    @staticmethod
    def getUp(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', (x if (Code02_DfnLCA1.dfn[x] < Code02_DfnLCA1.dfn[y]) else y))

    # dfn序递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code02_DfnLCA1.dfn, u, ((_java_obj_4 := Code02_DfnLCA1), (_java_key_5 := 'cntDfn'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code02_DfnLCA1.rmq[Code02_DfnLCA1.dfn[u]], 0, fa)
        e = jcast('int', Code02_DfnLCA1.headg[u])
        while (e > 0):
            v = jcast('int', Code02_DfnLCA1.tog[e])
            if (v != fa):
                Code02_DfnLCA1.dfs1(v, u)
            e = jcast('int', Code02_DfnLCA1.nextg[e])

    # dfs1迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code02_DfnLCA1.stacksize = jcast('int', 0)
        Code02_DfnLCA1.push(cur, fa, jcast('int', (-1)))
        while (Code02_DfnLCA1.stacksize > 0):
            Code02_DfnLCA1.pop()
            if (Code02_DfnLCA1.e == jcast('int', (-1))):
                jset(Code02_DfnLCA1.dfn, Code02_DfnLCA1.u, ((_java_obj_7 := Code02_DfnLCA1), (_java_key_8 := 'cntDfn'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                jset(Code02_DfnLCA1.rmq[Code02_DfnLCA1.dfn[Code02_DfnLCA1.u]], 0, Code02_DfnLCA1.f)
                Code02_DfnLCA1.e = jcast('int', Code02_DfnLCA1.headg[Code02_DfnLCA1.u])
            else:
                Code02_DfnLCA1.e = jcast('int', Code02_DfnLCA1.nextg[Code02_DfnLCA1.e])
            if (Code02_DfnLCA1.e != 0):
                Code02_DfnLCA1.push(Code02_DfnLCA1.u, Code02_DfnLCA1.f, Code02_DfnLCA1.e)
                v = jcast('int', Code02_DfnLCA1.tog[Code02_DfnLCA1.e])
                if (v != Code02_DfnLCA1.f):
                    Code02_DfnLCA1.push(v, Code02_DfnLCA1.u, jcast('int', (-1)))

    @staticmethod
    def buildRmq():
        # dfs1(root, 0);
        Code02_DfnLCA1.dfs2(Code02_DfnLCA1.root, 0)
        i = jcast('int', 2)
        while (i <= Code02_DfnLCA1.n):
            Code02_DfnLCA1.lg2[i] = jcast('int', jcast('int', jadd(Code02_DfnLCA1.lg2[jcast('int', (i >> (1 & 31)))], 1)))
            i = jcast('int', (i + 1))
        pre = jcast('int', 0)
        cur = jcast('int', 1)
        while (cur <= Code02_DfnLCA1.lg2[Code02_DfnLCA1.n]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (cur & 31))))) - 1)) <= Code02_DfnLCA1.n):
                jset(Code02_DfnLCA1.rmq[i], cur, Code02_DfnLCA1.getUp(Code02_DfnLCA1.rmq[i][pre], Code02_DfnLCA1.rmq[jcast('int', jadd(i, jcast('int', (1 << (pre & 31)))))][pre]))
                i = jcast('int', (i + 1))
            pre = jcast('int', (pre + 1))
            cur = jcast('int', (cur + 1))

    @staticmethod
    def getLCA(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (x == y):
            return jcast('int', x)
        x = jcast('int', Code02_DfnLCA1.dfn[x])
        y = jcast('int', Code02_DfnLCA1.dfn[y])
        if (x > y):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        x = jcast('int', (x + 1))
        k = jcast('int', Code02_DfnLCA1.lg2[jcast('int', jadd(jcast('int', (y - x)), 1))])
        return jcast('int', Code02_DfnLCA1.getUp(Code02_DfnLCA1.rmq[x][k], Code02_DfnLCA1.rmq[jcast('int', jadd(jcast('int', (y - jcast('int', (1 << (k & 31))))), 1))][k]))

    @staticmethod
    def main(args):
        in_ = Code02_DfnLCA1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_DfnLCA1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_DfnLCA1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_DfnLCA1.root = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code02_DfnLCA1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code02_DfnLCA1.addEdge(u, v)
            Code02_DfnLCA1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code02_DfnLCA1.buildRmq()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_DfnLCA1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jcall(out, 'println', Code02_DfnLCA1.getLCA(u, v))
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
            raise TypeError("No matching overload for Code02_DfnLCA1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DfnLCA1.MAXN = jcast('int', 500001)
Code02_DfnLCA1.MAXP = jcast('int', 20)
Code02_DfnLCA1.n = jcast('int', 0)
Code02_DfnLCA1.m = jcast('int', 0)
Code02_DfnLCA1.root = jcast('int', 0)
Code02_DfnLCA1.headg = jarray('int', [Code02_DfnLCA1.MAXN])
Code02_DfnLCA1.nextg = jarray('int', [jcast('int', (Code02_DfnLCA1.MAXN << (1 & 31)))])
Code02_DfnLCA1.tog = jarray('int', [jcast('int', (Code02_DfnLCA1.MAXN << (1 & 31)))])
Code02_DfnLCA1.cntg = jcast('int', 0)
Code02_DfnLCA1.dfn = jarray('int', [Code02_DfnLCA1.MAXN])
Code02_DfnLCA1.lg2 = jarray('int', [Code02_DfnLCA1.MAXN])
Code02_DfnLCA1.rmq = jarray('int', [Code02_DfnLCA1.MAXN, Code02_DfnLCA1.MAXP])
Code02_DfnLCA1.cntDfn = jcast('int', 0)
Code02_DfnLCA1.stack = jarray('int', [Code02_DfnLCA1.MAXN, 3])
Code02_DfnLCA1.u = jcast('int', 0)
Code02_DfnLCA1.f = jcast('int', 0)
Code02_DfnLCA1.e = jcast('int', 0)
Code02_DfnLCA1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_DfnLCA1.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 欧拉序求LCA，Python版
# 一共有n个节点，给定n-1条边，所有节点组成一棵树，给定树头root
# 一共有m条查询，格式 u v : 打印u和v的最低公共祖先
# 1 <= n、m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3379
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_EulerLCA2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'root': 'root', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'first': 'first', 'lg2': 'lg2', 'rmq': 'rmq', 'cntEuler': 'cntEuler', 'stack': 'stack', 'u': 'u', 'f': 'f', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXP = 0
    n = 0
    m = 0
    root = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    first = None
    lg2 = None
    rmq = None
    cntEuler = 0
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
        jset(Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize], 0, u)
        jset(Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize], 1, f)
        jset(Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize], 2, e)
        Code01_EulerLCA2.stacksize = jcast('int', (Code01_EulerLCA2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_EulerLCA2.stacksize = jcast('int', (Code01_EulerLCA2.stacksize - 1))
        Code01_EulerLCA2.u = jcast('int', Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize][0])
        Code01_EulerLCA2.f = jcast('int', Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize][1])
        Code01_EulerLCA2.e = jcast('int', Code01_EulerLCA2.stack[Code01_EulerLCA2.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_EulerLCA2.nextg, ((_java_obj_1 := Code01_EulerLCA2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_EulerLCA2.headg[u])
        Code01_EulerLCA2.tog[Code01_EulerLCA2.cntg] = jcast('int', v)
        Code01_EulerLCA2.headg[u] = jcast('int', Code01_EulerLCA2.cntg)

    @staticmethod
    def getUp(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('int', (x if (Code01_EulerLCA2.first[x] < Code01_EulerLCA2.first[y]) else y))

    # 欧拉序递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code01_EulerLCA2.first, u, ((_java_obj_4 := Code01_EulerLCA2), (_java_key_5 := 'cntEuler'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code01_EulerLCA2.rmq[Code01_EulerLCA2.first[u]], 0, u)
        e = jcast('int', Code01_EulerLCA2.headg[u])
        while (e > 0):
            v = jcast('int', Code01_EulerLCA2.tog[e])
            if (v != fa):
                Code01_EulerLCA2.dfs1(v, u)
                jset(Code01_EulerLCA2.rmq[((_java_obj_7 := Code01_EulerLCA2), (_java_key_8 := 'cntEuler'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3]], 0, u)
            e = jcast('int', Code01_EulerLCA2.nextg[e])

    # dfs1迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_EulerLCA2.stacksize = jcast('int', 0)
        Code01_EulerLCA2.push(cur, fa, jcast('int', (-1)))
        while (Code01_EulerLCA2.stacksize > 0):
            Code01_EulerLCA2.pop()
            if (Code01_EulerLCA2.e == jcast('int', (-1))):
                jset(Code01_EulerLCA2.first, Code01_EulerLCA2.u, ((_java_obj_10 := Code01_EulerLCA2), (_java_key_11 := 'cntEuler'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                jset(Code01_EulerLCA2.rmq[Code01_EulerLCA2.first[Code01_EulerLCA2.u]], 0, Code01_EulerLCA2.u)
                Code01_EulerLCA2.e = jcast('int', Code01_EulerLCA2.headg[Code01_EulerLCA2.u])
            else:
                if (Code01_EulerLCA2.tog[Code01_EulerLCA2.e] != Code01_EulerLCA2.f):
                    jset(Code01_EulerLCA2.rmq[((_java_obj_13 := Code01_EulerLCA2), (_java_key_14 := 'cntEuler'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]], 0, Code01_EulerLCA2.u)
                Code01_EulerLCA2.e = jcast('int', Code01_EulerLCA2.nextg[Code01_EulerLCA2.e])
            if (Code01_EulerLCA2.e != 0):
                Code01_EulerLCA2.push(Code01_EulerLCA2.u, Code01_EulerLCA2.f, Code01_EulerLCA2.e)
                v = jcast('int', Code01_EulerLCA2.tog[Code01_EulerLCA2.e])
                if (v != Code01_EulerLCA2.f):
                    Code01_EulerLCA2.push(v, Code01_EulerLCA2.u, jcast('int', (-1)))

    @staticmethod
    def buildRmq():
        # dfs1(root, 0);
        Code01_EulerLCA2.dfs2(Code01_EulerLCA2.root, 0)
        i = jcast('int', 2)
        while (i <= Code01_EulerLCA2.cntEuler):
            Code01_EulerLCA2.lg2[i] = jcast('int', jcast('int', jadd(Code01_EulerLCA2.lg2[jcast('int', (i >> (1 & 31)))], 1)))
            i = jcast('int', (i + 1))
        pre = jcast('int', 0)
        cur = jcast('int', 1)
        while (cur <= Code01_EulerLCA2.lg2[Code01_EulerLCA2.cntEuler]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (cur & 31))))) - 1)) <= Code01_EulerLCA2.cntEuler):
                jset(Code01_EulerLCA2.rmq[i], cur, Code01_EulerLCA2.getUp(Code01_EulerLCA2.rmq[i][pre], Code01_EulerLCA2.rmq[jcast('int', jadd(i, jcast('int', (1 << (pre & 31)))))][pre]))
                i = jcast('int', (i + 1))
            pre = jcast('int', (pre + 1))
            cur = jcast('int', (cur + 1))

    @staticmethod
    def getLCA(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        x = jcast('int', Code01_EulerLCA2.first[x])
        y = jcast('int', Code01_EulerLCA2.first[y])
        if (x > y):
            tmp = jcast('int', x)
            x = jcast('int', y)
            y = jcast('int', tmp)
        k = jcast('int', Code01_EulerLCA2.lg2[jcast('int', jadd(jcast('int', (y - x)), 1))])
        return jcast('int', Code01_EulerLCA2.getUp(Code01_EulerLCA2.rmq[x][k], Code01_EulerLCA2.rmq[jcast('int', jadd(jcast('int', (y - jcast('int', (1 << (k & 31))))), 1))][k]))

    @staticmethod
    def main(args):
        in_ = Code01_EulerLCA2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_EulerLCA2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_EulerLCA2.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_EulerLCA2.root = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_EulerLCA2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_EulerLCA2.addEdge(u, v)
            Code01_EulerLCA2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code01_EulerLCA2.buildRmq()
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code01_EulerLCA2.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jcall(out, 'println', Code01_EulerLCA2.getLCA(u, v))
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
            return jcast('int', self.buffer[((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]])

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
            raise TypeError("No matching overload for Code01_EulerLCA2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_EulerLCA2.MAXN = jcast('int', 500001)
Code01_EulerLCA2.MAXP = jcast('int', 20)
Code01_EulerLCA2.n = jcast('int', 0)
Code01_EulerLCA2.m = jcast('int', 0)
Code01_EulerLCA2.root = jcast('int', 0)
Code01_EulerLCA2.headg = jarray('int', [Code01_EulerLCA2.MAXN])
Code01_EulerLCA2.nextg = jarray('int', [jcast('int', (Code01_EulerLCA2.MAXN << (1 & 31)))])
Code01_EulerLCA2.tog = jarray('int', [jcast('int', (Code01_EulerLCA2.MAXN << (1 & 31)))])
Code01_EulerLCA2.cntg = jcast('int', 0)
Code01_EulerLCA2.first = jarray('int', [Code01_EulerLCA2.MAXN])
Code01_EulerLCA2.lg2 = jarray('int', [jcast('int', (Code01_EulerLCA2.MAXN << (1 & 31)))])
Code01_EulerLCA2.rmq = jarray('int', [jcast('int', (Code01_EulerLCA2.MAXN << (1 & 31))), Code01_EulerLCA2.MAXP])
Code01_EulerLCA2.cntEuler = jcast('int', 0)
Code01_EulerLCA2.stack = jarray('int', [Code01_EulerLCA2.MAXN, 3])
Code01_EulerLCA2.u = jcast('int', 0)
Code01_EulerLCA2.f = jcast('int', 0)
Code01_EulerLCA2.e = jcast('int', 0)
Code01_EulerLCA2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_EulerLCA2.main([])

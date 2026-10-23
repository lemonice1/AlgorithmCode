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

# 消息传递，Python版
# 一共有n个节点，给定n-1条边，每条边的权值为1，所有节点组成一棵树
# 一共有m条查询，格式 x k : 打印有多少点与x的距离恰好为k
# 1 <= n、m <= 10^5
# 0 <= k < n
# 测试链接 : https://www.luogu.com.cn/problem/P6626
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Message2:
    __java_fields__ = {'MAXN': 'MAXN', 't': 't', 'n': 'n', 'm': 'm', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headq': 'headq', 'nextq': 'nextq', 'dis': 'dis', 'qid': 'qid', 'cntq': 'cntq', 'vis': 'vis', 'siz': 'siz', 'nodeCnt': 'nodeCnt', 'maxEdge': 'maxEdge', 'needArr': 'needArr', 'qidArr': 'qidArr', 'cnta': 'cnta', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'f': 'f', 'edge': 'edge', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    t = 0
    n = 0
    m = 0
    headg = None
    nextg = None
    tog = None
    cntg = 0
    headq = None
    nextq = None
    dis = None
    qid = None
    cntq = 0
    vis = None
    siz = None
    # nodeCnt[i] = j，表示从u往下走i条边，一共能找到j个点
    nodeCnt = None
    maxEdge = 0
    needArr = None
    qidArr = None
    cnta = 0
    ans = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    edge = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, edge, e):
        u = jcast('int', u)
        f = jcast('int', f)
        edge = jcast('int', edge)
        e = jcast('int', e)
        jset(Code07_Message2.stack[Code07_Message2.stacksize], 0, u)
        jset(Code07_Message2.stack[Code07_Message2.stacksize], 1, f)
        jset(Code07_Message2.stack[Code07_Message2.stacksize], 2, edge)
        jset(Code07_Message2.stack[Code07_Message2.stacksize], 3, e)
        Code07_Message2.stacksize = jcast('int', (Code07_Message2.stacksize + 1))

    @staticmethod
    def pop():
        Code07_Message2.stacksize = jcast('int', (Code07_Message2.stacksize - 1))
        Code07_Message2.u = jcast('int', Code07_Message2.stack[Code07_Message2.stacksize][0])
        Code07_Message2.f = jcast('int', Code07_Message2.stack[Code07_Message2.stacksize][1])
        Code07_Message2.edge = jcast('int', Code07_Message2.stack[Code07_Message2.stacksize][2])
        Code07_Message2.e = jcast('int', Code07_Message2.stack[Code07_Message2.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_Message2.nextg, ((_java_obj_1 := Code07_Message2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_Message2.headg[u])
        Code07_Message2.tog[Code07_Message2.cntg] = jcast('int', v)
        Code07_Message2.headg[u] = jcast('int', Code07_Message2.cntg)

    @staticmethod
    def addQuery(u, k, id):
        u = jcast('int', u)
        k = jcast('int', k)
        id = jcast('int', id)
        jset(Code07_Message2.nextq, ((_java_obj_4 := Code07_Message2), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_Message2.headq[u])
        Code07_Message2.dis[Code07_Message2.cntq] = jcast('int', k)
        Code07_Message2.qid[Code07_Message2.cntq] = jcast('int', id)
        Code07_Message2.headq[u] = jcast('int', Code07_Message2.cntq)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code07_Message2.siz[u] = jcast('int', 1)
        e = jcast('int', Code07_Message2.headg[u])
        while (e > 0):
            v = jcast('int', Code07_Message2.tog[e])
            if ((v != fa) and (not Code07_Message2.vis[v])):
                Code07_Message2.getSize1(v, u)
                Code07_Message2.siz[u] = jcast('int', jcast('int', jadd(Code07_Message2.siz[u], Code07_Message2.siz[v])))
            e = jcast('int', Code07_Message2.nextg[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code07_Message2.stacksize = jcast('int', 0)
        Code07_Message2.push(cur, fa, 0, jcast('int', (-1)))
        while (Code07_Message2.stacksize > 0):
            Code07_Message2.pop()
            if (Code07_Message2.e == jcast('int', (-1))):
                Code07_Message2.siz[Code07_Message2.u] = jcast('int', 1)
                Code07_Message2.e = jcast('int', Code07_Message2.headg[Code07_Message2.u])
            else:
                Code07_Message2.e = jcast('int', Code07_Message2.nextg[Code07_Message2.e])
            if (Code07_Message2.e != 0):
                Code07_Message2.push(Code07_Message2.u, Code07_Message2.f, 0, Code07_Message2.e)
                v = jcast('int', Code07_Message2.tog[Code07_Message2.e])
                if ((v != Code07_Message2.f) and (not Code07_Message2.vis[v])):
                    Code07_Message2.push(v, Code07_Message2.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code07_Message2.headg[Code07_Message2.u])
                while (ei > 0):
                    v = jcast('int', Code07_Message2.tog[ei])
                    if ((v != Code07_Message2.f) and (not Code07_Message2.vis[v])):
                        Code07_Message2.siz[Code07_Message2.u] = jcast('int', jcast('int', jadd(Code07_Message2.siz[Code07_Message2.u], Code07_Message2.siz[v])))
                    ei = jcast('int', Code07_Message2.nextg[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code07_Message2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code07_Message2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code07_Message2.headg[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code07_Message2.tog[e])
                        if (((v != fa) and (not Code07_Message2.vis[v])) and (Code07_Message2.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                    except JBreak as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code07_Message2.nextg[e])
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
        return jcast('int', u)

    # 收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, edge):
        u = jcast('int', u)
        fa = jcast('int', fa)
        edge = jcast('int', edge)
        Code07_Message2.nodeCnt[edge] = jcast('int', (Code07_Message2.nodeCnt[edge] + 1))
        Code07_Message2.maxEdge = jcast('int', jstatic('Math', 'max', Code07_Message2.maxEdge, edge))
        e = jcast('int', Code07_Message2.headq[u])
        while (e > 0):
            if (Code07_Message2.dis[e] >= edge):
                jset(Code07_Message2.needArr, ((_java_obj_9 := Code07_Message2), (_java_key_10 := 'cnta'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], jcast('int', (Code07_Message2.dis[e] - edge)))
                Code07_Message2.qidArr[Code07_Message2.cnta] = jcast('int', Code07_Message2.qid[e])
            e = jcast('int', Code07_Message2.nextq[e])
        e = jcast('int', Code07_Message2.headg[u])
        while (e > 0):
            v = jcast('int', Code07_Message2.tog[e])
            if ((v != fa) and (not Code07_Message2.vis[v])):
                Code07_Message2.dfs1(v, u, jcast('int', jadd(edge, 1)))
            e = jcast('int', Code07_Message2.nextg[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, edg):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        edg = jcast('int', edg)
        Code07_Message2.stacksize = jcast('int', 0)
        Code07_Message2.push(cur, fa, edg, jcast('int', (-1)))
        while (Code07_Message2.stacksize > 0):
            Code07_Message2.pop()
            if (Code07_Message2.e == jcast('int', (-1))):
                Code07_Message2.nodeCnt[Code07_Message2.edge] = jcast('int', (Code07_Message2.nodeCnt[Code07_Message2.edge] + 1))
                Code07_Message2.maxEdge = jcast('int', jstatic('Math', 'max', Code07_Message2.maxEdge, Code07_Message2.edge))
                e = jcast('int', Code07_Message2.headq[Code07_Message2.u])
                while (e > 0):
                    if (Code07_Message2.dis[e] >= Code07_Message2.edge):
                        jset(Code07_Message2.needArr, ((_java_obj_12 := Code07_Message2), (_java_key_13 := 'cnta'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3], jcast('int', (Code07_Message2.dis[e] - Code07_Message2.edge)))
                        Code07_Message2.qidArr[Code07_Message2.cnta] = jcast('int', Code07_Message2.qid[e])
                    e = jcast('int', Code07_Message2.nextq[e])
                Code07_Message2.e = jcast('int', Code07_Message2.headg[Code07_Message2.u])
            else:
                Code07_Message2.e = jcast('int', Code07_Message2.nextg[Code07_Message2.e])
            if (Code07_Message2.e != 0):
                Code07_Message2.push(Code07_Message2.u, Code07_Message2.f, Code07_Message2.edge, Code07_Message2.e)
                v = jcast('int', Code07_Message2.tog[Code07_Message2.e])
                if ((v != Code07_Message2.f) and (not Code07_Message2.vis[v])):
                    Code07_Message2.push(Code07_Message2.tog[Code07_Message2.e], Code07_Message2.u, jcast('int', jadd(Code07_Message2.edge, 1)), jcast('int', (-1)))

    @staticmethod
    def calc(u, edge, effect):
        u = jcast('int', u)
        edge = jcast('int', edge)
        effect = jcast('int', effect)
        Code07_Message2.cnta = jcast('int', 0)
        Code07_Message2.maxEdge = jcast('int', 0)
        # dfs1(u, 0, edge);
        Code07_Message2.dfs2(u, 0, edge)
        i = jcast('int', 1)
        while (i <= Code07_Message2.cnta):
            ((_java_obj_15 := Code07_Message2.ans), (_java_key_16 := Code07_Message2.qidArr[i]), jset(_java_obj_15, _java_key_16, jcast('int', jadd(jget(_java_obj_15, _java_key_16), jcast('int', (Code07_Message2.nodeCnt[Code07_Message2.needArr[i]] * effect))))))[2]
            i = jcast('int', (i + 1))
        v = jcast('int', 0)
        while (v <= Code07_Message2.maxEdge):
            Code07_Message2.nodeCnt[v] = jcast('int', 0)
            v = jcast('int', (v + 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code07_Message2.vis[u] = jcast('boolean', True)
        Code07_Message2.calc(u, 0, 1)
        e = jcast('int', Code07_Message2.headg[u])
        while (e > 0):
            v = jcast('int', Code07_Message2.tog[e])
            if (not Code07_Message2.vis[v]):
                Code07_Message2.calc(v, 1, jcast('int', (-1)))
                Code07_Message2.solve(Code07_Message2.getCentroid(v, u))
            e = jcast('int', Code07_Message2.nextg[e])

    @staticmethod
    def prepare():
        Code07_Message2.cntg = jcast('int', 0)
        Code07_Message2.cntq = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_Message2.n):
            Code07_Message2.headg[i] = jcast('int', 0)
            Code07_Message2.headq[i] = jcast('int', 0)
            Code07_Message2.vis[i] = jcast('boolean', False)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Message2.m):
            Code07_Message2.ans[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_Message2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Message2.t = jcast('int', jcall(in_, 'nextInt'))
        c = jcast('int', 1)
        while (c <= Code07_Message2.t):
            Code07_Message2.n = jcast('int', jcall(in_, 'nextInt'))
            Code07_Message2.m = jcast('int', jcall(in_, 'nextInt'))
            Code07_Message2.prepare()
            i = jcast('int', 1)
            u = 0
            v = 0
            while (i < Code07_Message2.n):
                u = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code07_Message2.addEdge(u, v)
                Code07_Message2.addEdge(v, u)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            x = 0
            k = 0
            while (i <= Code07_Message2.m):
                x = jcast('int', jcall(in_, 'nextInt'))
                k = jcast('int', jcall(in_, 'nextInt'))
                Code07_Message2.addQuery(x, k, i)
                i = jcast('int', (i + 1))
            Code07_Message2.solve(Code07_Message2.getCentroid(1, 0))
            i = jcast('int', 1)
            while (i <= Code07_Message2.m):
                jcall(out, 'println', Code07_Message2.ans[i])
                i = jcast('int', (i + 1))
            c = jcast('int', (c + 1))
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
            return jcast('int', self.buffer[((_java_obj_17 := self), (_java_key_18 := 'ptr'), (_java_old_19 := jget(_java_obj_17, _java_key_18)), jset(_java_obj_17, _java_key_18, jcast('int', (_java_old_19 + (1)))), _java_old_19)[4]])

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
            raise TypeError("No matching overload for Code07_Message2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Message2.MAXN = jcast('int', 100001)
Code07_Message2.t = jcast('int', 0)
Code07_Message2.n = jcast('int', 0)
Code07_Message2.m = jcast('int', 0)
Code07_Message2.headg = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.nextg = jarray('int', [jcast('int', (Code07_Message2.MAXN << (1 & 31)))])
Code07_Message2.tog = jarray('int', [jcast('int', (Code07_Message2.MAXN << (1 & 31)))])
Code07_Message2.cntg = jcast('int', 0)
Code07_Message2.headq = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.nextq = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.dis = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.qid = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.cntq = jcast('int', 0)
Code07_Message2.vis = jarray('boolean', [Code07_Message2.MAXN])
Code07_Message2.siz = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.nodeCnt = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.maxEdge = jcast('int', 0)
Code07_Message2.needArr = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.qidArr = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.cnta = jcast('int', 0)
Code07_Message2.ans = jarray('int', [Code07_Message2.MAXN])
Code07_Message2.stack = jarray('int', [Code07_Message2.MAXN, 4])
Code07_Message2.u = jcast('int', 0)
Code07_Message2.f = jcast('int', 0)
Code07_Message2.edge = jcast('int', 0)
Code07_Message2.e = jcast('int', 0)
Code07_Message2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_Message2.main([])

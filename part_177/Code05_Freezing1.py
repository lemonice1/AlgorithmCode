# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大中位数路径，Python版
# 一共有n个节点，给定n-1条边，每条边给定边权，所有节点组成一棵树
# 一条简单路径上，收集所有边权组成序列，其中的 下中位数 作为路径的权
# 边数在[limitl, limitr]范围的所有路径中，找到最大权的路径
# 如果有多条路径，找到其中一个方案即可，打印两个端点
# 1 <= n <= 10^5    0 <= 边权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF150E
# 测试链接 : https://codeforces.com/problemset/problem/150/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Freezing1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'limitl': 'limitl', 'limitr': 'limitr', 'cntw': 'cntw', 'arr': 'arr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'edgeArr': 'edgeArr', 'cnte': 'cnte', 'preVal': 'preVal', 'preNode': 'preNode', 'preLen': 'preLen', 'curVal': 'curVal', 'curNode': 'curNode', 'curLen': 'curLen', 'que': 'que', 'ans': 'ans', 'ansu': 'ansu', 'ansv': 'ansv'}
    MAXN = 0
    INF = 0
    n = 0
    limitl = 0
    limitr = 0
    cntw = 0
    # 端点u、端点v、边权w
    arr = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    # 边的编号eid、边连接的子树大小size
    edgeArr = None
    cnte = 0
    preVal = None
    preNode = None
    preLen = 0
    curVal = None
    curNode = None
    curLen = 0
    que = None
    ans = 0
    ansu = 0
    ansv = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code05_Freezing1.nxt, ((_java_obj_1 := Code05_Freezing1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Freezing1.head[u])
        Code05_Freezing1.to[Code05_Freezing1.cntg] = jcast('int', v)
        Code05_Freezing1.weight[Code05_Freezing1.cntg] = jcast('int', w)
        Code05_Freezing1.head[u] = jcast('int', Code05_Freezing1.cntg)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_Freezing1.siz[u] = jcast('int', 1)
        e = jcast('int', Code05_Freezing1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Freezing1.to[e])
            if ((v != fa) and (not Code05_Freezing1.vis[v])):
                Code05_Freezing1.getSize(v, u)
                Code05_Freezing1.siz[u] = jcast('int', jcast('int', jadd(Code05_Freezing1.siz[u], Code05_Freezing1.siz[v])))
            e = jcast('int', Code05_Freezing1.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code05_Freezing1.getSize(u, fa)
        half = jcast('int', jcast('int', (Code05_Freezing1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code05_Freezing1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code05_Freezing1.to[e])
                        if (((v != fa) and (not Code05_Freezing1.vis[v])) and (Code05_Freezing1.siz[v] > half)):
                            fa = jcast('int', u)
                            u = jcast('int', v)
                            find = jcast('boolean', False)
                            raise JBreak(None)
                    except JContinue as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                    except JBreak as _java_control_5:
                        if _java_control_5.label not in (None,):
                            raise
                        break
                    e = jcast('int', Code05_Freezing1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa, edge, sum, limit):
        u = jcast('int', u)
        fa = jcast('int', fa)
        edge = jcast('int', edge)
        sum = jcast('int', sum)
        limit = jcast('int', limit)
        Code05_Freezing1.curLen = jcast('int', jstatic('Math', 'max', Code05_Freezing1.curLen, edge))
        if (sum > Code05_Freezing1.curVal[edge]):
            Code05_Freezing1.curVal[edge] = jcast('int', sum)
            Code05_Freezing1.curNode[edge] = jcast('int', u)
        e = jcast('int', Code05_Freezing1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Freezing1.to[e])
            w = jcast('int', Code05_Freezing1.weight[e])
            if ((v != fa) and (not Code05_Freezing1.vis[v])):
                Code05_Freezing1.dfs(v, u, jcast('int', jadd(edge, 1)), jcast('int', jadd(sum, (1 if (w >= limit) else jcast('int', (-1))))), limit)
            e = jcast('int', Code05_Freezing1.nxt[e])

    @staticmethod
    def check(u, limit):
        u = jcast('int', u)
        limit = jcast('int', limit)
        Code05_Freezing1.preVal[0] = jcast('int', 0)
        Code05_Freezing1.preNode[0] = jcast('int', u)
        Code05_Freezing1.preLen = jcast('int', 0)
        k = jcast('int', 1)
        while (k <= Code05_Freezing1.cnte):
            v = jcast('int', Code05_Freezing1.to[Code05_Freezing1.edgeArr[k][0]])
            w = jcast('int', Code05_Freezing1.weight[Code05_Freezing1.edgeArr[k][0]])
            i = jcast('int', 1)
            while (i <= Code05_Freezing1.siz[v]):
                Code05_Freezing1.curVal[i] = jcast('int', jcast('int', (-Code05_Freezing1.INF)))
                i = jcast('int', (i + 1))
            Code05_Freezing1.curLen = jcast('int', 0)
            Code05_Freezing1.dfs(v, u, 1, (1 if (w >= limit) else jcast('int', (-1))), limit)
            ql = jcast('int', 1)
            qr = jcast('int', 0)
            # 根据之前的信息，初步建立窗口，子树按秩处理非常重要
            i = jcast('int', jstatic('Math', 'min', Code05_Freezing1.preLen, Code05_Freezing1.limitr))
            while (i >= Code05_Freezing1.limitl):
                while ((ql <= qr) and (Code05_Freezing1.preVal[Code05_Freezing1.que[qr]] <= Code05_Freezing1.preVal[i])):
                    qr = jcast('int', (qr - 1))
                jset(Code05_Freezing1.que, (qr := jcast('int', (qr + (1)))), i)
                i = jcast('int', (i - 1))
            down = jcast('int', Code05_Freezing1.limitr)
            up = jcast('int', Code05_Freezing1.limitl)
            i = jcast('int', 1)
            while (i <= Code05_Freezing1.curLen):
                up = jcast('int', (up - 1))
                if ((up >= 0) and (up <= Code05_Freezing1.preLen)):
                    while ((ql <= qr) and (Code05_Freezing1.preVal[Code05_Freezing1.que[qr]] <= Code05_Freezing1.preVal[up])):
                        qr = jcast('int', (qr - 1))
                    jset(Code05_Freezing1.que, (qr := jcast('int', (qr + (1)))), up)
                if ((ql <= qr) and (Code05_Freezing1.que[ql] == down)):
                    ql = jcast('int', (ql + 1))
                down = jcast('int', (down - 1))
                if ((ql <= qr) and (jcast('int', jadd(Code05_Freezing1.preVal[Code05_Freezing1.que[ql]], Code05_Freezing1.curVal[i])) >= 0)):
                    if (limit > Code05_Freezing1.ans):
                        Code05_Freezing1.ans = jcast('int', limit)
                        Code05_Freezing1.ansu = jcast('int', Code05_Freezing1.curNode[i])
                        Code05_Freezing1.ansv = jcast('int', Code05_Freezing1.preNode[Code05_Freezing1.que[ql]])
                    return jcast('boolean', True)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code05_Freezing1.curLen):
                if ((i > Code05_Freezing1.preLen) or (Code05_Freezing1.curVal[i] > Code05_Freezing1.preVal[i])):
                    Code05_Freezing1.preVal[i] = jcast('int', Code05_Freezing1.curVal[i])
                    Code05_Freezing1.preNode[i] = jcast('int', Code05_Freezing1.curNode[i])
                i = jcast('int', (i + 1))
            Code05_Freezing1.preLen = jcast('int', jstatic('Math', 'max', Code05_Freezing1.preLen, Code05_Freezing1.curLen))
            k = jcast('int', (k + 1))
        return jcast('boolean', False)

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code05_Freezing1.getSize(u, 0)
        Code05_Freezing1.cnte = jcast('int', 0)
        e = jcast('int', Code05_Freezing1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Freezing1.to[e])
            if (not Code05_Freezing1.vis[v]):
                jset(Code05_Freezing1.edgeArr[((_java_obj_6 := Code05_Freezing1), (_java_key_7 := 'cnte'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3]], 0, e)
                jset(Code05_Freezing1.edgeArr[Code05_Freezing1.cnte], 1, Code05_Freezing1.siz[v])
            e = jcast('int', Code05_Freezing1.nxt[e])
        # 子树按大小或者高度排序，然后依次处理
        # 如果不按秩处理，建立窗口阶段，复杂度会炸
        # 课上会重点解释
        jstatic('Arrays', 'sort', Code05_Freezing1.edgeArr, 1, jcast('int', jadd(Code05_Freezing1.cnte, 1)), (lambda a, b: (a[1] - b[1])))
        l = jcast('int', 1)
        r = jcast('int', Code05_Freezing1.cntw)
        mid = 0
        while (l <= r):
            try:
                mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
                if Code05_Freezing1.check(u, mid):
                    l = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    r = jcast('int', jcast('int', (mid - 1)))
                if (r <= Code05_Freezing1.ans):
                    raise JBreak(None)
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code05_Freezing1.vis[u] = jcast('boolean', True)
        Code05_Freezing1.calc(u)
        e = jcast('int', Code05_Freezing1.head[u])
        while (e > 0):
            v = jcast('int', Code05_Freezing1.to[e])
            if (not Code05_Freezing1.vis[v]):
                Code05_Freezing1.solve(Code05_Freezing1.getCentroid(v, u))
            e = jcast('int', Code05_Freezing1.nxt[e])

    @staticmethod
    def main(args):
        in_ = Code05_Freezing1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_Freezing1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Freezing1.limitl = jcast('int', jcall(in_, 'nextInt'))
        Code05_Freezing1.limitr = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i < Code05_Freezing1.n):
            jset(Code05_Freezing1.arr[i], 0, jcall(in_, 'nextInt'))
            jset(Code05_Freezing1.arr[i], 1, jcall(in_, 'nextInt'))
            jset(Code05_Freezing1.arr[i], 2, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Freezing1.arr, 1, Code05_Freezing1.n, (lambda a, b: (a[2] - b[2])))
        Code05_Freezing1.cntw = jcast('int', 0)
        i = jcast('int', 1)
        while (i < Code05_Freezing1.n):
            if ((i == 1) or (Code05_Freezing1.arr[jcast('int', (i - 1))][2] != Code05_Freezing1.arr[i][2])):
                Code05_Freezing1.cntw = jcast('int', (Code05_Freezing1.cntw + 1))
            Code05_Freezing1.addEdge(Code05_Freezing1.arr[i][0], Code05_Freezing1.arr[i][1], Code05_Freezing1.cntw)
            Code05_Freezing1.addEdge(Code05_Freezing1.arr[i][1], Code05_Freezing1.arr[i][0], Code05_Freezing1.cntw)
            i = jcast('int', (i + 1))
        Code05_Freezing1.solve(Code05_Freezing1.getCentroid(1, 0))
        jcall(out, 'println', jadd(jadd(Code05_Freezing1.ansu, ' '), Code05_Freezing1.ansv))
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
            raise TypeError("No matching overload for Code05_Freezing1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Freezing1.MAXN = jcast('int', 100001)
Code05_Freezing1.INF = jcast('int', 1000000001)
Code05_Freezing1.n = jcast('int', 0)
Code05_Freezing1.limitl = jcast('int', 0)
Code05_Freezing1.limitr = jcast('int', 0)
Code05_Freezing1.cntw = jcast('int', 0)
Code05_Freezing1.arr = jarray('int', [Code05_Freezing1.MAXN, 3])
Code05_Freezing1.head = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.nxt = jarray('int', [jcast('int', (Code05_Freezing1.MAXN << (1 & 31)))])
Code05_Freezing1.to = jarray('int', [jcast('int', (Code05_Freezing1.MAXN << (1 & 31)))])
Code05_Freezing1.weight = jarray('int', [jcast('int', (Code05_Freezing1.MAXN << (1 & 31)))])
Code05_Freezing1.cntg = jcast('int', 0)
Code05_Freezing1.vis = jarray('boolean', [Code05_Freezing1.MAXN])
Code05_Freezing1.siz = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.edgeArr = jarray('int', [Code05_Freezing1.MAXN, 2])
Code05_Freezing1.cnte = jcast('int', 0)
Code05_Freezing1.preVal = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.preNode = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.preLen = jcast('int', 0)
Code05_Freezing1.curVal = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.curNode = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.curLen = jcast('int', 0)
Code05_Freezing1.que = jarray('int', [Code05_Freezing1.MAXN])
Code05_Freezing1.ans = jcast('int', 0)
Code05_Freezing1.ansu = jcast('int', 0)
Code05_Freezing1.ansv = jcast('int', 0)

if __name__ == '__main__':
    Code05_Freezing1.main([])

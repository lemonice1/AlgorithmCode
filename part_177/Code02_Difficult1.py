# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树的难题，Python版
# 一共有n个节点，给定n-1条边，每条边给定颜色，所有节点组成一棵树
# 颜色一共有m种，val[i]表示第i种颜色的权值，可能为负数
# 树上的一条简单路径，依次经过的边收集其颜色，可以组成一个颜色序列
# 颜色序列划分成若干个连续同色段，比如AABAACC，有4个连续同色段
# 每个连续同色段只算一次颜色权值，颜色权值的累加和作为路径的权
# 请计算边数在[limitl, limitr]范围的所有路径中，最大的权是多少
# 1 <= n、m <= 2 * 10^5
# 题目保证一定存在边数在[limitl, limitr]的路径
# 测试链接 : https://www.luogu.com.cn/problem/P3714
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Difficult1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'limitl': 'limitl', 'limitr': 'limitr', 'val': 'val', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'color': 'color', 'cntg': 'cntg', 'preTree': 'preTree', 'curTree': 'curTree', 'vis': 'vis', 'siz': 'siz', 'edgeArr': 'edgeArr', 'cnte': 'cnte', 'edgeCnt': 'edgeCnt', 'pathSum': 'pathSum', 'subtreeNode': 'subtreeNode', 'cnts': 'cnts', 'colorNode': 'colorNode', 'cntc': 'cntc', 'stack': 'stack', 'sumst': 'sumst', 'u': 'u', 'f': 'f', 'preColor': 'preColor', 'edge': 'edge', 'e': 'e', 'sum': 'sum', 'stacksize': 'stacksize'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    limitl = 0
    limitr = 0
    val = None
    head = None
    nxt = None
    to = None
    color = None
    cntg = 0
    # 之前颜色的子树形成的线段树，维护最大值信息
    preTree = None
    # 当前颜色的子树形成的线段树，维护最大值信息
    curTree = None
    vis = None
    siz = None
    # 每条边信息(连接的点，边的颜色)，根据边的颜色排序
    edgeArr = None
    cnte = 0
    edgeCnt = None
    pathSum = None
    subtreeNode = None
    cnts = 0
    colorNode = None
    cntc = 0
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    sumst = None
    u = 0
    f = 0
    preColor = 0
    edge = 0
    e = 0
    sum = 0
    stacksize = 0
    @staticmethod
    def push(u, f, preColor, edge, sum, e):
        u = jcast('int', u)
        f = jcast('int', f)
        preColor = jcast('int', preColor)
        edge = jcast('int', edge)
        sum = jcast('long', sum)
        e = jcast('int', e)
        jset(Code02_Difficult1.stack[Code02_Difficult1.stacksize], 0, u)
        jset(Code02_Difficult1.stack[Code02_Difficult1.stacksize], 1, f)
        jset(Code02_Difficult1.stack[Code02_Difficult1.stacksize], 2, preColor)
        jset(Code02_Difficult1.stack[Code02_Difficult1.stacksize], 3, edge)
        jset(Code02_Difficult1.stack[Code02_Difficult1.stacksize], 4, e)
        Code02_Difficult1.sumst[Code02_Difficult1.stacksize] = jcast('long', sum)
        Code02_Difficult1.stacksize = jcast('int', (Code02_Difficult1.stacksize + 1))

    @staticmethod
    def pop():
        Code02_Difficult1.stacksize = jcast('int', (Code02_Difficult1.stacksize - 1))
        Code02_Difficult1.u = jcast('int', Code02_Difficult1.stack[Code02_Difficult1.stacksize][0])
        Code02_Difficult1.f = jcast('int', Code02_Difficult1.stack[Code02_Difficult1.stacksize][1])
        Code02_Difficult1.preColor = jcast('int', Code02_Difficult1.stack[Code02_Difficult1.stacksize][2])
        Code02_Difficult1.edge = jcast('int', Code02_Difficult1.stack[Code02_Difficult1.stacksize][3])
        Code02_Difficult1.e = jcast('int', Code02_Difficult1.stack[Code02_Difficult1.stacksize][4])
        Code02_Difficult1.sum = jcast('long', Code02_Difficult1.sumst[Code02_Difficult1.stacksize])

    @staticmethod
    def addEdge(u, v, c):
        u = jcast('int', u)
        v = jcast('int', v)
        c = jcast('int', c)
        jset(Code02_Difficult1.nxt, ((_java_obj_1 := Code02_Difficult1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_Difficult1.head[u])
        Code02_Difficult1.to[Code02_Difficult1.cntg] = jcast('int', v)
        Code02_Difficult1.color[Code02_Difficult1.cntg] = jcast('int', c)
        Code02_Difficult1.head[u] = jcast('int', Code02_Difficult1.cntg)

    @staticmethod
    def build(tree, l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        tree[i] = jcast('long', jcast('long', (-Code02_Difficult1.INF)))
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_Difficult1.build(tree, l, mid, jcast('int', (i << (1 & 31))))
            Code02_Difficult1.build(tree, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def clear(tree, l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (tree[i] == jcast('long', (-Code02_Difficult1.INF))):
            return
        tree[i] = jcast('long', jcast('long', (-Code02_Difficult1.INF)))
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_Difficult1.clear(tree, l, mid, jcast('int', (i << (1 & 31))))
            Code02_Difficult1.clear(tree, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def update(tree, jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(tree, i, jstatic('Math', 'max', tree[i], jobv))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code02_Difficult1.update(tree, jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_Difficult1.update(tree, jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            jset(tree, i, jstatic('Math', 'max', tree[jcast('int', (i << (1 & 31)))], tree[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def query(tree, jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', tree[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('long', jcast('long', (-Code02_Difficult1.INF)))
        if (jobl <= mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code02_Difficult1.query(tree, jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('long', jstatic('Math', 'max', ans, Code02_Difficult1.query(tree, jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('long', ans)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code02_Difficult1.siz[u] = jcast('int', 1)
        e = jcast('int', Code02_Difficult1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Difficult1.to[e])
            if ((v != fa) and (not Code02_Difficult1.vis[v])):
                Code02_Difficult1.getSize1(v, u)
                Code02_Difficult1.siz[u] = jcast('int', jcast('int', jadd(Code02_Difficult1.siz[u], Code02_Difficult1.siz[v])))
            e = jcast('int', Code02_Difficult1.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code02_Difficult1.stacksize = jcast('int', 0)
        Code02_Difficult1.push(cur, fa, 0, 0, 0, jcast('int', (-1)))
        while (Code02_Difficult1.stacksize > 0):
            Code02_Difficult1.pop()
            if (Code02_Difficult1.e == jcast('int', (-1))):
                Code02_Difficult1.siz[Code02_Difficult1.u] = jcast('int', 1)
                Code02_Difficult1.e = jcast('int', Code02_Difficult1.head[Code02_Difficult1.u])
            else:
                Code02_Difficult1.e = jcast('int', Code02_Difficult1.nxt[Code02_Difficult1.e])
            if (Code02_Difficult1.e != 0):
                Code02_Difficult1.push(Code02_Difficult1.u, Code02_Difficult1.f, 0, 0, 0, Code02_Difficult1.e)
                v = jcast('int', Code02_Difficult1.to[Code02_Difficult1.e])
                if ((v != Code02_Difficult1.f) and (not Code02_Difficult1.vis[v])):
                    Code02_Difficult1.push(v, Code02_Difficult1.u, 0, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code02_Difficult1.head[Code02_Difficult1.u])
                while (ei > 0):
                    v = jcast('int', Code02_Difficult1.to[ei])
                    if ((v != Code02_Difficult1.f) and (not Code02_Difficult1.vis[v])):
                        Code02_Difficult1.siz[Code02_Difficult1.u] = jcast('int', jcast('int', jadd(Code02_Difficult1.siz[Code02_Difficult1.u], Code02_Difficult1.siz[v])))
                    ei = jcast('int', Code02_Difficult1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code02_Difficult1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code02_Difficult1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code02_Difficult1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code02_Difficult1.to[e])
                        if (((v != fa) and (not Code02_Difficult1.vis[v])) and (Code02_Difficult1.siz[v] > half)):
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
                    e = jcast('int', Code02_Difficult1.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    # 收集信息递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, preColor, edge, sum):
        u = jcast('int', u)
        fa = jcast('int', fa)
        preColor = jcast('int', preColor)
        edge = jcast('int', edge)
        sum = jcast('long', sum)
        if (edge > Code02_Difficult1.limitr):
            return
        Code02_Difficult1.edgeCnt[u] = jcast('int', edge)
        Code02_Difficult1.pathSum[u] = jcast('long', sum)
        jset(Code02_Difficult1.subtreeNode, ((_java_obj_6 := Code02_Difficult1), (_java_key_7 := 'cnts'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], u)
        e = jcast('int', Code02_Difficult1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Difficult1.to[e])
            c = jcast('int', Code02_Difficult1.color[e])
            if ((v != fa) and (not Code02_Difficult1.vis[v])):
                Code02_Difficult1.dfs1(v, u, c, jcast('int', jadd(edge, 1)), jcast('long', jadd(sum, (0 if (preColor == c) else Code02_Difficult1.val[c]))))
            e = jcast('int', Code02_Difficult1.nxt[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, pcolor, pedge, psum):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        pcolor = jcast('int', pcolor)
        pedge = jcast('int', pedge)
        psum = jcast('long', psum)
        Code02_Difficult1.stacksize = jcast('int', 0)
        Code02_Difficult1.push(cur, fa, pcolor, pedge, psum, jcast('int', (-1)))
        while (Code02_Difficult1.stacksize > 0):
            try:
                Code02_Difficult1.pop()
                if (Code02_Difficult1.e == jcast('int', (-1))):
                    if (Code02_Difficult1.edge > Code02_Difficult1.limitr):
                        raise JContinue(None)
                    Code02_Difficult1.edgeCnt[Code02_Difficult1.u] = jcast('int', Code02_Difficult1.edge)
                    Code02_Difficult1.pathSum[Code02_Difficult1.u] = jcast('long', Code02_Difficult1.sum)
                    jset(Code02_Difficult1.subtreeNode, ((_java_obj_10 := Code02_Difficult1), (_java_key_11 := 'cnts'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code02_Difficult1.u)
                    Code02_Difficult1.e = jcast('int', Code02_Difficult1.head[Code02_Difficult1.u])
                else:
                    Code02_Difficult1.e = jcast('int', Code02_Difficult1.nxt[Code02_Difficult1.e])
                if (Code02_Difficult1.e != 0):
                    Code02_Difficult1.push(Code02_Difficult1.u, Code02_Difficult1.f, Code02_Difficult1.preColor, Code02_Difficult1.edge, Code02_Difficult1.sum, Code02_Difficult1.e)
                    v = jcast('int', Code02_Difficult1.to[Code02_Difficult1.e])
                    c = jcast('int', Code02_Difficult1.color[Code02_Difficult1.e])
                    if ((v != Code02_Difficult1.f) and (not Code02_Difficult1.vis[v])):
                        Code02_Difficult1.push(v, Code02_Difficult1.u, c, jcast('int', jadd(Code02_Difficult1.edge, 1)), jcast('long', jadd(Code02_Difficult1.sum, (0 if (Code02_Difficult1.preColor == c) else Code02_Difficult1.val[c]))), jcast('int', (-1)))
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code02_Difficult1.cnte = jcast('int', 0)
        e = jcast('int', Code02_Difficult1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Difficult1.to[e])
            c = jcast('int', Code02_Difficult1.color[e])
            if (not Code02_Difficult1.vis[v]):
                jset(Code02_Difficult1.edgeArr[((_java_obj_13 := Code02_Difficult1), (_java_key_14 := 'cnte'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]], 0, v)
                jset(Code02_Difficult1.edgeArr[Code02_Difficult1.cnte], 1, c)
            e = jcast('int', Code02_Difficult1.nxt[e])
        jstatic('Arrays', 'sort', Code02_Difficult1.edgeArr, 1, jcast('int', jadd(Code02_Difficult1.cnte, 1)), (lambda a, b: (a[1] - b[1])))
        Code02_Difficult1.update(Code02_Difficult1.preTree, 0, 0, 0, Code02_Difficult1.n, 1)
        ans = jcast('long', jcast('long', (-Code02_Difficult1.INF)))
        Code02_Difficult1.cntc = jcast('int', 0)
        k = jcast('int', 1)
        while (k <= Code02_Difficult1.cnte):
            v = jcast('int', Code02_Difficult1.edgeArr[k][0])
            c = jcast('int', Code02_Difficult1.edgeArr[k][1])
            if ((k > 1) and (Code02_Difficult1.edgeArr[jcast('int', (k - 1))][1] != c)):
                Code02_Difficult1.clear(Code02_Difficult1.curTree, 0, Code02_Difficult1.n, 1)
                i = jcast('int', 1)
                while (i <= Code02_Difficult1.cntc):
                    node = jcast('int', Code02_Difficult1.colorNode[i])
                    Code02_Difficult1.update(Code02_Difficult1.preTree, Code02_Difficult1.edgeCnt[node], Code02_Difficult1.pathSum[node], 0, Code02_Difficult1.n, 1)
                    i = jcast('int', (i + 1))
                Code02_Difficult1.cntc = jcast('int', 0)
            Code02_Difficult1.cnts = jcast('int', 0)
            # dfs1(v, u, c, 1, val[c]);
            Code02_Difficult1.dfs2(v, u, c, 1, Code02_Difficult1.val[c])
            i = jcast('int', 1)
            while (i <= Code02_Difficult1.cnts):
                node = jcast('int', Code02_Difficult1.subtreeNode[i])
                l = jcast('int', jstatic('Math', 'max', 0, jcast('int', (Code02_Difficult1.limitl - Code02_Difficult1.edgeCnt[node]))))
                r = jcast('int', jcast('int', (Code02_Difficult1.limitr - Code02_Difficult1.edgeCnt[node])))
                ans = jcast('long', jstatic('Math', 'max', ans, jcast('long', jadd(Code02_Difficult1.query(Code02_Difficult1.preTree, l, r, 0, Code02_Difficult1.n, 1), Code02_Difficult1.pathSum[node]))))
                ans = jcast('long', jstatic('Math', 'max', ans, jcast('long', (jcast('long', jadd(Code02_Difficult1.query(Code02_Difficult1.curTree, l, r, 0, Code02_Difficult1.n, 1), Code02_Difficult1.pathSum[node])) - Code02_Difficult1.val[c]))))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code02_Difficult1.cnts):
                node = jcast('int', Code02_Difficult1.subtreeNode[i])
                jset(Code02_Difficult1.colorNode, ((_java_obj_16 := Code02_Difficult1), (_java_key_17 := 'cntc'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], node)
                Code02_Difficult1.update(Code02_Difficult1.curTree, Code02_Difficult1.edgeCnt[node], Code02_Difficult1.pathSum[node], 0, Code02_Difficult1.n, 1)
                i = jcast('int', (i + 1))
            k = jcast('int', (k + 1))
        Code02_Difficult1.clear(Code02_Difficult1.preTree, 0, Code02_Difficult1.n, 1)
        Code02_Difficult1.clear(Code02_Difficult1.curTree, 0, Code02_Difficult1.n, 1)
        return jcast('long', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code02_Difficult1.vis[u] = jcast('boolean', True)
        ans = jcast('long', Code02_Difficult1.calc(u))
        e = jcast('int', Code02_Difficult1.head[u])
        while (e > 0):
            v = jcast('int', Code02_Difficult1.to[e])
            if (not Code02_Difficult1.vis[v]):
                ans = jcast('long', jstatic('Math', 'max', ans, Code02_Difficult1.solve(Code02_Difficult1.getCentroid(v, u))))
            e = jcast('int', Code02_Difficult1.nxt[e])
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code02_Difficult1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Difficult1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Difficult1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_Difficult1.limitl = jcast('int', jcall(in_, 'nextInt'))
        Code02_Difficult1.limitr = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Difficult1.m):
            jset(Code02_Difficult1.val, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        c = 0
        while (i < Code02_Difficult1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            Code02_Difficult1.addEdge(u, v, c)
            Code02_Difficult1.addEdge(v, u, c)
            i = jcast('int', (i + 1))
        Code02_Difficult1.build(Code02_Difficult1.preTree, 0, Code02_Difficult1.n, 1)
        Code02_Difficult1.build(Code02_Difficult1.curTree, 0, Code02_Difficult1.n, 1)
        jcall(out, 'println', Code02_Difficult1.solve(Code02_Difficult1.getCentroid(1, 0)))
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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
            raise TypeError("No matching overload for Code02_Difficult1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Difficult1.MAXN = jcast('int', 200001)
Code02_Difficult1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code02_Difficult1.n = jcast('int', 0)
Code02_Difficult1.m = jcast('int', 0)
Code02_Difficult1.limitl = jcast('int', 0)
Code02_Difficult1.limitr = jcast('int', 0)
Code02_Difficult1.val = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.head = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.nxt = jarray('int', [jcast('int', (Code02_Difficult1.MAXN << (1 & 31)))])
Code02_Difficult1.to = jarray('int', [jcast('int', (Code02_Difficult1.MAXN << (1 & 31)))])
Code02_Difficult1.color = jarray('int', [jcast('int', (Code02_Difficult1.MAXN << (1 & 31)))])
Code02_Difficult1.cntg = jcast('int', 0)
Code02_Difficult1.preTree = jarray('long', [jcast('int', (Code02_Difficult1.MAXN << (2 & 31)))])
Code02_Difficult1.curTree = jarray('long', [jcast('int', (Code02_Difficult1.MAXN << (2 & 31)))])
Code02_Difficult1.vis = jarray('boolean', [Code02_Difficult1.MAXN])
Code02_Difficult1.siz = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.edgeArr = jarray('int', [Code02_Difficult1.MAXN, 2])
Code02_Difficult1.cnte = jcast('int', 0)
Code02_Difficult1.edgeCnt = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.pathSum = jarray('long', [Code02_Difficult1.MAXN])
Code02_Difficult1.subtreeNode = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.cnts = jcast('int', 0)
Code02_Difficult1.colorNode = jarray('int', [Code02_Difficult1.MAXN])
Code02_Difficult1.cntc = jcast('int', 0)
Code02_Difficult1.stack = jarray('int', [Code02_Difficult1.MAXN, 5])
Code02_Difficult1.sumst = jarray('long', [Code02_Difficult1.MAXN])
Code02_Difficult1.u = jcast('int', 0)
Code02_Difficult1.f = jcast('int', 0)
Code02_Difficult1.preColor = jcast('int', 0)
Code02_Difficult1.edge = jcast('int', 0)
Code02_Difficult1.e = jcast('int', 0)
Code02_Difficult1.sum = jcast('long', 0)
Code02_Difficult1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code02_Difficult1.main([])

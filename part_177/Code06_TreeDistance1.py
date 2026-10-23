# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 支配点对距离，Python版
# 一共有n个节点，给定n-1条边，每条边给定边权，所有节点组成一棵树
# 节点i到节点j的简单路径，边权的累加和，定义为dist(i, j)
# 编号区间[x, y]，考虑所有点对(a, b)，要求 x <= a < b <= y
# 如果dist(a, b)是所有情况中最小的，则称(a, b)为区间[x, y]的支配点对
# 也可以说，区间[x, y]的支配点对距离为dist(a, b)
# 特别的，如果x == y，那么不存在满足要求的点对，此时支配点对距离为-1
# 一共有m次查询，格式 x y : 保证x <= y，打印[x, y]的支配点对距离
# 1 <= n <= 2 * 10^5    1 <= m <= 10^6    1 <= 边权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P9678
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_TreeDistance1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'm': 'm', 'qx': 'qx', 'qy': 'qy', 'qid': 'qid', 'pa': 'pa', 'pb': 'pb', 'pdist': 'pdist', 'cntp': 'cntp', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'dist': 'dist', 'nodeArr': 'nodeArr', 'cnta': 'cnta', 'sta': 'sta', 'top': 'top', 'minTree': 'minTree', 'ans': 'ans', 'stack': 'stack', 'distst': 'distst', 'u': 'u', 'f': 'f', 'e': 'e', 'dis': 'dis', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXM = 0
    MAXP = 0
    INF = 0
    n = 0
    m = 0
    # 所有查询
    qx = None
    qy = None
    qid = None
    # 保留的点对
    pa = None
    pb = None
    pdist = None
    cntp = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    dist = None
    nodeArr = None
    cnta = 0
    # 单调栈
    sta = None
    top = 0
    # 维护最小值的线段树
    minTree = None
    # 查询的答案
    ans = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    distst = None
    u = 0
    f = 0
    e = 0
    dis = 0
    stacksize = 0
    @staticmethod
    def push(u, f, dis, e):
        u = jcast('int', u)
        f = jcast('int', f)
        dis = jcast('long', dis)
        e = jcast('int', e)
        jset(Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize], 0, u)
        jset(Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize], 1, f)
        jset(Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize], 2, e)
        Code06_TreeDistance1.distst[Code06_TreeDistance1.stacksize] = jcast('long', dis)
        Code06_TreeDistance1.stacksize = jcast('int', (Code06_TreeDistance1.stacksize + 1))

    @staticmethod
    def pop():
        Code06_TreeDistance1.stacksize = jcast('int', (Code06_TreeDistance1.stacksize - 1))
        Code06_TreeDistance1.u = jcast('int', Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize][0])
        Code06_TreeDistance1.f = jcast('int', Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize][1])
        Code06_TreeDistance1.e = jcast('int', Code06_TreeDistance1.stack[Code06_TreeDistance1.stacksize][2])
        Code06_TreeDistance1.dis = jcast('long', Code06_TreeDistance1.distst[Code06_TreeDistance1.stacksize])

    # 所有查询根据y从小到大排序，这里使用双指针快排完成排序
    @staticmethod
    def sortQuery(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code06_TreeDistance1.qy[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (Code06_TreeDistance1.qy[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code06_TreeDistance1.qy[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', Code06_TreeDistance1.qx[i])
                Code06_TreeDistance1.qx[i] = jcast('int', Code06_TreeDistance1.qx[j])
                Code06_TreeDistance1.qx[j] = jcast('int', tmp)
                tmp = jcast('int', Code06_TreeDistance1.qy[i])
                Code06_TreeDistance1.qy[i] = jcast('int', Code06_TreeDistance1.qy[j])
                Code06_TreeDistance1.qy[j] = jcast('int', tmp)
                tmp = jcast('int', Code06_TreeDistance1.qid[i])
                Code06_TreeDistance1.qid[i] = jcast('int', Code06_TreeDistance1.qid[j])
                Code06_TreeDistance1.qid[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code06_TreeDistance1.sortQuery(l, j)
        Code06_TreeDistance1.sortQuery(i, r)

    # 所有点对根据b从小到大排序，这里使用双指针快排完成排序
    @staticmethod
    def sortPair(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code06_TreeDistance1.pb[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        t1 = 0
        t2 = 0
        while (i <= j):
            while (Code06_TreeDistance1.pb[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code06_TreeDistance1.pb[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                t1 = jcast('int', Code06_TreeDistance1.pa[i])
                Code06_TreeDistance1.pa[i] = jcast('int', Code06_TreeDistance1.pa[j])
                Code06_TreeDistance1.pa[j] = jcast('int', t1)
                t1 = jcast('int', Code06_TreeDistance1.pb[i])
                Code06_TreeDistance1.pb[i] = jcast('int', Code06_TreeDistance1.pb[j])
                Code06_TreeDistance1.pb[j] = jcast('int', t1)
                t2 = jcast('long', Code06_TreeDistance1.pdist[i])
                Code06_TreeDistance1.pdist[i] = jcast('long', Code06_TreeDistance1.pdist[j])
                Code06_TreeDistance1.pdist[j] = jcast('long', t2)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code06_TreeDistance1.sortPair(l, j)
        Code06_TreeDistance1.sortPair(i, r)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_TreeDistance1.nxt, ((_java_obj_1 := Code06_TreeDistance1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_TreeDistance1.head[u])
        Code06_TreeDistance1.to[Code06_TreeDistance1.cntg] = jcast('int', v)
        Code06_TreeDistance1.weight[Code06_TreeDistance1.cntg] = jcast('int', w)
        Code06_TreeDistance1.head[u] = jcast('int', Code06_TreeDistance1.cntg)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_TreeDistance1.siz[u] = jcast('int', 1)
        e = jcast('int', Code06_TreeDistance1.head[u])
        while (e > 0):
            v = jcast('int', Code06_TreeDistance1.to[e])
            if ((v != fa) and (not Code06_TreeDistance1.vis[v])):
                Code06_TreeDistance1.getSize1(v, u)
                Code06_TreeDistance1.siz[u] = jcast('int', jcast('int', jadd(Code06_TreeDistance1.siz[u], Code06_TreeDistance1.siz[v])))
            e = jcast('int', Code06_TreeDistance1.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code06_TreeDistance1.stacksize = jcast('int', 0)
        Code06_TreeDistance1.push(cur, fa, 0, jcast('int', (-1)))
        while (Code06_TreeDistance1.stacksize > 0):
            Code06_TreeDistance1.pop()
            if (Code06_TreeDistance1.e == jcast('int', (-1))):
                Code06_TreeDistance1.siz[Code06_TreeDistance1.u] = jcast('int', 1)
                Code06_TreeDistance1.e = jcast('int', Code06_TreeDistance1.head[Code06_TreeDistance1.u])
            else:
                Code06_TreeDistance1.e = jcast('int', Code06_TreeDistance1.nxt[Code06_TreeDistance1.e])
            if (Code06_TreeDistance1.e != 0):
                Code06_TreeDistance1.push(Code06_TreeDistance1.u, Code06_TreeDistance1.f, 0, Code06_TreeDistance1.e)
                v = jcast('int', Code06_TreeDistance1.to[Code06_TreeDistance1.e])
                if ((v != Code06_TreeDistance1.f) and (not Code06_TreeDistance1.vis[v])):
                    Code06_TreeDistance1.push(v, Code06_TreeDistance1.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code06_TreeDistance1.head[Code06_TreeDistance1.u])
                while (ei > 0):
                    v = jcast('int', Code06_TreeDistance1.to[ei])
                    if ((v != Code06_TreeDistance1.f) and (not Code06_TreeDistance1.vis[v])):
                        Code06_TreeDistance1.siz[Code06_TreeDistance1.u] = jcast('int', jcast('int', jadd(Code06_TreeDistance1.siz[Code06_TreeDistance1.u], Code06_TreeDistance1.siz[v])))
                    ei = jcast('int', Code06_TreeDistance1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code06_TreeDistance1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code06_TreeDistance1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code06_TreeDistance1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code06_TreeDistance1.to[e])
                        if (((v != fa) and (not Code06_TreeDistance1.vis[v])) and (Code06_TreeDistance1.siz[v] > half)):
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
                    e = jcast('int', Code06_TreeDistance1.nxt[e])
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
    def dfs1(u, fa, dis):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('long', dis)
        Code06_TreeDistance1.dist[u] = jcast('long', dis)
        jset(Code06_TreeDistance1.nodeArr, ((_java_obj_6 := Code06_TreeDistance1), (_java_key_7 := 'cnta'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], u)
        e = jcast('int', Code06_TreeDistance1.head[u])
        while (e > 0):
            v = jcast('int', Code06_TreeDistance1.to[e])
            w = jcast('int', Code06_TreeDistance1.weight[e])
            if ((v != fa) and (not Code06_TreeDistance1.vis[v])):
                Code06_TreeDistance1.dfs1(v, u, jcast('long', jadd(dis, w)))
            e = jcast('int', Code06_TreeDistance1.nxt[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, d):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        d = jcast('long', d)
        Code06_TreeDistance1.stacksize = jcast('int', 0)
        Code06_TreeDistance1.push(cur, fa, d, jcast('int', (-1)))
        while (Code06_TreeDistance1.stacksize > 0):
            Code06_TreeDistance1.pop()
            if (Code06_TreeDistance1.e == jcast('int', (-1))):
                Code06_TreeDistance1.dist[Code06_TreeDistance1.u] = jcast('long', Code06_TreeDistance1.dis)
                jset(Code06_TreeDistance1.nodeArr, ((_java_obj_9 := Code06_TreeDistance1), (_java_key_10 := 'cnta'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], Code06_TreeDistance1.u)
                Code06_TreeDistance1.e = jcast('int', Code06_TreeDistance1.head[Code06_TreeDistance1.u])
            else:
                Code06_TreeDistance1.e = jcast('int', Code06_TreeDistance1.nxt[Code06_TreeDistance1.e])
            if (Code06_TreeDistance1.e != 0):
                Code06_TreeDistance1.push(Code06_TreeDistance1.u, Code06_TreeDistance1.f, Code06_TreeDistance1.dis, Code06_TreeDistance1.e)
                v = jcast('int', Code06_TreeDistance1.to[Code06_TreeDistance1.e])
                w = jcast('int', Code06_TreeDistance1.weight[Code06_TreeDistance1.e])
                if ((v != Code06_TreeDistance1.f) and (not Code06_TreeDistance1.vis[v])):
                    Code06_TreeDistance1.push(v, Code06_TreeDistance1.u, jcast('long', jadd(Code06_TreeDistance1.dis, w)), jcast('int', (-1)))

    @staticmethod
    def stackAdd(cur):
        cur = jcast('int', cur)
        while ((Code06_TreeDistance1.top > 0) and (Code06_TreeDistance1.dist[Code06_TreeDistance1.sta[Code06_TreeDistance1.top]] >= Code06_TreeDistance1.dist[cur])):
            jset(Code06_TreeDistance1.pa, ((_java_obj_12 := Code06_TreeDistance1), (_java_key_13 := 'cntp'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3], jstatic('Math', 'min', Code06_TreeDistance1.sta[Code06_TreeDistance1.top], cur))
            jset(Code06_TreeDistance1.pb, Code06_TreeDistance1.cntp, jstatic('Math', 'max', Code06_TreeDistance1.sta[Code06_TreeDistance1.top], cur))
            Code06_TreeDistance1.pdist[Code06_TreeDistance1.cntp] = jcast('long', jcast('long', jadd(Code06_TreeDistance1.dist[Code06_TreeDistance1.sta[Code06_TreeDistance1.top]], Code06_TreeDistance1.dist[cur])))
            Code06_TreeDistance1.top = jcast('int', (Code06_TreeDistance1.top - 1))
        jset(Code06_TreeDistance1.sta, ((_java_obj_15 := Code06_TreeDistance1), (_java_key_16 := 'top'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3], cur)

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code06_TreeDistance1.cnta = jcast('int', 0)
        # dfs1(u, 0, 0);
        Code06_TreeDistance1.dfs2(u, 0, 0)
        jstatic('Arrays', 'sort', Code06_TreeDistance1.nodeArr, 1, jcast('int', jadd(Code06_TreeDistance1.cnta, 1)))
        Code06_TreeDistance1.top = jcast('int', 0)
        # 所有点的编号，从左往右遍历
        # 找右侧最近的、距离 <= dist的点，去生成点对
        i = jcast('int', 1)
        while (i <= Code06_TreeDistance1.cnta):
            Code06_TreeDistance1.stackAdd(Code06_TreeDistance1.nodeArr[i])
            i = jcast('int', (i + 1))
        Code06_TreeDistance1.top = jcast('int', 0)
        # 所有点的编号，从右往左遍历
        # 找左侧最近的、距离 <= dist的点，去生成点对
        i = jcast('int', Code06_TreeDistance1.cnta)
        while (i >= 1):
            Code06_TreeDistance1.stackAdd(Code06_TreeDistance1.nodeArr[i])
            i = jcast('int', (i - 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code06_TreeDistance1.vis[u] = jcast('boolean', True)
        Code06_TreeDistance1.calc(u)
        e = jcast('int', Code06_TreeDistance1.head[u])
        while (e > 0):
            v = jcast('int', Code06_TreeDistance1.to[e])
            if (not Code06_TreeDistance1.vis[v]):
                Code06_TreeDistance1.solve(Code06_TreeDistance1.getCentroid(v, u))
            e = jcast('int', Code06_TreeDistance1.nxt[e])

    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code06_TreeDistance1.minTree, i, jstatic('Math', 'min', Code06_TreeDistance1.minTree[jcast('int', (i << (1 & 31)))], Code06_TreeDistance1.minTree[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code06_TreeDistance1.minTree[i] = jcast('long', Code06_TreeDistance1.INF)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_TreeDistance1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_TreeDistance1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_TreeDistance1.up(i)

    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code06_TreeDistance1.minTree, i, jstatic('Math', 'min', Code06_TreeDistance1.minTree[i], jobv))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code06_TreeDistance1.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code06_TreeDistance1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_TreeDistance1.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code06_TreeDistance1.minTree[i])
        ans = jcast('long', Code06_TreeDistance1.INF)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobl <= mid):
            ans = jcast('long', jstatic('Math', 'min', ans, Code06_TreeDistance1.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('long', jstatic('Math', 'min', ans, Code06_TreeDistance1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('long', ans)

    @staticmethod
    def compute():
        Code06_TreeDistance1.solve(Code06_TreeDistance1.getCentroid(1, 0))
        Code06_TreeDistance1.sortQuery(1, Code06_TreeDistance1.m)
        Code06_TreeDistance1.sortPair(1, Code06_TreeDistance1.cntp)
        Code06_TreeDistance1.build(1, Code06_TreeDistance1.n, 1)
        i = jcast('int', 1)
        j = jcast('int', 1)
        while (i <= Code06_TreeDistance1.m):
            while ((j <= Code06_TreeDistance1.cntp) and (Code06_TreeDistance1.pb[j] <= Code06_TreeDistance1.qy[i])):
                Code06_TreeDistance1.update(Code06_TreeDistance1.pa[j], Code06_TreeDistance1.pdist[j], 1, Code06_TreeDistance1.n, 1)
                j = jcast('int', (j + 1))
            if (Code06_TreeDistance1.qx[i] == Code06_TreeDistance1.qy[i]):
                jset(Code06_TreeDistance1.ans, Code06_TreeDistance1.qid[i], jcast('int', (-1)))
            else:
                jset(Code06_TreeDistance1.ans, Code06_TreeDistance1.qid[i], Code06_TreeDistance1.query(Code06_TreeDistance1.qx[i], Code06_TreeDistance1.qy[i], 1, Code06_TreeDistance1.n, 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code06_TreeDistance1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_TreeDistance1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code06_TreeDistance1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code06_TreeDistance1.addEdge(u, v, w)
            Code06_TreeDistance1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code06_TreeDistance1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_TreeDistance1.m):
            jset(Code06_TreeDistance1.qx, i, jcall(in_, 'nextInt'))
            jset(Code06_TreeDistance1.qy, i, jcall(in_, 'nextInt'))
            Code06_TreeDistance1.qid[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code06_TreeDistance1.compute()
        i = jcast('int', 1)
        while (i <= Code06_TreeDistance1.m):
            jcall(out, 'println', Code06_TreeDistance1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_18 := self), (_java_key_19 := 'ptr'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))), _java_old_20)[4]])

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
            raise TypeError("No matching overload for Code06_TreeDistance1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_TreeDistance1.MAXN = jcast('int', 200001)
Code06_TreeDistance1.MAXM = jcast('int', 1000001)
Code06_TreeDistance1.MAXP = jcast('int', 10000001)
Code06_TreeDistance1.INF = jcast('long', jcast('long', (1 << (60 & 63))))
Code06_TreeDistance1.n = jcast('int', 0)
Code06_TreeDistance1.m = jcast('int', 0)
Code06_TreeDistance1.qx = jarray('int', [Code06_TreeDistance1.MAXM])
Code06_TreeDistance1.qy = jarray('int', [Code06_TreeDistance1.MAXM])
Code06_TreeDistance1.qid = jarray('int', [Code06_TreeDistance1.MAXM])
Code06_TreeDistance1.pa = jarray('int', [Code06_TreeDistance1.MAXP])
Code06_TreeDistance1.pb = jarray('int', [Code06_TreeDistance1.MAXP])
Code06_TreeDistance1.pdist = jarray('long', [Code06_TreeDistance1.MAXP])
Code06_TreeDistance1.cntp = jcast('int', 0)
Code06_TreeDistance1.head = jarray('int', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.nxt = jarray('int', [jcast('int', (Code06_TreeDistance1.MAXN << (1 & 31)))])
Code06_TreeDistance1.to = jarray('int', [jcast('int', (Code06_TreeDistance1.MAXN << (1 & 31)))])
Code06_TreeDistance1.weight = jarray('int', [jcast('int', (Code06_TreeDistance1.MAXN << (1 & 31)))])
Code06_TreeDistance1.cntg = jcast('int', 0)
Code06_TreeDistance1.vis = jarray('boolean', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.siz = jarray('int', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.dist = jarray('long', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.nodeArr = jarray('int', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.cnta = jcast('int', 0)
Code06_TreeDistance1.sta = jarray('int', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.top = jcast('int', 0)
Code06_TreeDistance1.minTree = jarray('long', [jcast('int', (Code06_TreeDistance1.MAXN << (2 & 31)))])
Code06_TreeDistance1.ans = jarray('long', [Code06_TreeDistance1.MAXM])
Code06_TreeDistance1.stack = jarray('int', [Code06_TreeDistance1.MAXN, 3])
Code06_TreeDistance1.distst = jarray('long', [Code06_TreeDistance1.MAXN])
Code06_TreeDistance1.u = jcast('int', 0)
Code06_TreeDistance1.f = jcast('int', 0)
Code06_TreeDistance1.e = jcast('int', 0)
Code06_TreeDistance1.dis = jcast('long', 0)
Code06_TreeDistance1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_TreeDistance1.main([])

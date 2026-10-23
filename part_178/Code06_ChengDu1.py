# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 成都七中，Python版
# 树上有n个点，每个点给定颜色，给定n-1条边
# 一共m条查询，查询之间不会相互影响，格式如下
# 查询 l r x : 只保留编号在[l, r]的节点，打印点x所在连通块的颜色数量
# 1 <= 所有数据 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5311
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_ChengDu1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'color': 'color', 'headg': 'headg', 'nxtg': 'nxtg', 'tog': 'tog', 'cntg': 'cntg', 'headq': 'headq', 'nxtq': 'nxtq', 'ql': 'ql', 'qr': 'qr', 'qid': 'qid', 'cntq': 'cntq', 'vis': 'vis', 'siz': 'siz', 'nodel': 'nodel', 'noder': 'noder', 'ncolor': 'ncolor', 'cntNode': 'cntNode', 'quesl': 'quesl', 'quesr': 'quesr', 'quesid': 'quesid', 'cntQues': 'cntQues', 'pos': 'pos', 'tree': 'tree', 'ans': 'ans', 'stack': 'stack', 'u': 'u', 'f': 'f', 'nl': 'nl', 'nr': 'nr', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    m = 0
    color = None
    # 建树
    headg = None
    nxtg = None
    tog = None
    cntg = 0
    # 每个节点的问题列表
    headq = None
    nxtq = None
    ql = None
    qr = None
    qid = None
    cntq = 0
    # 点分治
    vis = None
    siz = None
    # 每来到一个重心，收集节点列表，nodel和noder是解锁条件，ncolor是节点颜色
    nodel = None
    noder = None
    ncolor = None
    cntNode = 0
    # 每来到一个重心，收集问题列表，只收集值得讨论的问题
    quesl = None
    quesr = None
    quesid = None
    cntQues = 0
    # pos[v] = i，表示颜色v的左边界，最右位置出现在i
    pos = None
    # 树状数组
    tree = None
    # 问题答案
    ans = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    nl = 0
    nr = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, nl, nr, e):
        u = jcast('int', u)
        f = jcast('int', f)
        nl = jcast('int', nl)
        nr = jcast('int', nr)
        e = jcast('int', e)
        jset(Code06_ChengDu1.stack[Code06_ChengDu1.stacksize], 0, u)
        jset(Code06_ChengDu1.stack[Code06_ChengDu1.stacksize], 1, f)
        jset(Code06_ChengDu1.stack[Code06_ChengDu1.stacksize], 2, nl)
        jset(Code06_ChengDu1.stack[Code06_ChengDu1.stacksize], 3, nr)
        jset(Code06_ChengDu1.stack[Code06_ChengDu1.stacksize], 4, e)
        Code06_ChengDu1.stacksize = jcast('int', (Code06_ChengDu1.stacksize + 1))

    @staticmethod
    def pop():
        Code06_ChengDu1.stacksize = jcast('int', (Code06_ChengDu1.stacksize - 1))
        Code06_ChengDu1.u = jcast('int', Code06_ChengDu1.stack[Code06_ChengDu1.stacksize][0])
        Code06_ChengDu1.f = jcast('int', Code06_ChengDu1.stack[Code06_ChengDu1.stacksize][1])
        Code06_ChengDu1.nl = jcast('int', Code06_ChengDu1.stack[Code06_ChengDu1.stacksize][2])
        Code06_ChengDu1.nr = jcast('int', Code06_ChengDu1.stack[Code06_ChengDu1.stacksize][3])
        Code06_ChengDu1.e = jcast('int', Code06_ChengDu1.stack[Code06_ChengDu1.stacksize][4])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code06_ChengDu1.nxtg, ((_java_obj_1 := Code06_ChengDu1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_ChengDu1.headg[u])
        Code06_ChengDu1.tog[Code06_ChengDu1.cntg] = jcast('int', v)
        Code06_ChengDu1.headg[u] = jcast('int', Code06_ChengDu1.cntg)

    @staticmethod
    def addQuery(u, l, r, id):
        u = jcast('int', u)
        l = jcast('int', l)
        r = jcast('int', r)
        id = jcast('int', id)
        jset(Code06_ChengDu1.nxtq, ((_java_obj_4 := Code06_ChengDu1), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_ChengDu1.headq[u])
        Code06_ChengDu1.ql[Code06_ChengDu1.cntq] = jcast('int', l)
        Code06_ChengDu1.qr[Code06_ChengDu1.cntq] = jcast('int', r)
        Code06_ChengDu1.qid[Code06_ChengDu1.cntq] = jcast('int', id)
        Code06_ChengDu1.headq[u] = jcast('int', Code06_ChengDu1.cntq)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (i <= 0):
            return
        while (i <= Code06_ChengDu1.n):
            Code06_ChengDu1.tree[i] = jcast('int', jcast('int', jadd(Code06_ChengDu1.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code06_ChengDu1.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code06_ChengDu1.tree[i])))
            i = jcast('int', jcast('int', (i - Code06_ChengDu1.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code06_ChengDu1.sum(r) - Code06_ChengDu1.sum(jcast('int', (l - 1))))))

    # 找重心需要计算子树大小的递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code06_ChengDu1.siz[u] = jcast('int', 1)
        e = jcast('int', Code06_ChengDu1.headg[u])
        while (e > 0):
            v = jcast('int', Code06_ChengDu1.tog[e])
            if ((v != fa) and (not Code06_ChengDu1.vis[v])):
                Code06_ChengDu1.getSize1(v, u)
                Code06_ChengDu1.siz[u] = jcast('int', jcast('int', jadd(Code06_ChengDu1.siz[u], Code06_ChengDu1.siz[v])))
            e = jcast('int', Code06_ChengDu1.nxtg[e])

    # getSize1的迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code06_ChengDu1.stacksize = jcast('int', 0)
        Code06_ChengDu1.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code06_ChengDu1.stacksize > 0):
            Code06_ChengDu1.pop()
            if (Code06_ChengDu1.e == jcast('int', (-1))):
                Code06_ChengDu1.siz[Code06_ChengDu1.u] = jcast('int', 1)
                Code06_ChengDu1.e = jcast('int', Code06_ChengDu1.headg[Code06_ChengDu1.u])
            else:
                Code06_ChengDu1.e = jcast('int', Code06_ChengDu1.nxtg[Code06_ChengDu1.e])
            if (Code06_ChengDu1.e != 0):
                Code06_ChengDu1.push(Code06_ChengDu1.u, Code06_ChengDu1.f, 0, 0, Code06_ChengDu1.e)
                v = jcast('int', Code06_ChengDu1.tog[Code06_ChengDu1.e])
                if ((v != Code06_ChengDu1.f) and (not Code06_ChengDu1.vis[v])):
                    Code06_ChengDu1.push(v, Code06_ChengDu1.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code06_ChengDu1.headg[Code06_ChengDu1.u])
                while (ei > 0):
                    v = jcast('int', Code06_ChengDu1.tog[ei])
                    if ((v != Code06_ChengDu1.f) and (not Code06_ChengDu1.vis[v])):
                        Code06_ChengDu1.siz[Code06_ChengDu1.u] = jcast('int', jcast('int', jadd(Code06_ChengDu1.siz[Code06_ChengDu1.u], Code06_ChengDu1.siz[v])))
                    ei = jcast('int', Code06_ChengDu1.nxtg[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code06_ChengDu1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code06_ChengDu1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code06_ChengDu1.headg[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code06_ChengDu1.tog[e])
                        if (((v != fa) and (not Code06_ChengDu1.vis[v])) and (Code06_ChengDu1.siz[v] > half)):
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
                    e = jcast('int', Code06_ChengDu1.nxtg[e])
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs1(u, fa, nl, nr):
        u = jcast('int', u)
        fa = jcast('int', fa)
        nl = jcast('int', nl)
        nr = jcast('int', nr)
        jset(Code06_ChengDu1.nodel, ((_java_obj_9 := Code06_ChengDu1), (_java_key_10 := 'cntNode'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], nl)
        Code06_ChengDu1.noder[Code06_ChengDu1.cntNode] = jcast('int', nr)
        Code06_ChengDu1.ncolor[Code06_ChengDu1.cntNode] = jcast('int', Code06_ChengDu1.color[u])
        ei = jcast('int', Code06_ChengDu1.headq[u])
        while (ei > 0):
            if ((Code06_ChengDu1.ql[ei] <= nl) and (nr <= Code06_ChengDu1.qr[ei])):
                jset(Code06_ChengDu1.quesl, ((_java_obj_12 := Code06_ChengDu1), (_java_key_13 := 'cntQues'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))))[3], Code06_ChengDu1.ql[ei])
                Code06_ChengDu1.quesr[Code06_ChengDu1.cntQues] = jcast('int', Code06_ChengDu1.qr[ei])
                Code06_ChengDu1.quesid[Code06_ChengDu1.cntQues] = jcast('int', Code06_ChengDu1.qid[ei])
            ei = jcast('int', Code06_ChengDu1.nxtq[ei])
        e = jcast('int', Code06_ChengDu1.headg[u])
        while (e > 0):
            v = jcast('int', Code06_ChengDu1.tog[e])
            if ((v != fa) and (not Code06_ChengDu1.vis[v])):
                Code06_ChengDu1.dfs1(v, u, jstatic('Math', 'min', v, nl), jstatic('Math', 'max', v, nr))
            e = jcast('int', Code06_ChengDu1.nxtg[e])

    # dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa, nodeMin, nodeMax):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        nodeMin = jcast('int', nodeMin)
        nodeMax = jcast('int', nodeMax)
        Code06_ChengDu1.stacksize = jcast('int', 0)
        Code06_ChengDu1.push(cur, fa, nodeMin, nodeMax, jcast('int', (-1)))
        while (Code06_ChengDu1.stacksize > 0):
            Code06_ChengDu1.pop()
            if (Code06_ChengDu1.e == jcast('int', (-1))):
                jset(Code06_ChengDu1.nodel, ((_java_obj_15 := Code06_ChengDu1), (_java_key_16 := 'cntNode'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3], Code06_ChengDu1.nl)
                Code06_ChengDu1.noder[Code06_ChengDu1.cntNode] = jcast('int', Code06_ChengDu1.nr)
                Code06_ChengDu1.ncolor[Code06_ChengDu1.cntNode] = jcast('int', Code06_ChengDu1.color[Code06_ChengDu1.u])
                ei = jcast('int', Code06_ChengDu1.headq[Code06_ChengDu1.u])
                while (ei > 0):
                    if ((Code06_ChengDu1.ql[ei] <= Code06_ChengDu1.nl) and (Code06_ChengDu1.nr <= Code06_ChengDu1.qr[ei])):
                        jset(Code06_ChengDu1.quesl, ((_java_obj_18 := Code06_ChengDu1), (_java_key_19 := 'cntQues'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3], Code06_ChengDu1.ql[ei])
                        Code06_ChengDu1.quesr[Code06_ChengDu1.cntQues] = jcast('int', Code06_ChengDu1.qr[ei])
                        Code06_ChengDu1.quesid[Code06_ChengDu1.cntQues] = jcast('int', Code06_ChengDu1.qid[ei])
                    ei = jcast('int', Code06_ChengDu1.nxtq[ei])
                Code06_ChengDu1.e = jcast('int', Code06_ChengDu1.headg[Code06_ChengDu1.u])
            else:
                Code06_ChengDu1.e = jcast('int', Code06_ChengDu1.nxtg[Code06_ChengDu1.e])
            if (Code06_ChengDu1.e != 0):
                Code06_ChengDu1.push(Code06_ChengDu1.u, Code06_ChengDu1.f, Code06_ChengDu1.nl, Code06_ChengDu1.nr, Code06_ChengDu1.e)
                v = jcast('int', Code06_ChengDu1.tog[Code06_ChengDu1.e])
                if ((v != Code06_ChengDu1.f) and (not Code06_ChengDu1.vis[v])):
                    Code06_ChengDu1.push(v, Code06_ChengDu1.u, jstatic('Math', 'min', v, Code06_ChengDu1.nl), jstatic('Math', 'max', v, Code06_ChengDu1.nr), jcast('int', (-1)))

    @staticmethod
    def sort(al, ar, ai, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', ar[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        tmp = 0
        while (i <= j):
            while (ar[i] < pivot):
                i = jcast('int', (i + 1))
            while (ar[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                tmp = jcast('int', al[i])
                al[i] = jcast('int', al[j])
                al[j] = jcast('int', tmp)
                tmp = jcast('int', ar[i])
                ar[i] = jcast('int', ar[j])
                ar[j] = jcast('int', tmp)
                tmp = jcast('int', ai[i])
                ai[i] = jcast('int', ai[j])
                ai[j] = jcast('int', tmp)
                i = jcast('int', (i + 1))
                j = jcast('int', (j - 1))
        Code06_ChengDu1.sort(al, ar, ai, l, j)
        Code06_ChengDu1.sort(al, ar, ai, i, r)

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        Code06_ChengDu1.cntNode = jcast('int', 0)
        Code06_ChengDu1.cntQues = jcast('int', 0)
        # dfs1(u, 0, u, u);
        Code06_ChengDu1.dfs2(u, 0, u, u)
        Code06_ChengDu1.sort(Code06_ChengDu1.nodel, Code06_ChengDu1.noder, Code06_ChengDu1.ncolor, 1, Code06_ChengDu1.cntNode)
        Code06_ChengDu1.sort(Code06_ChengDu1.quesl, Code06_ChengDu1.quesr, Code06_ChengDu1.quesid, 1, Code06_ChengDu1.cntQues)
        i = jcast('int', 1)
        j = jcast('int', 1)
        while (i <= Code06_ChengDu1.cntQues):
            while ((j <= Code06_ChengDu1.cntNode) and (Code06_ChengDu1.noder[j] <= Code06_ChengDu1.quesr[i])):
                if (Code06_ChengDu1.nodel[j] > Code06_ChengDu1.pos[Code06_ChengDu1.ncolor[j]]):
                    Code06_ChengDu1.add(Code06_ChengDu1.pos[Code06_ChengDu1.ncolor[j]], jcast('int', (-1)))
                    jset(Code06_ChengDu1.pos, Code06_ChengDu1.ncolor[j], Code06_ChengDu1.nodel[j])
                    Code06_ChengDu1.add(Code06_ChengDu1.pos[Code06_ChengDu1.ncolor[j]], 1)
                j = jcast('int', (j + 1))
            jset(Code06_ChengDu1.ans, Code06_ChengDu1.quesid[i], jstatic('Math', 'max', Code06_ChengDu1.ans[Code06_ChengDu1.quesid[i]], Code06_ChengDu1.query(Code06_ChengDu1.quesl[i], Code06_ChengDu1.n)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_ChengDu1.cntNode):
            Code06_ChengDu1.add(Code06_ChengDu1.pos[Code06_ChengDu1.ncolor[i]], jcast('int', (-1)))
            jset(Code06_ChengDu1.pos, Code06_ChengDu1.ncolor[i], 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code06_ChengDu1.vis[u] = jcast('boolean', True)
        Code06_ChengDu1.calc(u)
        e = jcast('int', Code06_ChengDu1.headg[u])
        while (e > 0):
            v = jcast('int', Code06_ChengDu1.tog[e])
            if (not Code06_ChengDu1.vis[v]):
                Code06_ChengDu1.solve(Code06_ChengDu1.getCentroid(v, u))
            e = jcast('int', Code06_ChengDu1.nxtg[e])

    @staticmethod
    def main(args):
        in_ = Code06_ChengDu1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_ChengDu1.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_ChengDu1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code06_ChengDu1.n):
            jset(Code06_ChengDu1.color, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code06_ChengDu1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code06_ChengDu1.addEdge(u, v)
            Code06_ChengDu1.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        l = 0
        r = 0
        x = 0
        while (i <= Code06_ChengDu1.m):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            Code06_ChengDu1.addQuery(x, l, r, i)
            i = jcast('int', (i + 1))
        Code06_ChengDu1.solve(Code06_ChengDu1.getCentroid(1, 0))
        i = jcast('int', 1)
        while (i <= Code06_ChengDu1.m):
            jcall(out, 'println', Code06_ChengDu1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_21 := self), (_java_key_22 := 'ptr'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))), _java_old_23)[4]])

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
            raise TypeError("No matching overload for Code06_ChengDu1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_ChengDu1.MAXN = jcast('int', 100001)
Code06_ChengDu1.n = jcast('int', 0)
Code06_ChengDu1.m = jcast('int', 0)
Code06_ChengDu1.color = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.headg = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.nxtg = jarray('int', [jcast('int', (Code06_ChengDu1.MAXN << (1 & 31)))])
Code06_ChengDu1.tog = jarray('int', [jcast('int', (Code06_ChengDu1.MAXN << (1 & 31)))])
Code06_ChengDu1.cntg = jcast('int', 0)
Code06_ChengDu1.headq = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.nxtq = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.ql = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.qr = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.qid = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.cntq = jcast('int', 0)
Code06_ChengDu1.vis = jarray('boolean', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.siz = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.nodel = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.noder = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.ncolor = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.cntNode = jcast('int', 0)
Code06_ChengDu1.quesl = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.quesr = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.quesid = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.cntQues = jcast('int', 0)
Code06_ChengDu1.pos = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.tree = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.ans = jarray('int', [Code06_ChengDu1.MAXN])
Code06_ChengDu1.stack = jarray('int', [Code06_ChengDu1.MAXN, 5])
Code06_ChengDu1.u = jcast('int', 0)
Code06_ChengDu1.f = jcast('int', 0)
Code06_ChengDu1.nl = jcast('int', 0)
Code06_ChengDu1.nr = jcast('int', 0)
Code06_ChengDu1.e = jcast('int', 0)
Code06_ChengDu1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code06_ChengDu1.main([])

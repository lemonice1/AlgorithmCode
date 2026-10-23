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

# 首都，Python版
# 一共有n个节点，给定n-1条边，所有节点组成一棵树
# 给定长度为n的数组color，color[i]表示i号节点的颜色，颜色有k种
# 你需要在树上找到一个连通区，连通区内出现的每种颜色，在连通区外不存在
# 这样的连通区可能有多个，希望包含的颜色数量尽量少，打印(最少颜色数 - 1)的结果
# 1 <= n、k <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P7215
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Capital2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'k': 'k', 'color': 'color', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'headc': 'headc', 'nextc': 'nextc', 'toc': 'toc', 'cntc': 'cntc', 'vis': 'vis', 'siz': 'siz', 'father': 'father', 'nodeRoot': 'nodeRoot', 'que': 'que', 'nodeVis': 'nodeVis', 'colorVis': 'colorVis', 'stack': 'stack', 'u': 'u', 'f': 'f', 'rt': 'rt', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    INF = 0
    n = 0
    k = 0
    color = None
    # 建树的链式前向星
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 颜色拥有的节点列表
    headc = None
    nextc = None
    toc = None
    cntc = 0
    # 点分治
    vis = None
    siz = None
    # father[x] = y，表示x此时的父亲节点是y
    father = None
    # nodeRoot[x] = y，表示x此时的重心是y
    nodeRoot = None
    # 宽度优先遍历的队列
    que = None
    # 节点是否进过队列
    nodeVis = None
    # 颜色是否讨论过
    colorVis = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    rt = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, rt, e):
        u = jcast('int', u)
        f = jcast('int', f)
        rt = jcast('int', rt)
        e = jcast('int', e)
        jset(Code01_Capital2.stack[Code01_Capital2.stacksize], 0, u)
        jset(Code01_Capital2.stack[Code01_Capital2.stacksize], 1, f)
        jset(Code01_Capital2.stack[Code01_Capital2.stacksize], 2, rt)
        jset(Code01_Capital2.stack[Code01_Capital2.stacksize], 3, e)
        Code01_Capital2.stacksize = jcast('int', (Code01_Capital2.stacksize + 1))

    @staticmethod
    def pop():
        Code01_Capital2.stacksize = jcast('int', (Code01_Capital2.stacksize - 1))
        Code01_Capital2.u = jcast('int', Code01_Capital2.stack[Code01_Capital2.stacksize][0])
        Code01_Capital2.f = jcast('int', Code01_Capital2.stack[Code01_Capital2.stacksize][1])
        Code01_Capital2.rt = jcast('int', Code01_Capital2.stack[Code01_Capital2.stacksize][2])
        Code01_Capital2.e = jcast('int', Code01_Capital2.stack[Code01_Capital2.stacksize][3])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_Capital2.nextg, ((_java_obj_1 := Code01_Capital2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Capital2.headg[u])
        Code01_Capital2.tog[Code01_Capital2.cntg] = jcast('int', v)
        Code01_Capital2.headg[u] = jcast('int', Code01_Capital2.cntg)

    @staticmethod
    def addNode(color, node):
        color = jcast('int', color)
        node = jcast('int', node)
        jset(Code01_Capital2.nextc, ((_java_obj_4 := Code01_Capital2), (_java_key_5 := 'cntc'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code01_Capital2.headc[color])
        Code01_Capital2.toc[Code01_Capital2.cntc] = jcast('int', node)
        Code01_Capital2.headc[color] = jcast('int', Code01_Capital2.cntc)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_Capital2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_Capital2.headg[u])
        while (e > 0):
            v = jcast('int', Code01_Capital2.tog[e])
            if ((v != fa) and (not Code01_Capital2.vis[v])):
                Code01_Capital2.getSize1(v, u)
                Code01_Capital2.siz[u] = jcast('int', jcast('int', jadd(Code01_Capital2.siz[u], Code01_Capital2.siz[v])))
            e = jcast('int', Code01_Capital2.nextg[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code01_Capital2.stacksize = jcast('int', 0)
        Code01_Capital2.push(cur, fa, 0, jcast('int', (-1)))
        while (Code01_Capital2.stacksize > 0):
            Code01_Capital2.pop()
            if (Code01_Capital2.e == jcast('int', (-1))):
                Code01_Capital2.siz[Code01_Capital2.u] = jcast('int', 1)
                Code01_Capital2.e = jcast('int', Code01_Capital2.headg[Code01_Capital2.u])
            else:
                Code01_Capital2.e = jcast('int', Code01_Capital2.nextg[Code01_Capital2.e])
            if (Code01_Capital2.e != 0):
                Code01_Capital2.push(Code01_Capital2.u, Code01_Capital2.f, 0, Code01_Capital2.e)
                v = jcast('int', Code01_Capital2.tog[Code01_Capital2.e])
                if ((v != Code01_Capital2.f) and (not Code01_Capital2.vis[v])):
                    Code01_Capital2.push(v, Code01_Capital2.u, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code01_Capital2.headg[Code01_Capital2.u])
                while (ei > 0):
                    v = jcast('int', Code01_Capital2.tog[ei])
                    if ((v != Code01_Capital2.f) and (not Code01_Capital2.vis[v])):
                        Code01_Capital2.siz[Code01_Capital2.u] = jcast('int', jcast('int', jadd(Code01_Capital2.siz[Code01_Capital2.u], Code01_Capital2.siz[v])))
                    ei = jcast('int', Code01_Capital2.nextg[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code01_Capital2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code01_Capital2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code01_Capital2.headg[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code01_Capital2.tog[e])
                        if (((v != fa) and (not Code01_Capital2.vis[v])) and (Code01_Capital2.siz[v] > half)):
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
                    e = jcast('int', Code01_Capital2.nextg[e])
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
    def dfs1(u, fa, rt):
        u = jcast('int', u)
        fa = jcast('int', fa)
        rt = jcast('int', rt)
        Code01_Capital2.father[u] = jcast('int', fa)
        Code01_Capital2.nodeRoot[u] = jcast('int', rt)
        Code01_Capital2.nodeVis[u] = jcast('boolean', False)
        jset(Code01_Capital2.colorVis, Code01_Capital2.color[u], False)
        e = jcast('int', Code01_Capital2.headg[u])
        while (e > 0):
            v = jcast('int', Code01_Capital2.tog[e])
            if ((v != fa) and (not Code01_Capital2.vis[v])):
                Code01_Capital2.dfs1(v, u, rt)
            e = jcast('int', Code01_Capital2.nextg[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, root):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        root = jcast('int', root)
        Code01_Capital2.stacksize = jcast('int', 0)
        Code01_Capital2.push(cur, fa, root, jcast('int', (-1)))
        while (Code01_Capital2.stacksize > 0):
            Code01_Capital2.pop()
            if (Code01_Capital2.e == jcast('int', (-1))):
                Code01_Capital2.father[Code01_Capital2.u] = jcast('int', Code01_Capital2.f)
                Code01_Capital2.nodeRoot[Code01_Capital2.u] = jcast('int', Code01_Capital2.rt)
                Code01_Capital2.nodeVis[Code01_Capital2.u] = jcast('boolean', False)
                jset(Code01_Capital2.colorVis, Code01_Capital2.color[Code01_Capital2.u], False)
                Code01_Capital2.e = jcast('int', Code01_Capital2.headg[Code01_Capital2.u])
            else:
                Code01_Capital2.e = jcast('int', Code01_Capital2.nextg[Code01_Capital2.e])
            if (Code01_Capital2.e != 0):
                Code01_Capital2.push(Code01_Capital2.u, Code01_Capital2.f, Code01_Capital2.rt, Code01_Capital2.e)
                v = jcast('int', Code01_Capital2.tog[Code01_Capital2.e])
                if ((v != Code01_Capital2.f) and (not Code01_Capital2.vis[v])):
                    Code01_Capital2.push(v, Code01_Capital2.u, Code01_Capital2.rt, jcast('int', (-1)))

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        # dfs1(u, 0, u);
        Code01_Capital2.dfs2(u, 0, u)
        l = jcast('int', 1)
        r = jcast('int', 0)
        jset(Code01_Capital2.que, (r := jcast('int', (r + (1)))), u)
        Code01_Capital2.nodeVis[u] = jcast('boolean', True)
        ans = jcast('int', 0)
        while (l <= r):
            cur = jcast('int', Code01_Capital2.que[((_java_old_9 := l), (l := jcast('int', (l + (1)))), _java_old_9)[2]])
            if ((cur != u) and (not Code01_Capital2.nodeVis[Code01_Capital2.father[cur]])):
                jset(Code01_Capital2.que, (r := jcast('int', (r + (1)))), Code01_Capital2.father[cur])
                jset(Code01_Capital2.nodeVis, Code01_Capital2.father[cur], True)
            if (not Code01_Capital2.colorVis[Code01_Capital2.color[cur]]):
                jset(Code01_Capital2.colorVis, Code01_Capital2.color[cur], True)
                ans = jcast('int', (ans + 1))
                e = jcast('int', Code01_Capital2.headc[Code01_Capital2.color[cur]])
                while (e > 0):
                    v = jcast('int', Code01_Capital2.toc[e])
                    if (Code01_Capital2.nodeRoot[v] != u):
                        return jcast('int', Code01_Capital2.INF)
                    if (not Code01_Capital2.nodeVis[v]):
                        jset(Code01_Capital2.que, (r := jcast('int', (r + (1)))), v)
                        Code01_Capital2.nodeVis[v] = jcast('boolean', True)
                    e = jcast('int', Code01_Capital2.nextc[e])
        return jcast('int', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code01_Capital2.vis[u] = jcast('boolean', True)
        ans = jcast('int', Code01_Capital2.calc(u))
        e = jcast('int', Code01_Capital2.headg[u])
        while (e > 0):
            v = jcast('int', Code01_Capital2.tog[e])
            if (not Code01_Capital2.vis[v]):
                ans = jcast('int', jstatic('Math', 'min', ans, Code01_Capital2.solve(Code01_Capital2.getCentroid(v, u))))
            e = jcast('int', Code01_Capital2.nextg[e])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_Capital2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Capital2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Capital2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code01_Capital2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code01_Capital2.addEdge(u, v)
            Code01_Capital2.addEdge(v, u)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Capital2.n):
            jset(Code01_Capital2.color, i, jcall(in_, 'nextInt'))
            Code01_Capital2.addNode(Code01_Capital2.color[i], i)
            i = jcast('int', (i + 1))
        ans = jcast('int', Code01_Capital2.solve(Code01_Capital2.getCentroid(1, 0)))
        jcall(out, 'println', jcast('int', (ans - 1)))
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
            raise TypeError("No matching overload for Code01_Capital2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Capital2.MAXN = jcast('int', 200001)
Code01_Capital2.INF = jcast('int', 1000000001)
Code01_Capital2.n = jcast('int', 0)
Code01_Capital2.k = jcast('int', 0)
Code01_Capital2.color = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.headg = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.nextg = jarray('int', [jcast('int', (Code01_Capital2.MAXN << (1 & 31)))])
Code01_Capital2.tog = jarray('int', [jcast('int', (Code01_Capital2.MAXN << (1 & 31)))])
Code01_Capital2.cntg = jcast('int', 0)
Code01_Capital2.headc = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.nextc = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.toc = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.cntc = jcast('int', 0)
Code01_Capital2.vis = jarray('boolean', [Code01_Capital2.MAXN])
Code01_Capital2.siz = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.father = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.nodeRoot = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.que = jarray('int', [Code01_Capital2.MAXN])
Code01_Capital2.nodeVis = jarray('boolean', [Code01_Capital2.MAXN])
Code01_Capital2.colorVis = jarray('boolean', [Code01_Capital2.MAXN])
Code01_Capital2.stack = jarray('int', [Code01_Capital2.MAXN, 4])
Code01_Capital2.u = jcast('int', 0)
Code01_Capital2.f = jcast('int', 0)
Code01_Capital2.rt = jcast('int', 0)
Code01_Capital2.e = jcast('int', 0)
Code01_Capital2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code01_Capital2.main([])

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

# 路径权值和为k的最少边数，Python版
# 一共有n个节点，给定n-1条边，每条边有边权，所有节点组成一棵树
# 给定数字k，要求找到路径权值和等于k的简单路径，并且边的数量最小
# 打印这个最小的边数，如果不存在路径权值和等于k的简单路径，那么打印-1
# 注意，本题给定的点的编号从0开始
# 1 <= n <= 2 * 10^5
# 0 <= 边权、k <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4149
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Race2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'INF': 'INF', 'n': 'n', 'k': 'k', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'curDis': 'curDis', 'curEdge': 'curEdge', 'cntc': 'cntc', 'allDis': 'allDis', 'cnta': 'cnta', 'dp': 'dp', 'stack': 'stack', 'u': 'u', 'f': 'f', 'dis': 'dis', 'edge': 'edge', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXK = 0
    INF = 0
    n = 0
    k = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    # 从u出发到当前子树的节点，收集(路径权值和, 路径边数)
    curDis = None
    curEdge = None
    cntc = 0
    # 从u出发到之前子树的节点，收集路径权值和
    allDis = None
    cnta = 0
    # dp[s]表示，从u出发到之前子树的节点，路径权值和为s的路径，最少边数是多少
    dp = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    dis = 0
    edge = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, dis, edge, e):
        u = jcast('int', u)
        f = jcast('int', f)
        dis = jcast('int', dis)
        edge = jcast('int', edge)
        e = jcast('int', e)
        jset(Code03_Race2.stack[Code03_Race2.stacksize], 0, u)
        jset(Code03_Race2.stack[Code03_Race2.stacksize], 1, f)
        jset(Code03_Race2.stack[Code03_Race2.stacksize], 2, dis)
        jset(Code03_Race2.stack[Code03_Race2.stacksize], 3, edge)
        jset(Code03_Race2.stack[Code03_Race2.stacksize], 4, e)
        Code03_Race2.stacksize = jcast('int', (Code03_Race2.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Race2.stacksize = jcast('int', (Code03_Race2.stacksize - 1))
        Code03_Race2.u = jcast('int', Code03_Race2.stack[Code03_Race2.stacksize][0])
        Code03_Race2.f = jcast('int', Code03_Race2.stack[Code03_Race2.stacksize][1])
        Code03_Race2.dis = jcast('int', Code03_Race2.stack[Code03_Race2.stacksize][2])
        Code03_Race2.edge = jcast('int', Code03_Race2.stack[Code03_Race2.stacksize][3])
        Code03_Race2.e = jcast('int', Code03_Race2.stack[Code03_Race2.stacksize][4])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_Race2.nxt, ((_java_obj_1 := Code03_Race2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Race2.head[u])
        Code03_Race2.to[Code03_Race2.cntg] = jcast('int', v)
        Code03_Race2.weight[Code03_Race2.cntg] = jcast('int', w)
        Code03_Race2.head[u] = jcast('int', Code03_Race2.cntg)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_Race2.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_Race2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Race2.to[e])
            if ((v != fa) and (not Code03_Race2.vis[v])):
                Code03_Race2.getSize1(v, u)
                Code03_Race2.siz[u] = jcast('int', jcast('int', jadd(Code03_Race2.siz[u], Code03_Race2.siz[v])))
            e = jcast('int', Code03_Race2.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code03_Race2.stacksize = jcast('int', 0)
        Code03_Race2.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code03_Race2.stacksize > 0):
            Code03_Race2.pop()
            if (Code03_Race2.e == jcast('int', (-1))):
                Code03_Race2.siz[Code03_Race2.u] = jcast('int', 1)
                Code03_Race2.e = jcast('int', Code03_Race2.head[Code03_Race2.u])
            else:
                Code03_Race2.e = jcast('int', Code03_Race2.nxt[Code03_Race2.e])
            if (Code03_Race2.e != 0):
                Code03_Race2.push(Code03_Race2.u, Code03_Race2.f, 0, 0, Code03_Race2.e)
                v = jcast('int', Code03_Race2.to[Code03_Race2.e])
                if ((v != Code03_Race2.f) and (not Code03_Race2.vis[v])):
                    Code03_Race2.push(v, Code03_Race2.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code03_Race2.head[Code03_Race2.u])
                while (ei > 0):
                    v = jcast('int', Code03_Race2.to[ei])
                    if ((v != Code03_Race2.f) and (not Code03_Race2.vis[v])):
                        Code03_Race2.siz[Code03_Race2.u] = jcast('int', jcast('int', jadd(Code03_Race2.siz[Code03_Race2.u], Code03_Race2.siz[v])))
                    ei = jcast('int', Code03_Race2.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code03_Race2.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code03_Race2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code03_Race2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code03_Race2.to[e])
                        if (((v != fa) and (not Code03_Race2.vis[v])) and (Code03_Race2.siz[v] > half)):
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
                    e = jcast('int', Code03_Race2.nxt[e])
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
    def dfs1(u, fa, dis, edge):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        edge = jcast('int', edge)
        if (dis > Code03_Race2.k):
            return
        jset(Code03_Race2.curDis, ((_java_obj_6 := Code03_Race2), (_java_key_7 := 'cntc'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))))[3], dis)
        Code03_Race2.curEdge[Code03_Race2.cntc] = jcast('int', edge)
        e = jcast('int', Code03_Race2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Race2.to[e])
            if ((v != fa) and (not Code03_Race2.vis[v])):
                Code03_Race2.dfs1(v, u, jcast('int', jadd(dis, Code03_Race2.weight[e])), jcast('int', jadd(edge, 1)))
            e = jcast('int', Code03_Race2.nxt[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, pathDis, pathEdge):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        pathDis = jcast('int', pathDis)
        pathEdge = jcast('int', pathEdge)
        Code03_Race2.stacksize = jcast('int', 0)
        Code03_Race2.push(cur, fa, pathDis, pathEdge, jcast('int', (-1)))
        while (Code03_Race2.stacksize > 0):
            try:
                Code03_Race2.pop()
                if (Code03_Race2.e == jcast('int', (-1))):
                    if (Code03_Race2.dis > Code03_Race2.k):
                        raise JContinue(None)
                    jset(Code03_Race2.curDis, ((_java_obj_10 := Code03_Race2), (_java_key_11 := 'cntc'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code03_Race2.dis)
                    Code03_Race2.curEdge[Code03_Race2.cntc] = jcast('int', Code03_Race2.edge)
                    Code03_Race2.e = jcast('int', Code03_Race2.head[Code03_Race2.u])
                else:
                    Code03_Race2.e = jcast('int', Code03_Race2.nxt[Code03_Race2.e])
                if (Code03_Race2.e != 0):
                    Code03_Race2.push(Code03_Race2.u, Code03_Race2.f, Code03_Race2.dis, Code03_Race2.edge, Code03_Race2.e)
                    v = jcast('int', Code03_Race2.to[Code03_Race2.e])
                    if ((v != Code03_Race2.f) and (not Code03_Race2.vis[v])):
                        Code03_Race2.push(Code03_Race2.to[Code03_Race2.e], Code03_Race2.u, jcast('int', jadd(Code03_Race2.dis, Code03_Race2.weight[Code03_Race2.e])), jcast('int', jadd(Code03_Race2.edge, 1)), jcast('int', (-1)))
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
        ans = jcast('int', Code03_Race2.INF)
        Code03_Race2.cnta = jcast('int', 0)
        Code03_Race2.dp[0] = jcast('int', 0)
        e = jcast('int', Code03_Race2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Race2.to[e])
            if (not Code03_Race2.vis[v]):
                Code03_Race2.cntc = jcast('int', 0)
                # dfs1(v, u, weight[e], 1);
                Code03_Race2.dfs2(v, u, Code03_Race2.weight[e], 1)
                i = jcast('int', 1)
                while (i <= Code03_Race2.cntc):
                    ans = jcast('int', jstatic('Math', 'min', ans, jcast('int', jadd(Code03_Race2.dp[jcast('int', (Code03_Race2.k - Code03_Race2.curDis[i]))], Code03_Race2.curEdge[i]))))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= Code03_Race2.cntc):
                    jset(Code03_Race2.allDis, ((_java_obj_13 := Code03_Race2), (_java_key_14 := 'cnta'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code03_Race2.curDis[i])
                    jset(Code03_Race2.dp, Code03_Race2.curDis[i], jstatic('Math', 'min', Code03_Race2.dp[Code03_Race2.curDis[i]], Code03_Race2.curEdge[i]))
                    i = jcast('int', (i + 1))
            e = jcast('int', Code03_Race2.nxt[e])
        i = jcast('int', 1)
        while (i <= Code03_Race2.cnta):
            jset(Code03_Race2.dp, Code03_Race2.allDis[i], Code03_Race2.INF)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        Code03_Race2.vis[u] = jcast('boolean', True)
        ans = jcast('int', Code03_Race2.calc(u))
        e = jcast('int', Code03_Race2.head[u])
        while (e > 0):
            v = jcast('int', Code03_Race2.to[e])
            if (not Code03_Race2.vis[v]):
                ans = jcast('int', jstatic('Math', 'min', ans, Code03_Race2.solve(Code03_Race2.getCentroid(v, u))))
            e = jcast('int', Code03_Race2.nxt[e])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_Race2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Race2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Race2.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_Race2.n):
            u = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
            v = jcast('int', jcast('int', jadd(jcall(in_, 'nextInt'), 1)))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_Race2.addEdge(u, v, w)
            Code03_Race2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code03_Race2.dp, Code03_Race2.INF)
        ans = jcast('int', Code03_Race2.solve(Code03_Race2.getCentroid(1, 0)))
        if (ans == Code03_Race2.INF):
            ans = jcast('int', jcast('int', (-1)))
        jcall(out, 'println', ans)
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
            raise TypeError("No matching overload for Code03_Race2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Race2.MAXN = jcast('int', 200001)
Code03_Race2.MAXK = jcast('int', 1000001)
Code03_Race2.INF = jcast('int', 1000000001)
Code03_Race2.n = jcast('int', 0)
Code03_Race2.k = jcast('int', 0)
Code03_Race2.head = jarray('int', [Code03_Race2.MAXN])
Code03_Race2.nxt = jarray('int', [jcast('int', (Code03_Race2.MAXN << (1 & 31)))])
Code03_Race2.to = jarray('int', [jcast('int', (Code03_Race2.MAXN << (1 & 31)))])
Code03_Race2.weight = jarray('int', [jcast('int', (Code03_Race2.MAXN << (1 & 31)))])
Code03_Race2.cntg = jcast('int', 0)
Code03_Race2.vis = jarray('boolean', [Code03_Race2.MAXN])
Code03_Race2.siz = jarray('int', [Code03_Race2.MAXN])
Code03_Race2.curDis = jarray('int', [Code03_Race2.MAXN])
Code03_Race2.curEdge = jarray('int', [Code03_Race2.MAXN])
Code03_Race2.cntc = jcast('int', 0)
Code03_Race2.allDis = jarray('int', [Code03_Race2.MAXN])
Code03_Race2.cnta = jcast('int', 0)
Code03_Race2.dp = jarray('int', [Code03_Race2.MAXK])
Code03_Race2.stack = jarray('int', [Code03_Race2.MAXN, 5])
Code03_Race2.u = jcast('int', 0)
Code03_Race2.f = jcast('int', 0)
Code03_Race2.dis = jcast('int', 0)
Code03_Race2.edge = jcast('int', 0)
Code03_Race2.e = jcast('int', 0)
Code03_Race2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_Race2.main([])

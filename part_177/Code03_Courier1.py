# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 快递员，Python版
# 一共有n个节点，给定n-1条边，每条边给定边权，所有节点组成一棵树
# 对于点对(a, b)，假设你选择的中心点为x，那么点对的距离如下
# 点对(a, b)的距离 = a到x的路径权值和 + b到x的路径权值和
# 一共有m个点对，你需要选择中心点x，使得点对距离的最大值尽量小
# 打印这个最小的点对距离最大值
# 1 <= n、m <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4886
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Courier1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'tree': 'tree', 'dist': 'dist', 'stack': 'stack', 'u': 'u', 'f': 'f', 'd': 'd', 't': 't', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    n = 0
    m = 0
    a = None
    b = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    vis = None
    siz = None
    tree = None
    dist = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    d = 0
    t = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, d, t, e):
        u = jcast('int', u)
        f = jcast('int', f)
        d = jcast('int', d)
        t = jcast('int', t)
        e = jcast('int', e)
        jset(Code03_Courier1.stack[Code03_Courier1.stacksize], 0, u)
        jset(Code03_Courier1.stack[Code03_Courier1.stacksize], 1, f)
        jset(Code03_Courier1.stack[Code03_Courier1.stacksize], 2, d)
        jset(Code03_Courier1.stack[Code03_Courier1.stacksize], 3, t)
        jset(Code03_Courier1.stack[Code03_Courier1.stacksize], 4, e)
        Code03_Courier1.stacksize = jcast('int', (Code03_Courier1.stacksize + 1))

    @staticmethod
    def pop():
        Code03_Courier1.stacksize = jcast('int', (Code03_Courier1.stacksize - 1))
        Code03_Courier1.u = jcast('int', Code03_Courier1.stack[Code03_Courier1.stacksize][0])
        Code03_Courier1.f = jcast('int', Code03_Courier1.stack[Code03_Courier1.stacksize][1])
        Code03_Courier1.d = jcast('int', Code03_Courier1.stack[Code03_Courier1.stacksize][2])
        Code03_Courier1.t = jcast('int', Code03_Courier1.stack[Code03_Courier1.stacksize][3])
        Code03_Courier1.e = jcast('int', Code03_Courier1.stack[Code03_Courier1.stacksize][4])

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code03_Courier1.nxt, ((_java_obj_1 := Code03_Courier1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Courier1.head[u])
        Code03_Courier1.to[Code03_Courier1.cntg] = jcast('int', v)
        Code03_Courier1.weight[Code03_Courier1.cntg] = jcast('int', w)
        Code03_Courier1.head[u] = jcast('int', Code03_Courier1.cntg)

    # 得到子树大小递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def getSize1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code03_Courier1.siz[u] = jcast('int', 1)
        e = jcast('int', Code03_Courier1.head[u])
        while (e > 0):
            v = jcast('int', Code03_Courier1.to[e])
            if ((v != fa) and (not Code03_Courier1.vis[v])):
                Code03_Courier1.getSize1(v, u)
                Code03_Courier1.siz[u] = jcast('int', jcast('int', jadd(Code03_Courier1.siz[u], Code03_Courier1.siz[v])))
            e = jcast('int', Code03_Courier1.nxt[e])

    # 得到子树大小迭代版
    @staticmethod
    def getSize2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code03_Courier1.stacksize = jcast('int', 0)
        Code03_Courier1.push(cur, fa, 0, 0, jcast('int', (-1)))
        while (Code03_Courier1.stacksize > 0):
            Code03_Courier1.pop()
            if (Code03_Courier1.e == jcast('int', (-1))):
                Code03_Courier1.siz[Code03_Courier1.u] = jcast('int', 1)
                Code03_Courier1.e = jcast('int', Code03_Courier1.head[Code03_Courier1.u])
            else:
                Code03_Courier1.e = jcast('int', Code03_Courier1.nxt[Code03_Courier1.e])
            if (Code03_Courier1.e != 0):
                Code03_Courier1.push(Code03_Courier1.u, Code03_Courier1.f, 0, 0, Code03_Courier1.e)
                v = jcast('int', Code03_Courier1.to[Code03_Courier1.e])
                if ((v != Code03_Courier1.f) and (not Code03_Courier1.vis[v])):
                    Code03_Courier1.push(v, Code03_Courier1.u, 0, 0, jcast('int', (-1)))
            else:
                ei = jcast('int', Code03_Courier1.head[Code03_Courier1.u])
                while (ei > 0):
                    v = jcast('int', Code03_Courier1.to[ei])
                    if ((v != Code03_Courier1.f) and (not Code03_Courier1.vis[v])):
                        Code03_Courier1.siz[Code03_Courier1.u] = jcast('int', jcast('int', jadd(Code03_Courier1.siz[Code03_Courier1.u], Code03_Courier1.siz[v])))
                    ei = jcast('int', Code03_Courier1.nxt[ei])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        # getSize1(u, fa);
        Code03_Courier1.getSize2(u, fa)
        half = jcast('int', jcast('int', (Code03_Courier1.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code03_Courier1.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code03_Courier1.to[e])
                        if (((v != fa) and (not Code03_Courier1.vis[v])) and (Code03_Courier1.siz[v] > half)):
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
                    e = jcast('int', Code03_Courier1.nxt[e])
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
    def dfs1(u, fa, d, t):
        u = jcast('int', u)
        fa = jcast('int', fa)
        d = jcast('int', d)
        t = jcast('int', t)
        Code03_Courier1.tree[u] = jcast('int', t)
        Code03_Courier1.dist[u] = jcast('int', d)
        e = jcast('int', Code03_Courier1.head[u])
        while (e > 0):
            v = jcast('int', Code03_Courier1.to[e])
            if (v != fa):
                Code03_Courier1.dfs1(v, u, jcast('int', jadd(d, Code03_Courier1.weight[e])), t)
            e = jcast('int', Code03_Courier1.nxt[e])

    # 收集信息迭代版
    @staticmethod
    def dfs2(cur, fa, di, tr):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        di = jcast('int', di)
        tr = jcast('int', tr)
        Code03_Courier1.stacksize = jcast('int', 0)
        Code03_Courier1.push(cur, fa, di, tr, jcast('int', (-1)))
        while (Code03_Courier1.stacksize > 0):
            Code03_Courier1.pop()
            if (Code03_Courier1.e == jcast('int', (-1))):
                Code03_Courier1.tree[Code03_Courier1.u] = jcast('int', Code03_Courier1.t)
                Code03_Courier1.dist[Code03_Courier1.u] = jcast('int', Code03_Courier1.d)
                Code03_Courier1.e = jcast('int', Code03_Courier1.head[Code03_Courier1.u])
            else:
                Code03_Courier1.e = jcast('int', Code03_Courier1.nxt[Code03_Courier1.e])
            if (Code03_Courier1.e != 0):
                Code03_Courier1.push(Code03_Courier1.u, Code03_Courier1.f, Code03_Courier1.d, Code03_Courier1.t, Code03_Courier1.e)
                v = jcast('int', Code03_Courier1.to[Code03_Courier1.e])
                if (v != Code03_Courier1.f):
                    Code03_Courier1.push(v, Code03_Courier1.u, jcast('int', jadd(Code03_Courier1.d, Code03_Courier1.weight[Code03_Courier1.e])), Code03_Courier1.t, jcast('int', (-1)))

    @staticmethod
    def compute():
        ans = jcast('int', 1000000001)
        u = jcast('int', Code03_Courier1.getCentroid(1, 0))
        while (not Code03_Courier1.vis[u]):
            try:
                Code03_Courier1.vis[u] = jcast('boolean', True)
                Code03_Courier1.tree[u] = jcast('int', u)
                Code03_Courier1.dist[u] = jcast('int', 0)
                e = jcast('int', Code03_Courier1.head[u])
                while (e > 0):
                    v = jcast('int', Code03_Courier1.to[e])
                    w = jcast('int', Code03_Courier1.weight[e])
                    # dfs1(v, u, w, v);
                    Code03_Courier1.dfs2(v, u, w, v)
                    e = jcast('int', Code03_Courier1.nxt[e])
                maxDist = jcast('int', 0)
                son = jcast('int', 0)
                i = jcast('int', 1)
                while (i <= Code03_Courier1.m):
                    curDist = jcast('int', jcast('int', jadd(Code03_Courier1.dist[Code03_Courier1.a[i]], Code03_Courier1.dist[Code03_Courier1.b[i]])))
                    t1 = jcast('int', Code03_Courier1.tree[Code03_Courier1.a[i]])
                    t2 = jcast('int', Code03_Courier1.tree[Code03_Courier1.b[i]])
                    if (maxDist < curDist):
                        maxDist = jcast('int', curDist)
                        son = jcast('int', (t1 if (t1 == t2) else 0))
                    else:
                        if ((maxDist == curDist) and ((t1 != t2) or (t1 != son))):
                            son = jcast('int', 0)
                    i = jcast('int', (i + 1))
                ans = jcast('int', jstatic('Math', 'min', ans, maxDist))
                if (son == 0):
                    raise JBreak(None)
                u = jcast('int', Code03_Courier1.getCentroid(son, u))
            except JContinue as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
            except JBreak as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_Courier1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Courier1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Courier1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code03_Courier1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code03_Courier1.addEdge(u, v, w)
            Code03_Courier1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Courier1.m):
            jset(Code03_Courier1.a, i, jcall(in_, 'nextInt'))
            jset(Code03_Courier1.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_Courier1.compute())
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code03_Courier1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Courier1.MAXN = jcast('int', 100001)
Code03_Courier1.n = jcast('int', 0)
Code03_Courier1.m = jcast('int', 0)
Code03_Courier1.a = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.b = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.head = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.nxt = jarray('int', [jcast('int', (Code03_Courier1.MAXN << (1 & 31)))])
Code03_Courier1.to = jarray('int', [jcast('int', (Code03_Courier1.MAXN << (1 & 31)))])
Code03_Courier1.weight = jarray('int', [jcast('int', (Code03_Courier1.MAXN << (1 & 31)))])
Code03_Courier1.cntg = jcast('int', 0)
Code03_Courier1.vis = jarray('boolean', [Code03_Courier1.MAXN])
Code03_Courier1.siz = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.tree = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.dist = jarray('int', [Code03_Courier1.MAXN])
Code03_Courier1.stack = jarray('int', [Code03_Courier1.MAXN, 5])
Code03_Courier1.u = jcast('int', 0)
Code03_Courier1.f = jcast('int', 0)
Code03_Courier1.d = jcast('int', 0)
Code03_Courier1.t = jcast('int', 0)
Code03_Courier1.e = jcast('int', 0)
Code03_Courier1.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_Courier1.main([])

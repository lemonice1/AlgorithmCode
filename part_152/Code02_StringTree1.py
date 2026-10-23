# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 字符串树，Python版
# 一共有n个节点，n-1条边，组成一棵树，每条边的边权为字符串
# 一共有m条查询，每条查询的格式为
# u v s : 查询节点u到节点v的路径中，有多少边的字符串以字符串s作为前缀
# 1 <= n、m <= 10^5
# 所有字符串长度不超过10，并且都由字符a~z组成
# 测试链接 : https://www.luogu.com.cn/problem/P6088
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_StringTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'MAXP': 'MAXP', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'root': 'root', 'tree': 'tree', 'pass': 'pass_', 'cntt': 'cntt', 'deep': 'deep', 'stjump': 'stjump', 'us': 'us', 'fs': 'fs', 'es': 'es', 'ps': 'ps', 'stackSize': 'stackSize', 'u': 'u', 'f': 'f', 'e': 'e', 'p': 'p'}
    MAXN = 0
    MAXT = 0
    MAXP = 0
    n = 0
    m = 0
    # 链式前向星需要
    head = None
    next = None
    to = None
    weight = None
    cntg = 0
    # 可持久化前缀树需要
    root = None
    tree = None
    pass_ = None
    cntt = 0
    # 树上倍增和LCA需要
    deep = None
    stjump = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code02_StringTree1.next, ((_java_obj_1 := Code02_StringTree1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_StringTree1.head[u])
        Code02_StringTree1.to[Code02_StringTree1.cntg] = jcast('int', v)
        Code02_StringTree1.weight[Code02_StringTree1.cntg] = w
        Code02_StringTree1.head[u] = jcast('int', Code02_StringTree1.cntg)

    @staticmethod
    def num(cha):
        cha = jcast('char', cha)
        return jcast('int', jcast('int', jadd(jcast('int', (cha - jchar('a'))), 1)))

    @staticmethod
    def clone(i):
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code02_StringTree1), (_java_key_5 := 'cntt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        cha = jcast('int', 1)
        while (cha <= 26):
            jset(Code02_StringTree1.tree[rt], cha, Code02_StringTree1.tree[i][cha])
            cha = jcast('int', (cha + 1))
        Code02_StringTree1.pass_[rt] = jcast('int', Code02_StringTree1.pass_[i])
        return jcast('int', rt)

    @staticmethod
    def insert(str, i):
        i = jcast('int', i)
        rt = jcast('int', Code02_StringTree1.clone(i))
        Code02_StringTree1.pass_[rt] = jcast('int', (Code02_StringTree1.pass_[rt] + 1))
        j = jcast('int', 0)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (j < jcall(str, 'length')):
            path = jcast('int', Code02_StringTree1.num(jcall(str, 'charAt', j)))
            i = jcast('int', Code02_StringTree1.tree[i][path])
            cur = jcast('int', Code02_StringTree1.clone(i))
            Code02_StringTree1.pass_[cur] = jcast('int', (Code02_StringTree1.pass_[cur] + 1))
            jset(Code02_StringTree1.tree[pre], path, cur)
            j = jcast('int', (j + 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    @staticmethod
    def query(str, i):
        i = jcast('int', i)
        j = jcast('int', 0)
        path = 0
        while (j < jcall(str, 'length')):
            path = jcast('int', Code02_StringTree1.num(jcall(str, 'charAt', j)))
            i = jcast('int', Code02_StringTree1.tree[i][path])
            if (i == 0):
                return jcast('int', 0)
            j = jcast('int', (j + 1))
        return jcast('int', Code02_StringTree1.pass_[i])

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa, path):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code02_StringTree1.root, u, Code02_StringTree1.insert(path, Code02_StringTree1.root[fa]))
        Code02_StringTree1.deep[u] = jcast('int', jcast('int', jadd(Code02_StringTree1.deep[fa], 1)))
        jset(Code02_StringTree1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code02_StringTree1.MAXP):
            jset(Code02_StringTree1.stjump[u], p, Code02_StringTree1.stjump[Code02_StringTree1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code02_StringTree1.head[u])
        while (e > 0):
            if (Code02_StringTree1.to[e] != fa):
                Code02_StringTree1.dfs1(Code02_StringTree1.to[e], u, Code02_StringTree1.weight[e])
            e = jcast('int', Code02_StringTree1.next[e])

    # 迭代版：使用显式状态保存遍历进度
    # 讲解118，详解了从递归版改迭代版
    us = None
    fs = None
    es = None
    ps = None
    stackSize = 0
    u = 0
    f = 0
    e = 0
    p = None
    @staticmethod
    def push(u, f, e, p):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        Code02_StringTree1.us[Code02_StringTree1.stackSize] = jcast('int', u)
        Code02_StringTree1.fs[Code02_StringTree1.stackSize] = jcast('int', f)
        Code02_StringTree1.es[Code02_StringTree1.stackSize] = jcast('int', e)
        Code02_StringTree1.ps[Code02_StringTree1.stackSize] = p
        Code02_StringTree1.stackSize = jcast('int', (Code02_StringTree1.stackSize + 1))

    @staticmethod
    def pop():
        Code02_StringTree1.stackSize = jcast('int', (Code02_StringTree1.stackSize - 1))
        Code02_StringTree1.u = jcast('int', Code02_StringTree1.us[Code02_StringTree1.stackSize])
        Code02_StringTree1.f = jcast('int', Code02_StringTree1.fs[Code02_StringTree1.stackSize])
        Code02_StringTree1.e = jcast('int', Code02_StringTree1.es[Code02_StringTree1.stackSize])
        Code02_StringTree1.p = Code02_StringTree1.ps[Code02_StringTree1.stackSize]

    # dfs1方法改成迭代版
    @staticmethod
    def dfs2():
        Code02_StringTree1.stackSize = jcast('int', 0)
        Code02_StringTree1.push(1, 0, jcast('int', (-1)), '')
        while (Code02_StringTree1.stackSize > 0):
            Code02_StringTree1.pop()
            if (Code02_StringTree1.e == jcast('int', (-1))):
                jset(Code02_StringTree1.root, Code02_StringTree1.u, Code02_StringTree1.insert(Code02_StringTree1.p, Code02_StringTree1.root[Code02_StringTree1.f]))
                Code02_StringTree1.deep[Code02_StringTree1.u] = jcast('int', jcast('int', jadd(Code02_StringTree1.deep[Code02_StringTree1.f], 1)))
                jset(Code02_StringTree1.stjump[Code02_StringTree1.u], 0, Code02_StringTree1.f)
                p = jcast('int', 1)
                while (p < Code02_StringTree1.MAXP):
                    jset(Code02_StringTree1.stjump[Code02_StringTree1.u], p, Code02_StringTree1.stjump[Code02_StringTree1.stjump[Code02_StringTree1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code02_StringTree1.e = jcast('int', Code02_StringTree1.head[Code02_StringTree1.u])
            else:
                Code02_StringTree1.e = jcast('int', Code02_StringTree1.next[Code02_StringTree1.e])
            if (Code02_StringTree1.e != 0):
                Code02_StringTree1.push(Code02_StringTree1.u, Code02_StringTree1.f, Code02_StringTree1.e, Code02_StringTree1.p)
                if (Code02_StringTree1.to[Code02_StringTree1.e] != Code02_StringTree1.f):
                    Code02_StringTree1.push(Code02_StringTree1.to[Code02_StringTree1.e], Code02_StringTree1.u, jcast('int', (-1)), Code02_StringTree1.weight[Code02_StringTree1.e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code02_StringTree1.deep[a] < Code02_StringTree1.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code02_StringTree1.MAXP - 1)))
        while (p >= 0):
            if (Code02_StringTree1.deep[Code02_StringTree1.stjump[a][p]] >= Code02_StringTree1.deep[b]):
                a = jcast('int', Code02_StringTree1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code02_StringTree1.MAXP - 1)))
        while (p >= 0):
            if (Code02_StringTree1.stjump[a][p] != Code02_StringTree1.stjump[b][p]):
                a = jcast('int', Code02_StringTree1.stjump[a][p])
                b = jcast('int', Code02_StringTree1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code02_StringTree1.stjump[a][0])

    @staticmethod
    def compute(u, v, s):
        u = jcast('int', u)
        v = jcast('int', v)
        return jcast('int', jcast('int', (jcast('int', jadd(Code02_StringTree1.query(s, Code02_StringTree1.root[u]), Code02_StringTree1.query(s, Code02_StringTree1.root[v]))) - jcast('int', (2 * Code02_StringTree1.query(s, Code02_StringTree1.root[Code02_StringTree1.lca(u, v)]))))))

    @staticmethod
    def main(args):
        io = Code02_StringTree1.Kattio(_java_ctor=0)
        Code02_StringTree1.n = jcast('int', jcall(io, 'nextInt'))
        u = 0
        v = 0
        s = None
        i = jcast('int', 1)
        while (i < Code02_StringTree1.n):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            s = jcall(io, 'next')
            Code02_StringTree1.addEdge(u, v, s)
            Code02_StringTree1.addEdge(v, u, s)
            i = jcast('int', (i + 1))
        # 使用迭代版防止爆栈
        Code02_StringTree1.dfs2()
        Code02_StringTree1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_StringTree1.m):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            s = jcall(io, 'next')
            jcall(io, 'println', Code02_StringTree1.compute(u, v, s))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_7:
                if jinstanceof(_java_exception_7, 'Exception'):
                    e = _java_exception_7
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code02_StringTree1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_StringTree1.MAXN = jcast('int', 100001)
Code02_StringTree1.MAXT = jcast('int', 1000001)
Code02_StringTree1.MAXP = jcast('int', 20)
Code02_StringTree1.n = jcast('int', 0)
Code02_StringTree1.m = jcast('int', 0)
Code02_StringTree1.head = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.next = jarray('int', [jcast('int', (Code02_StringTree1.MAXN << (1 & 31)))])
Code02_StringTree1.to = jarray('int', [jcast('int', (Code02_StringTree1.MAXN << (1 & 31)))])
Code02_StringTree1.weight = jarray('String', [jcast('int', (Code02_StringTree1.MAXN << (1 & 31)))])
Code02_StringTree1.cntg = jcast('int', 0)
Code02_StringTree1.root = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.tree = jarray('int', [Code02_StringTree1.MAXT, 27])
Code02_StringTree1.pass_ = jarray('int', [Code02_StringTree1.MAXT])
Code02_StringTree1.cntt = jcast('int', 0)
Code02_StringTree1.deep = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.stjump = jarray('int', [Code02_StringTree1.MAXN, Code02_StringTree1.MAXP])
Code02_StringTree1.us = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.fs = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.es = jarray('int', [Code02_StringTree1.MAXN])
Code02_StringTree1.ps = jarray('String', [Code02_StringTree1.MAXN])
Code02_StringTree1.stackSize = jcast('int', 0)
Code02_StringTree1.u = jcast('int', 0)
Code02_StringTree1.f = jcast('int', 0)
Code02_StringTree1.e = jcast('int', 0)
Code02_StringTree1.p = None

if __name__ == '__main__':
    Code02_StringTree1.main([])

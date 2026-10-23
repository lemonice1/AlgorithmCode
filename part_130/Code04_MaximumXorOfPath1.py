# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 路径最大异或和(递归版)
# 一共有n个点，编号1~n，由m条无向边连接
# 每条边有权值，输入保证图是连通的，可能有环
# 找到1到n的一条路径，路径可以重复经过某些点或边
# 当一条边在路径中出现了多次时，异或的时候也要算多次
# 希望找到一条从1到n的路径，所有边权异或和尽量大，返回这个最大异或和
# 1 <= n <= 50000
# 1 <= m <= 100000
# 0 <= 边权 <= 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P4151
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 递归实现：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
# 对应实现可参考 Code04_MaximumXorOfPath2.py
class Code04_MaximumXorOfPath1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'BIT': 'BIT', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'basis': 'basis', 'visited': 'visited', 'path': 'path'}
    MAXN = 0
    MAXM = 0
    BIT = 0
    # 链式前向星
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # 所有环的异或和构建的线性基
    basis = None
    # 某个节点在dfs过程中是否被访问过
    visited = None
    # 从头结点到当前节点的异或和
    path = None
    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        Code04_MaximumXorOfPath1.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_MaximumXorOfPath1.head, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximumXorOfPath1.basis, 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        Code04_MaximumXorOfPath1.next[Code04_MaximumXorOfPath1.cnt] = jcast('int', Code04_MaximumXorOfPath1.head[u])
        Code04_MaximumXorOfPath1.to[Code04_MaximumXorOfPath1.cnt] = jcast('int', v)
        Code04_MaximumXorOfPath1.weight[Code04_MaximumXorOfPath1.cnt] = jcast('long', w)
        jset(Code04_MaximumXorOfPath1.head, u, ((_java_obj_1 := Code04_MaximumXorOfPath1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', Code04_MaximumXorOfPath1.BIT)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (Code04_MaximumXorOfPath1.basis[i] == 0):
                    Code04_MaximumXorOfPath1.basis[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ Code04_MaximumXorOfPath1.basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def dfs(u, f, p):
        u = jcast('int', u)
        f = jcast('int', f)
        p = jcast('long', p)
        Code04_MaximumXorOfPath1.path[u] = jcast('long', p)
        Code04_MaximumXorOfPath1.visited[u] = jcast('boolean', True)
        e = jcast('int', Code04_MaximumXorOfPath1.head[u])
        while (e != 0):
            v = jcast('int', Code04_MaximumXorOfPath1.to[e])
            if (v != f):
                xor = jcast('long', jcast('long', (p ^ Code04_MaximumXorOfPath1.weight[e])))
                if Code04_MaximumXorOfPath1.visited[v]:
                    Code04_MaximumXorOfPath1.insert(jcast('long', (xor ^ Code04_MaximumXorOfPath1.path[v])))
                else:
                    Code04_MaximumXorOfPath1.dfs(v, u, xor)
            e = jcast('int', Code04_MaximumXorOfPath1.next[e])

    @staticmethod
    def query(init):
        init = jcast('long', init)
        i = jcast('int', Code04_MaximumXorOfPath1.BIT)
        while (i >= 0):
            init = jcast('long', jstatic('Math', 'max', init, jcast('long', (init ^ Code04_MaximumXorOfPath1.basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', init)

    @staticmethod
    def main(args):
        io = Code04_MaximumXorOfPath1.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        m = jcast('int', jcall(io, 'nextInt'))
        Code04_MaximumXorOfPath1.prepare(n)
        i = jcast('int', 1)
        while (i <= m):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            w = jcast('long', jcall(io, 'nextLong'))
            Code04_MaximumXorOfPath1.addEdge(u, v, w)
            Code04_MaximumXorOfPath1.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code04_MaximumXorOfPath1.dfs(1, 0, 0)
        jcall(io, 'println', Code04_MaximumXorOfPath1.query(Code04_MaximumXorOfPath1.path[n]))
        jcall(io, 'flush')
        jcall(io, 'close')

    # Kattio 与 StreamTokenizer 接口均由 Python 实现，按输入格式选择，不沿用原语言的速度比较
    # 输入包含特殊格式时，可使用本类先读取字符串，再选择 int 或 float 解析
    # Python 输入输出参考：https://docs.python.org/3/library/io.html
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
            except Exception as _java_exception_4:
                if jinstanceof(_java_exception_4, 'Exception'):
                    e = _java_exception_4
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
            raise TypeError("No matching overload for Code04_MaximumXorOfPath1.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MaximumXorOfPath1.MAXN = jcast('int', 50001)
Code04_MaximumXorOfPath1.MAXM = jcast('int', 200002)
Code04_MaximumXorOfPath1.BIT = jcast('int', 60)
Code04_MaximumXorOfPath1.head = jarray('int', [Code04_MaximumXorOfPath1.MAXN])
Code04_MaximumXorOfPath1.next = jarray('int', [Code04_MaximumXorOfPath1.MAXM])
Code04_MaximumXorOfPath1.to = jarray('int', [Code04_MaximumXorOfPath1.MAXM])
Code04_MaximumXorOfPath1.weight = jarray('long', [Code04_MaximumXorOfPath1.MAXM])
Code04_MaximumXorOfPath1.cnt = jcast('int', 0)
Code04_MaximumXorOfPath1.basis = jarray('long', [jcast('int', jadd(Code04_MaximumXorOfPath1.BIT, 1))])
Code04_MaximumXorOfPath1.visited = jarray('boolean', [Code04_MaximumXorOfPath1.MAXN])
Code04_MaximumXorOfPath1.path = jarray('long', [Code04_MaximumXorOfPath1.MAXN])

if __name__ == '__main__':
    Code04_MaximumXorOfPath1.main([])

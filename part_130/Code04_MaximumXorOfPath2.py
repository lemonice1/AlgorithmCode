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

# 路径最大异或和(迭代版)
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
class Code04_MaximumXorOfPath2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'BIT': 'BIT', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'basis': 'basis', 'visited': 'visited', 'path': 'path', 'ufe': 'ufe', 'pstack': 'pstack', 'u': 'u', 'f': 'f', 'e': 'e', 'p': 'p', 'stackSize': 'stackSize'}
    MAXN = 0
    MAXM = 0
    BIT = 0
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    basis = None
    visited = None
    path = None
    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        Code04_MaximumXorOfPath2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code04_MaximumXorOfPath2.head, 1, jcast('int', jadd(n, 1)), 0)
        jstatic('Arrays', 'fill', Code04_MaximumXorOfPath2.basis, 0)

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('long', w)
        Code04_MaximumXorOfPath2.next[Code04_MaximumXorOfPath2.cnt] = jcast('int', Code04_MaximumXorOfPath2.head[u])
        Code04_MaximumXorOfPath2.to[Code04_MaximumXorOfPath2.cnt] = jcast('int', v)
        Code04_MaximumXorOfPath2.weight[Code04_MaximumXorOfPath2.cnt] = jcast('long', w)
        jset(Code04_MaximumXorOfPath2.head, u, ((_java_obj_1 := Code04_MaximumXorOfPath2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', Code04_MaximumXorOfPath2.BIT)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (Code04_MaximumXorOfPath2.basis[i] == 0):
                    Code04_MaximumXorOfPath2.basis[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ Code04_MaximumXorOfPath2.basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    # dfs迭代版
    # 不懂去看讲解118，递归改迭代的部分
    ufe = None
    pstack = None
    u = 0
    f = 0
    e = 0
    p = 0
    stackSize = 0
    @staticmethod
    def push(u, f, e, p):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        p = jcast('long', p)
        jset(Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize], 0, u)
        jset(Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize], 1, f)
        jset(Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize], 2, e)
        Code04_MaximumXorOfPath2.pstack[Code04_MaximumXorOfPath2.stackSize] = jcast('long', p)
        Code04_MaximumXorOfPath2.stackSize = jcast('int', (Code04_MaximumXorOfPath2.stackSize + 1))

    @staticmethod
    def pop():
        Code04_MaximumXorOfPath2.stackSize = jcast('int', (Code04_MaximumXorOfPath2.stackSize - 1))
        Code04_MaximumXorOfPath2.u = jcast('int', Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize][0])
        Code04_MaximumXorOfPath2.f = jcast('int', Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize][1])
        Code04_MaximumXorOfPath2.e = jcast('int', Code04_MaximumXorOfPath2.ufe[Code04_MaximumXorOfPath2.stackSize][2])
        Code04_MaximumXorOfPath2.p = jcast('long', Code04_MaximumXorOfPath2.pstack[Code04_MaximumXorOfPath2.stackSize])

    @staticmethod
    def dfs(root):
        root = jcast('int', root)
        Code04_MaximumXorOfPath2.stackSize = jcast('int', 0)
        Code04_MaximumXorOfPath2.push(root, 0, jcast('int', (-1)), 0)
        while (Code04_MaximumXorOfPath2.stackSize > 0):
            Code04_MaximumXorOfPath2.pop()
            if (Code04_MaximumXorOfPath2.e == jcast('int', (-1))):
                Code04_MaximumXorOfPath2.path[Code04_MaximumXorOfPath2.u] = jcast('long', Code04_MaximumXorOfPath2.p)
                Code04_MaximumXorOfPath2.visited[Code04_MaximumXorOfPath2.u] = jcast('boolean', True)
                Code04_MaximumXorOfPath2.e = jcast('int', Code04_MaximumXorOfPath2.head[Code04_MaximumXorOfPath2.u])
            else:
                Code04_MaximumXorOfPath2.e = jcast('int', Code04_MaximumXorOfPath2.next[Code04_MaximumXorOfPath2.e])
            if (Code04_MaximumXorOfPath2.e != 0):
                Code04_MaximumXorOfPath2.push(Code04_MaximumXorOfPath2.u, Code04_MaximumXorOfPath2.f, Code04_MaximumXorOfPath2.e, Code04_MaximumXorOfPath2.p)
                v = jcast('int', Code04_MaximumXorOfPath2.to[Code04_MaximumXorOfPath2.e])
                xor = jcast('long', jcast('long', (Code04_MaximumXorOfPath2.p ^ Code04_MaximumXorOfPath2.weight[Code04_MaximumXorOfPath2.e])))
                if Code04_MaximumXorOfPath2.visited[v]:
                    Code04_MaximumXorOfPath2.insert(jcast('long', (xor ^ Code04_MaximumXorOfPath2.path[v])))
                else:
                    Code04_MaximumXorOfPath2.push(v, Code04_MaximumXorOfPath2.u, jcast('int', (-1)), xor)

    @staticmethod
    def query(init):
        init = jcast('long', init)
        i = jcast('int', Code04_MaximumXorOfPath2.BIT)
        while (i >= 0):
            init = jcast('long', jstatic('Math', 'max', init, jcast('long', (init ^ Code04_MaximumXorOfPath2.basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', init)

    @staticmethod
    def main(args):
        io = Code04_MaximumXorOfPath2.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        m = jcast('int', jcall(io, 'nextInt'))
        Code04_MaximumXorOfPath2.prepare(n)
        i = jcast('int', 1)
        while (i <= m):
            u = jcast('int', jcall(io, 'nextInt'))
            v = jcast('int', jcall(io, 'nextInt'))
            w = jcast('long', jcall(io, 'nextLong'))
            Code04_MaximumXorOfPath2.addEdge(u, v, w)
            Code04_MaximumXorOfPath2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        Code04_MaximumXorOfPath2.dfs(1)
        jcall(io, 'println', Code04_MaximumXorOfPath2.query(Code04_MaximumXorOfPath2.path[n]))
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
            raise TypeError("No matching overload for Code04_MaximumXorOfPath2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MaximumXorOfPath2.MAXN = jcast('int', 50001)
Code04_MaximumXorOfPath2.MAXM = jcast('int', 200002)
Code04_MaximumXorOfPath2.BIT = jcast('int', 60)
Code04_MaximumXorOfPath2.head = jarray('int', [Code04_MaximumXorOfPath2.MAXN])
Code04_MaximumXorOfPath2.next = jarray('int', [Code04_MaximumXorOfPath2.MAXM])
Code04_MaximumXorOfPath2.to = jarray('int', [Code04_MaximumXorOfPath2.MAXM])
Code04_MaximumXorOfPath2.weight = jarray('long', [Code04_MaximumXorOfPath2.MAXM])
Code04_MaximumXorOfPath2.cnt = jcast('int', 0)
Code04_MaximumXorOfPath2.basis = jarray('long', [jcast('int', jadd(Code04_MaximumXorOfPath2.BIT, 1))])
Code04_MaximumXorOfPath2.visited = jarray('boolean', [Code04_MaximumXorOfPath2.MAXN])
Code04_MaximumXorOfPath2.path = jarray('long', [Code04_MaximumXorOfPath2.MAXN])
Code04_MaximumXorOfPath2.ufe = jarray('int', [Code04_MaximumXorOfPath2.MAXN, 3])
Code04_MaximumXorOfPath2.pstack = jarray('long', [Code04_MaximumXorOfPath2.MAXN])
Code04_MaximumXorOfPath2.u = jcast('int', 0)
Code04_MaximumXorOfPath2.f = jcast('int', 0)
Code04_MaximumXorOfPath2.e = jcast('int', 0)
Code04_MaximumXorOfPath2.p = jcast('long', 0)
Code04_MaximumXorOfPath2.stackSize = jcast('int', 0)

if __name__ == '__main__':
    Code04_MaximumXorOfPath2.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 检查树上两节点间的路径是否是回文
# 一颗树上有n个节点，编号1~n
# 给定长度为n的数组parent, parent[i]表示节点i的父节点编号
# 给定长度为n的数组s, s[i]表示节点i上是什么字符
# 从节点a到节点b经过节点最少的路，叫做a和b的路径
# 一共有m条查询，每条查询(a,b)，a和b的路径字符串是否是回文
# 是回文打印"YES"，不是回文打印"NO"
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# parent[1] = 0，即整棵树的头节点一定是1号节点
# 每个节点上的字符一定是小写字母a~z
# 测试链接 : https://ac.nowcoder.com/acm/contest/78807/G
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_PathPalindrome:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 's': 's', 'head': 'head', 'to': 'to', 'next': 'next', 'cnt': 'cnt', 'deep': 'deep', 'jump': 'jump', 'K': 'K', 'kpow': 'kpow', 'stup': 'stup', 'stdown': 'stdown'}
    MAXN = 0
    LIMIT = 0
    power = 0
    s = None
    head = None
    to = None
    next = None
    cnt = 0
    deep = None
    jump = None
    K = 0
    # kpow[i] = k的i次方
    kpow = None
    stup = None
    stdown = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code05_PathPalindrome.power = jcast('int', Code05_PathPalindrome.log2(n))
        Code05_PathPalindrome.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code05_PathPalindrome.head, 1, jcast('int', jadd(n, 1)), 0)
        Code05_PathPalindrome.kpow[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            Code05_PathPalindrome.kpow[i] = jcast('long', jcast('long', (Code05_PathPalindrome.kpow[jcast('int', (i - 1))] * Code05_PathPalindrome.K)))
            i = jcast('int', (i + 1))

    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code05_PathPalindrome.next[Code05_PathPalindrome.cnt] = jcast('int', Code05_PathPalindrome.head[u])
        Code05_PathPalindrome.to[Code05_PathPalindrome.cnt] = jcast('int', v)
        jset(Code05_PathPalindrome.head, u, ((_java_obj_1 := Code05_PathPalindrome), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code05_PathPalindrome.deep[u] = jcast('int', jcast('int', jadd(Code05_PathPalindrome.deep[f], 1)))
        jset(Code05_PathPalindrome.jump[u], 0, f)
        jset(Code05_PathPalindrome.stup[u], 0, jset(Code05_PathPalindrome.stdown[u], 0, Code05_PathPalindrome.s[f]))
        p = jcast('int', 1)
        v = 0
        while (p <= Code05_PathPalindrome.power):
            v = jcast('int', Code05_PathPalindrome.jump[u][jcast('int', (p - 1))])
            jset(Code05_PathPalindrome.jump[u], p, Code05_PathPalindrome.jump[v][jcast('int', (p - 1))])
            jset(Code05_PathPalindrome.stup[u], p, jcast('long', jadd(jcast('long', (Code05_PathPalindrome.stup[u][jcast('int', (p - 1))] * Code05_PathPalindrome.kpow[jcast('int', (1 << (jcast('int', (p - 1)) & 31)))])), Code05_PathPalindrome.stup[v][jcast('int', (p - 1))])))
            jset(Code05_PathPalindrome.stdown[u], p, jcast('long', jadd(jcast('long', (Code05_PathPalindrome.stdown[v][jcast('int', (p - 1))] * Code05_PathPalindrome.kpow[jcast('int', (1 << (jcast('int', (p - 1)) & 31)))])), Code05_PathPalindrome.stdown[u][jcast('int', (p - 1))])))
            p = jcast('int', (p + 1))
        e = jcast('int', Code05_PathPalindrome.head[u])
        v = 0
        while (e != 0):
            v = jcast('int', Code05_PathPalindrome.to[e])
            if (v != f):
                Code05_PathPalindrome.dfs(v, u)
            e = jcast('int', Code05_PathPalindrome.next[e])

    @staticmethod
    def isPalindrome(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        lca = jcast('int', Code05_PathPalindrome.lca(a, b))
        hash1 = jcast('long', Code05_PathPalindrome.hash(a, lca, b))
        hash2 = jcast('long', Code05_PathPalindrome.hash(b, lca, a))
        return jcast('boolean', (hash1 == hash2))

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code05_PathPalindrome.deep[a] < Code05_PathPalindrome.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code05_PathPalindrome.power)
        while (p >= 0):
            if (Code05_PathPalindrome.deep[Code05_PathPalindrome.jump[a][p]] >= Code05_PathPalindrome.deep[b]):
                a = jcast('int', Code05_PathPalindrome.jump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code05_PathPalindrome.power)
        while (p >= 0):
            if (Code05_PathPalindrome.jump[a][p] != Code05_PathPalindrome.jump[b][p]):
                a = jcast('int', Code05_PathPalindrome.jump[a][p])
                b = jcast('int', Code05_PathPalindrome.jump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code05_PathPalindrome.jump[a][0])

    @staticmethod
    def hash(from_, lca, to):
        from_ = jcast('int', from_)
        lca = jcast('int', lca)
        to = jcast('int', to)
        # up是上坡hash值
        up = jcast('long', Code05_PathPalindrome.s[from_])
        p = jcast('int', Code05_PathPalindrome.power)
        while (p >= 0):
            if (Code05_PathPalindrome.deep[Code05_PathPalindrome.jump[from_][p]] >= Code05_PathPalindrome.deep[lca]):
                up = jcast('long', jcast('long', jadd(jcast('long', (up * Code05_PathPalindrome.kpow[jcast('int', (1 << (p & 31)))])), Code05_PathPalindrome.stup[from_][p])))
                from_ = jcast('int', Code05_PathPalindrome.jump[from_][p])
            p = jcast('int', (p - 1))
        if (to == lca):
            return jcast('long', up)
        # down是下坡hash值
        down = jcast('long', Code05_PathPalindrome.s[to])
        # height是目前下坡的总高度
        height = jcast('int', 1)
        p = jcast('int', Code05_PathPalindrome.power)
        while (p >= 0):
            if (Code05_PathPalindrome.deep[Code05_PathPalindrome.jump[to][p]] > Code05_PathPalindrome.deep[lca]):
                down = jcast('long', jcast('long', jadd(jcast('long', (Code05_PathPalindrome.stdown[to][p] * Code05_PathPalindrome.kpow[height])), down)))
                height = jcast('int', jcast('int', jadd(height, jcast('int', (1 << (p & 31))))))
                to = jcast('int', Code05_PathPalindrome.jump[to][p])
            p = jcast('int', (p - 1))
        return jcast('long', jcast('long', jadd(jcast('long', (up * Code05_PathPalindrome.kpow[height])), down)))

    @staticmethod
    def main(args):
        io = Code05_PathPalindrome.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        Code05_PathPalindrome.build(n)
        si = jcast('int', 1)
        for c in jcall(jcall(io, 'next'), 'toCharArray'):
            jset(Code05_PathPalindrome.s, ((_java_old_4 := si), (si := jcast('int', (si + (1)))), _java_old_4)[2], jcast('int', jadd(jcast('int', (c - jchar('a'))), 1)))
        u = jcast('int', 1)
        v = 0
        while (u <= n):
            v = jcast('int', jcall(io, 'nextInt'))
            Code05_PathPalindrome.addEdge(u, v)
            Code05_PathPalindrome.addEdge(v, u)
            u = jcast('int', (u + 1))
        Code05_PathPalindrome.dfs(1, 0)
        m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= m):
            a = jcast('int', jcall(io, 'nextInt'))
            b = jcast('int', jcall(io, 'nextInt'))
            jcall(io, 'println', ('YES' if Code05_PathPalindrome.isPalindrome(a, b) else 'NO'))
            i = jcast('int', (i + 1))
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
            except Exception as _java_exception_5:
                if jinstanceof(_java_exception_5, 'Exception'):
                    e = _java_exception_5
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
            raise TypeError("No matching overload for Code05_PathPalindrome.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_PathPalindrome.MAXN = jcast('int', 100001)
Code05_PathPalindrome.LIMIT = jcast('int', 17)
Code05_PathPalindrome.power = jcast('int', 0)
Code05_PathPalindrome.s = jarray('int', [Code05_PathPalindrome.MAXN])
Code05_PathPalindrome.head = jarray('int', [Code05_PathPalindrome.MAXN])
Code05_PathPalindrome.to = jarray('int', [jcast('int', (Code05_PathPalindrome.MAXN << (1 & 31)))])
Code05_PathPalindrome.next = jarray('int', [jcast('int', (Code05_PathPalindrome.MAXN << (1 & 31)))])
Code05_PathPalindrome.cnt = jcast('int', 0)
Code05_PathPalindrome.deep = jarray('int', [Code05_PathPalindrome.MAXN])
Code05_PathPalindrome.jump = jarray('int', [Code05_PathPalindrome.MAXN, Code05_PathPalindrome.LIMIT])
Code05_PathPalindrome.K = jcast('long', 499)
Code05_PathPalindrome.kpow = jarray('long', [Code05_PathPalindrome.MAXN])
Code05_PathPalindrome.stup = jarray('long', [Code05_PathPalindrome.MAXN, Code05_PathPalindrome.LIMIT])
Code05_PathPalindrome.stdown = jarray('long', [Code05_PathPalindrome.MAXN, Code05_PathPalindrome.LIMIT])

if __name__ == '__main__':
    Code05_PathPalindrome.main([])

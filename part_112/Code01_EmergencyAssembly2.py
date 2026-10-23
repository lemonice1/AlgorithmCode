# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 紧急集合
# 一共有n个节点，编号1 ~ n，一定有n-1条边连接形成一颗树
# 从一个点到另一个点的路径上有几条边，就需要耗费几个金币
# 每条查询(a, b, c)表示有三个人分别站在a、b、c点上
# 他们想集合在树上的某个点，并且想花费的金币总数最少
# 一共有m条查询，打印m个答案
# 1 <= n <= 5 * 10^5
# 1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4281
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_EmergencyAssembly2:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'deep': 'deep', 'stjump': 'stjump', 'togather': 'togather', 'cost': 'cost'}
    MAXN = 0
    LIMIT = 0
    power = 0
    head = None
    next = None
    to = None
    cnt = 0
    # deep[i] : i节点在第几层，算距离用
    deep = None
    # 利用stjump求最低公共祖先
    stjump = None
    togather = 0
    cost = 0
    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code01_EmergencyAssembly2.power = jcast('int', Code01_EmergencyAssembly2.log2(n))
        Code01_EmergencyAssembly2.cnt = jcast('int', 1)
        jstatic('Arrays', 'fill', Code01_EmergencyAssembly2.head, 1, jcast('int', jadd(n, 1)), 0)

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
        Code01_EmergencyAssembly2.next[Code01_EmergencyAssembly2.cnt] = jcast('int', Code01_EmergencyAssembly2.head[u])
        Code01_EmergencyAssembly2.to[Code01_EmergencyAssembly2.cnt] = jcast('int', v)
        jset(Code01_EmergencyAssembly2.head, u, ((_java_obj_1 := Code01_EmergencyAssembly2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def dfs(u, f):
        u = jcast('int', u)
        f = jcast('int', f)
        Code01_EmergencyAssembly2.deep[u] = jcast('int', jcast('int', jadd(Code01_EmergencyAssembly2.deep[f], 1)))
        jset(Code01_EmergencyAssembly2.stjump[u], 0, f)
        p = jcast('int', 1)
        while (p <= Code01_EmergencyAssembly2.power):
            jset(Code01_EmergencyAssembly2.stjump[u], p, Code01_EmergencyAssembly2.stjump[Code01_EmergencyAssembly2.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code01_EmergencyAssembly2.head[u])
        while (e != 0):
            if (Code01_EmergencyAssembly2.to[e] != f):
                Code01_EmergencyAssembly2.dfs(Code01_EmergencyAssembly2.to[e], u)
            e = jcast('int', Code01_EmergencyAssembly2.next[e])

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code01_EmergencyAssembly2.deep[a] < Code01_EmergencyAssembly2.deep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', Code01_EmergencyAssembly2.power)
        while (p >= 0):
            if (Code01_EmergencyAssembly2.deep[Code01_EmergencyAssembly2.stjump[a][p]] >= Code01_EmergencyAssembly2.deep[b]):
                a = jcast('int', Code01_EmergencyAssembly2.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', Code01_EmergencyAssembly2.power)
        while (p >= 0):
            if (Code01_EmergencyAssembly2.stjump[a][p] != Code01_EmergencyAssembly2.stjump[b][p]):
                a = jcast('int', Code01_EmergencyAssembly2.stjump[a][p])
                b = jcast('int', Code01_EmergencyAssembly2.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code01_EmergencyAssembly2.stjump[a][0])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_EmergencyAssembly2.build(n)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < n):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_EmergencyAssembly2.addEdge(u, v)
            Code01_EmergencyAssembly2.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code01_EmergencyAssembly2.dfs(1, 0)
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            c = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_EmergencyAssembly2.compute(a, b, c)
            jcall(out, 'println', jadd(jadd(Code01_EmergencyAssembly2.togather, ' '), Code01_EmergencyAssembly2.cost))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        # 来自对结构关系的深入分析，课上重点解释
        h1 = jcast('int', Code01_EmergencyAssembly2.lca(a, b))
        h2 = jcast('int', Code01_EmergencyAssembly2.lca(a, c))
        h3 = jcast('int', Code01_EmergencyAssembly2.lca(b, c))
        high = jcast('int', ((h1 if (Code01_EmergencyAssembly2.deep[h1] < Code01_EmergencyAssembly2.deep[h2]) else h2) if (h1 != h2) else h1))
        low = jcast('int', ((h1 if (Code01_EmergencyAssembly2.deep[h1] > Code01_EmergencyAssembly2.deep[h2]) else h2) if (h1 != h2) else h3))
        Code01_EmergencyAssembly2.togather = jcast('int', low)
        Code01_EmergencyAssembly2.cost = jcast('long', jcast('long', (jcast('long', (jcast('long', jadd(jcast('long', jadd(jcast('long', Code01_EmergencyAssembly2.deep[a]), Code01_EmergencyAssembly2.deep[b])), Code01_EmergencyAssembly2.deep[c])) - jcast('int', (Code01_EmergencyAssembly2.deep[high] * 2)))) - Code01_EmergencyAssembly2.deep[low])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_EmergencyAssembly2.MAXN = jcast('int', 500001)
Code01_EmergencyAssembly2.LIMIT = jcast('int', 19)
Code01_EmergencyAssembly2.power = jcast('int', 0)
Code01_EmergencyAssembly2.head = jarray('int', [Code01_EmergencyAssembly2.MAXN])
Code01_EmergencyAssembly2.next = jarray('int', [jcast('int', (Code01_EmergencyAssembly2.MAXN << (1 & 31)))])
Code01_EmergencyAssembly2.to = jarray('int', [jcast('int', (Code01_EmergencyAssembly2.MAXN << (1 & 31)))])
Code01_EmergencyAssembly2.cnt = jcast('int', 0)
Code01_EmergencyAssembly2.deep = jarray('int', [Code01_EmergencyAssembly2.MAXN])
Code01_EmergencyAssembly2.stjump = jarray('int', [Code01_EmergencyAssembly2.MAXN, Code01_EmergencyAssembly2.LIMIT])
Code01_EmergencyAssembly2.togather = jcast('int', 0)
Code01_EmergencyAssembly2.cost = jcast('long', 0)

if __name__ == '__main__':
    Code01_EmergencyAssembly2.main([])

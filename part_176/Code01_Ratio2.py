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

# 聪聪可可，Python版
# 一共有n个节点，给定n-1条边，每条边有边权，所有节点组成一棵树
# 如果点对(u, v)的简单路径权值和能被3整除，则称这个点对是合法的
# 认为点对(x, x)的简单路径权值和是0，并且认为(x, y)和(y, x)是不同的点对
# 打印(合法点对的数量 / 点对的总数量)的最简分数形式
# 1 <= n、边权 <= 2 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2634
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Ratio2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'vis': 'vis', 'siz': 'siz', 'cur': 'cur', 'all': 'all'}
    MAXN = 0
    n = 0
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    # vis[u] = true，表示u是之前的分治点
    vis = None
    siz = None
    # cur[v]，表示往下走的当前路径中，路径权值和 % 3 == v的路径有多少条
    # all[v]，表示往下走的所有路径中，路径权值和 % 3 == v的路径有多少条
    cur = None
    all = None
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code01_Ratio2.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code01_Ratio2.nxt, ((_java_obj_1 := Code01_Ratio2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_Ratio2.head[u])
        Code01_Ratio2.to[Code01_Ratio2.cntg] = jcast('int', v)
        Code01_Ratio2.weight[Code01_Ratio2.cntg] = jcast('int', w)
        Code01_Ratio2.head[u] = jcast('int', Code01_Ratio2.cntg)

    @staticmethod
    def getSize(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_Ratio2.siz[u] = jcast('int', 1)
        e = jcast('int', Code01_Ratio2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Ratio2.to[e])
            if ((v != fa) and (not Code01_Ratio2.vis[v])):
                Code01_Ratio2.getSize(v, u)
                Code01_Ratio2.siz[u] = jcast('int', jcast('int', jadd(Code01_Ratio2.siz[u], Code01_Ratio2.siz[v])))
            e = jcast('int', Code01_Ratio2.nxt[e])

    @staticmethod
    def getCentroid(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code01_Ratio2.getSize(u, fa)
        half = jcast('int', jcast('int', (Code01_Ratio2.siz[u] >> (1 & 31))))
        find = jcast('boolean', False)
        while (not find):
            try:
                find = jcast('boolean', True)
                e = jcast('int', Code01_Ratio2.head[u])
                while (e > 0):
                    try:
                        v = jcast('int', Code01_Ratio2.to[e])
                        if (((v != fa) and (not Code01_Ratio2.vis[v])) and (Code01_Ratio2.siz[v] > half)):
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
                    e = jcast('int', Code01_Ratio2.nxt[e])
            except JContinue as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
            except JBreak as _java_control_4:
                if _java_control_4.label not in (None,):
                    raise
                break
        return jcast('int', u)

    @staticmethod
    def dfs(u, fa, dis):
        u = jcast('int', u)
        fa = jcast('int', fa)
        dis = jcast('int', dis)
        ((_java_obj_6 := Code01_Ratio2.cur), (_java_key_7 := jcast('int', jmod(dis, 3))), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]
        e = jcast('int', Code01_Ratio2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Ratio2.to[e])
            if ((v != fa) and (not Code01_Ratio2.vis[v])):
                Code01_Ratio2.dfs(v, u, jcast('int', jadd(dis, Code01_Ratio2.weight[e])))
            e = jcast('int', Code01_Ratio2.nxt[e])

    @staticmethod
    def calc(u):
        u = jcast('int', u)
        ans = jcast('int', 1)
        jset(Code01_Ratio2.all, 0, jset(Code01_Ratio2.all, 1, jset(Code01_Ratio2.all, 2, 0)))
        e = jcast('int', Code01_Ratio2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Ratio2.to[e])
            w = jcast('int', Code01_Ratio2.weight[e])
            if (not Code01_Ratio2.vis[v]):
                jset(Code01_Ratio2.cur, 0, jset(Code01_Ratio2.cur, 1, jset(Code01_Ratio2.cur, 2, 0)))
                Code01_Ratio2.dfs(v, u, w)
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', jadd(jcast('int', jadd(jcast('int', (jcast('int', (Code01_Ratio2.all[0] * Code01_Ratio2.cur[0])) * 2)), jcast('int', (jcast('int', (Code01_Ratio2.all[1] * Code01_Ratio2.cur[2])) * 2)))), jcast('int', (jcast('int', (Code01_Ratio2.all[2] * Code01_Ratio2.cur[1])) * 2)))), jcast('int', (Code01_Ratio2.cur[0] * 2)))))))
                Code01_Ratio2.all[0] = jcast('int', jcast('int', jadd(Code01_Ratio2.all[0], Code01_Ratio2.cur[0])))
                Code01_Ratio2.all[1] = jcast('int', jcast('int', jadd(Code01_Ratio2.all[1], Code01_Ratio2.cur[1])))
                Code01_Ratio2.all[2] = jcast('int', jcast('int', jadd(Code01_Ratio2.all[2], Code01_Ratio2.cur[2])))
            e = jcast('int', Code01_Ratio2.nxt[e])
        return jcast('int', ans)

    @staticmethod
    def solve(u):
        u = jcast('int', u)
        ans = jcast('int', 0)
        Code01_Ratio2.vis[u] = jcast('boolean', True)
        ans = jcast('int', jcast('int', jadd(ans, Code01_Ratio2.calc(u))))
        e = jcast('int', Code01_Ratio2.head[u])
        while (e > 0):
            v = jcast('int', Code01_Ratio2.to[e])
            if (not Code01_Ratio2.vis[v]):
                ans = jcast('int', jcast('int', jadd(ans, Code01_Ratio2.solve(Code01_Ratio2.getCentroid(v, u)))))
            e = jcast('int', Code01_Ratio2.nxt[e])
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_Ratio2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Ratio2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        w = 0
        while (i < Code01_Ratio2.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            w = jcast('int', jcall(in_, 'nextInt'))
            Code01_Ratio2.addEdge(u, v, w)
            Code01_Ratio2.addEdge(v, u, w)
            i = jcast('int', (i + 1))
        centroid = jcast('int', Code01_Ratio2.getCentroid(1, 0))
        a = jcast('int', Code01_Ratio2.solve(centroid))
        b = jcast('int', jcast('int', (Code01_Ratio2.n * Code01_Ratio2.n)))
        c = jcast('int', Code01_Ratio2.gcd(a, b))
        a = jcast('int', jcast('int', jdiv(a, c)))
        b = jcast('int', jcast('int', jdiv(b, c)))
        jcall(out, 'println', jadd(jadd(a, '/'), b))
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
            return jcast('int', self.buffer[((_java_obj_9 := self), (_java_key_10 := 'ptr'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))), _java_old_11)[4]])

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
            raise TypeError("No matching overload for Code01_Ratio2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Ratio2.MAXN = jcast('int', 20001)
Code01_Ratio2.n = jcast('int', 0)
Code01_Ratio2.head = jarray('int', [Code01_Ratio2.MAXN])
Code01_Ratio2.nxt = jarray('int', [jcast('int', (Code01_Ratio2.MAXN << (1 & 31)))])
Code01_Ratio2.to = jarray('int', [jcast('int', (Code01_Ratio2.MAXN << (1 & 31)))])
Code01_Ratio2.weight = jarray('int', [jcast('int', (Code01_Ratio2.MAXN << (1 & 31)))])
Code01_Ratio2.cntg = jcast('int', 0)
Code01_Ratio2.vis = jarray('boolean', [Code01_Ratio2.MAXN])
Code01_Ratio2.siz = jarray('int', [Code01_Ratio2.MAXN])
Code01_Ratio2.cur = jarray('int', [3])
Code01_Ratio2.all = jarray('int', [3])

if __name__ == '__main__':
    Code01_Ratio2.main([])

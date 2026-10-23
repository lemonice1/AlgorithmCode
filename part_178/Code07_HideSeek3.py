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

# 捉迷藏，最优解，树的括号序 + 巧妙线段树，Python版
# 树上有n个点，点的初始颜色为黑，给定n-1条边，边权都是1
# 一共有m条操作，每条操作是如下两种类型中的一种
# 操作 C x : 改变点x的颜色，黑变成白，白变成黑
# 操作 G   : 打印最远的两个黑点的距离，只有一个黑点打印0，无黑点打印-1
# 1 <= n <= 10^5    1 <= m <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2056
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_HideSeek3:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'PAR': 'PAR', 'PAL': 'PAL', 'n': 'n', 'm': 'm', 'black': 'black', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'seg': 'seg', 'cntd': 'cntd', 'pr': 'pr', 'pl': 'pl', 'ladd': 'ladd', 'lminus': 'lminus', 'radd': 'radd', 'rminus': 'rminus', 'dist': 'dist', 'stack': 'stack', 'u': 'u', 'f': 'f', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXT = 0
    INF = 0
    PAR = 0
    PAL = 0
    n = 0
    m = 0
    black = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    seg = None
    cntd = 0
    # 以下概念都是括号序列消除到最简状态之后的情况
    # pr : 右括号数量
    # pl : 左括号数量
    # ladd   : 左端点到任意黑点，max(右括号 + 左括号)
    # lminus : 左端点到任意黑点，max(左括号 - 右括号)
    # radd   : 任意黑点到右端点，max(右括号 + 左括号)
    # rminus : 任意黑点到右端点，max(右括号 - 左括号)
    # dist   : 选择两个黑点的最大距离
    # 注意区分lminus、rminus
    pr = None
    pl = None
    ladd = None
    lminus = None
    radd = None
    rminus = None
    dist = None
    # 讲解118，递归函数改成迭代所需要的栈
    stack = None
    u = 0
    f = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code07_HideSeek3.stack[Code07_HideSeek3.stacksize], 0, u)
        jset(Code07_HideSeek3.stack[Code07_HideSeek3.stacksize], 1, f)
        jset(Code07_HideSeek3.stack[Code07_HideSeek3.stacksize], 2, e)
        Code07_HideSeek3.stacksize = jcast('int', (Code07_HideSeek3.stacksize + 1))

    @staticmethod
    def pop():
        Code07_HideSeek3.stacksize = jcast('int', (Code07_HideSeek3.stacksize - 1))
        Code07_HideSeek3.u = jcast('int', Code07_HideSeek3.stack[Code07_HideSeek3.stacksize][0])
        Code07_HideSeek3.f = jcast('int', Code07_HideSeek3.stack[Code07_HideSeek3.stacksize][1])
        Code07_HideSeek3.e = jcast('int', Code07_HideSeek3.stack[Code07_HideSeek3.stacksize][2])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code07_HideSeek3.nxt, ((_java_obj_1 := Code07_HideSeek3), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code07_HideSeek3.head[u])
        Code07_HideSeek3.to[Code07_HideSeek3.cntg] = jcast('int', v)
        Code07_HideSeek3.head[u] = jcast('int', Code07_HideSeek3.cntg)

    # 收集括号序递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        jset(Code07_HideSeek3.seg, ((_java_obj_4 := Code07_HideSeek3), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code07_HideSeek3.PAL)
        jset(Code07_HideSeek3.seg, ((_java_obj_7 := Code07_HideSeek3), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        Code07_HideSeek3.dfn[u] = jcast('int', Code07_HideSeek3.cntd)
        e = jcast('int', Code07_HideSeek3.head[u])
        while (e > 0):
            v = jcast('int', Code07_HideSeek3.to[e])
            if (v != fa):
                Code07_HideSeek3.dfs1(v, u)
            e = jcast('int', Code07_HideSeek3.nxt[e])
        jset(Code07_HideSeek3.seg, ((_java_obj_10 := Code07_HideSeek3), (_java_key_11 := 'cntd'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code07_HideSeek3.PAR)

    # dfs1的迭代版
    @staticmethod
    def dfs2(cur, fa):
        cur = jcast('int', cur)
        fa = jcast('int', fa)
        Code07_HideSeek3.stacksize = jcast('int', 0)
        Code07_HideSeek3.push(cur, fa, jcast('int', (-1)))
        while (Code07_HideSeek3.stacksize > 0):
            Code07_HideSeek3.pop()
            if (Code07_HideSeek3.e == jcast('int', (-1))):
                jset(Code07_HideSeek3.seg, ((_java_obj_13 := Code07_HideSeek3), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code07_HideSeek3.PAL)
                jset(Code07_HideSeek3.seg, ((_java_obj_16 := Code07_HideSeek3), (_java_key_17 := 'cntd'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code07_HideSeek3.u)
                Code07_HideSeek3.dfn[Code07_HideSeek3.u] = jcast('int', Code07_HideSeek3.cntd)
                Code07_HideSeek3.e = jcast('int', Code07_HideSeek3.head[Code07_HideSeek3.u])
            else:
                Code07_HideSeek3.e = jcast('int', Code07_HideSeek3.nxt[Code07_HideSeek3.e])
            if (Code07_HideSeek3.e != 0):
                Code07_HideSeek3.push(Code07_HideSeek3.u, Code07_HideSeek3.f, Code07_HideSeek3.e)
                v = jcast('int', Code07_HideSeek3.to[Code07_HideSeek3.e])
                if (v != Code07_HideSeek3.f):
                    Code07_HideSeek3.push(v, Code07_HideSeek3.u, jcast('int', (-1)))
            else:
                jset(Code07_HideSeek3.seg, ((_java_obj_19 := Code07_HideSeek3), (_java_key_20 := 'cntd'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], Code07_HideSeek3.PAR)

    @staticmethod
    def up(i):
        i = jcast('int', i)
        pre = jcast('int', jcast('int', (i << (1 & 31))))
        post = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        if (Code07_HideSeek3.pl[pre] > Code07_HideSeek3.pr[post]):
            Code07_HideSeek3.pr[i] = jcast('int', Code07_HideSeek3.pr[pre])
            Code07_HideSeek3.pl[i] = jcast('int', jcast('int', jadd(jcast('int', (Code07_HideSeek3.pl[pre] - Code07_HideSeek3.pr[post])), Code07_HideSeek3.pl[post])))
        else:
            Code07_HideSeek3.pr[i] = jcast('int', jcast('int', (jcast('int', jadd(Code07_HideSeek3.pr[pre], Code07_HideSeek3.pr[post])) - Code07_HideSeek3.pl[pre])))
            Code07_HideSeek3.pl[i] = jcast('int', Code07_HideSeek3.pl[post])
        jset(Code07_HideSeek3.ladd, i, jstatic('Math', 'max', Code07_HideSeek3.ladd[pre], jstatic('Math', 'max', jcast('int', (jcast('int', jadd(Code07_HideSeek3.pr[pre], Code07_HideSeek3.ladd[post])) - Code07_HideSeek3.pl[pre])), jcast('int', jadd(jcast('int', jadd(Code07_HideSeek3.pr[pre], Code07_HideSeek3.pl[pre])), Code07_HideSeek3.lminus[post])))))
        jset(Code07_HideSeek3.lminus, i, jstatic('Math', 'max', Code07_HideSeek3.lminus[pre], jcast('int', jadd(jcast('int', (Code07_HideSeek3.pl[pre] - Code07_HideSeek3.pr[pre])), Code07_HideSeek3.lminus[post]))))
        jset(Code07_HideSeek3.radd, i, jstatic('Math', 'max', Code07_HideSeek3.radd[post], jstatic('Math', 'max', jcast('int', jadd(jcast('int', (Code07_HideSeek3.radd[pre] - Code07_HideSeek3.pr[post])), Code07_HideSeek3.pl[post])), jcast('int', jadd(jcast('int', jadd(Code07_HideSeek3.rminus[pre], Code07_HideSeek3.pr[post])), Code07_HideSeek3.pl[post])))))
        jset(Code07_HideSeek3.rminus, i, jstatic('Math', 'max', Code07_HideSeek3.rminus[post], jcast('int', (jcast('int', jadd(Code07_HideSeek3.rminus[pre], Code07_HideSeek3.pr[post])) - Code07_HideSeek3.pl[post]))))
        jset(Code07_HideSeek3.dist, i, jstatic('Math', 'max', jstatic('Math', 'max', Code07_HideSeek3.dist[pre], Code07_HideSeek3.dist[post]), jstatic('Math', 'max', jcast('int', jadd(Code07_HideSeek3.radd[pre], Code07_HideSeek3.lminus[post])), jcast('int', jadd(Code07_HideSeek3.rminus[pre], Code07_HideSeek3.ladd[post])))))

    @staticmethod
    def point(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code07_HideSeek3.pr, i, jset(Code07_HideSeek3.pl, i, 0))
        jset(Code07_HideSeek3.ladd, i, jset(Code07_HideSeek3.lminus, i, jset(Code07_HideSeek3.radd, i, jset(Code07_HideSeek3.rminus, i, jset(Code07_HideSeek3.dist, i, jcast('int', (-Code07_HideSeek3.INF)))))))
        if (v == Code07_HideSeek3.PAR):
            Code07_HideSeek3.pr[i] = jcast('int', 1)
        else:
            if (v == Code07_HideSeek3.PAL):
                Code07_HideSeek3.pl[i] = jcast('int', 1)
            else:
                if Code07_HideSeek3.black[v]:
                    jset(Code07_HideSeek3.ladd, i, jset(Code07_HideSeek3.lminus, i, jset(Code07_HideSeek3.radd, i, jset(Code07_HideSeek3.rminus, i, jset(Code07_HideSeek3.dist, i, 0)))))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code07_HideSeek3.point(i, Code07_HideSeek3.seg[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code07_HideSeek3.build(l, mid, jcast('int', (i << (1 & 31))))
            Code07_HideSeek3.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code07_HideSeek3.up(i)

    @staticmethod
    def update(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code07_HideSeek3.point(i, Code07_HideSeek3.seg[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code07_HideSeek3.update(jobi, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code07_HideSeek3.update(jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code07_HideSeek3.up(i)

    @staticmethod
    def main(args):
        in_ = Code07_HideSeek3.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_HideSeek3.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_HideSeek3.n):
            Code07_HideSeek3.black[i] = jcast('boolean', True)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code07_HideSeek3.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code07_HideSeek3.addEdge(u, v)
            Code07_HideSeek3.addEdge(v, u)
            i = jcast('int', (i + 1))
        # dfs1(1, 0);
        Code07_HideSeek3.dfs2(1, 0)
        Code07_HideSeek3.build(1, Code07_HideSeek3.cntd, 1)
        Code07_HideSeek3.m = jcast('int', jcall(in_, 'nextInt'))
        blackCnt = jcast('int', Code07_HideSeek3.n)
        op = jchar(0)
        i = jcast('int', 1)
        x = 0
        while (i <= Code07_HideSeek3.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            if (op == jchar('C')):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code07_HideSeek3.black[x] = jcast('boolean', (not Code07_HideSeek3.black[x]))
                if Code07_HideSeek3.black[x]:
                    blackCnt = jcast('int', (blackCnt + 1))
                else:
                    blackCnt = jcast('int', (blackCnt - 1))
                Code07_HideSeek3.update(Code07_HideSeek3.dfn[x], 1, Code07_HideSeek3.cntd, 1)
            else:
                if (blackCnt <= 1):
                    jcall(out, 'println', jcast('int', (blackCnt - 1)))
                else:
                    jcall(out, 'println', Code07_HideSeek3.dist[1])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_HideSeek3.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_HideSeek3.MAXN = jcast('int', 100001)
Code07_HideSeek3.MAXT = jcast('int', jcast('int', (Code07_HideSeek3.MAXN * 12)))
Code07_HideSeek3.INF = jcast('int', 1000000001)
Code07_HideSeek3.PAR = jcast('int', jcast('int', (-1)))
Code07_HideSeek3.PAL = jcast('int', jcast('int', (-2)))
Code07_HideSeek3.n = jcast('int', 0)
Code07_HideSeek3.m = jcast('int', 0)
Code07_HideSeek3.black = jarray('boolean', [Code07_HideSeek3.MAXN])
Code07_HideSeek3.head = jarray('int', [Code07_HideSeek3.MAXN])
Code07_HideSeek3.nxt = jarray('int', [jcast('int', (Code07_HideSeek3.MAXN << (1 & 31)))])
Code07_HideSeek3.to = jarray('int', [jcast('int', (Code07_HideSeek3.MAXN << (1 & 31)))])
Code07_HideSeek3.cntg = jcast('int', 0)
Code07_HideSeek3.dfn = jarray('int', [Code07_HideSeek3.MAXN])
Code07_HideSeek3.seg = jarray('int', [jcast('int', (Code07_HideSeek3.MAXN * 3))])
Code07_HideSeek3.cntd = jcast('int', 0)
Code07_HideSeek3.pr = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.pl = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.ladd = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.lminus = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.radd = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.rminus = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.dist = jarray('int', [Code07_HideSeek3.MAXT])
Code07_HideSeek3.stack = jarray('int', [Code07_HideSeek3.MAXN, 3])
Code07_HideSeek3.u = jcast('int', 0)
Code07_HideSeek3.f = jcast('int', 0)
Code07_HideSeek3.e = jcast('int', 0)
Code07_HideSeek3.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code07_HideSeek3.main([])

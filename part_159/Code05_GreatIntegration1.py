# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 大融合，Python版
# 一共有n个点，一共有q条操作，每条操作是如下两种类型中的一种
# 操作 A x y : 点x和点y之间连一条边，保证之前x和y是不联通的
# 操作 Q x y : 打印点x和点y之间这条边的负载，保证x和y之间有一条边
# 边负载定义为，这条边两侧端点各自连通区大小的乘积
# 1 <= n、q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4219
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_GreatIntegration1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'q': 'q', 'op': 'op', 'u': 'u', 'v': 'v', 'event': 'event', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'head': 'head', 'next': 'next', 'tox': 'tox', 'toy': 'toy', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    n = 0
    q = 0
    op = None
    u = None
    v = None
    # 端点x、端点y、操作序号t
    event = None
    father = None
    siz = None
    rollback = None
    opsize = 0
    head = None
    next = None
    tox = None
    toy = None
    cnt = 0
    ans = None
    @staticmethod
    def addEdge(i, x, y):
        i = jcast('int', i)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code05_GreatIntegration1.next, ((_java_obj_1 := Code05_GreatIntegration1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_GreatIntegration1.head[i])
        Code05_GreatIntegration1.tox[Code05_GreatIntegration1.cnt] = jcast('int', x)
        Code05_GreatIntegration1.toy[Code05_GreatIntegration1.cnt] = jcast('int', y)
        Code05_GreatIntegration1.head[i] = jcast('int', Code05_GreatIntegration1.cnt)

    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code05_GreatIntegration1.father[i]):
            i = jcast('int', Code05_GreatIntegration1.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code05_GreatIntegration1.find(x))
        fy = jcast('int', Code05_GreatIntegration1.find(y))
        if (Code05_GreatIntegration1.siz[fx] < Code05_GreatIntegration1.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code05_GreatIntegration1.father[fy] = jcast('int', fx)
        Code05_GreatIntegration1.siz[fx] = jcast('int', jcast('int', jadd(Code05_GreatIntegration1.siz[fx], Code05_GreatIntegration1.siz[fy])))
        jset(Code05_GreatIntegration1.rollback[((_java_obj_4 := Code05_GreatIntegration1), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, fx)
        jset(Code05_GreatIntegration1.rollback[Code05_GreatIntegration1.opsize], 1, fy)

    @staticmethod
    def undo():
        fx = jcast('int', Code05_GreatIntegration1.rollback[Code05_GreatIntegration1.opsize][0])
        fy = jcast('int', Code05_GreatIntegration1.rollback[((_java_obj_7 := Code05_GreatIntegration1), (_java_key_8 := 'opsize'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]][1])
        Code05_GreatIntegration1.father[fy] = jcast('int', fy)
        Code05_GreatIntegration1.siz[fx] = jcast('int', jcast('int', (Code05_GreatIntegration1.siz[fx] - Code05_GreatIntegration1.siz[fy])))

    @staticmethod
    def add(jobl, jobr, jobx, joby, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobx = jcast('int', jobx)
        joby = jcast('int', joby)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_GreatIntegration1.addEdge(i, jobx, joby)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_GreatIntegration1.add(jobl, jobr, jobx, joby, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_GreatIntegration1.add(jobl, jobr, jobx, joby, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        unionCnt = jcast('int', 0)
        ei = jcast('int', Code05_GreatIntegration1.head[i])
        while (ei > 0):
            Code05_GreatIntegration1.union(Code05_GreatIntegration1.tox[ei], Code05_GreatIntegration1.toy[ei])
            unionCnt = jcast('int', (unionCnt + 1))
            ei = jcast('int', Code05_GreatIntegration1.next[ei])
        if (l == r):
            if (Code05_GreatIntegration1.op[l] == 2):
                jset(Code05_GreatIntegration1.ans, l, jcast('long', (jcast('long', Code05_GreatIntegration1.siz[Code05_GreatIntegration1.find(Code05_GreatIntegration1.u[l])]) * Code05_GreatIntegration1.siz[Code05_GreatIntegration1.find(Code05_GreatIntegration1.v[l])])))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_GreatIntegration1.dfs(l, mid, jcast('int', (i << (1 & 31))))
            Code05_GreatIntegration1.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        k = jcast('int', 1)
        while (k <= unionCnt):
            Code05_GreatIntegration1.undo()
            k = jcast('int', (k + 1))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code05_GreatIntegration1.n):
            Code05_GreatIntegration1.father[i] = jcast('int', i)
            Code05_GreatIntegration1.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_GreatIntegration1.q):
            jset(Code05_GreatIntegration1.event[i], 0, Code05_GreatIntegration1.u[i])
            jset(Code05_GreatIntegration1.event[i], 1, Code05_GreatIntegration1.v[i])
            jset(Code05_GreatIntegration1.event[i], 2, i)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_GreatIntegration1.event, 1, jcast('int', jadd(Code05_GreatIntegration1.q, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else ((a[1] - b[1]) if (a[1] != b[1]) else (a[2] - b[2])))))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code05_GreatIntegration1.q):
            x = jcast('int', Code05_GreatIntegration1.event[l][0])
            y = jcast('int', Code05_GreatIntegration1.event[l][1])
            t = jcast('int', Code05_GreatIntegration1.event[l][2])
            while (((jcast('int', jadd(r, 1)) <= Code05_GreatIntegration1.q) and (Code05_GreatIntegration1.event[jcast('int', jadd(r, 1))][0] == x)) and (Code05_GreatIntegration1.event[jcast('int', jadd(r, 1))][1] == y)):
                r = jcast('int', (r + 1))
            i = jcast('int', jcast('int', jadd(l, 1)))
            while (i <= r):
                Code05_GreatIntegration1.add(t, jcast('int', (Code05_GreatIntegration1.event[i][2] - 1)), x, y, 1, Code05_GreatIntegration1.q, 1)
                t = jcast('int', jcast('int', jadd(Code05_GreatIntegration1.event[i][2], 1)))
                i = jcast('int', (i + 1))
            if (t <= Code05_GreatIntegration1.q):
                Code05_GreatIntegration1.add(t, Code05_GreatIntegration1.q, x, y, 1, Code05_GreatIntegration1.q, 1)
            l = jcast('int', (r := jcast('int', (r + (1)))))

    @staticmethod
    def main(args):
        in_ = Code05_GreatIntegration1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_GreatIntegration1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_GreatIntegration1.q = jcast('int', jcall(in_, 'nextInt'))
        t = jchar(0)
        x = 0
        y = 0
        i = jcast('int', 1)
        while (i <= Code05_GreatIntegration1.q):
            t = jcast('char', jcall(in_, 'nextChar'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            Code05_GreatIntegration1.op[i] = jcast('int', (1 if (t == jchar('A')) else 2))
            jset(Code05_GreatIntegration1.u, i, jstatic('Math', 'min', x, y))
            jset(Code05_GreatIntegration1.v, i, jstatic('Math', 'max', x, y))
            i = jcast('int', (i + 1))
        Code05_GreatIntegration1.prepare()
        Code05_GreatIntegration1.dfs(1, Code05_GreatIntegration1.q, 1)
        i = jcast('int', 1)
        while (i <= Code05_GreatIntegration1.q):
            if (Code05_GreatIntegration1.op[i] == 2):
                jcall(out, 'println', Code05_GreatIntegration1.ans[i])
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
            return jcast('byte', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code05_GreatIntegration1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_GreatIntegration1.MAXN = jcast('int', 100001)
Code05_GreatIntegration1.MAXT = jcast('int', 3000001)
Code05_GreatIntegration1.n = jcast('int', 0)
Code05_GreatIntegration1.q = jcast('int', 0)
Code05_GreatIntegration1.op = jarray('int', [Code05_GreatIntegration1.MAXN])
Code05_GreatIntegration1.u = jarray('int', [Code05_GreatIntegration1.MAXN])
Code05_GreatIntegration1.v = jarray('int', [Code05_GreatIntegration1.MAXN])
Code05_GreatIntegration1.event = jarray('int', [Code05_GreatIntegration1.MAXN, 3])
Code05_GreatIntegration1.father = jarray('int', [Code05_GreatIntegration1.MAXN])
Code05_GreatIntegration1.siz = jarray('int', [Code05_GreatIntegration1.MAXN])
Code05_GreatIntegration1.rollback = jarray('int', [Code05_GreatIntegration1.MAXN, 2])
Code05_GreatIntegration1.opsize = jcast('int', 0)
Code05_GreatIntegration1.head = jarray('int', [jcast('int', (Code05_GreatIntegration1.MAXN << (2 & 31)))])
Code05_GreatIntegration1.next = jarray('int', [Code05_GreatIntegration1.MAXT])
Code05_GreatIntegration1.tox = jarray('int', [Code05_GreatIntegration1.MAXT])
Code05_GreatIntegration1.toy = jarray('int', [Code05_GreatIntegration1.MAXT])
Code05_GreatIntegration1.cnt = jcast('int', 0)
Code05_GreatIntegration1.ans = jarray('long', [Code05_GreatIntegration1.MAXN])

if __name__ == '__main__':
    Code05_GreatIntegration1.main([])

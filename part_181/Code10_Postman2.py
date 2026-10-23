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

# 邮递员，Python版
# 一共n个点，m条有向边，不会有重边和自环
# 邮递员一定要从1号点开始，最后回到1号点，每条边都要走1次
# 邮递员依次走过的点的编号，就可以形成一个路径
# 给定t个序列，每个序列先给定长度k，然后是k个节点的编号
# 希望每个序列都是路径的连续子段，如果不存在这样的路径，打印"NIE"
# 如果存在这样的路径，先打印"TAK"，然后打印依次走过的节点编号
# 2 <= n <= 5 * 10^4    1 <= m <= 2 * 10^5
# 0 <= t <= 10^4        所有序列的节点总量 <= 2 * 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P3443
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code10_Postman2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'MAXC': 'MAXC', 'n': 'n', 'm': 'm', 't': 't', 'a': 'a', 'b': 'b', 'seq': 'seq', 'pairEdge': 'pairEdge', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'chainHead': 'chainHead', 'cntg': 'cntg', 'edgeCnt': 'edgeCnt', 'cur': 'cur', 'inDeg': 'inDeg', 'outDeg': 'outDeg', 'isHead': 'isHead', 'etoe': 'etoe', 'vis': 'vis', 'path': 'path', 'cntp': 'cntp', 'ans': 'ans', 'cnta': 'cnta', 'sta': 'sta', 'u': 'u', 'h': 'h', 'stacksize': 'stacksize'}
    class PairMap:
        __java_fields__ = {'map': 'map'}
        # map：实例字段，在构造函数中初始化。
        def key(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            return jcast('long', jcast('long', (jcast('long', (jcast('long', a) << (32 & 63))) | jcast('long', (b & 4294967295)))))

        def contains(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            return jcast('boolean', jcall(self.map, 'containsKey', self.key(a, b)))

        def isEmpty(self):
            return jcast('boolean', jcall(self.map, 'isEmpty'))

        def put(self, a, b, v):
            a = jcast('int', a)
            b = jcast('int', b)
            v = jcast('int', v)
            jcall(self.map, 'put', self.key(a, b), v)

        def get(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            return jcast('int', jcall(self.map, 'get', self.key(a, b)))

        def remove(self, a, b):
            a = jcast('int', a)
            b = jcast('int', b)
            jcall(self.map, 'remove', self.key(a, b))

        def clear(self):
            jcall(self.map, 'clear')

        def __init__(self, *args, _java_ctor=None):
            self.map = jnew('HashMap')
            if args:
                raise TypeError('This class has a no-argument constructor')


    MAXN = 0
    MAXM = 0
    MAXC = 0
    n = 0
    m = 0
    t = 0
    a = None
    b = None
    seq = None
    pairEdge = None
    headg = None
    nextg = None
    tog = None
    chainHead = None
    cntg = 0
    edgeCnt = 0
    cur = None
    inDeg = None
    outDeg = None
    isHead = None
    etoe = None
    vis = None
    path = None
    cntp = 0
    ans = None
    cnta = 0
    sta = None
    u = 0
    h = 0
    stacksize = 0
    @staticmethod
    def push(u, c):
        u = jcast('int', u)
        c = jcast('int', c)
        jset(Code10_Postman2.sta[Code10_Postman2.stacksize], 0, u)
        jset(Code10_Postman2.sta[Code10_Postman2.stacksize], 1, c)
        Code10_Postman2.stacksize = jcast('int', (Code10_Postman2.stacksize + 1))

    @staticmethod
    def pop():
        Code10_Postman2.stacksize = jcast('int', (Code10_Postman2.stacksize - 1))
        Code10_Postman2.u = jcast('int', Code10_Postman2.sta[Code10_Postman2.stacksize][0])
        Code10_Postman2.h = jcast('int', Code10_Postman2.sta[Code10_Postman2.stacksize][1])

    @staticmethod
    def addEdge(x, y, h):
        x = jcast('int', x)
        y = jcast('int', y)
        h = jcast('int', h)
        jset(Code10_Postman2.nextg, ((_java_obj_1 := Code10_Postman2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code10_Postman2.headg[x])
        Code10_Postman2.tog[Code10_Postman2.cntg] = jcast('int', y)
        Code10_Postman2.chainHead[Code10_Postman2.cntg] = jcast('int', h)
        Code10_Postman2.headg[x] = jcast('int', Code10_Postman2.cntg)

    @staticmethod
    def linkEdge():
        i = jcast('int', 1)
        while (i <= Code10_Postman2.m):
            jcall(Code10_Postman2.pairEdge, 'put', Code10_Postman2.a[i], Code10_Postman2.b[i], i)
            Code10_Postman2.isHead[i] = jcast('boolean', True)
            i = jcast('int', (i + 1))
        siz = jcast('int', Code10_Postman2.seq[1])
        l = jcast('int', 2)
        r = jcast('int', jcast('int', (jcast('int', jadd(l, siz)) - 1)))
        a = 0
        b = 0
        ledge = 0
        redge = 0
        while (siz > 0):
            ledge = jcast('int', 0)
            i = jcast('int', l)
            while (i < r):
                a = jcast('int', Code10_Postman2.seq[i])
                b = jcast('int', Code10_Postman2.seq[jcast('int', jadd(i, 1))])
                if (not jcall(Code10_Postman2.pairEdge, 'contains', a, b)):
                    return jcast('boolean', False)
                redge = jcast('int', jcall(Code10_Postman2.pairEdge, 'get', a, b))
                if (ledge != 0):
                    if ((Code10_Postman2.etoe[ledge] != 0) and (Code10_Postman2.etoe[ledge] != redge)):
                        return jcast('boolean', False)
                    Code10_Postman2.etoe[ledge] = jcast('int', redge)
                    Code10_Postman2.isHead[redge] = jcast('boolean', False)
                ledge = jcast('int', redge)
                i = jcast('int', (i + 1))
            siz = jcast('int', Code10_Postman2.seq[jcast('int', jadd(r, 1))])
            l = jcast('int', jcast('int', jadd(r, 2)))
            r = jcast('int', jcast('int', (jcast('int', jadd(l, siz)) - 1)))
        return jcast('boolean', True)

    @staticmethod
    def getLinkEnd(edge):
        edge = jcast('int', edge)
        while (Code10_Postman2.etoe[edge] != 0):
            if (Code10_Postman2.vis[edge] == True):
                return jcast('int', jcast('int', (-1)))
            Code10_Postman2.vis[edge] = jcast('boolean', True)
            edge = jcast('int', Code10_Postman2.etoe[edge])
        return jcast('int', edge)

    @staticmethod
    def compress():
        i = jcast('int', 1)
        while (i <= Code10_Postman2.m):
            if Code10_Postman2.isHead[i]:
                x = jcast('int', Code10_Postman2.a[i])
                y = jcast('int', Code10_Postman2.b[i])
                if (Code10_Postman2.etoe[i] != 0):
                    end = jcast('int', Code10_Postman2.getLinkEnd(i))
                    if (end == jcast('int', (-1))):
                        return jcast('boolean', False)
                    y = jcast('int', Code10_Postman2.b[end])
                Code10_Postman2.outDeg[x] = jcast('int', (Code10_Postman2.outDeg[x] + 1))
                Code10_Postman2.inDeg[y] = jcast('int', (Code10_Postman2.inDeg[y] + 1))
                Code10_Postman2.edgeCnt = jcast('int', (Code10_Postman2.edgeCnt + 1))
                Code10_Postman2.addEdge(x, y, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code10_Postman2.n):
            if (Code10_Postman2.inDeg[i] != Code10_Postman2.outDeg[i]):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code10_Postman2.n):
            Code10_Postman2.cur[i] = jcast('int', Code10_Postman2.headg[i])
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    # 递归版，u表示当前节点，h表示来到当前节点的链，链头是什么边的序号
    @staticmethod
    def euler1(u, h):
        u = jcast('int', u)
        h = jcast('int', h)
        e = jcast('int', Code10_Postman2.cur[u])
        while (e > 0):
            Code10_Postman2.cur[u] = jcast('int', Code10_Postman2.nextg[e])
            Code10_Postman2.euler1(Code10_Postman2.tog[e], Code10_Postman2.chainHead[e])
            e = jcast('int', Code10_Postman2.cur[u])
        jset(Code10_Postman2.path, ((_java_obj_4 := Code10_Postman2), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], h)

    # 迭代版
    @staticmethod
    def euler2(node, chainh):
        node = jcast('int', node)
        chainh = jcast('int', chainh)
        Code10_Postman2.stacksize = jcast('int', 0)
        Code10_Postman2.push(node, chainh)
        while (Code10_Postman2.stacksize > 0):
            Code10_Postman2.pop()
            e = jcast('int', Code10_Postman2.cur[Code10_Postman2.u])
            if (e > 0):
                Code10_Postman2.cur[Code10_Postman2.u] = jcast('int', Code10_Postman2.nextg[e])
                Code10_Postman2.push(Code10_Postman2.u, Code10_Postman2.h)
                Code10_Postman2.push(Code10_Postman2.tog[e], Code10_Postman2.chainHead[e])
            else:
                jset(Code10_Postman2.path, ((_java_obj_7 := Code10_Postman2), (_java_key_8 := 'cntp'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code10_Postman2.h)

    @staticmethod
    def decompress():
        jset(Code10_Postman2.ans, ((_java_obj_10 := Code10_Postman2), (_java_key_11 := 'cnta'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], 1)
        i = jcast('int', jcast('int', (Code10_Postman2.cntp - 1)))
        while (i >= 1):
            e = jcast('int', Code10_Postman2.path[i])
            while (e > 0):
                jset(Code10_Postman2.ans, ((_java_obj_13 := Code10_Postman2), (_java_key_14 := 'cnta'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], Code10_Postman2.b[e])
                e = jcast('int', Code10_Postman2.etoe[e])
            i = jcast('int', (i - 1))

    @staticmethod
    def compute():
        if (not Code10_Postman2.linkEdge()):
            return jcast('boolean', False)
        if (not Code10_Postman2.compress()):
            return jcast('boolean', False)
        # euler1(1, -1);
        Code10_Postman2.euler2(1, jcast('int', (-1)))
        if (Code10_Postman2.cntp != jcast('int', jadd(Code10_Postman2.edgeCnt, 1))):
            return jcast('boolean', False)
        Code10_Postman2.decompress()
        return jcast('boolean', (Code10_Postman2.cnta == jcast('int', jadd(Code10_Postman2.m, 1))))

    @staticmethod
    def main(args):
        in_ = Code10_Postman2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code10_Postman2.n = jcast('int', jcall(in_, 'nextInt'))
        Code10_Postman2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code10_Postman2.m):
            jset(Code10_Postman2.a, i, jcall(in_, 'nextInt'))
            jset(Code10_Postman2.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code10_Postman2.t = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        siz = 0
        idx = jcast('int', 0)
        while (i <= Code10_Postman2.t):
            siz = jcast('int', jcall(in_, 'nextInt'))
            jset(Code10_Postman2.seq, (idx := jcast('int', (idx + (1)))), siz)
            j = jcast('int', 1)
            while (j <= siz):
                jset(Code10_Postman2.seq, (idx := jcast('int', (idx + (1)))), jcall(in_, 'nextInt'))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        check = jcast('boolean', Code10_Postman2.compute())
        if (not check):
            jcall(out, 'println', 'NIE')
        else:
            jcall(out, 'println', 'TAK')
            i = jcast('int', 1)
            while (i <= Code10_Postman2.cnta):
                jcall(out, 'println', Code10_Postman2.ans[i])
                i = jcast('int', (i + 1))
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
            raise TypeError("No matching overload for Code10_Postman2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code10_Postman2.MAXN = jcast('int', 50005)
Code10_Postman2.MAXM = jcast('int', 200005)
Code10_Postman2.MAXC = jcast('int', 2000005)
Code10_Postman2.n = jcast('int', 0)
Code10_Postman2.m = jcast('int', 0)
Code10_Postman2.t = jcast('int', 0)
Code10_Postman2.a = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.b = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.seq = jarray('int', [Code10_Postman2.MAXC])
Code10_Postman2.pairEdge = Code10_Postman2.PairMap()
Code10_Postman2.headg = jarray('int', [Code10_Postman2.MAXN])
Code10_Postman2.nextg = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.tog = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.chainHead = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.cntg = jcast('int', 0)
Code10_Postman2.edgeCnt = jcast('int', 0)
Code10_Postman2.cur = jarray('int', [Code10_Postman2.MAXN])
Code10_Postman2.inDeg = jarray('int', [Code10_Postman2.MAXN])
Code10_Postman2.outDeg = jarray('int', [Code10_Postman2.MAXN])
Code10_Postman2.isHead = jarray('boolean', [Code10_Postman2.MAXM])
Code10_Postman2.etoe = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.vis = jarray('boolean', [Code10_Postman2.MAXM])
Code10_Postman2.path = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.cntp = jcast('int', 0)
Code10_Postman2.ans = jarray('int', [Code10_Postman2.MAXM])
Code10_Postman2.cnta = jcast('int', 0)
Code10_Postman2.sta = jarray('int', [Code10_Postman2.MAXM, 2])
Code10_Postman2.u = jcast('int', 0)
Code10_Postman2.h = jcast('int', 0)
Code10_Postman2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code10_Postman2.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 无向图的欧拉路径，Python版
# 图中给定m条无向边，每条边给出两个端点
# 如果存在欧拉路径，输出字典序最小的结果，如果不存在打印No
# 节点编号的范围是[1, 500]，所有点不一定都出现，以给定的边为准
# 1 <= m <= 1024
# 测试链接 : https://www.luogu.com.cn/problem/P2731
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_UndirectedEuler1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'k': 'k', 'edgeArr': 'edgeArr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'eid': 'eid', 'cntg': 'cntg', 'cur': 'cur', 'deg': 'deg', 'vis': 'vis', 'path': 'path', 'cntp': 'cntp', 'sta': 'sta', 'top': 'top'}
    class EdgeCmp:
        __java_fields__ = {}
        def compare(self, e1, e2):
            return jcast('int', (jcast('int', (e1[0] - e2[0])) if (e1[0] != e2[0]) else jcast('int', (e1[1] - e2[1]))))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    k = 0
    edgeArr = None
    head = None
    nxt = None
    to = None
    eid = None
    cntg = 0
    cur = None
    deg = None
    vis = None
    path = None
    cntp = 0
    @staticmethod
    def addEdge(u, v, id):
        u = jcast('int', u)
        v = jcast('int', v)
        id = jcast('int', id)
        jset(Code02_UndirectedEuler1.nxt, ((_java_obj_1 := Code02_UndirectedEuler1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_UndirectedEuler1.head[u])
        Code02_UndirectedEuler1.to[Code02_UndirectedEuler1.cntg] = jcast('int', v)
        Code02_UndirectedEuler1.eid[Code02_UndirectedEuler1.cntg] = jcast('int', id)
        Code02_UndirectedEuler1.head[u] = jcast('int', Code02_UndirectedEuler1.cntg)

    @staticmethod
    def connect():
        jstatic('Arrays', 'sort', Code02_UndirectedEuler1.edgeArr, 1, jcast('int', jadd(Code02_UndirectedEuler1.k, 1)), Code02_UndirectedEuler1.EdgeCmp())
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code02_UndirectedEuler1.k):
            while ((jcast('int', jadd(r, 1)) <= Code02_UndirectedEuler1.k) and (Code02_UndirectedEuler1.edgeArr[l][0] == Code02_UndirectedEuler1.edgeArr[jcast('int', jadd(r, 1))][0])):
                r = jcast('int', (r + 1))
            i = jcast('int', r)
            u = 0
            v = 0
            id = 0
            while (i >= l):
                u = jcast('int', Code02_UndirectedEuler1.edgeArr[i][0])
                v = jcast('int', Code02_UndirectedEuler1.edgeArr[i][1])
                id = jcast('int', Code02_UndirectedEuler1.edgeArr[i][2])
                Code02_UndirectedEuler1.deg[u] = jcast('int', (Code02_UndirectedEuler1.deg[u] + 1))
                Code02_UndirectedEuler1.addEdge(u, v, id)
                i = jcast('int', (i - 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))
        i = jcast('int', 1)
        while (i <= Code02_UndirectedEuler1.n):
            Code02_UndirectedEuler1.cur[i] = jcast('int', Code02_UndirectedEuler1.head[i])
            i = jcast('int', (i + 1))

    # 无向图中找到一个起点，去生成欧拉回路 或者 欧拉路径
    @staticmethod
    def undirectedStart():
        odd = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_UndirectedEuler1.n):
            if (jcast('int', (Code02_UndirectedEuler1.deg[i] & 1)) == 1):
                odd = jcast('int', (odd + 1))
            i = jcast('int', (i + 1))
        if ((odd != 0) and (odd != 2)):
            return jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code02_UndirectedEuler1.n):
            if ((odd == 0) and (Code02_UndirectedEuler1.deg[i] > 0)):
                return jcast('int', i)
            if ((odd == 2) and (jcast('int', (Code02_UndirectedEuler1.deg[i] & 1)) == 1)):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    # Hierholzer算法递归版
    @staticmethod
    def euler1(u):
        u = jcast('int', u)
        e = jcast('int', Code02_UndirectedEuler1.cur[u])
        while (e > 0):
            Code02_UndirectedEuler1.cur[u] = jcast('int', Code02_UndirectedEuler1.nxt[e])
            if (not Code02_UndirectedEuler1.vis[Code02_UndirectedEuler1.eid[e]]):
                jset(Code02_UndirectedEuler1.vis, Code02_UndirectedEuler1.eid[e], True)
                Code02_UndirectedEuler1.euler1(Code02_UndirectedEuler1.to[e])
            e = jcast('int', Code02_UndirectedEuler1.cur[u])
        jset(Code02_UndirectedEuler1.path, ((_java_obj_4 := Code02_UndirectedEuler1), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)

    # Hierholzer算法迭代版
    sta = None
    top = 0
    @staticmethod
    def euler2(node):
        node = jcast('int', node)
        Code02_UndirectedEuler1.top = jcast('int', 0)
        jset(Code02_UndirectedEuler1.sta, ((_java_obj_7 := Code02_UndirectedEuler1), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], node)
        while (Code02_UndirectedEuler1.top > 0):
            u = jcast('int', Code02_UndirectedEuler1.sta[((_java_obj_10 := Code02_UndirectedEuler1), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
            e = jcast('int', Code02_UndirectedEuler1.cur[u])
            if (e != 0):
                Code02_UndirectedEuler1.cur[u] = jcast('int', Code02_UndirectedEuler1.nxt[e])
                if (not Code02_UndirectedEuler1.vis[Code02_UndirectedEuler1.eid[e]]):
                    jset(Code02_UndirectedEuler1.vis, Code02_UndirectedEuler1.eid[e], True)
                    jset(Code02_UndirectedEuler1.sta, ((_java_obj_13 := Code02_UndirectedEuler1), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], u)
                    jset(Code02_UndirectedEuler1.sta, ((_java_obj_16 := Code02_UndirectedEuler1), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code02_UndirectedEuler1.to[e])
                else:
                    jset(Code02_UndirectedEuler1.sta, ((_java_obj_19 := Code02_UndirectedEuler1), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], u)
            else:
                jset(Code02_UndirectedEuler1.path, ((_java_obj_22 := Code02_UndirectedEuler1), (_java_key_23 := 'cntp'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], u)

    @staticmethod
    def main(args):
        in_ = Code02_UndirectedEuler1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_UndirectedEuler1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_UndirectedEuler1.k = jcast('int', 0)
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code02_UndirectedEuler1.m):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            jset(Code02_UndirectedEuler1.edgeArr[((_java_obj_25 := Code02_UndirectedEuler1), (_java_key_26 := 'k'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3]], 0, u)
            jset(Code02_UndirectedEuler1.edgeArr[Code02_UndirectedEuler1.k], 1, v)
            jset(Code02_UndirectedEuler1.edgeArr[Code02_UndirectedEuler1.k], 2, i)
            jset(Code02_UndirectedEuler1.edgeArr[((_java_obj_28 := Code02_UndirectedEuler1), (_java_key_29 := 'k'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3]], 0, v)
            jset(Code02_UndirectedEuler1.edgeArr[Code02_UndirectedEuler1.k], 1, u)
            jset(Code02_UndirectedEuler1.edgeArr[Code02_UndirectedEuler1.k], 2, i)
            i = jcast('int', (i + 1))
        Code02_UndirectedEuler1.connect()
        start = jcast('int', Code02_UndirectedEuler1.undirectedStart())
        if (start == jcast('int', (-1))):
            jcall(out, 'println', 'No')
        else:
            # euler1(start);
            Code02_UndirectedEuler1.euler2(start)
            if (Code02_UndirectedEuler1.cntp != jcast('int', jadd(Code02_UndirectedEuler1.m, 1))):
                jcall(out, 'println', 'No')
            else:
                i = jcast('int', Code02_UndirectedEuler1.cntp)
                while (i >= 1):
                    jcall(out, 'println', Code02_UndirectedEuler1.path[i])
                    i = jcast('int', (i - 1))
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
            return jcast('int', self.buffer[((_java_obj_31 := self), (_java_key_32 := 'ptr'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))), _java_old_33)[4]])

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
            raise TypeError("No matching overload for Code02_UndirectedEuler1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_UndirectedEuler1.MAXN = jcast('int', 501)
Code02_UndirectedEuler1.MAXM = jcast('int', 2001)
Code02_UndirectedEuler1.n = jcast('int', 500)
Code02_UndirectedEuler1.m = jcast('int', 0)
Code02_UndirectedEuler1.k = jcast('int', 0)
Code02_UndirectedEuler1.edgeArr = jarray('int', [jcast('int', (Code02_UndirectedEuler1.MAXM << (1 & 31))), 3])
Code02_UndirectedEuler1.head = jarray('int', [Code02_UndirectedEuler1.MAXN])
Code02_UndirectedEuler1.nxt = jarray('int', [jcast('int', (Code02_UndirectedEuler1.MAXM << (1 & 31)))])
Code02_UndirectedEuler1.to = jarray('int', [jcast('int', (Code02_UndirectedEuler1.MAXM << (1 & 31)))])
Code02_UndirectedEuler1.eid = jarray('int', [jcast('int', (Code02_UndirectedEuler1.MAXM << (1 & 31)))])
Code02_UndirectedEuler1.cntg = jcast('int', 0)
Code02_UndirectedEuler1.cur = jarray('int', [Code02_UndirectedEuler1.MAXN])
Code02_UndirectedEuler1.deg = jarray('int', [Code02_UndirectedEuler1.MAXN])
Code02_UndirectedEuler1.vis = jarray('boolean', [Code02_UndirectedEuler1.MAXM])
Code02_UndirectedEuler1.path = jarray('int', [Code02_UndirectedEuler1.MAXM])
Code02_UndirectedEuler1.cntp = jcast('int', 0)
Code02_UndirectedEuler1.sta = jarray('int', [Code02_UndirectedEuler1.MAXM])
Code02_UndirectedEuler1.top = jcast('int', 0)

if __name__ == '__main__':
    Code02_UndirectedEuler1.main([])

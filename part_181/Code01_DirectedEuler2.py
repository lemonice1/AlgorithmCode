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

# 有向图的欧拉路径，Python版
# 图中有n个点，m条有向边，每条边给出两个端点
# 如果存在欧拉路径，输出字典序最小的结果，如果不存在打印No
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P7771
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DirectedEuler2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'edgeArr': 'edgeArr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'cur': 'cur', 'outDeg': 'outDeg', 'inDeg': 'inDeg', 'path': 'path', 'cntp': 'cntp', 'sta': 'sta', 'top': 'top'}
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
    edgeArr = None
    head = None
    nxt = None
    to = None
    cntg = 0
    cur = None
    outDeg = None
    inDeg = None
    path = None
    cntp = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code01_DirectedEuler2.nxt, ((_java_obj_1 := Code01_DirectedEuler2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_DirectedEuler2.head[u])
        Code01_DirectedEuler2.to[Code01_DirectedEuler2.cntg] = jcast('int', v)
        Code01_DirectedEuler2.head[u] = jcast('int', Code01_DirectedEuler2.cntg)

    @staticmethod
    def connect():
        jstatic('Arrays', 'sort', Code01_DirectedEuler2.edgeArr, 1, jcast('int', jadd(Code01_DirectedEuler2.m, 1)), Code01_DirectedEuler2.EdgeCmp())
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code01_DirectedEuler2.m):
            while ((jcast('int', jadd(r, 1)) <= Code01_DirectedEuler2.m) and (Code01_DirectedEuler2.edgeArr[l][0] == Code01_DirectedEuler2.edgeArr[jcast('int', jadd(r, 1))][0])):
                r = jcast('int', (r + 1))
            i = jcast('int', r)
            u = 0
            v = 0
            while (i >= l):
                u = jcast('int', Code01_DirectedEuler2.edgeArr[i][0])
                v = jcast('int', Code01_DirectedEuler2.edgeArr[i][1])
                Code01_DirectedEuler2.outDeg[u] = jcast('int', (Code01_DirectedEuler2.outDeg[u] + 1))
                Code01_DirectedEuler2.inDeg[v] = jcast('int', (Code01_DirectedEuler2.inDeg[v] + 1))
                Code01_DirectedEuler2.addEdge(u, v)
                i = jcast('int', (i - 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))
        i = jcast('int', 1)
        while (i <= Code01_DirectedEuler2.n):
            Code01_DirectedEuler2.cur[i] = jcast('int', Code01_DirectedEuler2.head[i])
            i = jcast('int', (i + 1))

    # 有向图中找到一个起点，去生成欧拉回路 或者 欧拉路径
    @staticmethod
    def directedStart():
        start = jcast('int', jcast('int', (-1)))
        end = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code01_DirectedEuler2.n):
            v = jcast('int', jcast('int', (Code01_DirectedEuler2.outDeg[i] - Code01_DirectedEuler2.inDeg[i])))
            if ((((v < jcast('int', (-1))) or (v > 1)) or ((v == 1) and (start != jcast('int', (-1))))) or ((v == jcast('int', (-1))) and (end != jcast('int', (-1))))):
                return jcast('int', jcast('int', (-1)))
            if (v == 1):
                start = jcast('int', i)
            if (v == jcast('int', (-1))):
                end = jcast('int', i)
            i = jcast('int', (i + 1))
        if ((start == jcast('int', (-1))) ^ (end == jcast('int', (-1)))):
            return jcast('int', jcast('int', (-1)))
        if (start != jcast('int', (-1))):
            return jcast('int', start)
        i = jcast('int', 1)
        while (i <= Code01_DirectedEuler2.n):
            if (Code01_DirectedEuler2.outDeg[i] > 0):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    # Hierholzer算法递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def euler1(u):
        u = jcast('int', u)
        e = jcast('int', Code01_DirectedEuler2.cur[u])
        while (e > 0):
            Code01_DirectedEuler2.cur[u] = jcast('int', Code01_DirectedEuler2.nxt[e])
            Code01_DirectedEuler2.euler1(Code01_DirectedEuler2.to[e])
            e = jcast('int', Code01_DirectedEuler2.cur[u])
        jset(Code01_DirectedEuler2.path, ((_java_obj_4 := Code01_DirectedEuler2), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], u)

    # Hierholzer算法迭代版
    sta = None
    top = 0
    @staticmethod
    def euler2(node):
        node = jcast('int', node)
        Code01_DirectedEuler2.top = jcast('int', 0)
        jset(Code01_DirectedEuler2.sta, ((_java_obj_7 := Code01_DirectedEuler2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], node)
        while (Code01_DirectedEuler2.top > 0):
            u = jcast('int', Code01_DirectedEuler2.sta[((_java_obj_10 := Code01_DirectedEuler2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
            e = jcast('int', Code01_DirectedEuler2.cur[u])
            if (e != 0):
                Code01_DirectedEuler2.cur[u] = jcast('int', Code01_DirectedEuler2.nxt[e])
                jset(Code01_DirectedEuler2.sta, ((_java_obj_13 := Code01_DirectedEuler2), (_java_key_14 := 'top'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], u)
                jset(Code01_DirectedEuler2.sta, ((_java_obj_16 := Code01_DirectedEuler2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code01_DirectedEuler2.to[e])
            else:
                jset(Code01_DirectedEuler2.path, ((_java_obj_19 := Code01_DirectedEuler2), (_java_key_20 := 'cntp'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))))[3], u)

    @staticmethod
    def main(args):
        in_ = Code01_DirectedEuler2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_DirectedEuler2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_DirectedEuler2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_DirectedEuler2.m):
            jset(Code01_DirectedEuler2.edgeArr[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_DirectedEuler2.edgeArr[i], 1, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_DirectedEuler2.connect()
        start = jcast('int', Code01_DirectedEuler2.directedStart())
        if (start == jcast('int', (-1))):
            jcall(out, 'println', 'No')
        else:
            # euler1(start);
            Code01_DirectedEuler2.euler2(start)
            if (Code01_DirectedEuler2.cntp != jcast('int', jadd(Code01_DirectedEuler2.m, 1))):
                jcall(out, 'println', 'No')
            else:
                i = jcast('int', Code01_DirectedEuler2.cntp)
                while (i >= 1):
                    jcall(out, 'print', jadd(Code01_DirectedEuler2.path[i], ' '))
                    i = jcast('int', (i - 1))
                jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_22 := self), (_java_key_23 := 'ptr'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))), _java_old_24)[4]])

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
            raise TypeError("No matching overload for Code01_DirectedEuler2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DirectedEuler2.MAXN = jcast('int', 100001)
Code01_DirectedEuler2.MAXM = jcast('int', 200002)
Code01_DirectedEuler2.n = jcast('int', 0)
Code01_DirectedEuler2.m = jcast('int', 0)
Code01_DirectedEuler2.edgeArr = jarray('int', [Code01_DirectedEuler2.MAXM, 2])
Code01_DirectedEuler2.head = jarray('int', [Code01_DirectedEuler2.MAXN])
Code01_DirectedEuler2.nxt = jarray('int', [Code01_DirectedEuler2.MAXM])
Code01_DirectedEuler2.to = jarray('int', [Code01_DirectedEuler2.MAXM])
Code01_DirectedEuler2.cntg = jcast('int', 0)
Code01_DirectedEuler2.cur = jarray('int', [Code01_DirectedEuler2.MAXN])
Code01_DirectedEuler2.outDeg = jarray('int', [Code01_DirectedEuler2.MAXN])
Code01_DirectedEuler2.inDeg = jarray('int', [Code01_DirectedEuler2.MAXN])
Code01_DirectedEuler2.path = jarray('int', [Code01_DirectedEuler2.MAXM])
Code01_DirectedEuler2.cntp = jcast('int', 0)
Code01_DirectedEuler2.sta = jarray('int', [Code01_DirectedEuler2.MAXM])
Code01_DirectedEuler2.top = jcast('int', 0)

if __name__ == '__main__':
    Code01_DirectedEuler2.main([])

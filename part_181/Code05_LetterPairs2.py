# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 无序字母对，Python版
# 给定n个字母对，每个字母对有两个字母，字母只可能是A~Z、a~z
# 字母对内部不区分顺序，ab和ba是相同的，但是区分大小写，Ab和ab是不同的
# 题目不会给定重复的字母对，构造一个长度n+1的字符串，让每个字母对都出现
# 一个字母对的两个字母，在字符串中相邻出现即可，请输出字典序最小的方案
# 如果没有满足要求的方案，打印"No Solution"
# 1 <= n <= 1326
# 测试链接 : https://www.luogu.com.cn/problem/P1341
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_LetterPairs2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'arr': 'arr', 'graph': 'graph', 'deg': 'deg', 'cur': 'cur', 'path': 'path', 'cntp': 'cntp'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    arr = None
    graph = None
    deg = None
    cur = None
    path = None
    cntp = 0
    @staticmethod
    def getInt(c):
        c = jcast('char', c)
        return jcast('int', (jcast('int', jadd(jcast('int', (c - jchar('A'))), 1)) if (c <= jchar('Z')) else jcast('int', jadd(jcast('int', (c - jchar('a'))), 27))))

    @staticmethod
    def getChar(v):
        v = jcast('int', v)
        return jcast('char', jcast('char', (jcast('int', (jcast('int', jadd(jchar('A'), v)) - 1)) if (v <= 26) else jcast('int', (jcast('int', jadd(jchar('a'), v)) - 27)))))

    @staticmethod
    def connect():
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= Code05_LetterPairs2.m):
            u = jcast('int', Code05_LetterPairs2.getInt(Code05_LetterPairs2.arr[i][0]))
            v = jcast('int', Code05_LetterPairs2.getInt(Code05_LetterPairs2.arr[i][1]))
            ((_java_obj_1 := Code05_LetterPairs2.graph[u]), (_java_key_2 := v), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            ((_java_obj_4 := Code05_LetterPairs2.graph[v]), (_java_key_5 := u), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
            Code05_LetterPairs2.deg[u] = jcast('int', (Code05_LetterPairs2.deg[u] + 1))
            Code05_LetterPairs2.deg[v] = jcast('int', (Code05_LetterPairs2.deg[v] + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_LetterPairs2.n):
            Code05_LetterPairs2.cur[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def undirectedStart():
        odd = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_LetterPairs2.n):
            if (jcast('int', (Code05_LetterPairs2.deg[i] & 1)) == 1):
                odd = jcast('int', (odd + 1))
            i = jcast('int', (i + 1))
        if ((odd != 0) and (odd != 2)):
            return jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code05_LetterPairs2.n):
            if ((odd == 0) and (Code05_LetterPairs2.deg[i] > 0)):
                return jcast('int', i)
            if ((odd == 2) and (jcast('int', (Code05_LetterPairs2.deg[i] & 1)) == 1)):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def euler(u):
        u = jcast('int', u)
        v = jcast('int', Code05_LetterPairs2.cur[u])
        while (v <= Code05_LetterPairs2.n):
            Code05_LetterPairs2.cur[u] = jcast('int', (Code05_LetterPairs2.cur[u] + 1))
            if (Code05_LetterPairs2.graph[u][v] > 0):
                ((_java_obj_7 := Code05_LetterPairs2.graph[u]), (_java_key_8 := v), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
                ((_java_obj_10 := Code05_LetterPairs2.graph[v]), (_java_key_11 := u), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]
                Code05_LetterPairs2.euler(v)
            v = jcast('int', Code05_LetterPairs2.cur[u])
        jset(Code05_LetterPairs2.path, ((_java_obj_13 := Code05_LetterPairs2), (_java_key_14 := 'cntp'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], u)

    @staticmethod
    def main(args):
        in_ = Code05_LetterPairs2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_LetterPairs2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_LetterPairs2.m):
            jset(Code05_LetterPairs2.arr[i], 0, jcall(in_, 'nextChar'))
            jset(Code05_LetterPairs2.arr[i], 1, jcall(in_, 'nextChar'))
            i = jcast('int', (i + 1))
        Code05_LetterPairs2.connect()
        start = jcast('int', Code05_LetterPairs2.undirectedStart())
        if (start == jcast('int', (-1))):
            jcall(out, 'println', 'No Solution')
        else:
            Code05_LetterPairs2.euler(start)
            if (Code05_LetterPairs2.cntp != jcast('int', jadd(Code05_LetterPairs2.m, 1))):
                jcall(out, 'println', 'No Solution')
            else:
                i = jcast('int', Code05_LetterPairs2.cntp)
                while (i >= 1):
                    jcall(out, 'print', Code05_LetterPairs2.getChar(Code05_LetterPairs2.path[i]))
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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((not (((c >= jchar('A')) and (c <= jchar('Z'))) or ((c >= jchar('a')) and (c <= jchar('z')))))):
                    break
            return jcast('char', jcast('char', c))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_LetterPairs2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_LetterPairs2.MAXN = jcast('int', 53)
Code05_LetterPairs2.MAXM = jcast('int', 2001)
Code05_LetterPairs2.n = jcast('int', 52)
Code05_LetterPairs2.m = jcast('int', 0)
Code05_LetterPairs2.arr = jarray('char', [Code05_LetterPairs2.MAXM, 2])
Code05_LetterPairs2.graph = jarray('int', [Code05_LetterPairs2.MAXN, Code05_LetterPairs2.MAXN])
Code05_LetterPairs2.deg = jarray('int', [Code05_LetterPairs2.MAXN])
Code05_LetterPairs2.cur = jarray('int', [Code05_LetterPairs2.MAXN])
Code05_LetterPairs2.path = jarray('int', [Code05_LetterPairs2.MAXM])
Code05_LetterPairs2.cntp = jcast('int', 0)

if __name__ == '__main__':
    Code05_LetterPairs2.main([])

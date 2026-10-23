# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 词链，Python版
# 给定n个由小写字母组成的单词，想把所有单词串成一个词链
# 同时要求前一个单词的结尾字符 == 后一个单词的开头字符
# 比如词链，aloha.arachnid.dog.gopher.rat.tiger
# 需要使用每个输入的单词恰好一次，同一单词出现k次就要用k次
# 返回字典序最小的结果，注意 . 的字典序 < 小写字母的字典序
# 如果不存在合法词链，输出***
# 1 <= n <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P1127
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_WordChain1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'str': 'str', 'a': 'a', 'b': 'b', 'eidArr': 'eidArr', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'weight': 'weight', 'cntg': 'cntg', 'cur': 'cur', 'outDeg': 'outDeg', 'inDeg': 'inDeg', 'path': 'path', 'cntp': 'cntp'}
    class EdgeCmp:
        __java_fields__ = {}
        def compare(self, i, j):
            if (Code04_WordChain1.a[i] != Code04_WordChain1.a[j]):
                return jcast('int', jcast('int', (Code04_WordChain1.a[i] - Code04_WordChain1.a[j])))
            return jcast('int', jcall(Code04_WordChain1.str[i], 'compareTo', Code04_WordChain1.str[j]))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    str = None
    a = None
    b = None
    eidArr = None
    head = None
    nxt = None
    to = None
    weight = None
    cntg = 0
    cur = None
    outDeg = None
    inDeg = None
    path = None
    cntp = 0
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_WordChain1.nxt, ((_java_obj_1 := Code04_WordChain1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_WordChain1.head[u])
        Code04_WordChain1.to[Code04_WordChain1.cntg] = jcast('int', v)
        Code04_WordChain1.weight[Code04_WordChain1.cntg] = w
        Code04_WordChain1.head[u] = jcast('int', Code04_WordChain1.cntg)

    @staticmethod
    def startNode(str):
        return jcast('int', jcast('int', jadd(jcast('int', (jcall(str, 'charAt', 0) - jchar('a'))), 1)))

    @staticmethod
    def endNode(str):
        return jcast('int', jcast('int', jadd(jcast('int', (jcall(str, 'charAt', jcast('int', (jcall(str, 'length') - 1))) - jchar('a'))), 1)))

    @staticmethod
    def connect():
        jstatic('Arrays', 'sort', Code04_WordChain1.eidArr, 1, jcast('int', jadd(Code04_WordChain1.m, 1)), Code04_WordChain1.EdgeCmp())
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= Code04_WordChain1.m):
            while ((jcast('int', jadd(r, 1)) <= Code04_WordChain1.m) and (Code04_WordChain1.a[Code04_WordChain1.eidArr[l]] == Code04_WordChain1.a[Code04_WordChain1.eidArr[jcast('int', jadd(r, 1))]])):
                r = jcast('int', (r + 1))
            i = jcast('int', r)
            u = 0
            v = 0
            while (i >= l):
                u = jcast('int', Code04_WordChain1.a[Code04_WordChain1.eidArr[i]])
                v = jcast('int', Code04_WordChain1.b[Code04_WordChain1.eidArr[i]])
                Code04_WordChain1.outDeg[u] = jcast('int', (Code04_WordChain1.outDeg[u] + 1))
                Code04_WordChain1.inDeg[v] = jcast('int', (Code04_WordChain1.inDeg[v] + 1))
                Code04_WordChain1.addEdge(u, v, Code04_WordChain1.str[Code04_WordChain1.eidArr[i]])
                i = jcast('int', (i - 1))
            l = jcast('int', (r := jcast('int', (r + (1)))))
        i = jcast('int', 1)
        while (i <= Code04_WordChain1.n):
            Code04_WordChain1.cur[i] = jcast('int', Code04_WordChain1.head[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def directedStart():
        start = jcast('int', jcast('int', (-1)))
        end = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= Code04_WordChain1.n):
            v = jcast('int', jcast('int', (Code04_WordChain1.outDeg[i] - Code04_WordChain1.inDeg[i])))
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
        while (i <= Code04_WordChain1.n):
            if (Code04_WordChain1.outDeg[i] > 0):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def euler(u, w):
        u = jcast('int', u)
        e = jcast('int', Code04_WordChain1.cur[u])
        while (e > 0):
            Code04_WordChain1.cur[u] = jcast('int', Code04_WordChain1.nxt[e])
            Code04_WordChain1.euler(Code04_WordChain1.to[e], Code04_WordChain1.weight[e])
            e = jcast('int', Code04_WordChain1.cur[u])
        jset(Code04_WordChain1.path, ((_java_obj_4 := Code04_WordChain1), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], w)

    @staticmethod
    def main(args):
        in_ = Code04_WordChain1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_WordChain1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_WordChain1.m):
            jset(Code04_WordChain1.str, i, jcall(in_, 'nextString'))
            jset(Code04_WordChain1.a, i, Code04_WordChain1.startNode(Code04_WordChain1.str[i]))
            jset(Code04_WordChain1.b, i, Code04_WordChain1.endNode(Code04_WordChain1.str[i]))
            Code04_WordChain1.eidArr[i] = i
            i = jcast('int', (i + 1))
        Code04_WordChain1.connect()
        start = jcast('int', Code04_WordChain1.directedStart())
        if (start == jcast('int', (-1))):
            jcall(out, 'println', '***')
        else:
            Code04_WordChain1.euler(start, '')
            if (Code04_WordChain1.cntp != jcast('int', jadd(Code04_WordChain1.m, 1))):
                jcall(out, 'println', '***')
            else:
                jcall(out, 'print', Code04_WordChain1.path[jcast('int', (Code04_WordChain1.cntp - 1))])
                i = jcast('int', jcast('int', (Code04_WordChain1.cntp - 2)))
                while (i >= 1):
                    jcall(out, 'print', jadd('.', Code04_WordChain1.path[i]))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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

        def nextString(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return None
                if not (((c < jchar('a')) or (c > jchar('z')))):
                    break
            sb = jnew('StringBuilder')
            while ((c >= jchar('a')) and (c <= jchar('z'))):
                try:
                    jcall(sb, 'append', jcast('char', c))
                    c = jcast('int', self.readByte())
                    if (c == jcast('int', (-1))):
                        raise JBreak(None)
                except JContinue as _java_control_10:
                    if _java_control_10.label not in (None,):
                        raise
                except JBreak as _java_control_10:
                    if _java_control_10.label not in (None,):
                        raise
                    break
            return jcall(sb, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_WordChain1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_WordChain1.MAXN = jcast('int', 27)
Code04_WordChain1.MAXM = jcast('int', 1002)
Code04_WordChain1.n = jcast('int', 26)
Code04_WordChain1.m = jcast('int', 0)
Code04_WordChain1.str = jarray('String', [Code04_WordChain1.MAXM])
Code04_WordChain1.a = jarray('int', [Code04_WordChain1.MAXM])
Code04_WordChain1.b = jarray('int', [Code04_WordChain1.MAXM])
Code04_WordChain1.eidArr = jarray('Integer', [Code04_WordChain1.MAXM])
Code04_WordChain1.head = jarray('int', [Code04_WordChain1.MAXN])
Code04_WordChain1.nxt = jarray('int', [Code04_WordChain1.MAXM])
Code04_WordChain1.to = jarray('int', [Code04_WordChain1.MAXM])
Code04_WordChain1.weight = jarray('String', [Code04_WordChain1.MAXM])
Code04_WordChain1.cntg = jcast('int', 0)
Code04_WordChain1.cur = jarray('int', [Code04_WordChain1.MAXN])
Code04_WordChain1.outDeg = jarray('int', [Code04_WordChain1.MAXN])
Code04_WordChain1.inDeg = jarray('int', [Code04_WordChain1.MAXN])
Code04_WordChain1.path = jarray('String', [Code04_WordChain1.MAXM])
Code04_WordChain1.cntp = jcast('int', 0)

if __name__ == '__main__':
    Code04_WordChain1.main([])

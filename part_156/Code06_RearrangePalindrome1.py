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

# 最长重排回文路径，Python版
# 一共有n个节点，编号1~n，给定n-1条边，所有节点连成一棵树，1号节点为树头
# 每条边上都有一个字符，字符范围[a~v]，字符一共22种，重排回文路径的定义如下
# 节点a到节点b的路径，如果所有边的字符收集起来，能重新排列成回文串，该路径是重排回文路径
# 打印1~n每个节点为头的子树中，最长重排回文路径的长度
# 1 <= n <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/CF741D
# 测试链接 : https://codeforces.com/problemset/problem/741/D
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_RearrangePalindrome1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'n': 'n', 'head': 'head', 'next': 'next', 'to': 'to', 'weight': 'weight', 'cnt': 'cnt', 'siz': 'siz', 'dep': 'dep', 'eor': 'eor', 'son': 'son', 'maxdep': 'maxdep', 'ans': 'ans'}
    MAXN = 0
    # 字符种类最多22种
    MAXV = 0
    n = 0
    # 链式前向星
    head = None
    next = None
    to = None
    weight = None
    cnt = 0
    # 树链剖分
    siz = None
    dep = None
    eor = None
    son = None
    # 树上启发式合并
    maxdep = None
    ans = None
    @staticmethod
    def addEdge(u, v, w):
        u = jcast('int', u)
        v = jcast('int', v)
        w = jcast('int', w)
        jset(Code06_RearrangePalindrome1.next, ((_java_obj_1 := Code06_RearrangePalindrome1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code06_RearrangePalindrome1.head[u])
        Code06_RearrangePalindrome1.to[Code06_RearrangePalindrome1.cnt] = jcast('int', v)
        Code06_RearrangePalindrome1.weight[Code06_RearrangePalindrome1.cnt] = jcast('int', w)
        Code06_RearrangePalindrome1.head[u] = jcast('int', Code06_RearrangePalindrome1.cnt)

    @staticmethod
    def dfs1(u, d, x):
        u = jcast('int', u)
        d = jcast('int', d)
        x = jcast('int', x)
        Code06_RearrangePalindrome1.siz[u] = jcast('int', 1)
        Code06_RearrangePalindrome1.dep[u] = jcast('int', d)
        Code06_RearrangePalindrome1.eor[u] = jcast('int', x)
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        while (e > 0):
            Code06_RearrangePalindrome1.dfs1(Code06_RearrangePalindrome1.to[e], jcast('int', jadd(d, 1)), jcast('int', (x ^ jcast('int', (1 << (Code06_RearrangePalindrome1.weight[e] & 31))))))
            e = jcast('int', Code06_RearrangePalindrome1.next[e])
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_RearrangePalindrome1.to[e])
            Code06_RearrangePalindrome1.siz[u] = jcast('int', jcast('int', jadd(Code06_RearrangePalindrome1.siz[u], Code06_RearrangePalindrome1.siz[v])))
            if ((Code06_RearrangePalindrome1.son[u] == 0) or (Code06_RearrangePalindrome1.siz[Code06_RearrangePalindrome1.son[u]] < Code06_RearrangePalindrome1.siz[v])):
                Code06_RearrangePalindrome1.son[u] = jcast('int', v)
            e = jcast('int', Code06_RearrangePalindrome1.next[e])

    @staticmethod
    def effect(u):
        u = jcast('int', u)
        jset(Code06_RearrangePalindrome1.maxdep, Code06_RearrangePalindrome1.eor[u], jstatic('Math', 'max', Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[u]], Code06_RearrangePalindrome1.dep[u]))
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        while (e > 0):
            Code06_RearrangePalindrome1.effect(Code06_RearrangePalindrome1.to[e])
            e = jcast('int', Code06_RearrangePalindrome1.next[e])

    @staticmethod
    def cancel(u):
        u = jcast('int', u)
        jset(Code06_RearrangePalindrome1.maxdep, Code06_RearrangePalindrome1.eor[u], 0)
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        while (e > 0):
            Code06_RearrangePalindrome1.cancel(Code06_RearrangePalindrome1.to[e])
            e = jcast('int', Code06_RearrangePalindrome1.next[e])

    @staticmethod
    def answerFromLight(light, u):
        light = jcast('int', light)
        u = jcast('int', u)
        if (Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[light]] != 0):
            jset(Code06_RearrangePalindrome1.ans, u, jstatic('Math', 'max', Code06_RearrangePalindrome1.ans[u], jcast('int', (jcast('int', jadd(Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[light]], Code06_RearrangePalindrome1.dep[light])) - jcast('int', (Code06_RearrangePalindrome1.dep[u] * 2))))))
        i = jcast('int', 0)
        while (i < Code06_RearrangePalindrome1.MAXV):
            if (Code06_RearrangePalindrome1.maxdep[jcast('int', (Code06_RearrangePalindrome1.eor[light] ^ jcast('int', (1 << (i & 31)))))] != 0):
                jset(Code06_RearrangePalindrome1.ans, u, jstatic('Math', 'max', Code06_RearrangePalindrome1.ans[u], jcast('int', (jcast('int', jadd(Code06_RearrangePalindrome1.maxdep[jcast('int', (Code06_RearrangePalindrome1.eor[light] ^ jcast('int', (1 << (i & 31)))))], Code06_RearrangePalindrome1.dep[light])) - jcast('int', (Code06_RearrangePalindrome1.dep[u] * 2))))))
            i = jcast('int', (i + 1))
        e = jcast('int', Code06_RearrangePalindrome1.head[light])
        while (e > 0):
            Code06_RearrangePalindrome1.answerFromLight(Code06_RearrangePalindrome1.to[e], u)
            e = jcast('int', Code06_RearrangePalindrome1.next[e])

    @staticmethod
    def dfs2(u, keep):
        u = jcast('int', u)
        keep = jcast('int', keep)
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_RearrangePalindrome1.to[e])
            if (v != Code06_RearrangePalindrome1.son[u]):
                Code06_RearrangePalindrome1.dfs2(v, 0)
            e = jcast('int', Code06_RearrangePalindrome1.next[e])
        if (Code06_RearrangePalindrome1.son[u] != 0):
            Code06_RearrangePalindrome1.dfs2(Code06_RearrangePalindrome1.son[u], 1)
        # 每一个儿子的子树，里得到的答案
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        while (e > 0):
            jset(Code06_RearrangePalindrome1.ans, u, jstatic('Math', 'max', Code06_RearrangePalindrome1.ans[u], Code06_RearrangePalindrome1.ans[Code06_RearrangePalindrome1.to[e]]))
            e = jcast('int', Code06_RearrangePalindrome1.next[e])
        # 选择当前节点，再选择重儿子树上的任意一点，得到的答案
        # 枚举所有可能得到的异或值
        if (Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[u]] != 0):
            jset(Code06_RearrangePalindrome1.ans, u, jstatic('Math', 'max', Code06_RearrangePalindrome1.ans[u], jcast('int', (Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[u]] - Code06_RearrangePalindrome1.dep[u]))))
        i = jcast('int', 0)
        while (i < Code06_RearrangePalindrome1.MAXV):
            if (Code06_RearrangePalindrome1.maxdep[jcast('int', (Code06_RearrangePalindrome1.eor[u] ^ jcast('int', (1 << (i & 31)))))] != 0):
                jset(Code06_RearrangePalindrome1.ans, u, jstatic('Math', 'max', Code06_RearrangePalindrome1.ans[u], jcast('int', (Code06_RearrangePalindrome1.maxdep[jcast('int', (Code06_RearrangePalindrome1.eor[u] ^ jcast('int', (1 << (i & 31)))))] - Code06_RearrangePalindrome1.dep[u]))))
            i = jcast('int', (i + 1))
        # 当前点的异或值，更新最大深度信息
        jset(Code06_RearrangePalindrome1.maxdep, Code06_RearrangePalindrome1.eor[u], jstatic('Math', 'max', Code06_RearrangePalindrome1.maxdep[Code06_RearrangePalindrome1.eor[u]], Code06_RearrangePalindrome1.dep[u]))
        # 选择遍历过的部分里的任意一点，再选择当前遍历到的子树里的任意一点，得到的答案
        e = jcast('int', Code06_RearrangePalindrome1.head[u])
        v = 0
        while (e > 0):
            v = jcast('int', Code06_RearrangePalindrome1.to[e])
            if (v != Code06_RearrangePalindrome1.son[u]):
                Code06_RearrangePalindrome1.answerFromLight(v, u)
                Code06_RearrangePalindrome1.effect(v)
            e = jcast('int', Code06_RearrangePalindrome1.next[e])
        if (keep == 0):
            Code06_RearrangePalindrome1.cancel(u)

    @staticmethod
    def main(args):
        in_ = Code06_RearrangePalindrome1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_RearrangePalindrome1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 2)
        fth = 0
        edg = 0
        while (i <= Code06_RearrangePalindrome1.n):
            fth = jcast('int', jcall(in_, 'nextInt'))
            edg = jcast('int', jcast('int', (jcall(in_, 'nextChar') - jchar('a'))))
            Code06_RearrangePalindrome1.addEdge(fth, i, edg)
            i = jcast('int', (i + 1))
        Code06_RearrangePalindrome1.dfs1(1, 1, 0)
        Code06_RearrangePalindrome1.dfs2(1, 0)
        i = jcast('int', 1)
        while (i <= Code06_RearrangePalindrome1.n):
            jcall(out, 'print', jadd(Code06_RearrangePalindrome1.ans[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            return jcast('byte', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

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
            raise TypeError("No matching overload for Code06_RearrangePalindrome1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_RearrangePalindrome1.MAXN = jcast('int', 500001)
Code06_RearrangePalindrome1.MAXV = jcast('int', 22)
Code06_RearrangePalindrome1.n = jcast('int', 0)
Code06_RearrangePalindrome1.head = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.next = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.to = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.weight = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.cnt = jcast('int', 0)
Code06_RearrangePalindrome1.siz = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.dep = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.eor = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.son = jarray('int', [Code06_RearrangePalindrome1.MAXN])
Code06_RearrangePalindrome1.maxdep = jarray('int', [jcast('int', (1 << (Code06_RearrangePalindrome1.MAXV & 31)))])
Code06_RearrangePalindrome1.ans = jarray('int', [Code06_RearrangePalindrome1.MAXN])

if __name__ == '__main__':
    Code06_RearrangePalindrome1.main([])

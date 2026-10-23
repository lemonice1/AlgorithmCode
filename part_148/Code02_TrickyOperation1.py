# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 棘手的操作，Python版
# 编号1~n个节点，每个节点独立且有自己的权值，实现如下7种操作，操作一共调用m次
# U x y  : x所在的集合和y所在的集合合并
# A1 x v : x节点的权值增加v
# A2 x v : x所在的集合所有节点的权值增加v
# A3 v   : 所有节点的权值增加v
# F1 x   : 打印x节点的权值
# F2 x   : 打印x所在的集合中，权值最大的节点的权值
# F3     : 打印所有节点中，权值最大的节点的权值
# 1 <= n、m <= 3 * 10^5，权值不会超过int类型的范围
# 测试链接 : https://www.luogu.com.cn/problem/P3273
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_TrickyOperation1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'num': 'num', 'up': 'up', 'left': 'left', 'right': 'right', 'dist': 'dist', 'father': 'father', 'size': 'size', 'add': 'add', 'heads': 'heads', 'addAll': 'addAll', 'stack': 'stack'}
    MAXN = 0
    n = 0
    m = 0
    # 左偏树需要
    num = None
    up = None
    left = None
    right = None
    dist = None
    # 并查集的路径信息
    father = None
    # 集合的大小信息
    size = None
    # 集合内所有数字应该加多少值
    add = None
    # 所有集合头节点的值，进入这个有序表，头节点有序表
    heads = None
    # 所有数字应该加多少
    addAll = 0
    # 准备好一个栈，用迭代方式实现先序遍历，不用递归方式
    stack = None
    # 编号为h的节点不再是左偏树的头，在头节点有序表里删掉一份h节点的值
    @staticmethod
    def minusHead(h):
        h = jcast('int', h)
        if (h != 0):
            hnum = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.num[h], Code02_TrickyOperation1.add[h])))
            if (jcall(Code02_TrickyOperation1.heads, 'get', hnum) == 1):
                jcall(Code02_TrickyOperation1.heads, 'remove', hnum)
            else:
                jcall(Code02_TrickyOperation1.heads, 'put', hnum, (jcall(Code02_TrickyOperation1.heads, 'get', hnum) - 1))

    # 编号为h的节点当前是左偏树的头，在头节点有序表里增加一份h节点的值
    @staticmethod
    def addHead(h):
        h = jcast('int', h)
        if (h != 0):
            hnum = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.num[h], Code02_TrickyOperation1.add[h])))
            jcall(Code02_TrickyOperation1.heads, 'put', hnum, jadd(jcall(Code02_TrickyOperation1.heads, 'getOrDefault', hnum, 0), 1))

    @staticmethod
    def prepare():
        Code02_TrickyOperation1.dist[0] = jcast('int', jcast('int', (-1)))
        jcall(Code02_TrickyOperation1.heads, 'clear')
        i = jcast('int', 1)
        while (i <= Code02_TrickyOperation1.n):
            jset(Code02_TrickyOperation1.up, i, jset(Code02_TrickyOperation1.left, i, jset(Code02_TrickyOperation1.right, i, jset(Code02_TrickyOperation1.dist, i, 0))))
            Code02_TrickyOperation1.father[i] = jcast('int', i)
            Code02_TrickyOperation1.size[i] = jcast('int', 1)
            Code02_TrickyOperation1.add[i] = jcast('int', 0)
            Code02_TrickyOperation1.addHead(i)
            i = jcast('int', (i + 1))
        Code02_TrickyOperation1.addAll = jcast('int', 0)

    # 返回i节点所在左偏树的树头
    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(Code02_TrickyOperation1.father, i, (i if (Code02_TrickyOperation1.father[i] == i) else Code02_TrickyOperation1.find(Code02_TrickyOperation1.father[i])))
        return jcast('int', Code02_TrickyOperation1.father[i])

    # 合并两棵左偏树
    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        if (Code02_TrickyOperation1.num[i] < Code02_TrickyOperation1.num[j]):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(Code02_TrickyOperation1.right, i, Code02_TrickyOperation1.merge(Code02_TrickyOperation1.right[i], j))
        jset(Code02_TrickyOperation1.up, Code02_TrickyOperation1.right[i], i)
        if (Code02_TrickyOperation1.dist[Code02_TrickyOperation1.left[i]] < Code02_TrickyOperation1.dist[Code02_TrickyOperation1.right[i]]):
            tmp = jcast('int', Code02_TrickyOperation1.left[i])
            Code02_TrickyOperation1.left[i] = jcast('int', Code02_TrickyOperation1.right[i])
            Code02_TrickyOperation1.right[i] = jcast('int', tmp)
        Code02_TrickyOperation1.dist[i] = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.dist[Code02_TrickyOperation1.right[i]], 1)))
        jset(Code02_TrickyOperation1.father, Code02_TrickyOperation1.left[i], jset(Code02_TrickyOperation1.father, Code02_TrickyOperation1.right[i], i))
        return jcast('int', i)

    # 节点i是所在左偏树的任意节点，删除节点i，返回整棵树的头节点编号
    @staticmethod
    def remove(i):
        i = jcast('int', i)
        h = jcast('int', Code02_TrickyOperation1.find(i))
        jset(Code02_TrickyOperation1.father, Code02_TrickyOperation1.left[i], Code02_TrickyOperation1.left[i])
        jset(Code02_TrickyOperation1.father, Code02_TrickyOperation1.right[i], Code02_TrickyOperation1.right[i])
        s = jcast('int', Code02_TrickyOperation1.merge(Code02_TrickyOperation1.left[i], Code02_TrickyOperation1.right[i]))
        f = jcast('int', Code02_TrickyOperation1.up[i])
        Code02_TrickyOperation1.father[i] = jcast('int', s)
        Code02_TrickyOperation1.up[s] = jcast('int', f)
        if (h != i):
            Code02_TrickyOperation1.father[s] = jcast('int', h)
            if (Code02_TrickyOperation1.left[f] == i):
                Code02_TrickyOperation1.left[f] = jcast('int', s)
            else:
                Code02_TrickyOperation1.right[f] = jcast('int', s)
            d = jcast('int', Code02_TrickyOperation1.dist[s])
            tmp = 0
            while (Code02_TrickyOperation1.dist[f] > jcast('int', jadd(d, 1))):
                Code02_TrickyOperation1.dist[f] = jcast('int', jcast('int', jadd(d, 1)))
                if (Code02_TrickyOperation1.dist[Code02_TrickyOperation1.left[f]] < Code02_TrickyOperation1.dist[Code02_TrickyOperation1.right[f]]):
                    tmp = jcast('int', Code02_TrickyOperation1.left[f])
                    Code02_TrickyOperation1.left[f] = jcast('int', Code02_TrickyOperation1.right[f])
                    Code02_TrickyOperation1.right[f] = jcast('int', tmp)
                f = jcast('int', Code02_TrickyOperation1.up[f])
                d = jcast('int', (d + 1))
        jset(Code02_TrickyOperation1.up, i, jset(Code02_TrickyOperation1.left, i, jset(Code02_TrickyOperation1.right, i, jset(Code02_TrickyOperation1.dist, i, 0))))
        return jcast('int', Code02_TrickyOperation1.father[s])

    # 以i为头的左偏树，遭遇了更大的左偏树
    # i的标签信息取消，以i为头的整棵树所有节点的值增加v
    # 不用递归实现先序遍历，容易爆栈，所以用迭代实现先序遍历
    @staticmethod
    def down(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (i != 0):
            Code02_TrickyOperation1.add[i] = jcast('int', 0)
            size = jcast('int', 0)
            jset(Code02_TrickyOperation1.stack, (size := jcast('int', (size + (1)))), i)
            while (size > 0):
                i = jcast('int', Code02_TrickyOperation1.stack[((_java_old_1 := size), (size := jcast('int', (size + (-1)))), _java_old_1)[2]])
                Code02_TrickyOperation1.num[i] = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.num[i], v)))
                if (Code02_TrickyOperation1.right[i] != 0):
                    jset(Code02_TrickyOperation1.stack, (size := jcast('int', (size + (1)))), Code02_TrickyOperation1.right[i])
                if (Code02_TrickyOperation1.left[i] != 0):
                    jset(Code02_TrickyOperation1.stack, (size := jcast('int', (size + (1)))), Code02_TrickyOperation1.left[i])

    @staticmethod
    def u(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        l = jcast('int', Code02_TrickyOperation1.find(i))
        r = jcast('int', Code02_TrickyOperation1.find(j))
        if (l == r):
            return
        lsize = jcast('int', Code02_TrickyOperation1.size[l])
        Code02_TrickyOperation1.minusHead(l)
        rsize = jcast('int', Code02_TrickyOperation1.size[r])
        Code02_TrickyOperation1.minusHead(r)
        addTag = 0
        if (lsize <= rsize):
            Code02_TrickyOperation1.down(l, jcast('int', (Code02_TrickyOperation1.add[l] - Code02_TrickyOperation1.add[r])))
            addTag = jcast('int', Code02_TrickyOperation1.add[r])
        else:
            Code02_TrickyOperation1.down(r, jcast('int', (Code02_TrickyOperation1.add[r] - Code02_TrickyOperation1.add[l])))
            addTag = jcast('int', Code02_TrickyOperation1.add[l])
        h = jcast('int', Code02_TrickyOperation1.merge(l, r))
        Code02_TrickyOperation1.size[h] = jcast('int', jcast('int', jadd(lsize, rsize)))
        Code02_TrickyOperation1.add[h] = jcast('int', addTag)
        Code02_TrickyOperation1.addHead(h)

    @staticmethod
    def a1(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        h = jcast('int', Code02_TrickyOperation1.find(i))
        Code02_TrickyOperation1.minusHead(h)
        l = jcast('int', Code02_TrickyOperation1.remove(i))
        if (l != 0):
            Code02_TrickyOperation1.size[l] = jcast('int', jcast('int', (Code02_TrickyOperation1.size[h] - 1)))
            Code02_TrickyOperation1.add[l] = jcast('int', Code02_TrickyOperation1.add[h])
            Code02_TrickyOperation1.addHead(l)
        Code02_TrickyOperation1.num[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_TrickyOperation1.num[i], Code02_TrickyOperation1.add[h])), v)))
        Code02_TrickyOperation1.father[i] = jcast('int', i)
        Code02_TrickyOperation1.size[i] = jcast('int', 1)
        Code02_TrickyOperation1.add[i] = jcast('int', 0)
        Code02_TrickyOperation1.addHead(i)
        Code02_TrickyOperation1.u(l, i)

    @staticmethod
    def a2(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        h = jcast('int', Code02_TrickyOperation1.find(i))
        Code02_TrickyOperation1.minusHead(h)
        Code02_TrickyOperation1.add[h] = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.add[h], v)))
        Code02_TrickyOperation1.addHead(h)

    @staticmethod
    def a3(v):
        v = jcast('int', v)
        Code02_TrickyOperation1.addAll = jcast('int', jcast('int', jadd(Code02_TrickyOperation1.addAll, v)))

    @staticmethod
    def f1(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_TrickyOperation1.num[i], Code02_TrickyOperation1.add[Code02_TrickyOperation1.find(i)])), Code02_TrickyOperation1.addAll)))

    @staticmethod
    def f2(i):
        i = jcast('int', i)
        h = jcast('int', Code02_TrickyOperation1.find(i))
        return jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_TrickyOperation1.num[h], Code02_TrickyOperation1.add[h])), Code02_TrickyOperation1.addAll)))

    @staticmethod
    def f3():
        return jcast('int', jadd(jcall(Code02_TrickyOperation1.heads, 'lastKey'), Code02_TrickyOperation1.addAll))

    @staticmethod
    def main(args):
        io = Code02_TrickyOperation1.ReaderWriter(_java_ctor=0)
        Code02_TrickyOperation1.n = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_TrickyOperation1.n):
            jset(Code02_TrickyOperation1.num, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_TrickyOperation1.prepare()
        Code02_TrickyOperation1.m = jcast('int', jcall(io, 'nextInt'))
        op = None
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code02_TrickyOperation1.m):
            op = jcall(io, 'next')
            if jcall(op, 'equals', 'F3'):
                jcall(io, 'println', Code02_TrickyOperation1.f3())
            else:
                x = jcast('int', jcall(io, 'nextInt'))
                if jcall(op, 'equals', 'U'):
                    y = jcast('int', jcall(io, 'nextInt'))
                    Code02_TrickyOperation1.u(x, y)
                else:
                    if jcall(op, 'equals', 'A1'):
                        y = jcast('int', jcall(io, 'nextInt'))
                        Code02_TrickyOperation1.a1(x, y)
                    else:
                        if jcall(op, 'equals', 'A2'):
                            y = jcast('int', jcall(io, 'nextInt'))
                            Code02_TrickyOperation1.a2(x, y)
                        else:
                            if jcall(op, 'equals', 'A3'):
                                Code02_TrickyOperation1.a3(x)
                            else:
                                if jcall(op, 'equals', 'F1'):
                                    jcall(io, 'println', Code02_TrickyOperation1.f1(x))
                                else:
                                    jcall(io, 'println', Code02_TrickyOperation1.f2(x))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class ReaderWriter(jclass('PrintWriter')):
        __java_fields__ = {'buf': 'buf', 'bId': 'bId', 'bSize': 'bSize', 'eof': 'eof', 'c': 'c'}
        # buf：实例字段，在构造函数中初始化。
        # bId：实例字段，在构造函数中初始化。
        # bSize：实例字段，在构造函数中初始化。
        # eof：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            super().__init__(jget(System, 'out'))

        def getByte(self):
            if (self.bId >= self.bSize):
                try:
                    self.bSize = jcast('int', jcall(jget(System, 'in'), 'read', self.buf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_2:
                    if jinstanceof(_java_exception_2, 'IOException'):
                        e = _java_exception_2
                        jcall(e, 'printStackTrace')
                    else:
                        raise
                if (self.bSize == jcast('int', (-1))):
                    self.eof = jcast('boolean', True)
                self.bId = jcast('int', 0)
            return jcast('byte', self.buf[((_java_obj_3 := self), (_java_key_4 := 'bId'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))), _java_old_5)[4]])

        # c：实例字段，在构造函数中初始化。
        def hasNext(self):
            if self.eof:
                return jcast('boolean', False)
            while ((jset(self, 'c', self.getByte()) <= 32) and (not self.eof)):
                None
            if self.eof:
                return jcast('boolean', False)
            self.bId = jcast('int', (self.bId - 1))
            return jcast('boolean', True)

        def next(self):
            if (not self.hasNext()):
                return None
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            sb = jnew('StringBuilder')
            while (c > 32):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.getByte())
            return jcall(sb, 'toString')

        def nextInt(self):
            if (not self.hasNext()):
                return jcast('int', jget(Integer, 'MIN_VALUE'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('int', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('int', jcast('int', (val * sign)))

        def nextLong(self):
            if (not self.hasNext()):
                return jcast('long', jget(Long, 'MIN_VALUE'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('long', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('long', jcast('long', (val * sign)))

        def nextDouble(self):
            if (not self.hasNext()):
                return jcast('double', jget(Double, 'NaN'))
            sign = jcast('int', 1)
            c = jcast('byte', self.getByte())
            while (c <= 32):
                c = jcast('byte', self.getByte())
            if (c == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
                c = jcast('byte', self.getByte())
            val = jcast('double', 0)
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                val = jcast('double', jadd((val * 10), jcast('int', (c - jchar('0')))))
                c = jcast('byte', self.getByte())
            if (c == jchar('.')):
                mul = jcast('double', 1)
                c = jcast('byte', self.getByte())
                while ((c >= jchar('0')) and (c <= jchar('9'))):
                    mul = jcast('double', (mul * 0.1))
                    val = jcast('double', jadd(val, (jcast('int', (c - jchar('0'))) * mul)))
                    c = jcast('byte', self.getByte())
            self.bId = jcast('int', (self.bId - 1))
            return jcast('double', (val * sign))

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [jcast('int', (1 << (10 & 31)))])
            self.bId = jcast('int', 0)
            self.bSize = jcast('int', 0)
            self.eof = jcast('boolean', False)
            self.c = jcast('byte', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_TrickyOperation1.ReaderWriter.ReaderWriter")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_TrickyOperation1.MAXN = jcast('int', 300001)
Code02_TrickyOperation1.n = jcast('int', 0)
Code02_TrickyOperation1.m = jcast('int', 0)
Code02_TrickyOperation1.num = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.up = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.left = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.right = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.dist = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.father = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.size = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.add = jarray('int', [Code02_TrickyOperation1.MAXN])
Code02_TrickyOperation1.heads = jnew('TreeMap')
Code02_TrickyOperation1.addAll = jcast('int', 0)
Code02_TrickyOperation1.stack = jarray('int', [Code02_TrickyOperation1.MAXN])

if __name__ == '__main__':
    Code02_TrickyOperation1.main([])

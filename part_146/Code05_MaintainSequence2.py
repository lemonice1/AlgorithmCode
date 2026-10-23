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

# 维护数列(Python版)
# 初始时给定一个数列，实现如下六种操作
# INSERT posi tot ...  : 在第posi个数字之后，插入长度为tot的数组，由...代表
# DELETE posi tot      : 从第posi个数字开始，删除长度为tot的部分
# MAKE-SAME posi tot c : 从第posi个数字开始，长度为tot的部分，值都设置成c
# REVERSE posi tot     : 从第posi个数字开始，翻转长度为tot的部分
# GET-SUM posi tot     : 从第posi个数字开始，查询长度为tot的部分的累加和
# MAX-SUM              : 查询整个数列中，非空子数组的最大累加和
# 任何时刻输入保证至少有一个数字在数列中，并且所有操作都合法
# 插入数字总数很多，但是任何时刻数列中最多有5 * 10^5个数，使用总空间要和该数量有关
# 测试链接 : https://www.luogu.com.cn/problem/P2042
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MaintainSequence2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'head': 'head', 'arr': 'arr', 'num': 'num', 'father': 'father', 'left': 'left', 'right': 'right', 'size': 'size', 'space': 'space', 'si': 'si', 'sum': 'sum', 'all': 'all', 'pre': 'pre', 'suf': 'suf', 'update': 'update', 'change': 'change', 'reverse': 'reverse_data'}
    MAXN = 0
    INF = 0
    head = 0
    arr = None
    num = None
    father = None
    left = None
    right = None
    size = None
    # 这个数组里拿空间编号
    space = None
    si = 0
    # 维护区间累加和信息
    sum = None
    # 维护区间子数组最大累加和信息，要求不能为空
    all = None
    # 维护区间前缀最大累加和信息，可以空
    pre = None
    # 维护区间后缀最大累加和信息，可以空
    suf = None
    # 懒更新信息，区间是否重新设了值
    update = None
    # 懒更新信息，如果区间重新设了值，设置成了什么
    change = None
    # 懒更新信息，区间是否发生了翻转
    reverse_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        l = jcast('int', Code05_MaintainSequence2.left[i])
        r = jcast('int', Code05_MaintainSequence2.right[i])
        Code05_MaintainSequence2.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_MaintainSequence2.size[l], Code05_MaintainSequence2.size[r])), 1)))
        Code05_MaintainSequence2.sum[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code05_MaintainSequence2.sum[l], Code05_MaintainSequence2.sum[r])), Code05_MaintainSequence2.num[i])))
        jset(Code05_MaintainSequence2.all, i, jstatic('Math', 'max', jstatic('Math', 'max', Code05_MaintainSequence2.all[l], Code05_MaintainSequence2.all[r]), jcast('int', jadd(jcast('int', jadd(Code05_MaintainSequence2.suf[l], Code05_MaintainSequence2.num[i])), Code05_MaintainSequence2.pre[r]))))
        jset(Code05_MaintainSequence2.pre, i, jstatic('Math', 'max', Code05_MaintainSequence2.pre[l], jcast('int', jadd(jcast('int', jadd(Code05_MaintainSequence2.sum[l], Code05_MaintainSequence2.num[i])), Code05_MaintainSequence2.pre[r]))))
        jset(Code05_MaintainSequence2.suf, i, jstatic('Math', 'max', Code05_MaintainSequence2.suf[r], jcast('int', jadd(jcast('int', jadd(Code05_MaintainSequence2.suf[l], Code05_MaintainSequence2.num[i])), Code05_MaintainSequence2.sum[r]))))

    @staticmethod
    def lr(i):
        i = jcast('int', i)
        return jcast('int', (1 if (Code05_MaintainSequence2.right[Code05_MaintainSequence2.father[i]] == i) else 0))

    @staticmethod
    def rotate(i):
        i = jcast('int', i)
        f = jcast('int', Code05_MaintainSequence2.father[i])
        g = jcast('int', Code05_MaintainSequence2.father[f])
        soni = jcast('int', Code05_MaintainSequence2.lr(i))
        sonf = jcast('int', Code05_MaintainSequence2.lr(f))
        if (soni == 1):
            Code05_MaintainSequence2.right[f] = jcast('int', Code05_MaintainSequence2.left[i])
            if (Code05_MaintainSequence2.right[f] != 0):
                jset(Code05_MaintainSequence2.father, Code05_MaintainSequence2.right[f], f)
            Code05_MaintainSequence2.left[i] = jcast('int', f)
        else:
            Code05_MaintainSequence2.left[f] = jcast('int', Code05_MaintainSequence2.right[i])
            if (Code05_MaintainSequence2.left[f] != 0):
                jset(Code05_MaintainSequence2.father, Code05_MaintainSequence2.left[f], f)
            Code05_MaintainSequence2.right[i] = jcast('int', f)
        if (g != 0):
            if (sonf == 1):
                Code05_MaintainSequence2.right[g] = jcast('int', i)
            else:
                Code05_MaintainSequence2.left[g] = jcast('int', i)
        Code05_MaintainSequence2.father[f] = jcast('int', i)
        Code05_MaintainSequence2.father[i] = jcast('int', g)
        Code05_MaintainSequence2.up(f)
        Code05_MaintainSequence2.up(i)

    @staticmethod
    def splay(i, goal):
        i = jcast('int', i)
        goal = jcast('int', goal)
        f = jcast('int', Code05_MaintainSequence2.father[i])
        g = jcast('int', Code05_MaintainSequence2.father[f])
        while (f != goal):
            if (g != goal):
                if (Code05_MaintainSequence2.lr(i) == Code05_MaintainSequence2.lr(f)):
                    Code05_MaintainSequence2.rotate(f)
                else:
                    Code05_MaintainSequence2.rotate(i)
            Code05_MaintainSequence2.rotate(i)
            f = jcast('int', Code05_MaintainSequence2.father[i])
            g = jcast('int', Code05_MaintainSequence2.father[f])
        if (goal == 0):
            Code05_MaintainSequence2.head = jcast('int', i)

    @staticmethod
    def setValue(i, val):
        i = jcast('int', i)
        val = jcast('int', val)
        if (i != 0):
            Code05_MaintainSequence2.update[i] = jcast('boolean', True)
            Code05_MaintainSequence2.change[i] = jcast('int', val)
            Code05_MaintainSequence2.num[i] = jcast('int', val)
            Code05_MaintainSequence2.sum[i] = jcast('int', jcast('int', (Code05_MaintainSequence2.size[i] * val)))
            jset(Code05_MaintainSequence2.all, i, jstatic('Math', 'max', Code05_MaintainSequence2.sum[i], val))
            jset(Code05_MaintainSequence2.pre, i, jstatic('Math', 'max', Code05_MaintainSequence2.sum[i], 0))
            jset(Code05_MaintainSequence2.suf, i, jstatic('Math', 'max', Code05_MaintainSequence2.sum[i], 0))

    @staticmethod
    def setReverse(i):
        i = jcast('int', i)
        if (i != 0):
            tmp = jcast('int', Code05_MaintainSequence2.pre[i])
            Code05_MaintainSequence2.pre[i] = jcast('int', Code05_MaintainSequence2.suf[i])
            Code05_MaintainSequence2.suf[i] = jcast('int', tmp)
            Code05_MaintainSequence2.reverse_data[i] = jcast('boolean', (not Code05_MaintainSequence2.reverse_data[i]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if Code05_MaintainSequence2.update[i]:
            Code05_MaintainSequence2.setValue(Code05_MaintainSequence2.left[i], Code05_MaintainSequence2.change[i])
            Code05_MaintainSequence2.setValue(Code05_MaintainSequence2.right[i], Code05_MaintainSequence2.change[i])
            Code05_MaintainSequence2.update[i] = jcast('boolean', False)
        if Code05_MaintainSequence2.reverse_data[i]:
            tmp = jcast('int', Code05_MaintainSequence2.left[i])
            Code05_MaintainSequence2.left[i] = jcast('int', Code05_MaintainSequence2.right[i])
            Code05_MaintainSequence2.right[i] = jcast('int', tmp)
            Code05_MaintainSequence2.setReverse(Code05_MaintainSequence2.left[i])
            Code05_MaintainSequence2.setReverse(Code05_MaintainSequence2.right[i])
            Code05_MaintainSequence2.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def init(val):
        val = jcast('int', val)
        i = jcast('int', Code05_MaintainSequence2.space[((_java_obj_1 := Code05_MaintainSequence2), (_java_key_2 := 'si'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]])
        Code05_MaintainSequence2.size[i] = jcast('int', 1)
        jset(Code05_MaintainSequence2.num, i, jset(Code05_MaintainSequence2.sum, i, jset(Code05_MaintainSequence2.all, i, val)))
        jset(Code05_MaintainSequence2.pre, i, jset(Code05_MaintainSequence2.suf, i, jstatic('Math', 'max', val, 0)))
        jset(Code05_MaintainSequence2.father, i, jset(Code05_MaintainSequence2.left, i, jset(Code05_MaintainSequence2.right, i, 0)))
        jset(Code05_MaintainSequence2.update, i, jset(Code05_MaintainSequence2.reverse_data, i, False))
        return jcast('int', i)

    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        root = jcast('int', Code05_MaintainSequence2.init(Code05_MaintainSequence2.arr[mid]))
        if (l < mid):
            jset(Code05_MaintainSequence2.left, root, Code05_MaintainSequence2.build(l, jcast('int', (mid - 1))))
            jset(Code05_MaintainSequence2.father, Code05_MaintainSequence2.left[root], root)
        if (mid < r):
            jset(Code05_MaintainSequence2.right, root, Code05_MaintainSequence2.build(jcast('int', jadd(mid, 1)), r))
            jset(Code05_MaintainSequence2.father, Code05_MaintainSequence2.right[root], root)
        Code05_MaintainSequence2.up(root)
        return jcast('int', root)

    @staticmethod
    def find(rank):
        rank = jcast('int', rank)
        i = jcast('int', Code05_MaintainSequence2.head)
        while (i != 0):
            Code05_MaintainSequence2.down(i)
            if (jcast('int', jadd(Code05_MaintainSequence2.size[Code05_MaintainSequence2.left[i]], 1)) == rank):
                return jcast('int', i)
            else:
                if (Code05_MaintainSequence2.size[Code05_MaintainSequence2.left[i]] >= rank):
                    i = jcast('int', Code05_MaintainSequence2.left[i])
                else:
                    rank = jcast('int', jcast('int', (rank - jcast('int', jadd(Code05_MaintainSequence2.size[Code05_MaintainSequence2.left[i]], 1)))))
                    i = jcast('int', Code05_MaintainSequence2.right[i])
        return jcast('int', 0)

    @staticmethod
    def insert(rank, n):
        rank = jcast('int', rank)
        n = jcast('int', n)
        if (rank == 0):
            Code05_MaintainSequence2.head = jcast('int', Code05_MaintainSequence2.build(1, n))
        else:
            l = jcast('int', Code05_MaintainSequence2.find(rank))
            r = jcast('int', Code05_MaintainSequence2.find(jcast('int', jadd(rank, 1))))
            Code05_MaintainSequence2.splay(l, 0)
            Code05_MaintainSequence2.splay(r, l)
            jset(Code05_MaintainSequence2.left, r, Code05_MaintainSequence2.build(1, n))
            jset(Code05_MaintainSequence2.father, Code05_MaintainSequence2.left[r], r)
            Code05_MaintainSequence2.up(r)
            Code05_MaintainSequence2.up(l)

    @staticmethod
    def recycle(i):
        i = jcast('int', i)
        if (i != 0):
            jset(Code05_MaintainSequence2.space, ((_java_obj_4 := Code05_MaintainSequence2), (_java_key_5 := 'si'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Code05_MaintainSequence2.recycle(Code05_MaintainSequence2.left[i])
            Code05_MaintainSequence2.recycle(Code05_MaintainSequence2.right[i])

    @staticmethod
    def delete(rank, n):
        rank = jcast('int', rank)
        n = jcast('int', n)
        l = jcast('int', Code05_MaintainSequence2.find(jcast('int', (rank - 1))))
        r = jcast('int', Code05_MaintainSequence2.find(jcast('int', jadd(rank, n))))
        Code05_MaintainSequence2.splay(l, 0)
        Code05_MaintainSequence2.splay(r, l)
        Code05_MaintainSequence2.recycle(Code05_MaintainSequence2.left[r])
        Code05_MaintainSequence2.left[r] = jcast('int', 0)
        Code05_MaintainSequence2.up(r)
        Code05_MaintainSequence2.up(l)

    @staticmethod
    def reset(rank, n, val):
        rank = jcast('int', rank)
        n = jcast('int', n)
        val = jcast('int', val)
        l = jcast('int', Code05_MaintainSequence2.find(jcast('int', (rank - 1))))
        r = jcast('int', Code05_MaintainSequence2.find(jcast('int', jadd(rank, n))))
        Code05_MaintainSequence2.splay(l, 0)
        Code05_MaintainSequence2.splay(r, l)
        Code05_MaintainSequence2.setValue(Code05_MaintainSequence2.left[r], val)
        Code05_MaintainSequence2.up(r)
        Code05_MaintainSequence2.up(l)

    @staticmethod
    def reverse(rank, n):
        rank = jcast('int', rank)
        n = jcast('int', n)
        l = jcast('int', Code05_MaintainSequence2.find(jcast('int', (rank - 1))))
        r = jcast('int', Code05_MaintainSequence2.find(jcast('int', jadd(rank, n))))
        Code05_MaintainSequence2.splay(l, 0)
        Code05_MaintainSequence2.splay(r, l)
        Code05_MaintainSequence2.setReverse(Code05_MaintainSequence2.left[r])
        Code05_MaintainSequence2.up(r)
        Code05_MaintainSequence2.up(l)

    @staticmethod
    def querySum(rank, n):
        rank = jcast('int', rank)
        n = jcast('int', n)
        l = jcast('int', Code05_MaintainSequence2.find(jcast('int', (rank - 1))))
        r = jcast('int', Code05_MaintainSequence2.find(jcast('int', jadd(rank, n))))
        Code05_MaintainSequence2.splay(l, 0)
        Code05_MaintainSequence2.splay(r, l)
        return jcast('int', Code05_MaintainSequence2.sum[Code05_MaintainSequence2.left[r]])

    @staticmethod
    def queryMax():
        return jcast('int', Code05_MaintainSequence2.all[Code05_MaintainSequence2.head])

    @staticmethod
    def main(args):
        in_ = Code05_MaintainSequence2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = Code05_MaintainSequence2.FastWriter(jget(System, 'out'), _java_ctor=1)
        n = jcast('int', jcall(in_, 'readInt'))
        m = jcast('int', jcall(in_, 'readInt'))
        # 所有可用空间编号，进入space数组
        Code05_MaintainSequence2.si = jcast('int', jcast('int', (Code05_MaintainSequence2.MAXN - 1)))
        i = jcast('int', 1)
        while (i <= Code05_MaintainSequence2.si):
            Code05_MaintainSequence2.space[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        # 这里很重要，一方面准备好最左和最右的准备值
        # 另一方面设置all[0] = 极小值
        # 表示没有范围时，子数组最大累加和为极小值，因为不能为空
        jset(Code05_MaintainSequence2.arr, 1, jset(Code05_MaintainSequence2.arr, jcast('int', jadd(n, 2)), jset(Code05_MaintainSequence2.all, 0, jcast('int', (-Code05_MaintainSequence2.INF)))))
        i = jcast('int', 1)
        j = jcast('int', 2)
        while (i <= n):
            jset(Code05_MaintainSequence2.arr, j, jcall(in_, 'readInt'))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        # 建立初始树
        Code05_MaintainSequence2.insert(0, jcast('int', jadd(n, 2)))
        op = None
        i = jcast('int', 1)
        posi = 0
        tot = 0
        c = 0
        while (i <= m):
            op = jcall(in_, 'readString')
            if jcall(op, 'equals', 'MAX-SUM'):
                jcall(out, 'println', Code05_MaintainSequence2.queryMax())
            else:
                # 因为有最左的准备值，所以位置要后移一位
                posi = jcast('int', jcast('int', jadd(jcall(in_, 'readInt'), 1)))
                tot = jcast('int', jcall(in_, 'readInt'))
                if jcall(op, 'equals', 'INSERT'):
                    j = jcast('int', 1)
                    while (j <= tot):
                        jset(Code05_MaintainSequence2.arr, j, jcall(in_, 'readInt'))
                        j = jcast('int', (j + 1))
                    Code05_MaintainSequence2.insert(posi, tot)
                else:
                    if jcall(op, 'equals', 'DELETE'):
                        Code05_MaintainSequence2.delete(posi, tot)
                    else:
                        if jcall(op, 'equals', 'MAKE-SAME'):
                            c = jcast('int', jcall(in_, 'readInt'))
                            Code05_MaintainSequence2.reset(posi, tot, c)
                        else:
                            if jcall(op, 'equals', 'REVERSE'):
                                Code05_MaintainSequence2.reverse(posi, tot)
                            else:
                                jcall(out, 'println', Code05_MaintainSequence2.querySum(posi, tot))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 快读
    class FastReader:
        __java_fields__ = {'is': 'is_', 'inbuf': 'inbuf', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf'}
        # is_：实例字段，在构造函数中初始化。
        # inbuf：实例字段，在构造函数中初始化。
        # lenbuf：实例字段，在构造函数中初始化。
        # ptrbuf：实例字段，在构造函数中初始化。
        def _java_init_0(self, is_):
            self.is_ = is_

        def readString(self):
            cur = jchar(0)
            while True:
                cur = jcast('char', jcast('char', self.readByte()))
                if not (((cur == jchar(' ')) or (cur == jchar('\n')))):
                    break
            builder = jnew('StringBuilder')
            while ((cur != jchar(' ')) and (cur != jchar('\n'))):
                jcall(builder, 'append', cur)
                cur = jcast('char', jcast('char', self.readByte()))
            return jcall(builder, 'toString')

        def readByte(self):
            if (self.lenbuf == jcast('int', (-1))):
                raise jnew('InputMismatchException')
            if (self.ptrbuf >= self.lenbuf):
                self.ptrbuf = jcast('int', 0)
                try:
                    self.lenbuf = jcast('int', jcall(self.is_, 'read', self.inbuf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_7:
                    if jinstanceof(_java_exception_7, 'IOException'):
                        e = _java_exception_7
                        raise jnew('InputMismatchException')
                    else:
                        raise
                if (self.lenbuf <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.inbuf[((_java_obj_8 := self), (_java_key_9 := 'ptrbuf'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

        def readInt(self):
            return jcast('int', jcast('int', self.readLong()))

        def readLong(self):
            num = jcast('long', 0)
            b = 0
            minus = jcast('boolean', False)
            while (((b := self.readByte()) != jcast('int', (-1))) and (not (((b >= jchar('0')) and (b <= jchar('9'))) or (b == jchar('-'))))):
                None
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('int', self.readByte())
            while True:
                if ((b >= jchar('0')) and (b <= jchar('9'))):
                    num = jcast('long', jcast('long', jadd(jcast('long', (num * 10)), jcast('int', (b - jchar('0'))))))
                else:
                    return jcast('long', (jcast('long', (-num)) if minus else num))
                b = jcast('int', self.readByte())

        def __init__(self, *args, _java_ctor=None):
            self.is_ = None
            self.inbuf = jarray('byte', [1024])
            self.lenbuf = jcast('int', 0)
            self.ptrbuf = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_MaintainSequence2.FastReader.FastReader")


    # 快写
    class FastWriter:
        __java_fields__ = {'BUF_SIZE': 'BUF_SIZE', 'buf': 'buf', 'out': 'out', 'writer': 'writer', 'ptr': 'ptr'}
        BUF_SIZE = 0
        # buf：实例字段，在构造函数中初始化。
        # out：实例字段，在构造函数中初始化。
        # writer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        def _java_init_0(self, writer):
            self.writer = jnew('BufferedWriter', writer)
            self.out = jnew('ByteArrayOutputStream')

        def _java_init_1(self, os):
            self.out = os

        def _java_init_2(self, path):
            try:
                self.out = jnew('FileOutputStream', path)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'FileNotFoundException'):
                    e = _java_exception_11
                    raise jnew('RuntimeException', 'FastWriter')
                else:
                    raise

        def _java_write_0(self, b):
            b = jcast('byte', b)
            jset(self.buf, ((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4], b)
            if (self.ptr == Code05_MaintainSequence2.FastWriter.BUF_SIZE):
                self.innerflush()
            return self

        def _java_write_1(self, s):
            jcall(jcall(s, 'chars'), 'forEach', (lambda c: _java_lambda_15(c, self)))
            return self

        @staticmethod
        def countDigits(l):
            l = jcast('long', l)
            if (l >= 1000000000000000000):
                return jcast('int', 19)
            if (l >= 100000000000000000):
                return jcast('int', 18)
            if (l >= 10000000000000000):
                return jcast('int', 17)
            if (l >= 1000000000000000):
                return jcast('int', 16)
            if (l >= 100000000000000):
                return jcast('int', 15)
            if (l >= 10000000000000):
                return jcast('int', 14)
            if (l >= 1000000000000):
                return jcast('int', 13)
            if (l >= 100000000000):
                return jcast('int', 12)
            if (l >= 10000000000):
                return jcast('int', 11)
            if (l >= 1000000000):
                return jcast('int', 10)
            if (l >= 100000000):
                return jcast('int', 9)
            if (l >= 10000000):
                return jcast('int', 8)
            if (l >= 1000000):
                return jcast('int', 7)
            if (l >= 100000):
                return jcast('int', 6)
            if (l >= 10000):
                return jcast('int', 5)
            if (l >= 1000):
                return jcast('int', 4)
            if (l >= 100):
                return jcast('int', 3)
            if (l >= 10):
                return jcast('int', 2)
            return jcast('int', 1)

        def _java_write_2(self, x):
            x = jcast('long', x)
            if (x == jget(Long, 'MIN_VALUE')):
                return self._java_write_1(jadd('', x))
            if (jcast('int', jadd(self.ptr, 21)) >= Code05_MaintainSequence2.FastWriter.BUF_SIZE):
                self.innerflush()
            if (x < 0):
                self._java_write_0(jcast('byte', jchar('-')))
                x = jcast('long', jcast('long', (-x)))
            d = jcast('int', Code05_MaintainSequence2.FastWriter.countDigits(x))
            i = jcast('int', jcast('int', (jcast('int', jadd(self.ptr, d)) - 1)))
            while (i >= self.ptr):
                self.buf[i] = jcast('byte', jcast('byte', jcast('long', jadd(jchar('0'), jcast('long', jmod(x, 10))))))
                x = jcast('long', jcast('long', jdiv(x, 10)))
                i = jcast('int', (i - 1))
            self.ptr = jcast('int', jcast('int', jadd(self.ptr, d)))
            return self

        def _java_writeln_0(self, x):
            x = jcast('long', x)
            return jcall(self._java_write_2(x), '_java_writeln_1')

        def _java_writeln_1(self):
            return self._java_write_0(jcast('byte', jchar('\n')))

        def innerflush(self):
            try:
                jcall(self.out, 'write', self.buf, 0, self.ptr)
                self.ptr = jcast('int', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_19:
                if jinstanceof(_java_exception_19, 'IOException'):
                    e = _java_exception_19
                    raise jnew('RuntimeException', 'innerflush')
                else:
                    raise

        def flush(self):
            self.innerflush()
            try:
                if (self.writer != None):
                    jcall(self.writer, 'write', jcall(jcast('ByteArrayOutputStream', self.out), 'toString'))
                    self.out = jnew('ByteArrayOutputStream')
                    jcall(self.writer, 'flush')
                else:
                    jcall(self.out, 'flush')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_20:
                if jinstanceof(_java_exception_20, 'IOException'):
                    e = _java_exception_20
                    raise jnew('RuntimeException', 'flush')
                else:
                    raise

        def println(self, x):
            x = jcast('long', x)
            return self._java_writeln_0(x)

        def close(self):
            self.flush()
            try:
                jcall(self.out, 'close')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_21:
                if jinstanceof(_java_exception_21, 'Exception'):
                    e = _java_exception_21
                    None
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [Code05_MaintainSequence2.FastWriter.BUF_SIZE])
            self.out = None
            self.writer = None
            self.ptr = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['Writer'], ['OutputStream'], ['String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code05_MaintainSequence2.FastWriter.FastWriter")

        def write(self, *args):
            _java_choice = jselect(args, [['byte'], ['String'], ['long']], [False, False, False])
            if _java_choice == 0:
                return self._java_write_0(*args)
            if _java_choice == 1:
                return self._java_write_1(*args)
            if _java_choice == 2:
                return self._java_write_2(*args)
            raise TypeError("No matching overload for Code05_MaintainSequence2.FastWriter.write")

        def writeln(self, *args):
            _java_choice = jselect(args, [['long'], []], [False, False])
            if _java_choice == 0:
                return self._java_writeln_0(*args)
            if _java_choice == 1:
                return self._java_writeln_1(*args)
            raise TypeError("No matching overload for Code05_MaintainSequence2.FastWriter.writeln")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


def _java_lambda_15(c, self):
    jset(self.buf, ((_java_obj_16 := self), (_java_key_17 := 'ptr'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4], jcast('byte', c))
    if (self.ptr == Code05_MaintainSequence2.FastWriter.BUF_SIZE):
        self.innerflush()

Code05_MaintainSequence2.MAXN = jcast('int', 500005)
Code05_MaintainSequence2.INF = jcast('int', 1000000001)
Code05_MaintainSequence2.head = jcast('int', 0)
Code05_MaintainSequence2.arr = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.num = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.father = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.left = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.right = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.size = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.space = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.si = jcast('int', 0)
Code05_MaintainSequence2.sum = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.all = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.pre = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.suf = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.update = jarray('boolean', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.change = jarray('int', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.reverse_data = jarray('boolean', [Code05_MaintainSequence2.MAXN])
Code05_MaintainSequence2.FastWriter.BUF_SIZE = jcast('int', jcast('int', (1 << (13 & 31))))

if __name__ == '__main__':
    Code05_MaintainSequence2.main([])

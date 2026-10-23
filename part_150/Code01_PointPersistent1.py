# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 单点修改的可持久化线段树模版题1，Python版
# 给定一个长度为n的数组arr，下标1~n，原始数组认为是0号版本
# 一共有m条操作，每条操作是如下两种类型中的一种
# v 1 x y : 基于v号版本的数组，把x位置的值设置成y，生成新版本的数组
# v 2 x   : 基于v号版本的数组，打印x位置的值，生成新版本的数组和v版本一致
# 每条操作后得到的新版本数组，版本编号为操作的计数
# 1 <= n, m <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P3919
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PointPersistent1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'value': 'value', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    # 原始数组
    arr = None
    # 可持久化线段树需要
    # root[i] : i号版本线段树的头节点编号
    root = None
    left = None
    right = None
    # value[i] : 节点i的值信息，只有叶节点有这个信息
    value = None
    # 可持久化线段树的节点空间计数
    cnt = 0
    # 建树，返回头节点编号
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code01_PointPersistent1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code01_PointPersistent1.value[rt] = jcast('int', Code01_PointPersistent1.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code01_PointPersistent1.left, rt, Code01_PointPersistent1.build(l, mid))
            jset(Code01_PointPersistent1.right, rt, Code01_PointPersistent1.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 线段树范围l~r，信息在i号节点里
    # 在l~r范围上，jobi位置的值，设置成jobv
    # 生成的新节点编号返回
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code01_PointPersistent1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code01_PointPersistent1.left[rt] = jcast('int', Code01_PointPersistent1.left[i])
        Code01_PointPersistent1.right[rt] = jcast('int', Code01_PointPersistent1.right[i])
        Code01_PointPersistent1.value[rt] = jcast('int', Code01_PointPersistent1.value[i])
        if (l == r):
            Code01_PointPersistent1.value[rt] = jcast('int', jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code01_PointPersistent1.left, rt, Code01_PointPersistent1.update(jobi, jobv, l, mid, Code01_PointPersistent1.left[rt]))
            else:
                jset(Code01_PointPersistent1.right, rt, Code01_PointPersistent1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code01_PointPersistent1.right[rt]))
        return jcast('int', rt)

    # 线段树范围l~r，信息在i号节点里
    # 返回l~r范围上jobi位置的值
    @staticmethod
    def query(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', Code01_PointPersistent1.value[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobi <= mid):
            return jcast('int', Code01_PointPersistent1.query(jobi, l, mid, Code01_PointPersistent1.left[i]))
        else:
            return jcast('int', Code01_PointPersistent1.query(jobi, jcast('int', jadd(mid, 1)), r, Code01_PointPersistent1.right[i]))

    @staticmethod
    def main(args):
        io = Code01_PointPersistent1.FastIO(jget(System, 'in'), jget(System, 'out'), _java_ctor=0)
        Code01_PointPersistent1.n = jcast('int', jcall(io, 'nextInt'))
        Code01_PointPersistent1.m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_PointPersistent1.n):
            jset(Code01_PointPersistent1.arr, i, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        jset(Code01_PointPersistent1.root, 0, Code01_PointPersistent1.build(1, Code01_PointPersistent1.n))
        i = jcast('int', 1)
        version = 0
        op = 0
        x = 0
        y = 0
        while (i <= Code01_PointPersistent1.m):
            version = jcast('int', jcall(io, 'nextInt'))
            op = jcast('int', jcall(io, 'nextInt'))
            x = jcast('int', jcall(io, 'nextInt'))
            if (op == 1):
                y = jcast('int', jcall(io, 'nextInt'))
                jset(Code01_PointPersistent1.root, i, Code01_PointPersistent1.update(x, y, 1, Code01_PointPersistent1.n, Code01_PointPersistent1.root[version]))
            else:
                Code01_PointPersistent1.root[i] = jcast('int', Code01_PointPersistent1.root[version])
                jcall(io, 'writelnInt', Code01_PointPersistent1.query(x, 1, Code01_PointPersistent1.n, Code01_PointPersistent1.root[i]))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')

    # 读写工具类
    class FastIO:
        __java_fields__ = {'is': 'is_', 'os': 'os', 'inbuf': 'inbuf', 'lenbuf': 'lenbuf', 'ptrbuf': 'ptrbuf', 'outBuf': 'outBuf'}
        # is_：实例字段，在构造函数中初始化。
        # os：实例字段，在构造函数中初始化。
        # inbuf：实例字段，在构造函数中初始化。
        # lenbuf：实例字段，在构造函数中初始化。
        # ptrbuf：实例字段，在构造函数中初始化。
        # outBuf：实例字段，在构造函数中初始化。
        def _java_init_0(self, is_, os):
            self.is_ = is_
            self.os = os

        def readByte(self):
            if (self.ptrbuf >= self.lenbuf):
                self.ptrbuf = jcast('int', 0)
                try:
                    self.lenbuf = jcast('int', jcall(self.is_, 'read', self.inbuf))
                except (JBreak, JContinue):
                    raise
                except Exception as _java_exception_7:
                    if jinstanceof(_java_exception_7, 'IOException'):
                        e = _java_exception_7
                        raise jnew('RuntimeException', e)
                    else:
                        raise
                if (self.lenbuf == jcast('int', (-1))):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', jcast('int', (self.inbuf[((_java_obj_8 := self), (_java_key_9 := 'ptrbuf'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]] & 255)))

        def skip(self):
            b = 0
            while ((b := self.readByte()) != jcast('int', (-1))):
                if (b > jchar(' ')):
                    return jcast('int', b)
            return jcast('int', jcast('int', (-1)))

        def nextInt(self):
            b = jcast('int', self.skip())
            if (b == jcast('int', (-1))):
                raise jnew('RuntimeException', 'No more integers (EOF)')
            negative = jcast('boolean', False)
            if (b == jchar('-')):
                negative = jcast('boolean', True)
                b = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((b >= jchar('0')) and (b <= jchar('9'))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if negative else val))

        def write(self, s):
            jcall(self.outBuf, 'append', s)

        def writeInt(self, x):
            x = jcast('int', x)
            jcall(self.outBuf, 'append', x)

        def writelnInt(self, x):
            x = jcast('int', x)
            jcall(jcall(self.outBuf, 'append', x), 'append', jchar('\n'))

        def flush(self):
            try:
                jcall(self.os, 'write', jcall(jcall(self.outBuf, 'toString'), 'getBytes'))
                jcall(self.os, 'flush')
                jcall(self.outBuf, 'setLength', 0)
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_11:
                if jinstanceof(_java_exception_11, 'IOException'):
                    e = _java_exception_11
                    raise jnew('RuntimeException', e)
                else:
                    raise

        def __init__(self, *args, _java_ctor=None):
            self.is_ = None
            self.os = None
            self.inbuf = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.lenbuf = jcast('int', 0)
            self.ptrbuf = jcast('int', 0)
            self.outBuf = jnew('StringBuilder')
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream', 'OutputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_PointPersistent1.FastIO.FastIO")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PointPersistent1.MAXN = jcast('int', 1000001)
Code01_PointPersistent1.MAXT = jcast('int', jcast('int', (Code01_PointPersistent1.MAXN * 23)))
Code01_PointPersistent1.n = jcast('int', 0)
Code01_PointPersistent1.m = jcast('int', 0)
Code01_PointPersistent1.arr = jarray('int', [Code01_PointPersistent1.MAXN])
Code01_PointPersistent1.root = jarray('int', [Code01_PointPersistent1.MAXN])
Code01_PointPersistent1.left = jarray('int', [Code01_PointPersistent1.MAXT])
Code01_PointPersistent1.right = jarray('int', [Code01_PointPersistent1.MAXT])
Code01_PointPersistent1.value = jarray('int', [Code01_PointPersistent1.MAXT])
Code01_PointPersistent1.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code01_PointPersistent1.main([])

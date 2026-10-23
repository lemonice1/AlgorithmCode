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

# 位图的实现
# Bitset是一种能以紧凑形式存储位的数据结构
# Bitset(int n) : 初始化n个位，所有位都是0
# void fix(int i) : 将下标i的位上的值更新为1
# void unfix(int i) : 将下标i的位上的值更新为0
# void flip() : 翻转所有位的值
# boolean all() : 是否所有位都是1
# boolean one() : 是否至少有一位是1
# int count() : 返回所有位中1的数量
# String toString() : 返回所有位的状态
class Code02_DesignBitsetTest:
    __java_fields__ = {}
    # 测试链接 : https://leetcode-cn.com/problems/design-bitset/
    class Bitset:
        __java_fields__ = {'set': 'set', 'size': 'size', 'zeros': 'zeros', 'ones': 'ones', 'reverse': 'reverse'}
        # set：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        # zeros：实例字段，在构造函数中初始化。
        # ones：实例字段，在构造函数中初始化。
        # reverse：实例字段，在构造函数中初始化。
        def _java_init_0(self, n):
            n = jcast('int', n)
            self.set = jarray('int', [jcast('int', jdiv(jcast('int', jadd(n, 31)), 32))])
            self.size = jcast('int', n)
            self.zeros = jcast('int', n)
            self.ones = jcast('int', 0)
            self.reverse = jcast('boolean', False)

        # 把i这个数字加入到位图
        def fix(self, i):
            i = jcast('int', i)
            index = jcast('int', jcast('int', jdiv(i, 32)))
            bit = jcast('int', jcast('int', jmod(i, 32)))
            if (not self.reverse):
                # 位图所有位的状态，维持原始含义
                # 0 : 不存在
                # 1 : 存在
                if (jcast('int', (self.set[index] & jcast('int', (1 << (bit & 31))))) == 0):
                    self.zeros = jcast('int', (self.zeros - 1))
                    self.ones = jcast('int', (self.ones + 1))
                    self.set[index] = jcast('int', jcast('int', (self.set[index] | jcast('int', (1 << (bit & 31))))))
            else:
                # 位图所有位的状态，翻转了
                # 0 : 存在
                # 1 : 不存在
                if (jcast('int', (self.set[index] & jcast('int', (1 << (bit & 31))))) != 0):
                    self.zeros = jcast('int', (self.zeros - 1))
                    self.ones = jcast('int', (self.ones + 1))
                    self.set[index] = jcast('int', jcast('int', (self.set[index] ^ jcast('int', (1 << (bit & 31))))))

        # 把i这个数字从位图中移除
        def unfix(self, i):
            i = jcast('int', i)
            index = jcast('int', jcast('int', jdiv(i, 32)))
            bit = jcast('int', jcast('int', jmod(i, 32)))
            if (not self.reverse):
                if (jcast('int', (self.set[index] & jcast('int', (1 << (bit & 31))))) != 0):
                    self.ones = jcast('int', (self.ones - 1))
                    self.zeros = jcast('int', (self.zeros + 1))
                    self.set[index] = jcast('int', jcast('int', (self.set[index] ^ jcast('int', (1 << (bit & 31))))))
            else:
                if (jcast('int', (self.set[index] & jcast('int', (1 << (bit & 31))))) == 0):
                    self.ones = jcast('int', (self.ones - 1))
                    self.zeros = jcast('int', (self.zeros + 1))
                    self.set[index] = jcast('int', jcast('int', (self.set[index] | jcast('int', (1 << (bit & 31))))))

        def flip(self):
            self.reverse = jcast('boolean', (not self.reverse))
            tmp = jcast('int', self.zeros)
            self.zeros = jcast('int', self.ones)
            self.ones = jcast('int', tmp)

        def all(self):
            return jcast('boolean', (self.ones == self.size))

        def one(self):
            return jcast('boolean', (self.ones > 0))

        def count(self):
            return jcast('int', self.ones)

        def toString(self):
            builder = jnew('StringBuilder')
            i = jcast('int', 0)
            k = jcast('int', 0)
            number = 0
            status = 0
            while (i < self.size):
                number = jcast('int', self.set[k])
                j = jcast('int', 0)
                while ((j < 32) and (i < self.size)):
                    status = jcast('int', jcast('int', (jcast('int', (number >> (j & 31))) & 1)))
                    status = jcast('int', jcast('int', (status ^ (1 if self.reverse else 0))))
                    jcall(builder, 'append', status)
                    j = jcast('int', (j + 1))
                    i = jcast('int', (i + 1))
                k = jcast('int', (k + 1))
            return jcall(builder, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.set = None
            self.size = jcast('int', 0)
            self.zeros = jcast('int', 0)
            self.ones = jcast('int', 0)
            self.reverse = jcast('boolean', False)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_DesignBitsetTest.Bitset.Bitset")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



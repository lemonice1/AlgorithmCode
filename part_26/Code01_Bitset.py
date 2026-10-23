# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 位图的实现
# Bitset(int size)
# void add(int num)
# void remove(int num)
# void reverse(int num)
# boolean contains(int num)
class Code01_Bitset:
    __java_fields__ = {}
    # 位图的实现
    # 使用时num不要超过初始化的大小
    class Bitset:
        __java_fields__ = {'set': 'set'}
        # set：实例字段，在构造函数中初始化。
        # n个数字 : 0~n-1
        def _java_init_0(self, n):
            n = jcast('int', n)
            # a/b如果结果想向上取整，可以写成 : (a+b-1)/b
            # 前提是a和b都是非负数
            self.set = jarray('int', [jcast('int', jdiv(jcast('int', jadd(n, 31)), 32))])

        def add(self, num):
            num = jcast('int', num)
            ((_java_obj_1 := self.set), (_java_key_2 := jcast('int', jdiv(num, 32))), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) | jcast('int', (1 << (jcast('int', jmod(num, 32)) & 31)))))))[2]

        def remove(self, num):
            num = jcast('int', num)
            ((_java_obj_3 := self.set), (_java_key_4 := jcast('int', jdiv(num, 32))), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) & jcast('int', (~jcast('int', (1 << (jcast('int', jmod(num, 32)) & 31)))))))))[2]

        def reverse(self, num):
            num = jcast('int', num)
            ((_java_obj_5 := self.set), (_java_key_6 := jcast('int', jdiv(num, 32))), jset(_java_obj_5, _java_key_6, jcast('int', (jget(_java_obj_5, _java_key_6) ^ jcast('int', (1 << (jcast('int', jmod(num, 32)) & 31)))))))[2]

        def contains(self, num):
            num = jcast('int', num)
            return jcast('boolean', (jcast('int', (jcast('int', (self.set[jcast('int', jdiv(num, 32))] >> (jcast('int', jmod(num, 32)) & 31))) & 1)) == 1))

        def __init__(self, *args, _java_ctor=None):
            self.set = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_Bitset.Bitset.Bitset")


    # 对数器测试
    @staticmethod
    def main(args):
        n = jcast('int', 1000)
        testTimes = jcast('int', 10000)
        jprint('测试开始', newline=True)
        # 实现的位图结构
        bitSet = Code01_Bitset.Bitset(n, _java_ctor=0)
        # 直接用HashSet做对比测试
        hashSet = jnew('HashSet')
        jprint('调用阶段开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            decide = jcast('double', jstatic('Math', 'random'))
            # number -> 0 ~ n-1，等概率得到
            number = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            if (decide < 0.333):
                jcall(bitSet, 'add', number)
                jcall(hashSet, 'add', number)
            else:
                if (decide < 0.666):
                    jcall(bitSet, 'remove', number)
                    jcall(hashSet, 'remove', number)
                else:
                    jcall(bitSet, 'reverse', number)
                    if jcall(hashSet, 'contains', number):
                        jcall(hashSet, 'remove', number)
                    else:
                        jcall(hashSet, 'add', number)
            i = jcast('int', (i + 1))
        jprint('调用阶段结束', newline=True)
        jprint('验证阶段开始', newline=True)
        i = jcast('int', 0)
        while (i < n):
            if (jcall(bitSet, 'contains', i) != jcall(hashSet, 'contains', i)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('验证阶段结束', newline=True)
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_Bitset.main([])

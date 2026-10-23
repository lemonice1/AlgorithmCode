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

# 全O(1)的数据结构
class Code07_AllO1:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/all-oone-data-structure/
    class AllOne:
        __java_fields__ = {'head': 'head', 'tail': 'tail', 'map': 'map'}
        class Bucket:
            __java_fields__ = {'set': 'set', 'cnt': 'cnt', 'last': 'last', 'next': 'next'}
            # set：实例字段，在构造函数中初始化。
            # cnt：实例字段，在构造函数中初始化。
            # last：实例字段，在构造函数中初始化。
            # next：实例字段，在构造函数中初始化。
            def _java_init_0(self, s, c):
                c = jcast('int', c)
                self.set = jnew('HashSet')
                jcall(self.set, 'add', s)
                self.cnt = jcast('int', c)

            def __init__(self, *args, _java_ctor=None):
                self.set = None
                self.cnt = jcast('int', 0)
                self.last = None
                self.next = None
                _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['String', 'int']], [False])
                if _java_choice == 0:
                    return self._java_init_0(*args)
                raise TypeError("No matching overload for Code07_AllO1.AllOne.Bucket.Bucket")


        def insert(self, cur, pos):
            jset(jget(cur, 'next'), 'last', pos)
            pos.next = jget(cur, 'next')
            cur.next = pos
            pos.last = cur

        def remove(self, cur):
            jset(jget(cur, 'last'), 'next', jget(cur, 'next'))
            jset(jget(cur, 'next'), 'last', jget(cur, 'last'))

        # head：实例字段，在构造函数中初始化。
        # tail：实例字段，在构造函数中初始化。
        # map：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.head = Code07_AllO1.AllOne.Bucket('', 0, _java_ctor=0)
            self.tail = Code07_AllO1.AllOne.Bucket('', jget(Integer, 'MAX_VALUE'), _java_ctor=0)
            jset(self.head, 'next', self.tail)
            jset(self.tail, 'last', self.head)
            self.map = jnew('HashMap')

        def inc(self, key):
            if (not jcall(self.map, 'containsKey', key)):
                if (jget(jget(self.head, 'next'), 'cnt') == 1):
                    jcall(self.map, 'put', key, jget(self.head, 'next'))
                    jcall(jget(jget(self.head, 'next'), 'set'), 'add', key)
                else:
                    newBucket = Code07_AllO1.AllOne.Bucket(key, 1, _java_ctor=0)
                    jcall(self.map, 'put', key, newBucket)
                    self.insert(self.head, newBucket)
            else:
                bucket = jcall(self.map, 'get', key)
                if (jget(jget(bucket, 'next'), 'cnt') == jcast('int', jadd(jget(bucket, 'cnt'), 1))):
                    jcall(self.map, 'put', key, jget(bucket, 'next'))
                    jcall(jget(jget(bucket, 'next'), 'set'), 'add', key)
                else:
                    newBucket = Code07_AllO1.AllOne.Bucket(key, jcast('int', jadd(jget(bucket, 'cnt'), 1)), _java_ctor=0)
                    jcall(self.map, 'put', key, newBucket)
                    self.insert(bucket, newBucket)
                jcall(jget(bucket, 'set'), 'remove', key)
                if jcall(jget(bucket, 'set'), 'isEmpty'):
                    self.remove(bucket)

        def dec(self, key):
            bucket = jcall(self.map, 'get', key)
            if (jget(bucket, 'cnt') == 1):
                jcall(self.map, 'remove', key)
            else:
                if (jget(jget(bucket, 'last'), 'cnt') == jcast('int', (jget(bucket, 'cnt') - 1))):
                    jcall(self.map, 'put', key, jget(bucket, 'last'))
                    jcall(jget(jget(bucket, 'last'), 'set'), 'add', key)
                else:
                    newBucket = Code07_AllO1.AllOne.Bucket(key, jcast('int', (jget(bucket, 'cnt') - 1)), _java_ctor=0)
                    jcall(self.map, 'put', key, newBucket)
                    self.insert(jget(bucket, 'last'), newBucket)
            jcall(jget(bucket, 'set'), 'remove', key)
            if jcall(jget(bucket, 'set'), 'isEmpty'):
                self.remove(bucket)

        def getMaxKey(self):
            return jcall(jcall(jget(jget(self.tail, 'last'), 'set'), 'iterator'), 'next')

        def getMinKey(self):
            return jcall(jcall(jget(jget(self.head, 'next'), 'set'), 'iterator'), 'next')

        def __init__(self, *args, _java_ctor=None):
            self.head = None
            self.tail = None
            self.map = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_AllO1.AllOne.AllOne")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



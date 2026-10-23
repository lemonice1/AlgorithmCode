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

# 破解保险箱，Python版
# 给定正数n，表示密码有n位，给定正数k，表示每一位可能的数字是[0..k-1]
# 密码有(k^n)个可能性，构造一个字符串，其中的连续子串包含所有可能的密码
# 先保证字符串的长度最短，作为加强要求，保证字典序尽量的小，返回字符串
# 1 <= n <= 4    1 <= k <= 10
# 测试链接 : https://leetcode.cn/problems/cracking-the-safe/
# 在线评测时提交题目要求的方法接口，并一并提供使用到的公共辅助模块
class Code06_CrackingTheSafe1:
    __java_fields__ = {}
    class Solution:
        __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'm': 'm', 'cur': 'cur', 'path': 'path', 'cntp': 'cntp', 'sta': 'sta', 'u': 'u', 'e': 'e', 'stacksize': 'stacksize'}
        # MAXN：实例字段，在构造函数中初始化。
        # n：实例字段，在构造函数中初始化。
        # k：实例字段，在构造函数中初始化。
        # m：实例字段，在构造函数中初始化。
        # cur：实例字段，在构造函数中初始化。
        # path：实例字段，在构造函数中初始化。
        # cntp：实例字段，在构造函数中初始化。
        # sta：实例字段，在构造函数中初始化。
        # u：实例字段，在构造函数中初始化。
        # e：实例字段，在构造函数中初始化。
        # stacksize：实例字段，在构造函数中初始化。
        def push(self, u, e):
            u = jcast('int', u)
            e = jcast('int', e)
            jset(self.sta[self.stacksize], 0, u)
            jset(self.sta[self.stacksize], 1, e)
            self.stacksize = jcast('int', (self.stacksize + 1))

        def pop(self):
            self.stacksize = jcast('int', (self.stacksize - 1))
            self.u = jcast('int', self.sta[self.stacksize][0])
            self.e = jcast('int', self.sta[self.stacksize][1])

        def prepare(self, len, num):
            len = jcast('int', len)
            num = jcast('int', num)
            self.n = jcast('int', len)
            self.k = jcast('int', num)
            self.m = jcast('int', 1)
            i = jcast('int', 1)
            while (i <= jcast('int', (self.n - 1))):
                self.m = jcast('int', jcast('int', (self.m * self.k)))
                i = jcast('int', (i + 1))
            i = jcast('int', 0)
            while (i < self.m):
                self.cur[i] = jcast('int', 0)
                i = jcast('int', (i + 1))
            self.cntp = jcast('int', 0)

        # 递归版
        def euler1(self, u, e):
            u = jcast('int', u)
            e = jcast('int', e)
            while (self.cur[u] < self.k):
                ne = jcast('int', ((_java_obj_1 := self.cur), (_java_key_2 := u), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
                self.euler1(jcast('int', jmod(jcast('int', jadd(jcast('int', (u * self.k)), ne)), self.m)), ne)
            jset(self.path, ((_java_obj_4 := self), (_java_key_5 := 'cntp'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], e)

        # 迭代版
        def euler2(self, node, edge):
            node = jcast('int', node)
            edge = jcast('int', edge)
            self.stacksize = jcast('int', 0)
            self.push(node, edge)
            while (self.stacksize > 0):
                self.pop()
                if (self.cur[self.u] < self.k):
                    ne = jcast('int', ((_java_obj_7 := self.cur), (_java_key_8 := self.u), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4])
                    self.push(self.u, self.e)
                    self.push(jcast('int', jmod(jcast('int', jadd(jcast('int', (self.u * self.k)), ne)), self.m)), ne)
                else:
                    jset(self.path, ((_java_obj_10 := self), (_java_key_11 := 'cntp'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], self.e)

        def crackSafe(self, len, num):
            len = jcast('int', len)
            num = jcast('int', num)
            self.prepare(len, num)
            self.euler1(0, jcast('int', (-1)))
            # euler2(0, -1);
            str = jnew('StringBuilder')
            i = jcast('int', 1)
            while (i <= jcast('int', (self.n - 1))):
                jcall(str, 'append', '0')
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', (self.cntp - 1)))
            while (i >= 1):
                jcall(str, 'append', self.path[i])
                i = jcast('int', (i - 1))
            return jcall(str, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.MAXN = jcast('int', 5001)
            self.n = jcast('int', 0)
            self.k = jcast('int', 0)
            self.m = jcast('int', 0)
            self.cur = jarray('int', [self.MAXN])
            self.path = jarray('int', [self.MAXN])
            self.cntp = jcast('int', 0)
            self.sta = jarray('int', [self.MAXN, 2])
            self.u = jcast('int', 0)
            self.e = jcast('int', 0)
            self.stacksize = jcast('int', 0)
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



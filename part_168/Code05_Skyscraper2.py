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

# 雅加达的摩天楼，Python版
# 有n个大楼，编号0~n-1，有m个狗子，编号0~m-1
# 每只狗子有两个参数，idx表示狗子的初始大楼，jump表示狗子的跳跃能力
# 狗子在i位置，可以来到 i - jump 或 i + jump，向左向右自由跳跃，但不能越界
# 0号狗子有消息希望传给1号狗子，所有狗子都可帮忙，返回至少传送几次，无法送达打印-1
# 1 <= n、m <= 30000
# 测试链接 : https://www.luogu.com.cn/problem/P3645
# 测试链接 : https://uoj.ac/problem/111
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Skyscraper2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'que': 'que', 'vis': 'vis'}
    class Node:
        __java_fields__ = {'idx': 'idx', 'jump': 'jump', 'time': 'time'}
        # idx：实例字段，在构造函数中初始化。
        # jump：实例字段，在构造函数中初始化。
        # time：实例字段，在构造函数中初始化。
        def _java_init_0(self, i, j, t):
            i = jcast('int', i)
            j = jcast('int', j)
            t = jcast('int', t)
            self.idx = jcast('int', i)
            self.jump = jcast('int', j)
            self.time = jcast('int', t)

        def __init__(self, *args, _java_ctor=None):
            self.idx = jcast('int', 0)
            self.jump = jcast('int', 0)
            self.time = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['int', 'int', 'int']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Skyscraper2.Node.Node")


    MAXN = 0
    n = 0
    m = 0
    # 每个大楼拥有的狗子列表
    head = None
    next = None
    to = None
    cnt = 0
    # bfs过程
    que = None
    # vis[idx]是个位图，可以表示vis[idx][jump]是否出现过
    vis = None
    @staticmethod
    def add(idx, jump):
        idx = jcast('int', idx)
        jump = jcast('int', jump)
        jset(Code05_Skyscraper2.next, ((_java_obj_1 := Code05_Skyscraper2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code05_Skyscraper2.head[idx])
        Code05_Skyscraper2.to[Code05_Skyscraper2.cnt] = jcast('int', jump)
        Code05_Skyscraper2.head[idx] = jcast('int', Code05_Skyscraper2.cnt)

    @staticmethod
    def trigger(idx, time):
        idx = jcast('int', idx)
        time = jcast('int', time)
        e = jcast('int', Code05_Skyscraper2.head[idx])
        jump = 0
        while (e > 0):
            jump = jcast('int', Code05_Skyscraper2.to[e])
            if (not jcall(Code05_Skyscraper2.vis[idx], 'get', jump)):
                jcall(Code05_Skyscraper2.vis[idx], 'set', jump)
                jcall(Code05_Skyscraper2.que, 'addLast', Code05_Skyscraper2.Node(idx, jump, time, _java_ctor=0))
            e = jcast('int', Code05_Skyscraper2.next[e])
        Code05_Skyscraper2.head[idx] = jcast('int', 0)

    @staticmethod
    def extend(idx, jump, time):
        idx = jcast('int', idx)
        jump = jcast('int', jump)
        time = jcast('int', time)
        Code05_Skyscraper2.trigger(idx, time)
        if (not jcall(Code05_Skyscraper2.vis[idx], 'get', jump)):
            jcall(Code05_Skyscraper2.vis[idx], 'set', jump)
            jcall(Code05_Skyscraper2.que, 'addLast', Code05_Skyscraper2.Node(idx, jump, time, _java_ctor=0))

    @staticmethod
    def bfs(s, t):
        s = jcast('int', s)
        t = jcast('int', t)
        if (s == t):
            return jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code05_Skyscraper2.MAXN):
            jset(Code05_Skyscraper2.vis, i, jnew('BitSet'))
            i = jcast('int', (i + 1))
        Code05_Skyscraper2.trigger(s, 0)
        while (not jcall(Code05_Skyscraper2.que, 'isEmpty')):
            cur = jcall(Code05_Skyscraper2.que, 'pollFirst')
            idx = jcast('int', jget(cur, 'idx'))
            jump = jcast('int', jget(cur, 'jump'))
            time = jcast('int', jget(cur, 'time'))
            if ((jcast('int', (idx - jump)) == t) or (jcast('int', jadd(idx, jump)) == t)):
                return jcast('int', jcast('int', jadd(time, 1)))
            if (jcast('int', (idx - jump)) >= 0):
                Code05_Skyscraper2.extend(jcast('int', (idx - jump)), jump, jcast('int', jadd(time, 1)))
            if (jcast('int', jadd(idx, jump)) < Code05_Skyscraper2.n):
                Code05_Skyscraper2.extend(jcast('int', jadd(idx, jump)), jump, jcast('int', jadd(time, 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def main(args):
        in_ = Code05_Skyscraper2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jget(System, 'out'))
        Code05_Skyscraper2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_Skyscraper2.m = jcast('int', jcall(in_, 'nextInt'))
        s = jcast('int', jcall(in_, 'nextInt'))
        sjump = jcast('int', jcall(in_, 'nextInt'))
        t = jcast('int', jcall(in_, 'nextInt'))
        tjump = jcast('int', jcall(in_, 'nextInt'))
        Code05_Skyscraper2.add(s, sjump)
        Code05_Skyscraper2.add(t, tjump)
        i = jcast('int', 2)
        idx = 0
        jump = 0
        while (i < Code05_Skyscraper2.m):
            idx = jcast('int', jcall(in_, 'nextInt'))
            jump = jcast('int', jcall(in_, 'nextInt'))
            Code05_Skyscraper2.add(idx, jump)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_Skyscraper2.bfs(s, t))
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_Skyscraper2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Skyscraper2.MAXN = jcast('int', 30001)
Code05_Skyscraper2.n = jcast('int', 0)
Code05_Skyscraper2.m = jcast('int', 0)
Code05_Skyscraper2.head = jarray('int', [Code05_Skyscraper2.MAXN])
Code05_Skyscraper2.next = jarray('int', [Code05_Skyscraper2.MAXN])
Code05_Skyscraper2.to = jarray('int', [Code05_Skyscraper2.MAXN])
Code05_Skyscraper2.cnt = jcast('int', 0)
Code05_Skyscraper2.que = jnew('ArrayDeque')
Code05_Skyscraper2.vis = jarray('BitSet', [Code05_Skyscraper2.MAXN])

if __name__ == '__main__':
    Code05_Skyscraper2.main([])

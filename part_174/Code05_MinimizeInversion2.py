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

# 最小化逆序对，Python版
# 给定数字n，表示一棵二叉树有n个叶节点，叶节点的权值都不同并且都是1~n范围的数字
# 树上的任何节点，要么是叶节点，要么一定有两个孩子，请从输入流中不断读取数字x来建树
# 如果 x != 0，表示当前来到叶节点并且权值为x，注意只有叶节点有权值
# 如果 x == 0，表示当前来到非叶节点，先递归建立左树，再递归建立右树
# 输入流保证根据规则可以建好这棵二叉树，你可以任选一些节点，交换这些节点的左右子树
# 目的是先序遍历整棵树之后，所有叶节点权值组成的序列中，逆序对数量尽可能小，打印这个最小值
# 2 <= n <= 2 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3521
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MinimizeInversion2:
    __java_fields__ = {'MAXT': 'MAXT', 'n': 'n', 'ls': 'ls', 'rs': 'rs', 'siz': 'siz', 'cntt': 'cntt', 'ans': 'ans', 'no': 'no', 'yes': 'yes', 'in': 'in_', 'out': 'out'}
    MAXT = 0
    n = 0
    ls = None
    rs = None
    siz = None
    cntt = 0
    ans = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code05_MinimizeInversion2.siz[i] = jcast('int', jcast('int', jadd(Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.ls[i]], Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.rs[i]])))

    @staticmethod
    def build(jobi, l, r):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code05_MinimizeInversion2), (_java_key_2 := 'cntt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code05_MinimizeInversion2.siz[rt] = jcast('int', (Code05_MinimizeInversion2.siz[rt] + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code05_MinimizeInversion2.ls, rt, Code05_MinimizeInversion2.build(jobi, l, mid))
            else:
                jset(Code05_MinimizeInversion2.rs, rt, Code05_MinimizeInversion2.build(jobi, jcast('int', jadd(mid, 1)), r))
            Code05_MinimizeInversion2.up(rt)
        return jcast('int', rt)

    no = 0
    yes = 0
    @staticmethod
    def merge(l, r, t1, t2):
        l = jcast('int', l)
        r = jcast('int', r)
        t1 = jcast('int', t1)
        t2 = jcast('int', t2)
        if ((t1 == 0) or (t2 == 0)):
            return jcast('int', jcast('int', jadd(t1, t2)))
        if (l == r):
            Code05_MinimizeInversion2.siz[t1] = jcast('int', jcast('int', jadd(Code05_MinimizeInversion2.siz[t1], Code05_MinimizeInversion2.siz[t2])))
        else:
            Code05_MinimizeInversion2.no = jcast('int', jcast('long', jadd(Code05_MinimizeInversion2.no, jcast('long', (jcast('long', Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.rs[t1]]) * Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.ls[t2]])))))
            Code05_MinimizeInversion2.yes = jcast('int', jcast('long', jadd(Code05_MinimizeInversion2.yes, jcast('long', (jcast('long', Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.rs[t2]]) * Code05_MinimizeInversion2.siz[Code05_MinimizeInversion2.ls[t1]])))))
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            jset(Code05_MinimizeInversion2.ls, t1, Code05_MinimizeInversion2.merge(l, mid, Code05_MinimizeInversion2.ls[t1], Code05_MinimizeInversion2.ls[t2]))
            jset(Code05_MinimizeInversion2.rs, t1, Code05_MinimizeInversion2.merge(jcast('int', jadd(mid, 1)), r, Code05_MinimizeInversion2.rs[t1], Code05_MinimizeInversion2.rs[t2]))
            Code05_MinimizeInversion2.up(t1)
        return jcast('int', t1)

    @staticmethod
    def dfs():
        rt = 0
        val = jcast('int', jcall(Code05_MinimizeInversion2.in_, 'nextInt'))
        if (val == 0):
            left = jcast('int', Code05_MinimizeInversion2.dfs())
            right = jcast('int', Code05_MinimizeInversion2.dfs())
            Code05_MinimizeInversion2.no = jcast('int', jset(Code05_MinimizeInversion2, 'yes', 0))
            rt = jcast('int', Code05_MinimizeInversion2.merge(1, Code05_MinimizeInversion2.n, left, right))
            Code05_MinimizeInversion2.ans = jcast('long', jcast('long', jadd(Code05_MinimizeInversion2.ans, jstatic('Math', 'min', Code05_MinimizeInversion2.no, Code05_MinimizeInversion2.yes))))
        else:
            rt = jcast('int', Code05_MinimizeInversion2.build(val, 1, Code05_MinimizeInversion2.n))
        return jcast('int', rt)

    in_ = None
    out = None
    @staticmethod
    def main(args):
        Code05_MinimizeInversion2.n = jcast('int', jcall(Code05_MinimizeInversion2.in_, 'nextInt'))
        Code05_MinimizeInversion2.dfs()
        jcall(Code05_MinimizeInversion2.out, 'println', Code05_MinimizeInversion2.ans)
        jcall(Code05_MinimizeInversion2.out, 'flush')
        jcall(Code05_MinimizeInversion2.out, 'close')

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
            raise TypeError("No matching overload for Code05_MinimizeInversion2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MinimizeInversion2.MAXT = jcast('int', 5000001)
Code05_MinimizeInversion2.n = jcast('int', 0)
Code05_MinimizeInversion2.ls = jarray('int', [Code05_MinimizeInversion2.MAXT])
Code05_MinimizeInversion2.rs = jarray('int', [Code05_MinimizeInversion2.MAXT])
Code05_MinimizeInversion2.siz = jarray('int', [Code05_MinimizeInversion2.MAXT])
Code05_MinimizeInversion2.cntt = jcast('int', 0)
Code05_MinimizeInversion2.ans = jcast('long', 0)
Code05_MinimizeInversion2.no = jcast('int', 0)
Code05_MinimizeInversion2.yes = jcast('int', 0)
Code05_MinimizeInversion2.in_ = Code05_MinimizeInversion2.FastReader(jget(System, 'in'), _java_ctor=0)
Code05_MinimizeInversion2.out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))

if __name__ == '__main__':
    Code05_MinimizeInversion2.main([])

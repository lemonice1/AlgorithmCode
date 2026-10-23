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

# 最小异或查询，Python版
# 一共有q条操作，每种操作是如下三种类型中的一种
# 操作 1 x : 黑板上写上一个数字x，同一种数字可以出现多次
# 操作 2 x : 将一个x从黑板上擦掉，操作时保证至少有一个x在黑板上
# 操作 3   : 打印黑板上任意两数的最小异或值，操作时保证黑板上至少有两个数
# 1 <= q <= 3 * 10^5
# 0 <= x <= 2^30
# 测试链接 : https://www.luogu.com.cn/problem/AT_abc308_g
# 测试链接 : https://atcoder.jp/contests/abc308/tasks/abc308_g
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_MinimumXor1:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'INF': 'INF', 'fa': 'fa', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt', 'mineor': 'mineor', 'only': 'only'}
    MAXN = 0
    BIT = 0
    INF = 0
    fa = None
    tree = None
    pass_ = None
    cnt = 0
    # 整棵树上最小异或值
    mineor = None
    # 整棵树上如果只有一个数x，才有记录，否则记录是0
    only = None
    @staticmethod
    def change(x, changeCnt):
        x = jcast('int', x)
        changeCnt = jcast('int', changeCnt)
        cur = jcast('int', 1)
        Code07_MinimumXor1.pass_[cur] = jcast('int', jcast('int', jadd(Code07_MinimumXor1.pass_[cur], changeCnt)))
        b = jcast('int', Code07_MinimumXor1.BIT)
        path = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (x >> (b & 31))) & 1)))
            if (Code07_MinimumXor1.tree[cur][path] == 0):
                jset(Code07_MinimumXor1.tree[cur], path, ((_java_obj_1 := Code07_MinimumXor1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
                jset(Code07_MinimumXor1.fa, Code07_MinimumXor1.tree[cur][path], cur)
            cur = jcast('int', Code07_MinimumXor1.tree[cur][path])
            Code07_MinimumXor1.pass_[cur] = jcast('int', jcast('int', jadd(Code07_MinimumXor1.pass_[cur], changeCnt)))
            b = jcast('int', (b - 1))
        return jcast('int', cur)

    @staticmethod
    def compute(x, changeCnt):
        x = jcast('int', x)
        changeCnt = jcast('int', changeCnt)
        bottom = jcast('int', Code07_MinimumXor1.change(x, changeCnt))
        Code07_MinimumXor1.mineor[bottom] = jcast('int', (0 if (Code07_MinimumXor1.pass_[bottom] >= 2) else Code07_MinimumXor1.INF))
        Code07_MinimumXor1.only[bottom] = jcast('int', (x if (Code07_MinimumXor1.pass_[bottom] == 1) else 0))
        i = jcast('int', Code07_MinimumXor1.fa[bottom])
        l = 0
        r = 0
        while (i > 0):
            l = jcast('int', Code07_MinimumXor1.tree[i][0])
            r = jcast('int', Code07_MinimumXor1.tree[i][1])
            if (Code07_MinimumXor1.pass_[i] < 2):
                Code07_MinimumXor1.mineor[i] = jcast('int', Code07_MinimumXor1.INF)
            else:
                if ((Code07_MinimumXor1.pass_[l] == 1) and (Code07_MinimumXor1.pass_[r] == 1)):
                    Code07_MinimumXor1.mineor[i] = jcast('int', jcast('int', (Code07_MinimumXor1.only[l] ^ Code07_MinimumXor1.only[r])))
                else:
                    if ((Code07_MinimumXor1.pass_[l] == 0) ^ (Code07_MinimumXor1.pass_[r] == 0)):
                        Code07_MinimumXor1.mineor[i] = jcast('int', (Code07_MinimumXor1.mineor[r] if (Code07_MinimumXor1.pass_[l] == 0) else Code07_MinimumXor1.mineor[l]))
                    else:
                        jset(Code07_MinimumXor1.mineor, i, jstatic('Math', 'min', Code07_MinimumXor1.mineor[l], Code07_MinimumXor1.mineor[r]))
            if (jcast('int', jadd(Code07_MinimumXor1.pass_[l], Code07_MinimumXor1.pass_[r])) == 1):
                Code07_MinimumXor1.only[i] = jcast('int', (Code07_MinimumXor1.only[l] if (Code07_MinimumXor1.pass_[l] == 1) else Code07_MinimumXor1.only[r]))
            else:
                Code07_MinimumXor1.only[i] = jcast('int', 0)
            i = jcast('int', Code07_MinimumXor1.fa[i])

    @staticmethod
    def main(args):
        in_ = Code07_MinimumXor1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        op = 0
        x = 0
        while (i <= q):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 3):
                jcall(out, 'println', Code07_MinimumXor1.mineor[1])
            else:
                x = jcast('int', jcall(in_, 'nextInt'))
                if (op == 1):
                    Code07_MinimumXor1.compute(x, 1)
                else:
                    Code07_MinimumXor1.compute(x, jcast('int', (-1)))
            i = jcast('int', (i + 1))
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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_MinimumXor1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_MinimumXor1.MAXN = jcast('int', 10000001)
Code07_MinimumXor1.BIT = jcast('int', 29)
Code07_MinimumXor1.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code07_MinimumXor1.fa = jarray('int', [Code07_MinimumXor1.MAXN])
Code07_MinimumXor1.tree = jarray('int', [Code07_MinimumXor1.MAXN, 2])
Code07_MinimumXor1.pass_ = jarray('int', [Code07_MinimumXor1.MAXN])
Code07_MinimumXor1.cnt = jcast('int', 1)
Code07_MinimumXor1.mineor = jarray('int', [Code07_MinimumXor1.MAXN])
Code07_MinimumXor1.only = jarray('int', [Code07_MinimumXor1.MAXN])

if __name__ == '__main__':
    Code07_MinimumXor1.main([])

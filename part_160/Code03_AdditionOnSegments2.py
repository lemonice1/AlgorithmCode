# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 打印所有合法数，Python版
# 一个长度为n的序列，一开始所有值都是0
# 一共有q条操作，每条操作为 l r k : 序列[l..r]范围上，每个数字加k
# 你可以随意选择操作来执行，但是每条操作只能执行一次
# 如果你能让序列中的最大值正好为v，那么v就算一个合法数
# 打印1~n范围内有多少合法数，并且从小到大打印所有的合法数
# 1 <= k <= n、q <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/CF981E
# 测试链接 : https://codeforces.com/problemset/problem/981/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_AdditionOnSegments2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'DEEP': 'DEEP', 'INT_BIT': 'INT_BIT', 'LEN': 'LEN', 'n': 'n', 'q': 'q', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'tmp': 'tmp', 'dp': 'dp', 'backup': 'backup', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    DEEP = 0
    INT_BIT = 0
    LEN = 0
    n = 0
    q = 0
    head = None
    next = None
    to = None
    cnt = 0
    tmp = None
    dp = None
    backup = None
    ans = None
    # 清空
    @staticmethod
    def clear(bitset):
        i = jcast('int', 0)
        while (i < Code03_AdditionOnSegments2.LEN):
            bitset[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    # 位图set1 拷贝 位图set2
    @staticmethod
    def clone(set1, set2):
        i = jcast('int', 0)
        while (i < Code03_AdditionOnSegments2.LEN):
            set1[i] = jcast('int', set2[i])
            i = jcast('int', (i + 1))

    # 返回位图第i位的状态
    @staticmethod
    def getBit(bitset, i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (jcast('int', (bitset[jcast('int', jdiv(i, Code03_AdditionOnSegments2.INT_BIT))] >> (jcast('int', jmod(i, Code03_AdditionOnSegments2.INT_BIT)) & 31))) & 1)))

    # 第i位的状态设置成v
    @staticmethod
    def setBit(bitset, i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        if (v == 0):
            ((_java_obj_1 := bitset), (_java_key_2 := jcast('int', jdiv(i, Code03_AdditionOnSegments2.INT_BIT))), jset(_java_obj_1, _java_key_2, jcast('int', (jget(_java_obj_1, _java_key_2) & jcast('int', (~jcast('int', (1 << (jcast('int', jmod(i, Code03_AdditionOnSegments2.INT_BIT)) & 31)))))))))[2]
        else:
            ((_java_obj_3 := bitset), (_java_key_4 := jcast('int', jdiv(i, Code03_AdditionOnSegments2.INT_BIT))), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) | jcast('int', (1 << (jcast('int', jmod(i, Code03_AdditionOnSegments2.INT_BIT)) & 31)))))))[2]

    # 位图set1 或 位图set2
    @staticmethod
    def bitOr(set1, set2):
        i = jcast('int', 0)
        while (i < Code03_AdditionOnSegments2.LEN):
            set1[i] = jcast('int', jcast('int', (set1[i] | set2[i])))
            i = jcast('int', (i + 1))

    # 位图ret 变成 位图bitset左移move位的状态
    # 不使用一位一位拷贝的方式，因为太慢了
    # 采用整块左移的方式，这样比较快
    @staticmethod
    def bitLeft(ret, bitset, move):
        move = jcast('int', move)
        Code03_AdditionOnSegments2.clear(ret)
        if (move > Code03_AdditionOnSegments2.BIT):
            return
        if (move <= 0):
            Code03_AdditionOnSegments2.clone(ret, bitset)
            return
        shift = jcast('int', jcast('int', jdiv(move, Code03_AdditionOnSegments2.INT_BIT)))
        offset = jcast('int', jcast('int', jmod(move, Code03_AdditionOnSegments2.INT_BIT)))
        if (offset == 0):
            i = jcast('int', jcast('int', (Code03_AdditionOnSegments2.LEN - 1)))
            j = jcast('int', jcast('int', (i - shift)))
            while (j >= 0):
                ret[i] = jcast('int', bitset[j])
                i = jcast('int', (i - 1))
                j = jcast('int', (j - 1))
        else:
            carry = jcast('int', jcast('int', (Code03_AdditionOnSegments2.INT_BIT - offset)))
            high = 0
            low = 0
            i = jcast('int', jcast('int', (Code03_AdditionOnSegments2.LEN - 1)))
            while (i > shift):
                high = jcast('int', jcast('int', (bitset[jcast('int', (i - shift))] << (offset & 31))))
                low = jcast('int', jcast('int', jushr(bitset[jcast('int', (jcast('int', (i - shift)) - 1))], carry, 32)))
                ret[i] = jcast('int', jcast('int', (high | low)))
                i = jcast('int', (i - 1))
            ret[shift] = jcast('int', jcast('int', (bitset[0] << (offset & 31))))
        # 最高位BIT到最低位0，一共BIT+1个有效位
        # 其他更高位信息需要清空，rest就是有多少无效的更高位
        rest = jcast('int', jcast('int', (jcast('int', (Code03_AdditionOnSegments2.LEN * Code03_AdditionOnSegments2.INT_BIT)) - jcast('int', jadd(Code03_AdditionOnSegments2.BIT, 1)))))
        if (rest > 0):
            ret[jcast('int', (Code03_AdditionOnSegments2.LEN - 1))] = jcast('int', jcast('int', (ret[jcast('int', (Code03_AdditionOnSegments2.LEN - 1))] & jcast('int', (jcast('int', (1 << (jcast('int', (Code03_AdditionOnSegments2.INT_BIT - rest)) & 31))) - 1)))))

    @staticmethod
    def addEdge(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code03_AdditionOnSegments2.next, ((_java_obj_5 := Code03_AdditionOnSegments2), (_java_key_6 := 'cnt'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3], Code03_AdditionOnSegments2.head[i])
        Code03_AdditionOnSegments2.to[Code03_AdditionOnSegments2.cnt] = jcast('int', v)
        Code03_AdditionOnSegments2.head[i] = jcast('int', Code03_AdditionOnSegments2.cnt)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_AdditionOnSegments2.addEdge(i, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_AdditionOnSegments2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_AdditionOnSegments2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i, dep):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dep = jcast('int', dep)
        Code03_AdditionOnSegments2.clone(Code03_AdditionOnSegments2.backup[dep], Code03_AdditionOnSegments2.dp)
        e = jcast('int', Code03_AdditionOnSegments2.head[i])
        while (e > 0):
            Code03_AdditionOnSegments2.bitLeft(Code03_AdditionOnSegments2.tmp, Code03_AdditionOnSegments2.dp, Code03_AdditionOnSegments2.to[e])
            Code03_AdditionOnSegments2.bitOr(Code03_AdditionOnSegments2.dp, Code03_AdditionOnSegments2.tmp)
            e = jcast('int', Code03_AdditionOnSegments2.next[e])
        if (l == r):
            Code03_AdditionOnSegments2.bitOr(Code03_AdditionOnSegments2.ans, Code03_AdditionOnSegments2.dp)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code03_AdditionOnSegments2.dfs(l, mid, jcast('int', (i << (1 & 31))), jcast('int', jadd(dep, 1)))
            Code03_AdditionOnSegments2.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)), jcast('int', jadd(dep, 1)))
        Code03_AdditionOnSegments2.clone(Code03_AdditionOnSegments2.dp, Code03_AdditionOnSegments2.backup[dep])

    @staticmethod
    def main(args):
        in_ = Code03_AdditionOnSegments2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_AdditionOnSegments2.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_AdditionOnSegments2.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        l = 0
        r = 0
        k = 0
        while (i <= Code03_AdditionOnSegments2.q):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            k = jcast('int', jcall(in_, 'nextInt'))
            Code03_AdditionOnSegments2.add(l, r, k, 1, Code03_AdditionOnSegments2.n, 1)
            i = jcast('int', (i + 1))
        Code03_AdditionOnSegments2.setBit(Code03_AdditionOnSegments2.dp, 0, 1)
        Code03_AdditionOnSegments2.dfs(1, Code03_AdditionOnSegments2.n, 1, 1)
        ansCnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_AdditionOnSegments2.n):
            if (Code03_AdditionOnSegments2.getBit(Code03_AdditionOnSegments2.ans, i) == 1):
                ansCnt = jcast('int', (ansCnt + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ansCnt)
        i = jcast('int', 1)
        while (i <= Code03_AdditionOnSegments2.n):
            if (Code03_AdditionOnSegments2.getBit(Code03_AdditionOnSegments2.ans, i) == 1):
                jcall(out, 'print', jadd(i, ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code03_AdditionOnSegments2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_AdditionOnSegments2.MAXN = jcast('int', 10001)
Code03_AdditionOnSegments2.MAXT = jcast('int', 500001)
Code03_AdditionOnSegments2.BIT = jcast('int', 10000)
Code03_AdditionOnSegments2.DEEP = jcast('int', 20)
Code03_AdditionOnSegments2.INT_BIT = jcast('int', 32)
Code03_AdditionOnSegments2.LEN = jcast('int', jcast('int', jadd(jcast('int', jdiv(Code03_AdditionOnSegments2.BIT, Code03_AdditionOnSegments2.INT_BIT)), 1)))
Code03_AdditionOnSegments2.n = jcast('int', 0)
Code03_AdditionOnSegments2.q = jcast('int', 0)
Code03_AdditionOnSegments2.head = jarray('int', [jcast('int', (Code03_AdditionOnSegments2.MAXN << (2 & 31)))])
Code03_AdditionOnSegments2.next = jarray('int', [Code03_AdditionOnSegments2.MAXT])
Code03_AdditionOnSegments2.to = jarray('int', [Code03_AdditionOnSegments2.MAXT])
Code03_AdditionOnSegments2.cnt = jcast('int', 0)
Code03_AdditionOnSegments2.tmp = jarray('int', [Code03_AdditionOnSegments2.LEN])
Code03_AdditionOnSegments2.dp = jarray('int', [Code03_AdditionOnSegments2.LEN])
Code03_AdditionOnSegments2.backup = jarray('int', [Code03_AdditionOnSegments2.DEEP, Code03_AdditionOnSegments2.LEN])
Code03_AdditionOnSegments2.ans = jarray('int', [Code03_AdditionOnSegments2.LEN])

if __name__ == '__main__':
    Code03_AdditionOnSegments2.main([])

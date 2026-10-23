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

# 一开始1~n范围上的数字都是0，一共有m个操作，每次操作为(l,r,s,e,d)
# 表示在l~r范围上依次加上首项为s、末项为e、公差为d的数列
# m个操作做完之后，统计1~n范围上所有数字的最大值和异或和
# 测试链接 : https://www.luogu.com.cn/problem/P4231
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_ArithmeticSequenceDifference:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'm': 'm'}
    MAXN = 0
    arr = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_ArithmeticSequenceDifference.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_ArithmeticSequenceDifference.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            l = 0
            r = 0
            s = 0
            e = 0
            while (i < Code02_ArithmeticSequenceDifference.m):
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                s = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                e = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_ArithmeticSequenceDifference.set(l, r, s, e, jcast('int', jdiv(jcast('int', (e - s)), jcast('int', (r - l)))))
                i = jcast('int', (i + 1))
            Code02_ArithmeticSequenceDifference.build()
            max = jcast('long', 0)
            xor = jcast('long', 0)
            i = jcast('int', 1)
            while (i <= Code02_ArithmeticSequenceDifference.n):
                max = jcast('long', jstatic('Math', 'max', max, Code02_ArithmeticSequenceDifference.arr[i]))
                xor = jcast('long', jcast('long', (xor ^ Code02_ArithmeticSequenceDifference.arr[i])))
                i = jcast('int', (i + 1))
            jcall(out, 'println', jadd(jadd(xor, ' '), max))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def set(l, r, s, e, d):
        l = jcast('int', l)
        r = jcast('int', r)
        s = jcast('int', s)
        e = jcast('int', e)
        d = jcast('int', d)
        Code02_ArithmeticSequenceDifference.arr[l] = jcast('long', jcast('long', jadd(Code02_ArithmeticSequenceDifference.arr[l], s)))
        Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(l, 1))] = jcast('long', jcast('long', jadd(Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(l, 1))], jcast('int', (d - s)))))
        Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(r, 1))] = jcast('long', jcast('long', (Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(r, 1))] - jcast('int', jadd(d, e)))))
        Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(r, 2))] = jcast('long', jcast('long', jadd(Code02_ArithmeticSequenceDifference.arr[jcast('int', jadd(r, 2))], e)))

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code02_ArithmeticSequenceDifference.n):
            Code02_ArithmeticSequenceDifference.arr[i] = jcast('long', jcast('long', jadd(Code02_ArithmeticSequenceDifference.arr[i], Code02_ArithmeticSequenceDifference.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_ArithmeticSequenceDifference.n):
            Code02_ArithmeticSequenceDifference.arr[i] = jcast('long', jcast('long', jadd(Code02_ArithmeticSequenceDifference.arr[i], Code02_ArithmeticSequenceDifference.arr[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ArithmeticSequenceDifference.MAXN = jcast('int', 10000005)
Code02_ArithmeticSequenceDifference.arr = jarray('long', [Code02_ArithmeticSequenceDifference.MAXN])
Code02_ArithmeticSequenceDifference.n = jcast('int', 0)
Code02_ArithmeticSequenceDifference.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_ArithmeticSequenceDifference.main([])

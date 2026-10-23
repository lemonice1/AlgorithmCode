# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大异或和
# 给定一个长度为n的数组arr，arr中都是long类型的非负数，可能有重复值
# 在这些数中选取任意个，使得异或和最大，返回最大的异或和
# 1 <= n <= 50
# 0 <= arr[i] <= 2^50
# 测试链接 : https://www.luogu.com.cn/problem/P3812
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MaximumXor:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'arr': 'arr', 'basis': 'basis', 'n': 'n'}
    MAXN = 0
    BIT = 0
    arr = None
    basis = None
    n = 0
    # 普通消元
    # 计算最大异或和
    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code01_MaximumXor.n):
            Code01_MaximumXor.insert(Code01_MaximumXor.arr[i])
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', Code01_MaximumXor.BIT)
        while (i >= 0):
            ans = jcast('long', jstatic('Math', 'max', ans, jcast('long', (ans ^ Code01_MaximumXor.basis[i]))))
            i = jcast('int', (i - 1))
        return jcast('long', ans)

    # 线性基里插入num，如果线性基增加了返回true，否则返回false
    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', Code01_MaximumXor.BIT)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (Code01_MaximumXor.basis[i] == 0):
                    Code01_MaximumXor.basis[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ Code01_MaximumXor.basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_MaximumXor.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_MaximumXor.n):
            jcall(in_, 'nextToken')
            Code01_MaximumXor.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_MaximumXor.compute()
        jcall(out, 'println', Code01_MaximumXor.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaximumXor.MAXN = jcast('int', 51)
Code01_MaximumXor.BIT = jcast('int', 50)
Code01_MaximumXor.arr = jarray('long', [Code01_MaximumXor.MAXN])
Code01_MaximumXor.basis = jarray('long', [jcast('int', jadd(Code01_MaximumXor.BIT, 1))])
Code01_MaximumXor.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_MaximumXor.main([])

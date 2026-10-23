# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 第k小的异或和
# 给定一个长度为n的数组arr，arr中都是long类型的非负数，可能有重复值
# 在这些数中选取任意个，至少要选一个数字
# 可以得到很多异或和，假设异或和的结果去重
# 返回第k小的异或和
# 1 <= n <= 10^5
# 0 <= arr[i] <= 2^50
# 1 <= k <= 2^50
# 测试链接 : https://loj.ac/p/114
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_KthXor:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'arr': 'arr', 'len': 'len', 'zero': 'zero', 'n': 'n'}
    MAXN = 0
    BIT = 0
    arr = None
    len = 0
    zero = False
    n = 0
    # 高斯消元
    @staticmethod
    def compute():
        Code02_KthXor.len = jcast('int', 1)
        i = jcast('long', Code02_KthXor.BIT)
        while (i >= 0):
            try:
                j = jcast('int', Code02_KthXor.len)
                while (j <= Code02_KthXor.n):
                    try:
                        if (jcast('long', (Code02_KthXor.arr[j] & jcast('long', (1 << (i & 63))))) != 0):
                            Code02_KthXor.swap(j, Code02_KthXor.len)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (jcast('long', (Code02_KthXor.arr[Code02_KthXor.len] & jcast('long', (1 << (i & 63))))) != 0):
                    j = jcast('int', 1)
                    while (j <= Code02_KthXor.n):
                        if ((j != Code02_KthXor.len) and (jcast('long', (Code02_KthXor.arr[j] & jcast('long', (1 << (i & 63))))) != 0)):
                            Code02_KthXor.arr[j] = jcast('long', jcast('long', (Code02_KthXor.arr[j] ^ Code02_KthXor.arr[Code02_KthXor.len])))
                        j = jcast('int', (j + 1))
                    Code02_KthXor.len = jcast('int', (Code02_KthXor.len + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('long', (i - 1))
        Code02_KthXor.len = jcast('int', (Code02_KthXor.len - 1))
        Code02_KthXor.zero = jcast('boolean', (Code02_KthXor.len != Code02_KthXor.n))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = jcast('long', Code02_KthXor.arr[a])
        Code02_KthXor.arr[a] = jcast('long', Code02_KthXor.arr[b])
        Code02_KthXor.arr[b] = jcast('long', tmp)

    # 返回第k小的异或和
    @staticmethod
    def query(k):
        k = jcast('long', k)
        if (Code02_KthXor.zero and (k == 1)):
            return jcast('long', 0)
        if Code02_KthXor.zero:
            k = jcast('long', (k - 1))
        if (k >= jcast('long', (1 << (Code02_KthXor.len & 63)))):
            return jcast('long', jcast('int', (-1)))
        ans = jcast('long', 0)
        i = jcast('int', Code02_KthXor.len)
        j = jcast('int', 0)
        while (i >= 1):
            if (jcast('long', (k & jcast('long', (1 << (j & 63))))) != 0):
                ans = jcast('long', jcast('long', (ans ^ Code02_KthXor.arr[i])))
            i = jcast('int', (i - 1))
            j = jcast('int', (j + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_KthXor.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_KthXor.n):
            jcall(in_, 'nextToken')
            Code02_KthXor.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_KthXor.compute()
        jcall(in_, 'nextToken')
        q = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= q):
            jcall(in_, 'nextToken')
            k = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(out, 'println', Code02_KthXor.query(k))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_KthXor.MAXN = jcast('int', 100001)
Code02_KthXor.BIT = jcast('int', 50)
Code02_KthXor.arr = jarray('long', [Code02_KthXor.MAXN])
Code02_KthXor.len = jcast('int', 0)
Code02_KthXor.zero = jcast('boolean', False)
Code02_KthXor.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_KthXor.main([])

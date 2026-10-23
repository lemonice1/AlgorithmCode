# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 相邻与结果不为0的最长子序列
# 给定一个长度为n的数组arr，你可以随意选择数字组成子序列
# 但是要求任意相邻的两个数&的结果不能是0，这样的子序列才是合法的
# 返回最长合法子序列的长度
# 1 <= n <= 10^5
# 0 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4310
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_LongestAddNotZero:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'pre': 'pre', 'n': 'n'}
    MAXN = 0
    arr = None
    pre = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_LongestAddNotZero.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code04_LongestAddNotZero.n):
            jcall(in_, 'nextToken')
            Code04_LongestAddNotZero.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_LongestAddNotZero.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code04_LongestAddNotZero.pre, 0)
        i = jcast('int', 0)
        num = 0
        cur = 0
        while (i < Code04_LongestAddNotZero.n):
            num = jcast('int', Code04_LongestAddNotZero.arr[i])
            cur = jcast('int', 1)
            j = jcast('int', 0)
            while (j < 31):
                if (jcast('int', (jcast('int', (num >> (j & 31))) & 1)) == 1):
                    cur = jcast('int', jstatic('Math', 'max', cur, jcast('int', jadd(Code04_LongestAddNotZero.pre[j], 1))))
                j = jcast('int', (j + 1))
            j = jcast('int', 0)
            while (j < 31):
                if (jcast('int', (jcast('int', (num >> (j & 31))) & 1)) == 1):
                    jset(Code04_LongestAddNotZero.pre, j, jstatic('Math', 'max', Code04_LongestAddNotZero.pre[j], cur))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        j = jcast('int', 0)
        while (j < 31):
            ans = jcast('int', jstatic('Math', 'max', ans, Code04_LongestAddNotZero.pre[j]))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_LongestAddNotZero.MAXN = jcast('int', 100001)
Code04_LongestAddNotZero.arr = jarray('int', [Code04_LongestAddNotZero.MAXN])
Code04_LongestAddNotZero.pre = jarray('int', [32])
Code04_LongestAddNotZero.n = jcast('int', 0)

if __name__ == '__main__':
    Code04_LongestAddNotZero.main([])

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

# 还原数组的方法数(优化枚举)
# 原本有一个长度为n的数组arr，下标从1开始，数组中都是<=200的正数
# 并且任意i位置的数字都满足 : arr[i] <= max(arr[i-1], arr[i+1])
# 特别的，arr[1] <= arr[2]，arr[n] <= arr[n-1]
# 但是输入的arr中有些数字丢失了，丢失的数字用0表示
# 返回还原成不违规的arr有多少种方法，答案对 998244353 取模
# 3 <= n <= 10^4
# 测试链接 : https://www.nowcoder.com/practice/49c5284278974cbda474ec13d8bd86a9
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_WaysOfRevert2:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'm': 'm', 'memo': 'memo', 'dp': 'dp', 'suf0': 'suf0', 'pre1': 'pre1'}
    MOD = 0
    MAXN = 0
    arr = None
    n = 0
    m = 0
    memo = None
    dp = None
    suf0 = None
    pre1 = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_WaysOfRevert2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code03_WaysOfRevert2.n):
                jcall(in_, 'nextToken')
                Code03_WaysOfRevert2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_WaysOfRevert2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 正式方法
    # 优化枚举 + 空间压缩
    # 时间复杂度O(n * m)
    @staticmethod
    def compute():
        v = jcast('int', 0)
        while (v <= Code03_WaysOfRevert2.m):
            jset(Code03_WaysOfRevert2.memo[v], 0, 0)
            jset(Code03_WaysOfRevert2.memo[v], 1, 1)
            v = jcast('int', (v + 1))
        i = jcast('int', 1)
        while (i <= Code03_WaysOfRevert2.n):
            Code03_WaysOfRevert2.prepare()
            v = jcast('int', 0)
            while (v <= Code03_WaysOfRevert2.m):
                s = jcast('int', 0)
                while (s <= 1):
                    ans = jcast('int', 0)
                    if (Code03_WaysOfRevert2.arr[i] != 0):
                        if ((Code03_WaysOfRevert2.arr[i] >= v) or (s == 1)):
                            ans = jcast('int', Code03_WaysOfRevert2.memo[Code03_WaysOfRevert2.arr[i]][(0 if (Code03_WaysOfRevert2.arr[i] > v) else 1)])
                    else:
                        if (jcast('int', jadd(v, 1)) <= Code03_WaysOfRevert2.m):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert2.suf0[jcast('int', jadd(v, 1))])), Code03_WaysOfRevert2.MOD)))
                        if (v != 0):
                            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert2.memo[v][1])), Code03_WaysOfRevert2.MOD)))
                        if (s == 1):
                            if (jcast('int', (v - 1)) >= 0):
                                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code03_WaysOfRevert2.pre1[jcast('int', (v - 1))])), Code03_WaysOfRevert2.MOD)))
                    jset(Code03_WaysOfRevert2.dp[v], s, ans)
                    s = jcast('int', (s + 1))
                v = jcast('int', (v + 1))
            tmp = Code03_WaysOfRevert2.memo
            Code03_WaysOfRevert2.memo = Code03_WaysOfRevert2.dp
            Code03_WaysOfRevert2.dp = tmp
            i = jcast('int', (i + 1))
        return jcast('int', Code03_WaysOfRevert2.memo[0][1])

    # 预处理结构优化枚举
    @staticmethod
    def prepare():
        Code03_WaysOfRevert2.suf0[Code03_WaysOfRevert2.m] = jcast('int', Code03_WaysOfRevert2.memo[Code03_WaysOfRevert2.m][0])
        v = jcast('int', jcast('int', (Code03_WaysOfRevert2.m - 1)))
        while (v >= 0):
            Code03_WaysOfRevert2.suf0[v] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code03_WaysOfRevert2.suf0[jcast('int', jadd(v, 1))], Code03_WaysOfRevert2.memo[v][0])), Code03_WaysOfRevert2.MOD)))
            v = jcast('int', (v - 1))
        Code03_WaysOfRevert2.pre1[1] = jcast('int', Code03_WaysOfRevert2.memo[1][1])
        v = jcast('int', 2)
        while (v <= Code03_WaysOfRevert2.m):
            Code03_WaysOfRevert2.pre1[v] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code03_WaysOfRevert2.pre1[jcast('int', (v - 1))], Code03_WaysOfRevert2.memo[v][1])), Code03_WaysOfRevert2.MOD)))
            v = jcast('int', (v + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_WaysOfRevert2.MOD = jcast('int', 998244353)
Code03_WaysOfRevert2.MAXN = jcast('int', 10000)
Code03_WaysOfRevert2.arr = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert2.MAXN, 1))])
Code03_WaysOfRevert2.n = jcast('int', 0)
Code03_WaysOfRevert2.m = jcast('int', 200)
Code03_WaysOfRevert2.memo = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert2.m, 1)), 2])
Code03_WaysOfRevert2.dp = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert2.m, 1)), 2])
Code03_WaysOfRevert2.suf0 = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert2.m, 1))])
Code03_WaysOfRevert2.pre1 = jarray('int', [jcast('int', jadd(Code03_WaysOfRevert2.m, 1))])

if __name__ == '__main__':
    Code03_WaysOfRevert2.main([])

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

# 砖块消除
# 给定一个长度为n的数组arr，arr[i]为i号砖块的重量
# 选择一个没有消除的砖块进行消除，收益为被消除砖块联通区域的重量之和，比如arr = {3,5,2,1}
# 如果先消除5，那么获得3+5+2+1的收益，arr = {3,X,2,1}
# 如果再消除1，那么获得2+1的收益，arr = {3,X,2,X}
# 如果再消除2，那么获得2的收益，arr = {3,X,X,X}
# 如果再消除3，那么获得3的收益，arr = {X,X,X,X}
# 一共有n!种消除方案，返回所有消除方案的收益总和，答案对 1000000007 取模
# 1 <= n <= 10^5    1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/AT_agc028_b
# 测试链接 : https://atcoder.jp/contests/agc028/tasks/agc028_b
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_RemovingBlocks:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'arr': 'arr', 'inv': 'inv', 'sum': 'sum', 'n': 'n'}
    MOD = 0
    MAXN = 0
    # 所有数字
    arr = None
    # 连续数字逆元表
    inv = None
    # sum[i] = (1/1 + 1/2 + 1/3 + ... + 1/i)，%MOD意义下的余数
    sum = None
    n = 0
    @staticmethod
    def build():
        Code06_RemovingBlocks.inv[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code06_RemovingBlocks.n):
            Code06_RemovingBlocks.inv[i] = jcast('int', jcast('int', jcast('long', (Code06_RemovingBlocks.MOD - jcast('long', jmod(jcast('long', (jcast('long', Code06_RemovingBlocks.inv[jcast('int', jmod(Code06_RemovingBlocks.MOD, i))]) * jcast('int', jdiv(Code06_RemovingBlocks.MOD, i)))), Code06_RemovingBlocks.MOD))))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_RemovingBlocks.n):
            Code06_RemovingBlocks.sum[i] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code06_RemovingBlocks.sum[jcast('int', (i - 1))], Code06_RemovingBlocks.inv[i])), Code06_RemovingBlocks.MOD)))
            i = jcast('int', (i + 1))

    @staticmethod
    def compute():
        Code06_RemovingBlocks.build()
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code06_RemovingBlocks.n):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', (jcast('long', jcast('int', (jcast('int', jadd(Code06_RemovingBlocks.sum[i], Code06_RemovingBlocks.sum[jcast('int', jadd(jcast('int', (Code06_RemovingBlocks.n - i)), 1))])) - 1))) * Code06_RemovingBlocks.arr[i])))), Code06_RemovingBlocks.MOD)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_RemovingBlocks.n):
            ans = jcast('long', jcast('long', jmod(jcast('long', (ans * i)), Code06_RemovingBlocks.MOD)))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_RemovingBlocks.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code06_RemovingBlocks.n):
            jcall(in_, 'nextToken')
            Code06_RemovingBlocks.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code06_RemovingBlocks.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_RemovingBlocks.MOD = jcast('int', 1000000007)
Code06_RemovingBlocks.MAXN = jcast('int', 100001)
Code06_RemovingBlocks.arr = jarray('int', [Code06_RemovingBlocks.MAXN])
Code06_RemovingBlocks.inv = jarray('int', [Code06_RemovingBlocks.MAXN])
Code06_RemovingBlocks.sum = jarray('int', [Code06_RemovingBlocks.MAXN])
Code06_RemovingBlocks.n = jcast('int', 0)

if __name__ == '__main__':
    Code06_RemovingBlocks.main([])

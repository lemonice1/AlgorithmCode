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

# 最大公约数为1的子序列数量
# 给你一个数组，返回有多少个子序列的最大公约数是1
# 结果可能很大对1000000007取模
# 测试链接 : https://www.luogu.com.cn/problem/CF803F
# 测试链接 : https://codeforces.com/problemset/problem/803/F
# 1 <= n <= 10^5
# 1 <= nums[i] <= 10^5
# 扩展问题
# 最大公约数为k的子序列数量
# 给定一个长度为n的正数数组nums，还有正数k
# 返回有多少子序列的最大公约数为k
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_NumberOfSubsetGcdK:
    __java_fields__ = {'MOD': 'MOD', 'LIMIT': 'LIMIT', 'dp': 'dp', 'cnt': 'cnt', 'pow2': 'pow2'}
    MOD = 0
    LIMIT = 0
    dp = None
    cnt = None
    pow2 = None
    @staticmethod
    def build():
        Code04_NumberOfSubsetGcdK.pow2[0] = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= Code04_NumberOfSubsetGcdK.LIMIT):
            Code04_NumberOfSubsetGcdK.pow2[i] = jcast('long', jcast('long', jmod(jcast('long', (Code04_NumberOfSubsetGcdK.pow2[jcast('int', (i - 1))] * 2)), Code04_NumberOfSubsetGcdK.MOD)))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        Code04_NumberOfSubsetGcdK.build()
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= n):
                jcall(in_, 'nextToken')
                ((_java_obj_1 := Code04_NumberOfSubsetGcdK.cnt), (_java_key_2 := jcast('int', jget(in_, 'nval'))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('long', (_java_old_3 + (1)))), _java_old_3)[4]
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_NumberOfSubsetGcdK.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(v * log v)
    @staticmethod
    def compute():
        i = jcast('int', Code04_NumberOfSubsetGcdK.LIMIT)
        while (i >= 1):
            counts = jcast('long', 0)
            j = jcast('int', i)
            while (j <= Code04_NumberOfSubsetGcdK.LIMIT):
                counts = jcast('long', jcast('long', jadd(counts, Code04_NumberOfSubsetGcdK.cnt[j])))
                j = jcast('int', jcast('int', jadd(j, i)))
            Code04_NumberOfSubsetGcdK.dp[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code04_NumberOfSubsetGcdK.pow2[jcast('int', counts)] - 1)), Code04_NumberOfSubsetGcdK.MOD)), Code04_NumberOfSubsetGcdK.MOD)))
            j = jcast('int', jcast('int', (2 * i)))
            while (j <= Code04_NumberOfSubsetGcdK.LIMIT):
                Code04_NumberOfSubsetGcdK.dp[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', (Code04_NumberOfSubsetGcdK.dp[i] - Code04_NumberOfSubsetGcdK.dp[j])), Code04_NumberOfSubsetGcdK.MOD)), Code04_NumberOfSubsetGcdK.MOD)))
                j = jcast('int', jcast('int', jadd(j, i)))
            i = jcast('int', (i - 1))
        return jcast('long', Code04_NumberOfSubsetGcdK.dp[1])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_NumberOfSubsetGcdK.MOD = jcast('int', 1000000007)
Code04_NumberOfSubsetGcdK.LIMIT = jcast('int', 100000)
Code04_NumberOfSubsetGcdK.dp = jarray('long', [jcast('int', jadd(Code04_NumberOfSubsetGcdK.LIMIT, 1))])
Code04_NumberOfSubsetGcdK.cnt = jarray('long', [jcast('int', jadd(Code04_NumberOfSubsetGcdK.LIMIT, 1))])
Code04_NumberOfSubsetGcdK.pow2 = jarray('long', [jcast('int', jadd(Code04_NumberOfSubsetGcdK.LIMIT, 1))])

if __name__ == '__main__':
    Code04_NumberOfSubsetGcdK.main([])

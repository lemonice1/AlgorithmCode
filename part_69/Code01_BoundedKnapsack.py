# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 多重背包不进行枚举优化
# 宝物筛选
# 一共有n种货物, 背包容量为t
# 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
# 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1776
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_BoundedKnapsack:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'v': 'v', 'w': 'w', 'c': 'c', 'dp': 'dp', 'n': 'n', 't': 't'}
    MAXN = 0
    MAXW = 0
    v = None
    w = None
    c = None
    dp = None
    n = 0
    t = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_BoundedKnapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_BoundedKnapsack.t = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code01_BoundedKnapsack.n):
                jcall(in_, 'nextToken')
                Code01_BoundedKnapsack.v[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code01_BoundedKnapsack.w[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code01_BoundedKnapsack.c[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_BoundedKnapsack.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划
    # 时间复杂度O(n * t * 每种商品的平均个数)
    @staticmethod
    def compute1():
        # dp[0][....] = 0，表示没有货物的情况下，背包容量不管是多少，最大价值都是0
        dp = jarray('int', [jcast('int', jadd(Code01_BoundedKnapsack.n, 1)), jcast('int', jadd(Code01_BoundedKnapsack.t, 1))])
        i = jcast('int', 1)
        while (i <= Code01_BoundedKnapsack.n):
            j = jcast('int', 0)
            while (j <= Code01_BoundedKnapsack.t):
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                k = jcast('int', 1)
                while ((k <= Code01_BoundedKnapsack.c[i]) and (jcast('int', (Code01_BoundedKnapsack.w[i] * k)) <= j)):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - jcast('int', (k * Code01_BoundedKnapsack.w[i]))))], jcast('int', (k * Code01_BoundedKnapsack.v[i]))))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[Code01_BoundedKnapsack.n][Code01_BoundedKnapsack.t])

    # 空间压缩
    # 部分测试用例超时
    # 因为没有优化枚举
    # 时间复杂度O(n * t * 每种商品的平均个数)
    @staticmethod
    def compute2():
        i = jcast('int', 1)
        while (i <= Code01_BoundedKnapsack.n):
            j = jcast('int', Code01_BoundedKnapsack.t)
            while (j >= 0):
                k = jcast('int', 1)
                while ((k <= Code01_BoundedKnapsack.c[i]) and (jcast('int', (Code01_BoundedKnapsack.w[i] * k)) <= j)):
                    jset(Code01_BoundedKnapsack.dp, j, jstatic('Math', 'max', Code01_BoundedKnapsack.dp[j], jcast('int', jadd(Code01_BoundedKnapsack.dp[jcast('int', (j - jcast('int', (k * Code01_BoundedKnapsack.w[i]))))], jcast('int', (k * Code01_BoundedKnapsack.v[i]))))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_BoundedKnapsack.dp[Code01_BoundedKnapsack.t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_BoundedKnapsack.MAXN = jcast('int', 101)
Code01_BoundedKnapsack.MAXW = jcast('int', 40001)
Code01_BoundedKnapsack.v = jarray('int', [Code01_BoundedKnapsack.MAXN])
Code01_BoundedKnapsack.w = jarray('int', [Code01_BoundedKnapsack.MAXN])
Code01_BoundedKnapsack.c = jarray('int', [Code01_BoundedKnapsack.MAXN])
Code01_BoundedKnapsack.dp = jarray('int', [Code01_BoundedKnapsack.MAXW])
Code01_BoundedKnapsack.n = jcast('int', 0)
Code01_BoundedKnapsack.t = jcast('int', 0)

if __name__ == '__main__':
    Code01_BoundedKnapsack.main([])

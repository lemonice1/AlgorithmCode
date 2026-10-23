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

# 分组背包(模版)
# 给定一个正数m表示背包的容量，有n个货物可供挑选
# 每个货物有自己的体积(容量消耗)、价值(获得收益)、组号(分组)
# 同一个组的物品只能挑选1件，所有挑选物品的体积总和不能超过背包容量
# 怎么挑选货物能达到价值最大，返回最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1757
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_PartitionedKnapsack:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'arr': 'arr', 'dp': 'dp', 'm': 'm', 'n': 'n'}
    MAXN = 0
    MAXM = 0
    # arr[i][0] i号物品的体积
    # arr[i][1] i号物品的价值
    # arr[i][2] i号物品的组号
    arr = None
    dp = None
    m = 0
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_PartitionedKnapsack.m = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_PartitionedKnapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code01_PartitionedKnapsack.n):
                jcall(in_, 'nextToken')
                jset(Code01_PartitionedKnapsack.arr[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code01_PartitionedKnapsack.arr[i], 1, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code01_PartitionedKnapsack.arr[i], 2, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jstatic('Arrays', 'sort', Code01_PartitionedKnapsack.arr, 1, jcast('int', jadd(Code01_PartitionedKnapsack.n, 1)), (lambda a, b: (a[2] - b[2])))
            jcall(out, 'println', Code01_PartitionedKnapsack.compute1())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划
    @staticmethod
    def compute1():
        teams = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_PartitionedKnapsack.n):
            if (Code01_PartitionedKnapsack.arr[jcast('int', (i - 1))][2] != Code01_PartitionedKnapsack.arr[i][2]):
                teams = jcast('int', (teams + 1))
            i = jcast('int', (i + 1))
        # 组的编号1~teams
        # dp[i][j] : 1~i是组的范围，每个组的物品挑一件，容量不超过j的情况下，最大收益
        dp = jarray('int', [jcast('int', jadd(teams, 1)), jcast('int', jadd(Code01_PartitionedKnapsack.m, 1))])
        # dp[0][....] = 0
        start = jcast('int', 1)
        end = jcast('int', 2)
        i = jcast('int', 1)
        while (start <= Code01_PartitionedKnapsack.n):
            while ((end <= Code01_PartitionedKnapsack.n) and (Code01_PartitionedKnapsack.arr[end][2] == Code01_PartitionedKnapsack.arr[start][2])):
                end = jcast('int', (end + 1))
            # start ... end-1 -> i组
            j = jcast('int', 0)
            while (j <= Code01_PartitionedKnapsack.m):
                # arr[start...end-1]是当前组，组号一样
                # 其中的每一件商品枚举一遍
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                k = jcast('int', start)
                while (k < end):
                    # k是组内的一个商品编号
                    if (jcast('int', (j - Code01_PartitionedKnapsack.arr[k][0])) >= 0):
                        jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - Code01_PartitionedKnapsack.arr[k][0]))], Code01_PartitionedKnapsack.arr[k][1]))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j + 1))
            # start去往下一组的第一个物品
            # 继续处理剩下的组
            start = jcast('int', ((_java_old_1 := end), (end := jcast('int', (end + (1)))), _java_old_1)[2])
            i = jcast('int', (i + 1))
        return jcast('int', dp[teams][Code01_PartitionedKnapsack.m])

    # 空间压缩
    @staticmethod
    def compute2():
        # dp[0][...] = 0
        jstatic('Arrays', 'fill', Code01_PartitionedKnapsack.dp, 0, jcast('int', jadd(Code01_PartitionedKnapsack.m, 1)), 0)
        start = jcast('int', 1)
        end = jcast('int', 2)
        while (start <= Code01_PartitionedKnapsack.n):
            while ((end <= Code01_PartitionedKnapsack.n) and (Code01_PartitionedKnapsack.arr[end][2] == Code01_PartitionedKnapsack.arr[start][2])):
                end = jcast('int', (end + 1))
            # start....end-1
            j = jcast('int', Code01_PartitionedKnapsack.m)
            while (j >= 0):
                k = jcast('int', start)
                while (k < end):
                    if (jcast('int', (j - Code01_PartitionedKnapsack.arr[k][0])) >= 0):
                        jset(Code01_PartitionedKnapsack.dp, j, jstatic('Math', 'max', Code01_PartitionedKnapsack.dp[j], jcast('int', jadd(Code01_PartitionedKnapsack.arr[k][1], Code01_PartitionedKnapsack.dp[jcast('int', (j - Code01_PartitionedKnapsack.arr[k][0]))]))))
                    k = jcast('int', (k + 1))
                j = jcast('int', (j - 1))
            start = jcast('int', ((_java_old_2 := end), (end := jcast('int', (end + (1)))), _java_old_2)[2])
        return jcast('int', Code01_PartitionedKnapsack.dp[Code01_PartitionedKnapsack.m])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_PartitionedKnapsack.MAXN = jcast('int', 1001)
Code01_PartitionedKnapsack.MAXM = jcast('int', 1001)
Code01_PartitionedKnapsack.arr = jarray('int', [Code01_PartitionedKnapsack.MAXN, 3])
Code01_PartitionedKnapsack.dp = jarray('int', [Code01_PartitionedKnapsack.MAXM])
Code01_PartitionedKnapsack.m = jcast('int', 0)
Code01_PartitionedKnapsack.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_PartitionedKnapsack.main([])

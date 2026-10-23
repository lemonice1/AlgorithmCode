# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 01背包(模版)
# 给定一个正数t，表示背包的容量
# 有m个货物，每个货物可以选择一次
# 每个货物有自己的体积costs[i]和价值values[i]
# 返回在不超过总容量的情况下，怎么挑选货物能达到价值最大
# 返回最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1048
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_01Knapsack:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXT': 'MAXT', 'cost': 'cost', 'val': 'val', 'dp': 'dp', 't': 't', 'n': 'n'}
    MAXM = 0
    MAXT = 0
    cost = None
    val = None
    dp = None
    t = 0
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_01Knapsack.t = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_01Knapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code01_01Knapsack.n):
                jcall(in_, 'nextToken')
                Code01_01Knapsack.cost[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code01_01Knapsack.val[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_01Knapsack.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划
    # n个物品编号1~n，第i号物品的花费cost[i]、价值val[i]
    # cost、val数组是全局变量，已经把数据读入了
    @staticmethod
    def compute1():
        dp = jarray('int', [jcast('int', jadd(Code01_01Knapsack.n, 1)), jcast('int', jadd(Code01_01Knapsack.t, 1))])
        i = jcast('int', 1)
        while (i <= Code01_01Knapsack.n):
            j = jcast('int', 0)
            while (j <= Code01_01Knapsack.t):
                # 不要i号物品
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if (jcast('int', (j - Code01_01Knapsack.cost[i])) >= 0):
                    # 要i号物品
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[jcast('int', (i - 1))][jcast('int', (j - Code01_01Knapsack.cost[i]))], Code01_01Knapsack.val[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[Code01_01Knapsack.n][Code01_01Knapsack.t])

    # 空间压缩
    @staticmethod
    def compute2():
        jstatic('Arrays', 'fill', Code01_01Knapsack.dp, 0, jcast('int', jadd(Code01_01Knapsack.t, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code01_01Knapsack.n):
            j = jcast('int', Code01_01Knapsack.t)
            while (j >= Code01_01Knapsack.cost[i]):
                jset(Code01_01Knapsack.dp, j, jstatic('Math', 'max', Code01_01Knapsack.dp[j], jcast('int', jadd(Code01_01Knapsack.dp[jcast('int', (j - Code01_01Knapsack.cost[i]))], Code01_01Knapsack.val[i]))))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_01Knapsack.dp[Code01_01Knapsack.t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_01Knapsack.MAXM = jcast('int', 101)
Code01_01Knapsack.MAXT = jcast('int', 1001)
Code01_01Knapsack.cost = jarray('int', [Code01_01Knapsack.MAXM])
Code01_01Knapsack.val = jarray('int', [Code01_01Knapsack.MAXM])
Code01_01Knapsack.dp = jarray('int', [Code01_01Knapsack.MAXT])
Code01_01Knapsack.t = jcast('int', 0)
Code01_01Knapsack.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_01Knapsack.main([])

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

# 完全背包(模版)
# 给定一个正数t，表示背包的容量
# 有m种货物，每种货物可以选择任意个
# 每种货物都有体积costs[i]和价值values[i]
# 返回在不超过总容量的情况下，怎么挑选货物能达到价值最大
# 返回最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1616
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_UnboundedKnapsack:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXT': 'MAXT', 'cost': 'cost', 'val': 'val', 'dp': 'dp', 't': 't', 'm': 'm'}
    MAXM = 0
    MAXT = 0
    cost = None
    val = None
    dp = None
    t = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_UnboundedKnapsack.t = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_UnboundedKnapsack.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code03_UnboundedKnapsack.m):
                jcall(in_, 'nextToken')
                Code03_UnboundedKnapsack.cost[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code03_UnboundedKnapsack.val[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_UnboundedKnapsack.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划
    # 状态集合较大，需关注空间复杂度与容器开销
    @staticmethod
    def compute1():
        # dp[0][.....] = 0
        dp = jarray('int', [jcast('int', jadd(Code03_UnboundedKnapsack.m, 1)), jcast('int', jadd(Code03_UnboundedKnapsack.t, 1))])
        i = jcast('int', 1)
        while (i <= Code03_UnboundedKnapsack.m):
            j = jcast('int', 0)
            while (j <= Code03_UnboundedKnapsack.t):
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if (jcast('int', (j - Code03_UnboundedKnapsack.cost[i])) >= 0):
                    jset(dp[i], j, jstatic('Math', 'max', dp[i][j], jcast('int', jadd(dp[i][jcast('int', (j - Code03_UnboundedKnapsack.cost[i]))], Code03_UnboundedKnapsack.val[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', dp[Code03_UnboundedKnapsack.m][Code03_UnboundedKnapsack.t])

    # 空间压缩
    # 用例
    @staticmethod
    def compute2():
        jstatic('Arrays', 'fill', Code03_UnboundedKnapsack.dp, 1, jcast('int', jadd(Code03_UnboundedKnapsack.t, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code03_UnboundedKnapsack.m):
            j = jcast('int', Code03_UnboundedKnapsack.cost[i])
            while (j <= Code03_UnboundedKnapsack.t):
                jset(Code03_UnboundedKnapsack.dp, j, jstatic('Math', 'max', Code03_UnboundedKnapsack.dp[j], jcast('long', jadd(Code03_UnboundedKnapsack.dp[jcast('int', (j - Code03_UnboundedKnapsack.cost[i]))], Code03_UnboundedKnapsack.val[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('long', Code03_UnboundedKnapsack.dp[Code03_UnboundedKnapsack.t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_UnboundedKnapsack.MAXM = jcast('int', 10001)
Code03_UnboundedKnapsack.MAXT = jcast('int', 10000001)
Code03_UnboundedKnapsack.cost = jarray('int', [Code03_UnboundedKnapsack.MAXM])
Code03_UnboundedKnapsack.val = jarray('int', [Code03_UnboundedKnapsack.MAXM])
Code03_UnboundedKnapsack.dp = jarray('long', [Code03_UnboundedKnapsack.MAXT])
Code03_UnboundedKnapsack.t = jcast('int', 0)
Code03_UnboundedKnapsack.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_UnboundedKnapsack.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 购买足量干草的最小花费
# 有n个提供干草的公司，每个公司都有两个信息
# cost[i]代表购买1次产品需要花的钱
# val[i]代表购买1次产品所获得的干草数量
# 每个公司的产品都可以购买任意次
# 你一定要至少购买h数量的干草，返回最少要花多少钱
# 测试链接 : https://www.luogu.com.cn/problem/P2918
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_BuyingHayMinimumCost:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'val': 'val', 'cost': 'cost', 'dp': 'dp', 'n': 'n', 'h': 'h', 'maxv': 'maxv', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    val = None
    cost = None
    dp = None
    n = 0
    h = 0
    maxv = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code06_BuyingHayMinimumCost.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code06_BuyingHayMinimumCost.h = jcast('int', jcast('int', jget(in_, 'nval')))
            Code06_BuyingHayMinimumCost.maxv = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code06_BuyingHayMinimumCost.n):
                jcall(in_, 'nextToken')
                Code06_BuyingHayMinimumCost.val[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                Code06_BuyingHayMinimumCost.maxv = jcast('int', jstatic('Math', 'max', Code06_BuyingHayMinimumCost.maxv, Code06_BuyingHayMinimumCost.val[i]))
                jcall(in_, 'nextToken')
                Code06_BuyingHayMinimumCost.cost[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            # 最核心的一句
            # 包含重要分析
            Code06_BuyingHayMinimumCost.m = jcast('int', jcast('int', jadd(Code06_BuyingHayMinimumCost.h, Code06_BuyingHayMinimumCost.maxv)))
            jcall(out, 'println', Code06_BuyingHayMinimumCost.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # dp[i][j] : 1...i里挑公司，购买严格j磅干草，需要的最少花费
    # 1) dp[i-1][j]
    # 2) dp[i][j-val[i]] + cost[i]
    # 两种可能性中选最小
    # 但是关于j需要进行一定的扩充，原因视频里讲了
    @staticmethod
    def compute1():
        dp = jarray('int', [jcast('int', jadd(Code06_BuyingHayMinimumCost.n, 1)), jcast('int', jadd(Code06_BuyingHayMinimumCost.m, 1))])
        jstatic('Arrays', 'fill', dp[0], 1, jcast('int', jadd(Code06_BuyingHayMinimumCost.m, 1)), jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 1)
        while (i <= Code06_BuyingHayMinimumCost.n):
            j = jcast('int', 0)
            while (j <= Code06_BuyingHayMinimumCost.m):
                jset(dp[i], j, dp[jcast('int', (i - 1))][j])
                if ((jcast('int', (j - Code06_BuyingHayMinimumCost.val[i])) >= 0) and (dp[i][jcast('int', (j - Code06_BuyingHayMinimumCost.val[i]))] != jget(Integer, 'MAX_VALUE'))):
                    jset(dp[i], j, jstatic('Math', 'min', dp[i][j], jcast('int', jadd(dp[i][jcast('int', (j - Code06_BuyingHayMinimumCost.val[i]))], Code06_BuyingHayMinimumCost.cost[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        # >= h
        # h h+1 h+2 ... m
        j = jcast('int', Code06_BuyingHayMinimumCost.h)
        while (j <= Code06_BuyingHayMinimumCost.m):
            ans = jcast('int', jstatic('Math', 'min', ans, dp[Code06_BuyingHayMinimumCost.n][j]))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # 空间压缩
    @staticmethod
    def compute2():
        jstatic('Arrays', 'fill', Code06_BuyingHayMinimumCost.dp, 1, jcast('int', jadd(Code06_BuyingHayMinimumCost.m, 1)), jget(Integer, 'MAX_VALUE'))
        i = jcast('int', 1)
        while (i <= Code06_BuyingHayMinimumCost.n):
            j = jcast('int', Code06_BuyingHayMinimumCost.val[i])
            while (j <= Code06_BuyingHayMinimumCost.m):
                if (Code06_BuyingHayMinimumCost.dp[jcast('int', (j - Code06_BuyingHayMinimumCost.val[i]))] != jget(Integer, 'MAX_VALUE')):
                    jset(Code06_BuyingHayMinimumCost.dp, j, jstatic('Math', 'min', Code06_BuyingHayMinimumCost.dp[j], jcast('int', jadd(Code06_BuyingHayMinimumCost.dp[jcast('int', (j - Code06_BuyingHayMinimumCost.val[i]))], Code06_BuyingHayMinimumCost.cost[i]))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', Code06_BuyingHayMinimumCost.h)
        while (j <= Code06_BuyingHayMinimumCost.m):
            ans = jcast('int', jstatic('Math', 'min', ans, Code06_BuyingHayMinimumCost.dp[j]))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_BuyingHayMinimumCost.MAXN = jcast('int', 101)
Code06_BuyingHayMinimumCost.MAXM = jcast('int', 55001)
Code06_BuyingHayMinimumCost.val = jarray('int', [Code06_BuyingHayMinimumCost.MAXN])
Code06_BuyingHayMinimumCost.cost = jarray('int', [Code06_BuyingHayMinimumCost.MAXN])
Code06_BuyingHayMinimumCost.dp = jarray('int', [Code06_BuyingHayMinimumCost.MAXM])
Code06_BuyingHayMinimumCost.n = jcast('int', 0)
Code06_BuyingHayMinimumCost.h = jcast('int', 0)
Code06_BuyingHayMinimumCost.maxv = jcast('int', 0)
Code06_BuyingHayMinimumCost.m = jcast('int', 0)

if __name__ == '__main__':
    Code06_BuyingHayMinimumCost.main([])

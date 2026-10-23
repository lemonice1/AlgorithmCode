# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 混合背包 + 多重背包普通窗口优化
# 能成功找零的钱数种类
# 每一种货币都给定面值val[i]，和拥有的数量cnt[i]
# 想知道目前拥有的货币，在钱数为1、2、3...m时
# 能找零成功的钱数有多少
# 也就是说当钱数的范围是1~m
# 返回这个范围上有多少可以找零成功的钱数
# 比如只有3元的货币，数量是5张
# m = 10
# 那么在1~10范围上，只有钱数是3、6、9时，可以成功找零
# 所以返回3表示有3种钱数可以找零成功
# 测试链接 : http://poj.org/problem?id=1742
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_MixedKnapsack:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'val': 'val', 'cnt': 'cnt', 'dp': 'dp', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    val = None
    cnt = None
    dp = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code05_MixedKnapsack.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_MixedKnapsack.m = jcast('int', jcast('int', jget(in_, 'nval')))
            if ((Code05_MixedKnapsack.n != 0) or (Code05_MixedKnapsack.m != 0)):
                i = jcast('int', 1)
                while (i <= Code05_MixedKnapsack.n):
                    jcall(in_, 'nextToken')
                    Code05_MixedKnapsack.val[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                    i = jcast('int', (i + 1))
                i = jcast('int', 1)
                while (i <= Code05_MixedKnapsack.n):
                    jcall(in_, 'nextToken')
                    Code05_MixedKnapsack.cnt[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                    i = jcast('int', (i + 1))
                jcall(out, 'println', Code05_MixedKnapsack.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 直接提供空间压缩版
    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code05_MixedKnapsack.dp, 1, jcast('int', jadd(Code05_MixedKnapsack.m, 1)), False)
        Code05_MixedKnapsack.dp[0] = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code05_MixedKnapsack.n):
            if (Code05_MixedKnapsack.cnt[i] == 1):
                # 01背包的空间压缩实现是从右往左更新的
                j = jcast('int', Code05_MixedKnapsack.m)
                while (j >= Code05_MixedKnapsack.val[i]):
                    if Code05_MixedKnapsack.dp[jcast('int', (j - Code05_MixedKnapsack.val[i]))]:
                        Code05_MixedKnapsack.dp[j] = jcast('boolean', True)
                    j = jcast('int', (j - 1))
            else:
                if (jcast('int', (Code05_MixedKnapsack.val[i] * Code05_MixedKnapsack.cnt[i])) > Code05_MixedKnapsack.m):
                    # 完全背包的空间压缩实现是从左往右更新的
                    j = jcast('int', Code05_MixedKnapsack.val[i])
                    while (j <= Code05_MixedKnapsack.m):
                        if Code05_MixedKnapsack.dp[jcast('int', (j - Code05_MixedKnapsack.val[i]))]:
                            Code05_MixedKnapsack.dp[j] = jcast('boolean', True)
                        j = jcast('int', (j + 1))
                else:
                    # 多重背包的空间压缩实现
                    # 每一组都是从右往左更新的
                    # 同余分组
                    mod = jcast('int', 0)
                    while (mod < Code05_MixedKnapsack.val[i]):
                        trueCnt = jcast('int', 0)
                        j = jcast('int', jcast('int', (Code05_MixedKnapsack.m - mod)))
                        size = jcast('int', 0)
                        while ((j >= 0) and (size <= Code05_MixedKnapsack.cnt[i])):
                            trueCnt = jcast('int', jcast('int', jadd(trueCnt, (1 if Code05_MixedKnapsack.dp[j] else 0))))
                            j = jcast('int', jcast('int', (j - Code05_MixedKnapsack.val[i])))
                            size = jcast('int', (size + 1))
                        j = jcast('int', jcast('int', (Code05_MixedKnapsack.m - mod)))
                        l = jcast('int', jcast('int', (j - jcast('int', (Code05_MixedKnapsack.val[i] * jcast('int', jadd(Code05_MixedKnapsack.cnt[i], 1)))))))
                        while (j >= 1):
                            if Code05_MixedKnapsack.dp[j]:
                                trueCnt = jcast('int', (trueCnt - 1))
                            else:
                                if (trueCnt != 0):
                                    Code05_MixedKnapsack.dp[j] = jcast('boolean', True)
                            if (l >= 0):
                                trueCnt = jcast('int', jcast('int', jadd(trueCnt, (1 if Code05_MixedKnapsack.dp[l] else 0))))
                            j = jcast('int', jcast('int', (j - Code05_MixedKnapsack.val[i])))
                            l = jcast('int', jcast('int', (l - Code05_MixedKnapsack.val[i])))
                        mod = jcast('int', (mod + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code05_MixedKnapsack.m):
            if Code05_MixedKnapsack.dp[i]:
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_MixedKnapsack.MAXN = jcast('int', 101)
Code05_MixedKnapsack.MAXM = jcast('int', 100001)
Code05_MixedKnapsack.val = jarray('int', [Code05_MixedKnapsack.MAXN])
Code05_MixedKnapsack.cnt = jarray('int', [Code05_MixedKnapsack.MAXN])
Code05_MixedKnapsack.dp = jarray('boolean', [Code05_MixedKnapsack.MAXM])
Code05_MixedKnapsack.n = jcast('int', 0)
Code05_MixedKnapsack.m = jcast('int', 0)

if __name__ == '__main__':
    Code05_MixedKnapsack.main([])

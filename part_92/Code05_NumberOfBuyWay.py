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

# 多次查询购买方法
# 一共有4种硬币，面值分别为v0、v1、v2、v3，这个永远是确定的
# 每次去购物的细节由一个数组arr来表示，每次购物都是一次查询
# arr[0] = 携带v0面值的硬币数量
# arr[1] = 携带v1面值的硬币数量
# arr[2] = 携带v2面值的硬币数量
# arr[3] = 携带v3面值的硬币数量
# arr[4] = 本次购物一定要花多少钱
# 返回每次有多少种花钱的方法
# 1 <= v0、v1、v2、v3、arr[i] <= 10^5
# 查询数量 <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P1450
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_NumberOfBuyWay:
    __java_fields__ = {'LIMIT': 'LIMIT', 'dp': 'dp', 'value': 'value', 'cnt': 'cnt', 'n': 'n', 's': 's'}
    LIMIT = 0
    # dp表就是查询系统
    # dp[i]表示当所有硬币无限制的情况下，花掉i元，方法数是多少
    dp = None
    value = None
    cnt = None
    n = 0
    s = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            # 总体时间复杂度O(LIMIT + 查询次数)
            Code05_NumberOfBuyWay.value[0] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_NumberOfBuyWay.value[1] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_NumberOfBuyWay.value[2] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_NumberOfBuyWay.value[3] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_NumberOfBuyWay.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_NumberOfBuyWay.build()
            i = jcast('int', 1)
            while (i <= Code05_NumberOfBuyWay.n):
                jcall(in_, 'nextToken')
                Code05_NumberOfBuyWay.cnt[0] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_NumberOfBuyWay.cnt[1] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_NumberOfBuyWay.cnt[2] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_NumberOfBuyWay.cnt[3] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code05_NumberOfBuyWay.s = jcast('int', jcast('int', jget(in_, 'nval')))
                # query时间复杂度O(1)
                jcall(out, 'println', Code05_NumberOfBuyWay.query())
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(LIMIT)
    # 最基本的完全背包问题 + 空间压缩
    # 完全背包在讲解074，不会的同学看一下
    @staticmethod
    def build():
        Code05_NumberOfBuyWay.dp[0] = jcast('long', 1)
        i = jcast('int', 0)
        while (i <= 3):
            j = jcast('int', Code05_NumberOfBuyWay.value[i])
            while (j <= Code05_NumberOfBuyWay.LIMIT):
                Code05_NumberOfBuyWay.dp[j] = jcast('long', jcast('long', jadd(Code05_NumberOfBuyWay.dp[j], Code05_NumberOfBuyWay.dp[jcast('int', (j - Code05_NumberOfBuyWay.value[i]))])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    # 时间复杂度O(15 * 4) -> O(1)
    @staticmethod
    def query():
        illegal = jcast('long', 0)
        # status -> 0001到1111
        status = jcast('int', 1)
        while (status <= 15):
            t = jcast('long', Code05_NumberOfBuyWay.s)
            # 遇到奇数个1，sigh变成1
            # 遇到偶数个1，sigh变成-1
            sign = jcast('int', jcast('int', (-1)))
            j = jcast('int', 0)
            while (j <= 3):
                if (jcast('int', (jcast('int', (status >> (j & 31))) & 1)) == 1):
                    t = jcast('long', jcast('long', (t - jcast('int', (Code05_NumberOfBuyWay.value[j] * jcast('int', jadd(Code05_NumberOfBuyWay.cnt[j], 1)))))))
                    sign = jcast('int', jcast('int', (-sign)))
                j = jcast('int', (j + 1))
            if (t >= 0):
                illegal = jcast('long', jcast('long', jadd(illegal, jcast('long', (Code05_NumberOfBuyWay.dp[jcast('int', t)] * sign)))))
            status = jcast('int', (status + 1))
        return jcast('long', jcast('long', (Code05_NumberOfBuyWay.dp[Code05_NumberOfBuyWay.s] - illegal)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_NumberOfBuyWay.LIMIT = jcast('int', 100000)
Code05_NumberOfBuyWay.dp = jarray('long', [jcast('int', jadd(Code05_NumberOfBuyWay.LIMIT, 1))])
Code05_NumberOfBuyWay.value = jarray('int', [4])
Code05_NumberOfBuyWay.cnt = jarray('int', [4])
Code05_NumberOfBuyWay.n = jcast('int', 0)
Code05_NumberOfBuyWay.s = jcast('int', 0)

if __name__ == '__main__':
    Code05_NumberOfBuyWay.main([])

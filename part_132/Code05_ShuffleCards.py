# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 洗牌
# 一共有n张牌，n一定是偶数，每张牌的牌面从1到n，洗牌规则如下
# 比如n = 6，牌面最初排列为1 2 3 4 5 6
# 先分成左堆1 2 3，右堆4 5 6，然后按照右堆第i张在前，左堆第i张在后的方式依次放置
# 所以洗一次后，得到 4 1 5 2 6 3
# 如果再洗一次，得到 2 4 6 1 3 5
# 如果再洗一次，得到 1 2 3 4 5 6
# 想知道n张牌洗m次的之后，第l张牌，是什么牌面
# 1 <= n <= 10^10，n为偶数
# 0 <= m <= 10^10
# 测试链接 : https://www.luogu.com.cn/problem/P2054
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_ShuffleCards:
    __java_fields__ = {'d': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
    # 扩展欧几里得算法
    d = 0
    x = 0
    y = 0
    px = 0
    py = 0
    @staticmethod
    def exgcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        if (b == 0):
            Code05_ShuffleCards.d = jcast('long', a)
            Code05_ShuffleCards.x = jcast('long', 1)
            Code05_ShuffleCards.y = jcast('long', 0)
        else:
            Code05_ShuffleCards.exgcd(b, jcast('long', jmod(a, b)))
            Code05_ShuffleCards.px = jcast('long', Code05_ShuffleCards.x)
            Code05_ShuffleCards.py = jcast('long', Code05_ShuffleCards.y)
            Code05_ShuffleCards.x = jcast('long', Code05_ShuffleCards.py)
            Code05_ShuffleCards.y = jcast('long', jcast('long', (Code05_ShuffleCards.px - jcast('long', (Code05_ShuffleCards.py * jcast('long', jdiv(a, b)))))))

    # 原理来自，讲解033，位运算实现乘法
    # a * b的过程自己实现，每一个中间过程都%mod
    # 这么写目的是防止溢出，也叫龟速乘
    @staticmethod
    def multiply(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('long', mod)
        # 既然是在%mod的意义下，那么a和b可以都转化成非负的
        # 本题不转化无所谓，但是其他题目可能需要转化
        # 尤其是b需要转化，否则while循环会跑不完
        a = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(a, mod)), mod)), mod)))
        b = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(b, mod)), mod)), mod)))
        ans = jcast('long', 0)
        while (b != 0):
            if (jcast('long', (b & 1)) != 0):
                ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, a)), mod)))
            a = jcast('long', jcast('long', jmod(jcast('long', jadd(a, a)), mod)))
            b = jcast('long', jcast('long', (b >> (1 & 63))))
        return jcast('long', ans)

    # 原理来自，讲解098，乘法快速幂
    # 计算a的b次方，最终 % mod 的结果
    @staticmethod
    def power(a, b, mod):
        a = jcast('long', a)
        b = jcast('long', b)
        mod = jcast('long', mod)
        ans = jcast('long', 1)
        while (b > 0):
            if (jcast('long', (b & 1)) == 1):
                ans = jcast('long', Code05_ShuffleCards.multiply(ans, a, mod))
            a = jcast('long', Code05_ShuffleCards.multiply(a, a, mod))
            b = jcast('long', jcast('long', (b >> (1 & 63))))
        return jcast('long', ans)

    @staticmethod
    def compute(n, m, l):
        n = jcast('long', n)
        m = jcast('long', m)
        l = jcast('long', l)
        mod = jcast('long', jcast('long', jadd(n, 1)))
        Code05_ShuffleCards.exgcd(Code05_ShuffleCards.power(2, m, mod), mod)
        x0 = jcast('long', jcast('long', jmod(jcast('long', jadd(jcast('long', jmod(Code05_ShuffleCards.x, mod)), mod)), mod)))
        return jcast('long', Code05_ShuffleCards.multiply(x0, l, mod))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        l = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(out, 'println', Code05_ShuffleCards.compute(n, m, l))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_ShuffleCards.d = jcast('long', 0)
Code05_ShuffleCards.x = jcast('long', 0)
Code05_ShuffleCards.y = jcast('long', 0)
Code05_ShuffleCards.px = jcast('long', 0)
Code05_ShuffleCards.py = jcast('long', 0)

if __name__ == '__main__':
    Code05_ShuffleCards.main([])

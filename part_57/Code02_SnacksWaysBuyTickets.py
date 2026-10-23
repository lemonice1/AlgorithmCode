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

# 牛牛的背包问题 & 世界冰球锦标赛
# 牛牛准备参加学校组织的春游, 出发前牛牛准备往背包里装入一些零食, 牛牛的背包容量为w。
# 牛牛家里一共有n袋零食, 第i袋零食体积为v[i]。
# 牛牛想知道在总体积不超过背包容量的情况下,他一共有多少种零食放法(总体积为0也算一种放法)。
# 输入描述：
# 输入包括两行
# 第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量
# 第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积
# 输出描述：
# 输出一个正整数, 表示牛牛一共有多少种零食放法。
# 测试链接 : https://www.luogu.com.cn/problem/P4799
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SnacksWaysBuyTickets:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'arr': 'arr', 'lsum': 'lsum', 'rsum': 'rsum', 'n': 'n', 'w': 'w'}
    MAXN = 0
    MAXM = 0
    arr = None
    lsum = None
    rsum = None
    n = 0
    w = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_SnacksWaysBuyTickets.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_SnacksWaysBuyTickets.w = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code02_SnacksWaysBuyTickets.n):
                jcall(in_, 'nextToken')
                Code02_SnacksWaysBuyTickets.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_SnacksWaysBuyTickets.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        lsize = jcast('int', Code02_SnacksWaysBuyTickets.f(0, jcast('int', (Code02_SnacksWaysBuyTickets.n >> (1 & 31))), 0, Code02_SnacksWaysBuyTickets.w, Code02_SnacksWaysBuyTickets.lsum, 0))
        rsize = jcast('int', Code02_SnacksWaysBuyTickets.f(jcast('int', (Code02_SnacksWaysBuyTickets.n >> (1 & 31))), Code02_SnacksWaysBuyTickets.n, 0, Code02_SnacksWaysBuyTickets.w, Code02_SnacksWaysBuyTickets.rsum, 0))
        jstatic('Arrays', 'sort', Code02_SnacksWaysBuyTickets.lsum, 0, lsize)
        jstatic('Arrays', 'sort', Code02_SnacksWaysBuyTickets.rsum, 0, rsize)
        ans = jcast('long', 0)
        i = jcast('int', jcast('int', (lsize - 1)))
        j = jcast('int', 0)
        while (i >= 0):
            while ((j < rsize) and (jcast('long', jadd(Code02_SnacksWaysBuyTickets.lsum[i], Code02_SnacksWaysBuyTickets.rsum[j])) <= Code02_SnacksWaysBuyTickets.w)):
                j = jcast('int', (j + 1))
            ans = jcast('long', jcast('long', jadd(ans, j)))
            i = jcast('int', (i - 1))
        return jcast('long', ans)

    # arr[i..e-1]范围上展开，到达e就停止
    # 返回值 : ans数组填到了什么位置！
    @staticmethod
    def f(i, e, s, w, ans, j):
        i = jcast('int', i)
        e = jcast('int', e)
        s = jcast('long', s)
        w = jcast('long', w)
        j = jcast('int', j)
        if (s > w):
            return jcast('int', j)
        # s <= w
        if (i == e):
            jset(ans, ((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2], s)
        else:
            # 不要arr[i]位置的数
            j = jcast('int', Code02_SnacksWaysBuyTickets.f(jcast('int', jadd(i, 1)), e, s, w, ans, j))
            # 要arr[i]位置的数
            j = jcast('int', Code02_SnacksWaysBuyTickets.f(jcast('int', jadd(i, 1)), e, jcast('long', jadd(s, Code02_SnacksWaysBuyTickets.arr[i])), w, ans, j))
        return jcast('int', j)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SnacksWaysBuyTickets.MAXN = jcast('int', 40)
Code02_SnacksWaysBuyTickets.MAXM = jcast('int', jcast('int', (1 << (20 & 31))))
Code02_SnacksWaysBuyTickets.arr = jarray('long', [Code02_SnacksWaysBuyTickets.MAXN])
Code02_SnacksWaysBuyTickets.lsum = jarray('long', [Code02_SnacksWaysBuyTickets.MAXM])
Code02_SnacksWaysBuyTickets.rsum = jarray('long', [Code02_SnacksWaysBuyTickets.MAXM])
Code02_SnacksWaysBuyTickets.n = jcast('int', 0)
Code02_SnacksWaysBuyTickets.w = jcast('long', 0)

if __name__ == '__main__':
    Code02_SnacksWaysBuyTickets.main([])

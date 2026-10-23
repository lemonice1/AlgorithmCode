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

# 萌数
# 如果一个数字，存在长度至少为2的回文子串，那么这种数字被称为萌数
# 比如101、110、111、1234321、45568
# 求[l,r]范围上，有多少个萌数
# 由于答案可能很大，所以输出答案对1000000007求余
# 测试链接 : https://www.luogu.com.cn/problem/P3413
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MengNumber:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'dp': 'dp'}
    MOD = 0
    MAXN = 0
    dp = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        a = jcast('int', 0)
        while (a < n):
            b = jcast('int', 0)
            while (b <= 10):
                c = jcast('int', 0)
                while (c <= 10):
                    d = jcast('int', 0)
                    while (d <= 1):
                        jset(Code02_MengNumber.dp[a][b][c], d, jcast('int', (-1)))
                        d = jcast('int', (d + 1))
                    c = jcast('int', (c + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        strs = jcall(jcall(br, 'readLine'), 'split', ' ')
        jcall(out, 'println', Code02_MengNumber.compute(jcall(strs[0], 'toCharArray'), jcall(strs[1], 'toCharArray')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(l, r):
        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', (Code02_MengNumber.cnt(r) - Code02_MengNumber.cnt(l))), Code02_MengNumber.MOD)), Code02_MengNumber.MOD)))
        if Code02_MengNumber.check(l):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, 1)), Code02_MengNumber.MOD)))
        return jcast('int', ans)

    # 返回0~num范围上萌数有多少个
    @staticmethod
    def cnt(num):
        if (num[0] == jchar('0')):
            return jcast('int', 0)
        n = jcast('int', jget(num, 'length'))
        all = jcast('long', 0)
        base = jcast('long', 1)
        i = jcast('int', jcast('int', (n - 1)))
        while (i >= 0):
            # 不理解的话看一下，讲解041-同余原理
            all = jcast('long', jcast('long', jmod(jcast('long', jadd(all, jcast('long', (base * jcast('int', (num[i] - jchar('0'))))))), Code02_MengNumber.MOD)))
            base = jcast('long', jcast('long', jmod(jcast('long', (base * 10)), Code02_MengNumber.MOD)))
            i = jcast('int', (i - 1))
        Code02_MengNumber.build(n)
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', jadd(jcast('long', (all - Code02_MengNumber.f(num, 0, 10, 10, 0))), Code02_MengNumber.MOD)), Code02_MengNumber.MOD))))

    # 从num的高位开始，当前来到第i位
    # 前一位数字是p、前前一位数字是pp，如果值是10，则表示那一位没有选择过数字
    # 如果之前的位已经确定比num小，那么free == 1，表示接下的数字可以自由选择
    # 如果之前的位和num一样，那么free == 0，表示接下的数字不能大于num当前位的数字
    # 返回<=num且不是萌数的数字有多少个
    @staticmethod
    def f(num, i, pp, p, free):
        i = jcast('int', i)
        pp = jcast('int', pp)
        p = jcast('int', p)
        free = jcast('int', free)
        if (i == jget(num, 'length')):
            return jcast('int', 1)
        if (Code02_MengNumber.dp[i][pp][p][free] != jcast('int', (-1))):
            return jcast('int', Code02_MengNumber.dp[i][pp][p][free])
        ans = jcast('int', 0)
        if (free == 0):
            if (p == 10):
                # 当前来到的就是num的最高位
                # 当前位不选数字
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), 10, 10, 1))), Code02_MengNumber.MOD)))
                cur = jcast('int', 1)
                while (cur < jcast('int', (num[i] - jchar('0')))):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, cur, 1))), Code02_MengNumber.MOD)))
                    cur = jcast('int', (cur + 1))
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, jcast('int', (num[i] - jchar('0'))), 0))), Code02_MengNumber.MOD)))
            else:
                # free == 0，之前和num一样，此时不能自由选择数字
                # 前一位p，选择过数字，p -> 0 ~ 9
                cur = jcast('int', 0)
                while (cur < jcast('int', (num[i] - jchar('0')))):
                    if ((pp != cur) and (p != cur)):
                        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, cur, 1))), Code02_MengNumber.MOD)))
                    cur = jcast('int', (cur + 1))
                if ((pp != jcast('int', (num[i] - jchar('0')))) and (p != jcast('int', (num[i] - jchar('0'))))):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, jcast('int', (num[i] - jchar('0'))), 0))), Code02_MengNumber.MOD)))
        else:
            if (p == 10):
                # free == 1，能自由选择数字
                # 从来没选过数字
                # 依然不选数字
                ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), 10, 10, 1))), Code02_MengNumber.MOD)))
                cur = jcast('int', 1)
                while (cur <= 9):
                    ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, cur, 1))), Code02_MengNumber.MOD)))
                    cur = jcast('int', (cur + 1))
            else:
                # free == 1，能自由选择数字
                # 之前选择过数字
                cur = jcast('int', 0)
                while (cur <= 9):
                    if ((pp != cur) and (p != cur)):
                        ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code02_MengNumber.f(num, jcast('int', jadd(i, 1)), p, cur, 1))), Code02_MengNumber.MOD)))
                    cur = jcast('int', (cur + 1))
        jset(Code02_MengNumber.dp[i][pp][p], free, ans)
        return jcast('int', ans)

    @staticmethod
    def check(num):
        pp = jcast('int', jcast('int', (-2)))
        p = jcast('int', jcast('int', (-1)))
        i = jcast('int', 0)
        while (i < jget(num, 'length')):
            if ((pp >= 0) and (num[pp] == num[i])):
                return jcast('boolean', True)
            if ((p >= 0) and (num[p] == num[i])):
                return jcast('boolean', True)
            pp = jcast('int', (pp + 1))
            p = jcast('int', (p + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', False)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MengNumber.MOD = jcast('int', 1000000007)
Code02_MengNumber.MAXN = jcast('int', 1001)
Code02_MengNumber.dp = jarray('int', [Code02_MengNumber.MAXN, 11, 11, 2])

if __name__ == '__main__':
    Code02_MengNumber.main([])

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

# 信封问题(错排问题)
# 一共n个人，每个人都写了一封信
# 每个人必须寄出一封信，每个人必须收到一封信，并且不能自己寄给自己
# 返回一共有多少种寄信的方法
# 1 <= n <= 20
# 测试链接 : https://www.luogu.com.cn/problem/P1595
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Derangement:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        # out.println(ways1(n));
        jcall(out, 'println', Code01_Derangement.ways2(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 普通动态规划的方法
    @staticmethod
    def ways1(n):
        n = jcast('int', n)
        dp = jarray('long', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            if (i == 1):
                dp[i] = jcast('long', 0)
            else:
                if (i == 2):
                    dp[i] = jcast('long', 1)
                else:
                    dp[i] = jcast('long', jcast('long', (jcast('int', (i - 1)) * jcast('long', jadd(dp[jcast('int', (i - 1))], dp[jcast('int', (i - 2))])))))
            i = jcast('int', (i + 1))
        return jcast('long', dp[n])

    # 二项式反演的方法
    @staticmethod
    def ways2(n):
        n = jcast('int', n)
        # n!
        facn = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            facn = jcast('long', jcast('long', (facn * i)))
            i = jcast('int', (i + 1))
        # i = 0时的项
        ans = jcast('long', facn)
        # i!
        faci = jcast('long', 1)
        i = jcast('int', 1)
        while (i <= n):
            # i = 1...n
            # (-1)的i次方 * (n! / i!)
            faci = jcast('long', jcast('long', (faci * i)))
            if (jcast('int', (i & 1)) == 0):
                ans = jcast('long', jcast('long', jadd(ans, jcast('long', jdiv(facn, faci)))))
            else:
                ans = jcast('long', jcast('long', (ans - jcast('long', jdiv(facn, faci)))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_Derangement.main([])

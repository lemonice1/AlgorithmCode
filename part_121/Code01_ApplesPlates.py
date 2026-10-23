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

# 苹果和盘子
# 有m个苹果，认为苹果之间无差别，有n个盘子，认为盘子之间无差别
# 比如5个苹果如果放进3个盘子，那么(1, 3, 1) (1, 1, 3) (3, 1, 1)认为是同一种方法
# 允许有些盘子是空的，返回有多少种放置方法
# 测试链接 : https://www.nowcoder.com/practice/bfd8234bb5e84be0b493656e390bdebf
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_ApplesPlates:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXN': 'MAXN', 'dp': 'dp'}
    MAXM = 0
    MAXN = 0
    dp = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code01_ApplesPlates.compute(m, n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        i = jcast('int', 0)
        while (i <= m):
            j = jcast('int', 0)
            while (j <= n):
                jset(Code01_ApplesPlates.dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_ApplesPlates.f(m, n))

    @staticmethod
    def f(m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        if (m == 0):
            return jcast('int', 1)
        if (n == 0):
            return jcast('int', 0)
        if (Code01_ApplesPlates.dp[m][n] != jcast('int', (-1))):
            return jcast('int', Code01_ApplesPlates.dp[m][n])
        ans = 0
        if (n > m):
            ans = jcast('int', Code01_ApplesPlates.f(m, m))
        else:
            ans = jcast('int', jcast('int', jadd(Code01_ApplesPlates.f(m, jcast('int', (n - 1))), Code01_ApplesPlates.f(jcast('int', (m - n)), n))))
        jset(Code01_ApplesPlates.dp[m], n, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_ApplesPlates.MAXM = jcast('int', 11)
Code01_ApplesPlates.MAXN = jcast('int', 11)
Code01_ApplesPlates.dp = jarray('int', [Code01_ApplesPlates.MAXM, Code01_ApplesPlates.MAXN])

if __name__ == '__main__':
    Code01_ApplesPlates.main([])

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

# 康托展开
# 数字从1到n，可以有很多排列，给出具体的一个排列，求该排列的名次，答案对 998244353 取模
# 1 <= n <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P5367
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_CantorExpansion:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'arr': 'arr', 'fac': 'fac', 'tree': 'tree', 'n': 'n'}
    MAXN = 0
    MOD = 0
    arr = None
    # 阶乘余数表
    fac = None
    # 树状数组
    tree = None
    n = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jmod(jcast('int', jadd(ans, Code01_CantorExpansion.tree[i])), Code01_CantorExpansion.MOD)))
            i = jcast('int', jcast('int', (i - Code01_CantorExpansion.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code01_CantorExpansion.n):
            Code01_CantorExpansion.tree[i] = jcast('int', jcast('int', jadd(Code01_CantorExpansion.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code01_CantorExpansion.lowbit(i))))

    @staticmethod
    def compute():
        Code01_CantorExpansion.fac[0] = jcast('int', 1)
        i = jcast('int', 1)
        while (i < Code01_CantorExpansion.n):
            Code01_CantorExpansion.fac[i] = jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', Code01_CantorExpansion.fac[jcast('int', (i - 1))]) * i)), Code01_CantorExpansion.MOD))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_CantorExpansion.n):
            Code01_CantorExpansion.add(i, 1)
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code01_CantorExpansion.n):
            ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, jcast('long', jmod(jcast('long', (jcast('long', Code01_CantorExpansion.sum(jcast('int', (Code01_CantorExpansion.arr[i] - 1)))) * Code01_CantorExpansion.fac[jcast('int', (Code01_CantorExpansion.n - i))])), Code01_CantorExpansion.MOD)))), Code01_CantorExpansion.MOD)))
            Code01_CantorExpansion.add(Code01_CantorExpansion.arr[i], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        # 求的排名从0开始，但是题目要求从1开始，所以最后+1再返回
        ans = jcast('long', jcast('long', jmod(jcast('long', jadd(ans, 1)), Code01_CantorExpansion.MOD)))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_CantorExpansion.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_CantorExpansion.n):
            jcall(in_, 'nextToken')
            Code01_CantorExpansion.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_CantorExpansion.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_CantorExpansion.MAXN = jcast('int', 1000001)
Code01_CantorExpansion.MOD = jcast('int', 998244353)
Code01_CantorExpansion.arr = jarray('int', [Code01_CantorExpansion.MAXN])
Code01_CantorExpansion.fac = jarray('int', [Code01_CantorExpansion.MAXN])
Code01_CantorExpansion.tree = jarray('int', [Code01_CantorExpansion.MAXN])
Code01_CantorExpansion.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_CantorExpansion.main([])

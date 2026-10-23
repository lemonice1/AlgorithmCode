# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 方伯伯的玉米田
# 给定一个长度为n的数组arr
# 每次可以选择一个区间[l,r]，区间内的数字都+1，最多执行k次
# 返回执行完成后，最长的不下降子序列长度
# 1 <= n <= 10^4
# 1 <= arr[i] <= 5000
# 2 <= k <= 500
# 测试链接 : https://www.luogu.com.cn/problem/P3287
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_CornField:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 'MAXH': 'MAXH', 'arr': 'arr', 'tree': 'tree', 'n': 'n', 'k': 'k'}
    MAXN = 0
    MAXK = 0
    MAXH = 0
    arr = None
    tree = None
    n = 0
    k = 0
    @staticmethod
    def update(x, y, v):
        x = jcast('int', x)
        y = jcast('int', y)
        v = jcast('int', v)
        i = jcast('int', x)
        while (i <= Code03_CornField.MAXH):
            j = jcast('int', y)
            while (j <= jcast('int', jadd(Code03_CornField.k, 1))):
                jset(Code03_CornField.tree[i], j, jstatic('Math', 'max', Code03_CornField.tree[i][j], v))
                j = jcast('int', jcast('int', jadd(j, jcast('int', (j & jcast('int', (-j)))))))
            i = jcast('int', jcast('int', jadd(i, jcast('int', (i & jcast('int', (-i)))))))

    @staticmethod
    def max(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        ans = jcast('int', 0)
        i = jcast('int', x)
        while (i > 0):
            j = jcast('int', y)
            while (j > 0):
                ans = jcast('int', jstatic('Math', 'max', ans, Code03_CornField.tree[i][j]))
                j = jcast('int', jcast('int', (j - jcast('int', (j & jcast('int', (-j)))))))
            i = jcast('int', jcast('int', (i - jcast('int', (i & jcast('int', (-i)))))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_CornField.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_CornField.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_CornField.n):
            jcall(in_, 'nextToken')
            Code03_CornField.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_CornField.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        # 注意这里第二层for循环，j一定是从k~0的枚举
        # 课上进行了重点图解，防止同一个i产生的记录之间相互影响
        v = 0
        dp = 0
        i = jcast('int', 1)
        while (i <= Code03_CornField.n):
            j = jcast('int', Code03_CornField.k)
            while (j >= 0):
                v = jcast('int', jcast('int', jadd(Code03_CornField.arr[i], j)))
                # 修改次数j，树状数组中对应的下标是j+1
                dp = jcast('int', jcast('int', jadd(Code03_CornField.max(v, jcast('int', jadd(j, 1))), 1)))
                Code03_CornField.update(v, jcast('int', jadd(j, 1)), dp)
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        # 修改次数k，树状数组中对应的下标是k+1
        return jcast('int', Code03_CornField.max(Code03_CornField.MAXH, jcast('int', jadd(Code03_CornField.k, 1))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_CornField.MAXN = jcast('int', 10001)
Code03_CornField.MAXK = jcast('int', 501)
Code03_CornField.MAXH = jcast('int', 5500)
Code03_CornField.arr = jarray('int', [Code03_CornField.MAXN])
Code03_CornField.tree = jarray('int', [jcast('int', jadd(Code03_CornField.MAXH, 1)), jcast('int', jadd(Code03_CornField.MAXK, 1))])
Code03_CornField.n = jcast('int', 0)
Code03_CornField.k = jcast('int', 0)

if __name__ == '__main__':
    Code03_CornField.main([])

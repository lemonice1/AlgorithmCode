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

# 逆序对数量(值域树状数组)
# 给定一个长度为n的数组arr
# 如果 i < j 且 arr[i] > arr[j]
# 那么(i,j)就是一个逆序对
# 求arr中逆序对的数量
# 1 <= n <= 5 * 10^5
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1908
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_NumberOfReversePair2:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sort': 'sort', 'tree': 'tree', 'n': 'n', 'm': 'm'}
    MAXN = 0
    arr = None
    sort = None
    tree = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code01_NumberOfReversePair2.m):
            Code01_NumberOfReversePair2.tree[i] = jcast('int', jcast('int', jadd(Code01_NumberOfReversePair2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code01_NumberOfReversePair2.lowbit(i))))

    # 1~i范围的累加和
    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('long', 0)
        while (i > 0):
            ans = jcast('long', jcast('long', jadd(ans, Code01_NumberOfReversePair2.tree[i])))
            i = jcast('int', jcast('int', (i - Code01_NumberOfReversePair2.lowbit(i))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_NumberOfReversePair2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_NumberOfReversePair2.n):
            jcall(in_, 'nextToken')
            Code01_NumberOfReversePair2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_NumberOfReversePair2.sort[i] = jcast('int', Code01_NumberOfReversePair2.arr[i])
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_NumberOfReversePair2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code01_NumberOfReversePair2.sort, 1, jcast('int', jadd(Code01_NumberOfReversePair2.n, 1)))
        Code01_NumberOfReversePair2.m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code01_NumberOfReversePair2.n):
            if (Code01_NumberOfReversePair2.sort[Code01_NumberOfReversePair2.m] != Code01_NumberOfReversePair2.sort[i]):
                jset(Code01_NumberOfReversePair2.sort, ((_java_obj_1 := Code01_NumberOfReversePair2), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_NumberOfReversePair2.sort[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_NumberOfReversePair2.n):
            jset(Code01_NumberOfReversePair2.arr, i, Code01_NumberOfReversePair2.rank(Code01_NumberOfReversePair2.arr[i]))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', Code01_NumberOfReversePair2.n)
        while (i >= 1):
            # 右边有多少数字是 <= 当前数值 - 1
            ans = jcast('long', jcast('long', jadd(ans, Code01_NumberOfReversePair2.sum(jcast('int', (Code01_NumberOfReversePair2.arr[i] - 1))))))
            # 增加当前数字的词频
            Code01_NumberOfReversePair2.add(Code01_NumberOfReversePair2.arr[i], 1)
            i = jcast('int', (i - 1))
        return jcast('long', ans)

    # 给定原始值v
    # 返回排名值(排序部分1~m中的下标)
    @staticmethod
    def rank(v):
        v = jcast('int', v)
        l = jcast('int', 1)
        r = jcast('int', Code01_NumberOfReversePair2.m)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code01_NumberOfReversePair2.sort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_NumberOfReversePair2.MAXN = jcast('int', 500001)
Code01_NumberOfReversePair2.arr = jarray('int', [Code01_NumberOfReversePair2.MAXN])
Code01_NumberOfReversePair2.sort = jarray('int', [Code01_NumberOfReversePair2.MAXN])
Code01_NumberOfReversePair2.tree = jarray('int', [Code01_NumberOfReversePair2.MAXN])
Code01_NumberOfReversePair2.n = jcast('int', 0)
Code01_NumberOfReversePair2.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_NumberOfReversePair2.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 逆康托展开
# 数字从1到n，可以有很多排列，给定一个长度为n的数组s，表示具体的一个排列
# 求出这个排列的排名假设为x，打印第x+m名的排列是什么
# 1 <= n <= 10^5
# 1 <= m <= 10^15
# 题目保证s是一个由1~n数字组成的正确排列，题目保证x+m不会超过排列的总数
# 测试链接 : https://www.luogu.com.cn/problem/U72177
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_InverseCantorExpansion:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum_data', 'n': 'n', 'm': 'm'}
    MAXN = 0
    arr = None
    # 线段树
    # 这种使用线段树的方式叫线段树二分
    # 讲解169的题目1，也涉及线段树二分
    sum_data = None
    n = 0
    m = 0
    # 初始化线段树，单点范围的初始累加和为1，认为所有数字都可用
    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_InverseCantorExpansion.build(l, mid, jcast('int', (i << (1 & 31))))
            Code02_InverseCantorExpansion.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', jcast('int', jadd(Code02_InverseCantorExpansion.sum_data[jcast('int', (i << (1 & 31)))], Code02_InverseCantorExpansion.sum_data[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 单点jobi上，增加jobv，因为是单点更新，所以不需要建立懒更新机制
    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', jcast('int', jadd(Code02_InverseCantorExpansion.sum_data[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code02_InverseCantorExpansion.add(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_InverseCantorExpansion.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', jcast('int', jadd(Code02_InverseCantorExpansion.sum_data[jcast('int', (i << (1 & 31)))], Code02_InverseCantorExpansion.sum_data[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 查询jobl~jobr范围的累加和
    @staticmethod
    def sum(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code02_InverseCantorExpansion.sum_data[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_InverseCantorExpansion.sum(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code02_InverseCantorExpansion.sum(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    # 线段树上找到第k名的是什么，找到后删掉词频，返回的过程修改累加和
    @staticmethod
    def getAndDelete(k, l, r, i):
        k = jcast('int', k)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        ans = 0
        if (l == r):
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', (Code02_InverseCantorExpansion.sum_data[i] - 1))
            ans = jcast('int', l)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_InverseCantorExpansion.sum_data[jcast('int', (i << (1 & 31)))] >= k):
                ans = jcast('int', Code02_InverseCantorExpansion.getAndDelete(k, l, mid, jcast('int', (i << (1 & 31)))))
            else:
                ans = jcast('int', Code02_InverseCantorExpansion.getAndDelete(jcast('int', (k - Code02_InverseCantorExpansion.sum_data[jcast('int', (i << (1 & 31)))])), jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))
            Code02_InverseCantorExpansion.sum_data[i] = jcast('int', jcast('int', jadd(Code02_InverseCantorExpansion.sum_data[jcast('int', (i << (1 & 31)))], Code02_InverseCantorExpansion.sum_data[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        return jcast('int', ans)

    @staticmethod
    def compute():
        # 当前排列转化为阶乘进制的排名
        Code02_InverseCantorExpansion.build(1, Code02_InverseCantorExpansion.n, 1)
        i = jcast('int', 1)
        x = 0
        while (i <= Code02_InverseCantorExpansion.n):
            x = jcast('int', jcast('int', Code02_InverseCantorExpansion.arr[i]))
            if (x == 1):
                Code02_InverseCantorExpansion.arr[i] = jcast('long', 0)
            else:
                jset(Code02_InverseCantorExpansion.arr, i, Code02_InverseCantorExpansion.sum(1, jcast('int', (x - 1)), 1, Code02_InverseCantorExpansion.n, 1))
            Code02_InverseCantorExpansion.add(x, jcast('int', (-1)), 1, Code02_InverseCantorExpansion.n, 1)
            i = jcast('int', (i + 1))
        # 当前排名加上m之后，得到新的排名，用阶乘进制表示
        # 最低位获得增加的幅度
        Code02_InverseCantorExpansion.arr[Code02_InverseCantorExpansion.n] = jcast('long', jcast('long', jadd(Code02_InverseCantorExpansion.arr[Code02_InverseCantorExpansion.n], Code02_InverseCantorExpansion.m)))
        i = jcast('int', Code02_InverseCantorExpansion.n)
        while (i >= 1):
            # 往上进位多少
            Code02_InverseCantorExpansion.arr[jcast('int', (i - 1))] = jcast('long', jcast('long', jadd(Code02_InverseCantorExpansion.arr[jcast('int', (i - 1))], jcast('long', jdiv(Code02_InverseCantorExpansion.arr[i], jcast('int', jadd(jcast('int', (Code02_InverseCantorExpansion.n - i)), 1)))))))
            # 当前位是多少
            Code02_InverseCantorExpansion.arr[i] = jcast('long', jcast('long', jmod(Code02_InverseCantorExpansion.arr[i], jcast('int', jadd(jcast('int', (Code02_InverseCantorExpansion.n - i)), 1)))))
            i = jcast('int', (i - 1))
        # 根据阶乘进制转化为具体的排列
        Code02_InverseCantorExpansion.build(1, Code02_InverseCantorExpansion.n, 1)
        i = jcast('int', 1)
        while (i <= Code02_InverseCantorExpansion.n):
            jset(Code02_InverseCantorExpansion.arr, i, Code02_InverseCantorExpansion.getAndDelete(jcast('int', jadd(jcast('int', Code02_InverseCantorExpansion.arr[i]), 1)), 1, Code02_InverseCantorExpansion.n, 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_InverseCantorExpansion.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_InverseCantorExpansion.m = jcast('long', jcast('long', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_InverseCantorExpansion.n):
            jcall(in_, 'nextToken')
            Code02_InverseCantorExpansion.arr[i] = jcast('long', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_InverseCantorExpansion.compute()
        i = jcast('int', 1)
        while (i <= Code02_InverseCantorExpansion.n):
            jcall(out, 'print', jadd(Code02_InverseCantorExpansion.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_InverseCantorExpansion.MAXN = jcast('int', 100001)
Code02_InverseCantorExpansion.arr = jarray('long', [Code02_InverseCantorExpansion.MAXN])
Code02_InverseCantorExpansion.sum_data = jarray('int', [jcast('int', (Code02_InverseCantorExpansion.MAXN << (2 & 31)))])
Code02_InverseCantorExpansion.n = jcast('int', 0)
Code02_InverseCantorExpansion.m = jcast('long', 0)

if __name__ == '__main__':
    Code02_InverseCantorExpansion.main([])

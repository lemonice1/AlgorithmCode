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

# 开关
# 现有n盏灯排成一排，从左到右依次编号为1~n，一开始所有的灯都是关着的
# 操作分两种
# 操作 0 l r : 改变l~r范围上所有灯的状态，开着的灯关上、关着的灯打开
# 操作 1 l r : 查询l~r范围上有多少灯是打开的
# 测试链接 : https://www.luogu.com.cn/problem/P3870
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Switch:
    __java_fields__ = {'MAXN': 'MAXN', 'light': 'light', 'reverse': 'reverse_data'}
    MAXN = 0
    light = None
    reverse_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_Switch.light[i] = jcast('int', jcast('int', jadd(Code01_Switch.light[jcast('int', (i << (1 & 31)))], Code01_Switch.light[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code01_Switch.reverse_data[i]:
            Code01_Switch.lazy(jcast('int', (i << (1 & 31))), ln)
            Code01_Switch.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), rn)
            Code01_Switch.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def lazy(i, n):
        i = jcast('int', i)
        n = jcast('int', n)
        Code01_Switch.light[i] = jcast('int', jcast('int', (n - Code01_Switch.light[i])))
        Code01_Switch.reverse_data[i] = jcast('boolean', (not Code01_Switch.reverse_data[i]))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code01_Switch.light[i] = jcast('int', 0)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_Switch.build(l, mid, jcast('int', (i << (1 & 31))))
            Code01_Switch.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_Switch.up(i)
        Code01_Switch.reverse_data[i] = jcast('boolean', False)

    @staticmethod
    def reverse(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_Switch.lazy(i, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_Switch.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_Switch.reverse(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_Switch.reverse(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_Switch.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code01_Switch.light[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_Switch.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_Switch.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code01_Switch.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_Switch.build(1, n, 1)
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jobl = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jobr = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 0):
                Code01_Switch.reverse(jobl, jobr, 1, n, 1)
            else:
                jcall(out, 'println', Code01_Switch.query(jobl, jobr, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Switch.MAXN = jcast('int', 100001)
Code01_Switch.light = jarray('int', [jcast('int', (Code01_Switch.MAXN << (2 & 31)))])
Code01_Switch.reverse_data = jarray('boolean', [jcast('int', (Code01_Switch.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code01_Switch.main([])

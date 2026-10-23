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

# 贪婪大陆
# 一共有n个格子，编号1~n，开始时格子上没有地雷，实现两种操作，一共调用m次
# 操作 1 l r : 在l~r范围的格子上放置一种新型地雷，每次地雷都是新款
# 操作 2 l r : 查询l~r范围的格子上一共放置过多少款不同的地雷
# 操作1并不是范围上替换地雷，而是范围上新增新型地雷，注意如下的例子
# 执行 1 3 6，表示3~6范围上新加一种地雷，假设地雷类型是A
# 执行 1 3 4，表示3~4范围上又新加一种地雷，和上次的地雷不同，假设地雷类型是B
# 格子3有两种地雷(A、B)、格子4有两种地雷(A、B)、格子5有一种地雷(A)、格子6有一种地雷(A)
# 执行 2 4 5，返回2；执行 2 5 6，会返回1
# 测试链接 : https://www.luogu.com.cn/problem/P2184
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Bombs:
    __java_fields__ = {'MAXN': 'MAXN', 'bombStarts': 'bombStarts', 'bombEnds': 'bombEnds'}
    MAXN = 0
    bombStarts = None
    bombEnds = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_Bombs.bombStarts[i] = jcast('int', jcast('int', jadd(Code02_Bombs.bombStarts[jcast('int', (i << (1 & 31)))], Code02_Bombs.bombStarts[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code02_Bombs.bombEnds[i] = jcast('int', jcast('int', jadd(Code02_Bombs.bombEnds[jcast('int', (i << (1 & 31)))], Code02_Bombs.bombEnds[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_Bombs.build(l, mid, jcast('int', (i << (1 & 31))))
            Code02_Bombs.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code02_Bombs.bombStarts[i] = jcast('int', 0)
        Code02_Bombs.bombEnds[i] = jcast('int', 0)

    # jobt==0表示在添加地雷范围的开头，jobi就是地雷范围的开头位置
    # jobt==1表示在添加地雷范围的结尾，jobi就是地雷范围的结尾位置
    @staticmethod
    def add(jobt, jobi, l, r, i):
        jobt = jcast('int', jobt)
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            if (jobt == 0):
                Code02_Bombs.bombStarts[i] = jcast('int', (Code02_Bombs.bombStarts[i] + 1))
            else:
                Code02_Bombs.bombEnds[i] = jcast('int', (Code02_Bombs.bombEnds[i] + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code02_Bombs.add(jobt, jobi, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_Bombs.add(jobt, jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_Bombs.up(i)

    # jobt==0表示在查询[jobl ~ jobr]范围上有多少地雷范围的开头
    # jobt==1表示在查询[jobl ~ jobr]范围上有多少地雷范围的结尾
    @staticmethod
    def query(jobt, jobl, jobr, l, r, i):
        jobt = jcast('int', jobt)
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', (Code02_Bombs.bombStarts[i] if (jobt == 0) else Code02_Bombs.bombEnds[i]))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            ans = jcast('int', 0)
            if (jobl <= mid):
                ans = jcast('int', jcast('int', jadd(ans, Code02_Bombs.query(jobt, jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
            if (jobr > mid):
                ans = jcast('int', jcast('int', jadd(ans, Code02_Bombs.query(jobt, jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
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
        Code02_Bombs.build(1, n, 1)
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
            if (op == 1):
                Code02_Bombs.add(0, jobl, 1, n, 1)
                Code02_Bombs.add(1, jobr, 1, n, 1)
            else:
                s = jcast('int', Code02_Bombs.query(0, 1, jobr, 1, n, 1))
                # 如果jobl==1，说明没有更左的区域
                # 如果jobl>1，说明有更左的区域
                e = jcast('int', (0 if (jobl == 1) else Code02_Bombs.query(1, 1, jcast('int', (jobl - 1)), 1, n, 1)))
                jcall(out, 'println', jcast('int', (s - e)))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Bombs.MAXN = jcast('int', 100001)
Code02_Bombs.bombStarts = jarray('int', [jcast('int', (Code02_Bombs.MAXN << (2 & 31)))])
Code02_Bombs.bombEnds = jarray('int', [jcast('int', (Code02_Bombs.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code02_Bombs.main([])

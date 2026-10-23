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

# 国旗计划
# 给定点的数量m，点的编号1~m，所有点围成一个环
# i号点一定顺时针到达i+1号点，最终m号点顺指针回到1号点
# 给定n条线段，每条线段(a, b)，表示线段从点a顺时针到点b
# 输入数据保证所有线段可以把整个环覆盖
# 输入数据保证每条线段不会完全在另一条线段的内部
# 也就是线段之间可能有重合但一定互不包含
# 返回一个长度为n的结果数组ans，ans[x]表示一定选x号线段的情况下
# 至少选几条线段能覆盖整个环
# 测试链接 : https://www.luogu.com.cn/problem/P4155
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_FlagPlan:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'power': 'power', 'line': 'line', 'stjump': 'stjump', 'ans': 'ans', 'n': 'n', 'm': 'm'}
    MAXN = 0
    LIMIT = 0
    power = 0
    # 每条线段3个信息 : 线段编号、线段左边界、线段右边界
    line = None
    # stjump[i][p] : 从i号线段出发，跳的次数是2的p次方，能到达的最右线段的编号
    stjump = None
    ans = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_FlagPlan.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_FlagPlan.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_FlagPlan.n):
            jset(Code01_FlagPlan.line[i], 0, i)
            jcall(in_, 'nextToken')
            jset(Code01_FlagPlan.line[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code01_FlagPlan.line[i], 2, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_FlagPlan.compute()
        jcall(out, 'print', Code01_FlagPlan.ans[1])
        i = jcast('int', 2)
        while (i <= Code01_FlagPlan.n):
            jcall(out, 'print', jadd(' ', Code01_FlagPlan.ans[i]))
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        Code01_FlagPlan.power = jcast('int', Code01_FlagPlan.log2(Code01_FlagPlan.n))
        Code01_FlagPlan.build()
        i = jcast('int', 1)
        while (i <= Code01_FlagPlan.n):
            jset(Code01_FlagPlan.ans, Code01_FlagPlan.line[i][0], Code01_FlagPlan.jump(i))
            i = jcast('int', (i + 1))

    # <=n最接近的2的幂，是2的几次方
    @staticmethod
    def log2(n):
        n = jcast('int', n)
        ans = jcast('int', 0)
        while (jcast('int', (1 << (ans & 31))) <= jcast('int', (n >> (1 & 31)))):
            ans = jcast('int', (ans + 1))
        return jcast('int', ans)

    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i <= Code01_FlagPlan.n):
            if (Code01_FlagPlan.line[i][1] > Code01_FlagPlan.line[i][2]):
                ((_java_obj_1 := Code01_FlagPlan.line[i]), (_java_key_2 := 2), jset(_java_obj_1, _java_key_2, jcast('int', jadd(jget(_java_obj_1, _java_key_2), Code01_FlagPlan.m))))[2]
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_FlagPlan.line, 1, jcast('int', jadd(Code01_FlagPlan.n, 1)), (lambda a, b: (a[1] - b[1])))
        i = jcast('int', 1)
        while (i <= Code01_FlagPlan.n):
            jset(Code01_FlagPlan.line[jcast('int', jadd(i, Code01_FlagPlan.n))], 0, Code01_FlagPlan.line[i][0])
            jset(Code01_FlagPlan.line[jcast('int', jadd(i, Code01_FlagPlan.n))], 1, jcast('int', jadd(Code01_FlagPlan.line[i][1], Code01_FlagPlan.m)))
            jset(Code01_FlagPlan.line[jcast('int', jadd(i, Code01_FlagPlan.n))], 2, jcast('int', jadd(Code01_FlagPlan.line[i][2], Code01_FlagPlan.m)))
            i = jcast('int', (i + 1))
        e = jcast('int', jcast('int', (Code01_FlagPlan.n << (1 & 31))))
        i = jcast('int', 1)
        arrive = jcast('int', 1)
        while (i <= e):
            while ((jcast('int', jadd(arrive, 1)) <= e) and (Code01_FlagPlan.line[jcast('int', jadd(arrive, 1))][1] <= Code01_FlagPlan.line[i][2])):
                arrive = jcast('int', (arrive + 1))
            jset(Code01_FlagPlan.stjump[i], 0, arrive)
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code01_FlagPlan.power):
            i = jcast('int', 1)
            while (i <= e):
                jset(Code01_FlagPlan.stjump[i], p, Code01_FlagPlan.stjump[Code01_FlagPlan.stjump[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    @staticmethod
    def jump(i):
        i = jcast('int', i)
        aim = jcast('int', jcast('int', jadd(Code01_FlagPlan.line[i][1], Code01_FlagPlan.m)))
        cur = jcast('int', i)
        next = 0
        ans = jcast('int', 0)
        p = jcast('int', Code01_FlagPlan.power)
        while (p >= 0):
            next = jcast('int', Code01_FlagPlan.stjump[cur][p])
            if ((next != 0) and (Code01_FlagPlan.line[next][2] < aim)):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (p & 31))))))
                cur = jcast('int', next)
            p = jcast('int', (p - 1))
        return jcast('int', jcast('int', jadd(jcast('int', jadd(ans, 1)), 1)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_FlagPlan.MAXN = jcast('int', 200001)
Code01_FlagPlan.LIMIT = jcast('int', 18)
Code01_FlagPlan.power = jcast('int', 0)
Code01_FlagPlan.line = jarray('int', [jcast('int', (Code01_FlagPlan.MAXN << (1 & 31))), 3])
Code01_FlagPlan.stjump = jarray('int', [jcast('int', (Code01_FlagPlan.MAXN << (1 & 31))), Code01_FlagPlan.LIMIT])
Code01_FlagPlan.ans = jarray('int', [Code01_FlagPlan.MAXN])
Code01_FlagPlan.n = jcast('int', 0)
Code01_FlagPlan.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_FlagPlan.main([])

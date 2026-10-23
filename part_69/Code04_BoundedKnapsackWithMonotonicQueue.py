# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 多重背包单调队列优化
# 宝物筛选
# 一共有n种货物, 背包容量为t
# 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
# 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1776
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_BoundedKnapsackWithMonotonicQueue:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'v': 'v', 'w': 'w', 'c': 'c', 'dp': 'dp', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 't': 't'}
    MAXN = 0
    MAXW = 0
    v = None
    w = None
    c = None
    dp = None
    queue = None
    l = 0
    r = 0
    n = 0
    t = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_BoundedKnapsackWithMonotonicQueue.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_BoundedKnapsackWithMonotonicQueue.t = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code04_BoundedKnapsackWithMonotonicQueue.n):
                jcall(in_, 'nextToken')
                Code04_BoundedKnapsackWithMonotonicQueue.v[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code04_BoundedKnapsackWithMonotonicQueue.w[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code04_BoundedKnapsackWithMonotonicQueue.c[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_BoundedKnapsackWithMonotonicQueue.compute2())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 严格位置依赖的动态规划 + 单调队列优化枚举
    @staticmethod
    def compute1():
        dp = jarray('int', [jcast('int', jadd(Code04_BoundedKnapsackWithMonotonicQueue.n, 1)), jcast('int', jadd(Code04_BoundedKnapsackWithMonotonicQueue.t, 1))])
        i = jcast('int', 1)
        while (i <= Code04_BoundedKnapsackWithMonotonicQueue.n):
            # 同余分组
            mod = jcast('int', 0)
            while (mod <= jstatic('Math', 'min', Code04_BoundedKnapsackWithMonotonicQueue.t, jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.w[i] - 1)))):
                Code04_BoundedKnapsackWithMonotonicQueue.l = jcast('int', jset(Code04_BoundedKnapsackWithMonotonicQueue, 'r', 0))
                j = jcast('int', mod)
                while (j <= Code04_BoundedKnapsackWithMonotonicQueue.t):
                    while ((Code04_BoundedKnapsackWithMonotonicQueue.l < Code04_BoundedKnapsackWithMonotonicQueue.r) and (Code04_BoundedKnapsackWithMonotonicQueue.value1(dp, i, Code04_BoundedKnapsackWithMonotonicQueue.queue[jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))]) <= Code04_BoundedKnapsackWithMonotonicQueue.value1(dp, i, j))):
                        Code04_BoundedKnapsackWithMonotonicQueue.r = jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))
                    jset(Code04_BoundedKnapsackWithMonotonicQueue.queue, ((_java_obj_1 := Code04_BoundedKnapsackWithMonotonicQueue), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], j)
                    if (Code04_BoundedKnapsackWithMonotonicQueue.queue[Code04_BoundedKnapsackWithMonotonicQueue.l] == jcast('int', (j - jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.w[i] * jcast('int', jadd(Code04_BoundedKnapsackWithMonotonicQueue.c[i], 1))))))):
                        Code04_BoundedKnapsackWithMonotonicQueue.l = jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.l + 1))
                    jset(dp[i], j, jcast('int', jadd(Code04_BoundedKnapsackWithMonotonicQueue.value1(dp, i, Code04_BoundedKnapsackWithMonotonicQueue.queue[Code04_BoundedKnapsackWithMonotonicQueue.l]), jcast('int', (jcast('int', jdiv(j, Code04_BoundedKnapsackWithMonotonicQueue.w[i])) * Code04_BoundedKnapsackWithMonotonicQueue.v[i])))))
                    j = jcast('int', jcast('int', jadd(j, Code04_BoundedKnapsackWithMonotonicQueue.w[i])))
                mod = jcast('int', (mod + 1))
            i = jcast('int', (i + 1))
        return jcast('int', dp[Code04_BoundedKnapsackWithMonotonicQueue.n][Code04_BoundedKnapsackWithMonotonicQueue.t])

    # 当前来到i号货物，需要j位置的指标，返回指标值
    @staticmethod
    def value1(dp, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('int', jcast('int', (dp[jcast('int', (i - 1))][j] - jcast('int', (jcast('int', jdiv(j, Code04_BoundedKnapsackWithMonotonicQueue.w[i])) * Code04_BoundedKnapsackWithMonotonicQueue.v[i])))))

    # 空间压缩的动态规划 + 单调队列优化枚举
    # 因为求dp[i][j]时需要上一行左侧的若干格子
    # 所以做空间压缩时，每一行需要从右往左求
    # 以此来保证左侧的格子还没有更新，还是"上一行"的状况
    @staticmethod
    def compute2():
        i = jcast('int', 1)
        while (i <= Code04_BoundedKnapsackWithMonotonicQueue.n):
            mod = jcast('int', 0)
            while (mod <= jstatic('Math', 'min', Code04_BoundedKnapsackWithMonotonicQueue.t, jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.w[i] - 1)))):
                Code04_BoundedKnapsackWithMonotonicQueue.l = jcast('int', jset(Code04_BoundedKnapsackWithMonotonicQueue, 'r', 0))
                # 先把c[i]个的指标进入单调队列
                j = jcast('int', jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.t - mod)))
                cnt = jcast('int', 1)
                while ((j >= 0) and (cnt <= Code04_BoundedKnapsackWithMonotonicQueue.c[i])):
                    while ((Code04_BoundedKnapsackWithMonotonicQueue.l < Code04_BoundedKnapsackWithMonotonicQueue.r) and (Code04_BoundedKnapsackWithMonotonicQueue.value2(i, Code04_BoundedKnapsackWithMonotonicQueue.queue[jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))]) <= Code04_BoundedKnapsackWithMonotonicQueue.value2(i, j))):
                        Code04_BoundedKnapsackWithMonotonicQueue.r = jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))
                    jset(Code04_BoundedKnapsackWithMonotonicQueue.queue, ((_java_obj_4 := Code04_BoundedKnapsackWithMonotonicQueue), (_java_key_5 := 'r'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4], j)
                    j = jcast('int', jcast('int', (j - Code04_BoundedKnapsackWithMonotonicQueue.w[i])))
                    cnt = jcast('int', (cnt + 1))
                j = jcast('int', jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.t - mod)))
                enter = jcast('int', jcast('int', (j - jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.w[i] * Code04_BoundedKnapsackWithMonotonicQueue.c[i])))))
                while (j >= 0):
                    # 窗口进入enter位置的指标
                    if (enter >= 0):
                        while ((Code04_BoundedKnapsackWithMonotonicQueue.l < Code04_BoundedKnapsackWithMonotonicQueue.r) and (Code04_BoundedKnapsackWithMonotonicQueue.value2(i, Code04_BoundedKnapsackWithMonotonicQueue.queue[jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))]) <= Code04_BoundedKnapsackWithMonotonicQueue.value2(i, enter))):
                            Code04_BoundedKnapsackWithMonotonicQueue.r = jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.r - 1))
                        jset(Code04_BoundedKnapsackWithMonotonicQueue.queue, ((_java_obj_7 := Code04_BoundedKnapsackWithMonotonicQueue), (_java_key_8 := 'r'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4], enter)
                    # 计算dp[i][j]
                    jset(Code04_BoundedKnapsackWithMonotonicQueue.dp, j, jcast('int', jadd(Code04_BoundedKnapsackWithMonotonicQueue.value2(i, Code04_BoundedKnapsackWithMonotonicQueue.queue[Code04_BoundedKnapsackWithMonotonicQueue.l]), jcast('int', (jcast('int', jdiv(j, Code04_BoundedKnapsackWithMonotonicQueue.w[i])) * Code04_BoundedKnapsackWithMonotonicQueue.v[i])))))
                    # 窗口弹出j位置的指标
                    if (Code04_BoundedKnapsackWithMonotonicQueue.queue[Code04_BoundedKnapsackWithMonotonicQueue.l] == j):
                        Code04_BoundedKnapsackWithMonotonicQueue.l = jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.l + 1))
                    j = jcast('int', jcast('int', (j - Code04_BoundedKnapsackWithMonotonicQueue.w[i])))
                    enter = jcast('int', jcast('int', (enter - Code04_BoundedKnapsackWithMonotonicQueue.w[i])))
                mod = jcast('int', (mod + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_BoundedKnapsackWithMonotonicQueue.dp[Code04_BoundedKnapsackWithMonotonicQueue.t])

    # 当前来到i号货物，需要j位置的指标，返回指标值
    @staticmethod
    def value2(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        return jcast('int', jcast('int', (Code04_BoundedKnapsackWithMonotonicQueue.dp[j] - jcast('int', (jcast('int', jdiv(j, Code04_BoundedKnapsackWithMonotonicQueue.w[i])) * Code04_BoundedKnapsackWithMonotonicQueue.v[i])))))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_BoundedKnapsackWithMonotonicQueue.MAXN = jcast('int', 101)
Code04_BoundedKnapsackWithMonotonicQueue.MAXW = jcast('int', 40001)
Code04_BoundedKnapsackWithMonotonicQueue.v = jarray('int', [Code04_BoundedKnapsackWithMonotonicQueue.MAXN])
Code04_BoundedKnapsackWithMonotonicQueue.w = jarray('int', [Code04_BoundedKnapsackWithMonotonicQueue.MAXN])
Code04_BoundedKnapsackWithMonotonicQueue.c = jarray('int', [Code04_BoundedKnapsackWithMonotonicQueue.MAXN])
Code04_BoundedKnapsackWithMonotonicQueue.dp = jarray('int', [Code04_BoundedKnapsackWithMonotonicQueue.MAXW])
Code04_BoundedKnapsackWithMonotonicQueue.queue = jarray('int', [Code04_BoundedKnapsackWithMonotonicQueue.MAXW])
Code04_BoundedKnapsackWithMonotonicQueue.l = jcast('int', 0)
Code04_BoundedKnapsackWithMonotonicQueue.r = jcast('int', 0)
Code04_BoundedKnapsackWithMonotonicQueue.n = jcast('int', 0)
Code04_BoundedKnapsackWithMonotonicQueue.t = jcast('int', 0)

if __name__ == '__main__':
    Code04_BoundedKnapsackWithMonotonicQueue.main([])

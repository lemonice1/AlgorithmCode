# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 连接棒材的最低费用(洛谷测试)
# 你有一些长度为正整数的棍子
# 这些长度以数组sticks的形式给出
# sticks[i]是第i个木棍的长度
# 你可以通过支付x+y的成本将任意两个长度为x和y的棍子连接成一个棍子
# 你必须连接所有的棍子，直到剩下一个棍子
# 返回以这种方式将所有给定的棍子连接成一个棍子的最小成本
# 测试链接 : https://www.luogu.com.cn/problem/P1090
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_MinimumCostToConnectSticks2:
    __java_fields__ = {'MAXN': 'MAXN', 'nums': 'nums', 'n': 'n', 'heap': 'heap', 'size': 'size'}
    MAXN = 0
    nums = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code06_MinimumCostToConnectSticks2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code06_MinimumCostToConnectSticks2.n):
                jcall(in_, 'nextToken')
                Code06_MinimumCostToConnectSticks2.nums[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code06_MinimumCostToConnectSticks2.minCost())
            jcall(out, 'flush')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def minCost():
        Code06_MinimumCostToConnectSticks2.size = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code06_MinimumCostToConnectSticks2.n):
            Code06_MinimumCostToConnectSticks2.add(Code06_MinimumCostToConnectSticks2.nums[i])
            i = jcast('int', (i + 1))
        sum = jcast('int', 0)
        cur = jcast('int', 0)
        while (Code06_MinimumCostToConnectSticks2.size > 1):
            cur = jcast('int', jcast('int', jadd(Code06_MinimumCostToConnectSticks2.pop(), Code06_MinimumCostToConnectSticks2.pop())))
            sum = jcast('int', jcast('int', jadd(sum, cur)))
            Code06_MinimumCostToConnectSticks2.add(cur)
        return jcast('int', sum)

    # 手写小根堆
    heap = None
    # 堆的大小
    size = 0
    @staticmethod
    def add(x):
        x = jcast('int', x)
        Code06_MinimumCostToConnectSticks2.heap[Code06_MinimumCostToConnectSticks2.size] = jcast('int', x)
        i = jcast('int', ((_java_obj_1 := Code06_MinimumCostToConnectSticks2), (_java_key_2 := 'size'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])
        while (Code06_MinimumCostToConnectSticks2.heap[i] < Code06_MinimumCostToConnectSticks2.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))]):
            Code06_MinimumCostToConnectSticks2.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def pop():
        ans = jcast('int', Code06_MinimumCostToConnectSticks2.heap[0])
        Code06_MinimumCostToConnectSticks2.swap(0, ((_java_obj_4 := Code06_MinimumCostToConnectSticks2), (_java_key_5 := 'size'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3])
        i = jcast('int', 0)
        l = jcast('int', 1)
        best = 0
        while (l < Code06_MinimumCostToConnectSticks2.size):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code06_MinimumCostToConnectSticks2.size) and (Code06_MinimumCostToConnectSticks2.heap[jcast('int', jadd(l, 1))] < Code06_MinimumCostToConnectSticks2.heap[l])) else l))
                best = jcast('int', (best if (Code06_MinimumCostToConnectSticks2.heap[best] < Code06_MinimumCostToConnectSticks2.heap[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code06_MinimumCostToConnectSticks2.swap(i, best)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code06_MinimumCostToConnectSticks2.heap[i])
        Code06_MinimumCostToConnectSticks2.heap[i] = jcast('int', Code06_MinimumCostToConnectSticks2.heap[j])
        Code06_MinimumCostToConnectSticks2.heap[j] = jcast('int', tmp)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_MinimumCostToConnectSticks2.MAXN = jcast('int', 10001)
Code06_MinimumCostToConnectSticks2.nums = jarray('int', [Code06_MinimumCostToConnectSticks2.MAXN])
Code06_MinimumCostToConnectSticks2.n = jcast('int', 0)
Code06_MinimumCostToConnectSticks2.heap = jarray('int', [Code06_MinimumCostToConnectSticks2.MAXN])
Code06_MinimumCostToConnectSticks2.size = jcast('int', 0)

if __name__ == '__main__':
    Code06_MinimumCostToConnectSticks2.main([])

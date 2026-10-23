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

# 多重背包通过二进制分组转化成01背包(模版)
# 宝物筛选
# 一共有n种货物, 背包容量为t
# 每种货物的价值(v[i])、重量(w[i])、数量(c[i])都给出
# 请返回选择货物不超过背包容量的情况下，能得到的最大的价值
# 测试链接 : https://www.luogu.com.cn/problem/P1776
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BoundedKnapsackWithBinarySplitting:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXW': 'MAXW', 'v': 'v', 'w': 'w', 'dp': 'dp', 'n': 'n', 't': 't', 'm': 'm'}
    MAXN = 0
    MAXW = 0
    # 把每一种货物根据个数做二进制分组，去生成衍生商品
    # 衍生出来的每一种商品，价值放入v、重量放入w
    v = None
    w = None
    dp = None
    n = 0
    t = 0
    m = 0
    # 时间复杂度O(t * (log(第1种商品的个数) + log(第2种商品的个数) + ... + log(第n种商品的个数)))
    # 对每一种商品的个数取log，所以时间复杂度虽然大于O(n * t)，但也不会大多少
    # 多重背包最常用的方式
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_BoundedKnapsackWithBinarySplitting.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code02_BoundedKnapsackWithBinarySplitting.t = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_BoundedKnapsackWithBinarySplitting.m = jcast('int', 0)
            i = jcast('int', 1)
            value = 0
            weight = 0
            cnt = 0
            while (i <= Code02_BoundedKnapsackWithBinarySplitting.n):
                jcall(in_, 'nextToken')
                value = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                weight = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                cnt = jcast('int', jcast('int', jget(in_, 'nval')))
                # 整个文件最重要的逻辑 : 二进制分组
                # 一般都使用这种技巧，这段代码非常重要
                # 虽然时间复杂度不如单调队列优化的版本
                # 但是好写，而且即便是比赛，时间复杂度也达标
                # 二进制分组的时间复杂度为O(log cnt)
                k = jcast('int', 1)
                while (k <= cnt):
                    jset(Code02_BoundedKnapsackWithBinarySplitting.v, ((_java_obj_1 := Code02_BoundedKnapsackWithBinarySplitting), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], jcast('int', (k * value)))
                    Code02_BoundedKnapsackWithBinarySplitting.w[Code02_BoundedKnapsackWithBinarySplitting.m] = jcast('int', jcast('int', (k * weight)))
                    cnt = jcast('int', jcast('int', (cnt - k)))
                    k = jcast('int', jcast('int', (k << (1 & 31))))
                if (cnt > 0):
                    jset(Code02_BoundedKnapsackWithBinarySplitting.v, ((_java_obj_4 := Code02_BoundedKnapsackWithBinarySplitting), (_java_key_5 := 'm'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], jcast('int', (cnt * value)))
                    Code02_BoundedKnapsackWithBinarySplitting.w[Code02_BoundedKnapsackWithBinarySplitting.m] = jcast('int', jcast('int', (cnt * weight)))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_BoundedKnapsackWithBinarySplitting.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 01背包的空间压缩代码(模版)
    @staticmethod
    def compute():
        jstatic('Arrays', 'fill', Code02_BoundedKnapsackWithBinarySplitting.dp, 0, jcast('int', jadd(Code02_BoundedKnapsackWithBinarySplitting.t, 1)), 0)
        i = jcast('int', 1)
        while (i <= Code02_BoundedKnapsackWithBinarySplitting.m):
            j = jcast('int', Code02_BoundedKnapsackWithBinarySplitting.t)
            while (j >= Code02_BoundedKnapsackWithBinarySplitting.w[i]):
                jset(Code02_BoundedKnapsackWithBinarySplitting.dp, j, jstatic('Math', 'max', Code02_BoundedKnapsackWithBinarySplitting.dp[j], jcast('int', jadd(Code02_BoundedKnapsackWithBinarySplitting.dp[jcast('int', (j - Code02_BoundedKnapsackWithBinarySplitting.w[i]))], Code02_BoundedKnapsackWithBinarySplitting.v[i]))))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code02_BoundedKnapsackWithBinarySplitting.dp[Code02_BoundedKnapsackWithBinarySplitting.t])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BoundedKnapsackWithBinarySplitting.MAXN = jcast('int', 1001)
Code02_BoundedKnapsackWithBinarySplitting.MAXW = jcast('int', 40001)
Code02_BoundedKnapsackWithBinarySplitting.v = jarray('int', [Code02_BoundedKnapsackWithBinarySplitting.MAXN])
Code02_BoundedKnapsackWithBinarySplitting.w = jarray('int', [Code02_BoundedKnapsackWithBinarySplitting.MAXN])
Code02_BoundedKnapsackWithBinarySplitting.dp = jarray('int', [Code02_BoundedKnapsackWithBinarySplitting.MAXW])
Code02_BoundedKnapsackWithBinarySplitting.n = jcast('int', 0)
Code02_BoundedKnapsackWithBinarySplitting.t = jcast('int', 0)
Code02_BoundedKnapsackWithBinarySplitting.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_BoundedKnapsackWithBinarySplitting.main([])

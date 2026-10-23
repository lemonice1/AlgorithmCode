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

# 有一次错误称重求最重物品
# 一共有n个物品，编号1~n，定义合法方案如下：
# 1，每个物品的重量都是确定的
# 2，每个物品的重量一定都是正整数
# 3，最重的物品有且仅有1个
# 每次称重格式类似：3 2 5 6 10，代表本次称重涉3个物品，编号为2、5、6，总重量10
# 一共有n+1条称重数据，称重数据整体有效的条件为：
# 错误的称重数据有且仅有1条，只有排除这条错误称重，才能求出一种合法方案
# 如果称重数据有效，打印最重三角形的编号
# 如果称重数据无效，打印"illegal"
# 1 <= m <= n <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P5027
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 这道题目后来增加了一个测试用例，让double类型的精度不够，导致出错
# 另一种实现可参考 Code04_FindMaxWeighing2.py
class Code04_FindMaxWeighing:
    __java_fields__ = {'MAXN': 'MAXN', 'data': 'data', 'mat': 'mat', 'n': 'n', 'sml': 'sml'}
    MAXN = 0
    data = None
    mat = None
    n = 0
    sml = 0.0
    # 高斯消元解决加法方程组模版
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                max = jcast('int', i)
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (jstatic('Math', 'abs', Code04_FindMaxWeighing.mat[j][j]) >= Code04_FindMaxWeighing.sml)):
                            raise JContinue(None)
                        if (jstatic('Math', 'abs', Code04_FindMaxWeighing.mat[j][i]) > jstatic('Math', 'abs', Code04_FindMaxWeighing.mat[max][i])):
                            max = jcast('int', j)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                Code04_FindMaxWeighing.swap(i, max)
                if (jstatic('Math', 'abs', Code04_FindMaxWeighing.mat[i][i]) >= Code04_FindMaxWeighing.sml):
                    tmp = jcast('double', Code04_FindMaxWeighing.mat[i][i])
                    j = jcast('int', i)
                    while (j <= jcast('int', jadd(n, 1))):
                        ((_java_obj_3 := Code04_FindMaxWeighing.mat[i]), (_java_key_4 := j), jset(_java_obj_3, _java_key_4, jdiv(jget(_java_obj_3, _java_key_4), tmp)))[2]
                        j = jcast('int', (j + 1))
                    j = jcast('int', 1)
                    while (j <= n):
                        if (i != j):
                            rate = jcast('double', jdiv(Code04_FindMaxWeighing.mat[j][i], Code04_FindMaxWeighing.mat[i][i]))
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_5 := Code04_FindMaxWeighing.mat[j]), (_java_key_6 := k), jset(_java_obj_5, _java_key_6, (jget(_java_obj_5, _java_key_6) - (Code04_FindMaxWeighing.mat[i][k] * rate))))[2]
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code04_FindMaxWeighing.mat[a]
        Code04_FindMaxWeighing.mat[a] = Code04_FindMaxWeighing.mat[b]
        Code04_FindMaxWeighing.mat[b] = tmp

    # 如果计算结果不是合法方案返回0
    # 如果计算结果是合法方案返回最重三角形的编号
    @staticmethod
    def check():
        Code04_FindMaxWeighing.gauss(Code04_FindMaxWeighing.n)
        maxv = jcast('double', jget(Double, 'MIN_VALUE'))
        maxt = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_FindMaxWeighing.n):
            if (Code04_FindMaxWeighing.mat[i][i] == 0):
                return jcast('int', 0)
            if ((Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))] <= 0) or (Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))] != jcast('int', Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))]))):
                return jcast('int', 0)
            if (maxv < Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))]):
                maxv = jcast('double', Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))])
                maxt = jcast('int', 1)
                ans = jcast('int', i)
            else:
                if (maxv == Code04_FindMaxWeighing.mat[i][jcast('int', jadd(Code04_FindMaxWeighing.n, 1))]):
                    maxt = jcast('int', (maxt + 1))
            i = jcast('int', (i + 1))
        if (maxt > 1):
            return jcast('int', 0)
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code04_FindMaxWeighing.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        m = 0
        while (i <= jcast('int', jadd(Code04_FindMaxWeighing.n, 1))):
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            j = jcast('int', 1)
            cur = 0
            while (j <= m):
                jcall(in_, 'nextToken')
                cur = jcast('int', jcast('int', jget(in_, 'nval')))
                jset(Code04_FindMaxWeighing.data[i], cur, 1)
                j = jcast('int', (j + 1))
            jcall(in_, 'nextToken')
            jset(Code04_FindMaxWeighing.data[i], jcast('int', jadd(Code04_FindMaxWeighing.n, 1)), jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        times = jcast('int', 0)
        k = jcast('int', 1)
        while (k <= jcast('int', jadd(Code04_FindMaxWeighing.n, 1))):
            Code04_FindMaxWeighing.swapData(k, jcast('int', jadd(Code04_FindMaxWeighing.n, 1)))
            i = jcast('int', 1)
            while (i <= Code04_FindMaxWeighing.n):
                j = jcast('int', 1)
                while (j <= jcast('int', jadd(Code04_FindMaxWeighing.n, 1))):
                    jset(Code04_FindMaxWeighing.mat[i], j, Code04_FindMaxWeighing.data[i][j])
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            Code04_FindMaxWeighing.swapData(k, jcast('int', jadd(Code04_FindMaxWeighing.n, 1)))
            cur = jcast('int', Code04_FindMaxWeighing.check())
            if (cur != 0):
                times = jcast('int', (times + 1))
                ans = jcast('int', cur)
            k = jcast('int', (k + 1))
        if (times != 1):
            jcall(out, 'println', 'illegal')
        else:
            jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def swapData(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code04_FindMaxWeighing.data[i]
        Code04_FindMaxWeighing.data[i] = Code04_FindMaxWeighing.data[j]
        Code04_FindMaxWeighing.data[j] = tmp

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FindMaxWeighing.MAXN = jcast('int', 102)
Code04_FindMaxWeighing.data = jarray('int', [Code04_FindMaxWeighing.MAXN, Code04_FindMaxWeighing.MAXN])
Code04_FindMaxWeighing.mat = jarray('double', [Code04_FindMaxWeighing.MAXN, Code04_FindMaxWeighing.MAXN])
Code04_FindMaxWeighing.n = jcast('int', 0)
Code04_FindMaxWeighing.sml = jcast('double', 1e-07)

if __name__ == '__main__':
    Code04_FindMaxWeighing.main([])

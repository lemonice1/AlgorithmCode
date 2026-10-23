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

# 球形空间的中心点
# 如果在n维空间中，那么表达一个点的位置，需要n个坐标的值
# 现在给定n+1个点，每个点都有n个坐标的值，代表在n维空间中的位置
# 假设这n+1个点都在n维空间的球面上，请返回球心的位置
# 球心的位置当然也是n个坐标的值，打印出来
# 在n维空间中，计算任意两点的距离，请用经典的欧式距离
# 1 <= n <= 10
# 坐标信息精确到小数点后6位，绝对值都不超过20000
# 测试链接 : https://www.luogu.com.cn/problem/P4035
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_SphereCenter:
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
                        if ((j < i) and (jstatic('Math', 'abs', Code03_SphereCenter.mat[j][j]) >= Code03_SphereCenter.sml)):
                            raise JContinue(None)
                        if (jstatic('Math', 'abs', Code03_SphereCenter.mat[j][i]) > jstatic('Math', 'abs', Code03_SphereCenter.mat[max][i])):
                            max = jcast('int', j)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                Code03_SphereCenter.swap(i, max)
                if (jstatic('Math', 'abs', Code03_SphereCenter.mat[i][i]) >= Code03_SphereCenter.sml):
                    tmp = jcast('double', Code03_SphereCenter.mat[i][i])
                    j = jcast('int', i)
                    while (j <= jcast('int', jadd(n, 1))):
                        ((_java_obj_3 := Code03_SphereCenter.mat[i]), (_java_key_4 := j), jset(_java_obj_3, _java_key_4, jdiv(jget(_java_obj_3, _java_key_4), tmp)))[2]
                        j = jcast('int', (j + 1))
                    j = jcast('int', 1)
                    while (j <= n):
                        if (i != j):
                            rate = jcast('double', jdiv(Code03_SphereCenter.mat[j][i], Code03_SphereCenter.mat[i][i]))
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_5 := Code03_SphereCenter.mat[j]), (_java_key_6 := k), jset(_java_obj_5, _java_key_6, (jget(_java_obj_5, _java_key_6) - (Code03_SphereCenter.mat[i][k] * rate))))[2]
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
        tmp = Code03_SphereCenter.mat[a]
        Code03_SphereCenter.mat[a] = Code03_SphereCenter.mat[b]
        Code03_SphereCenter.mat[b] = tmp

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_SphereCenter.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= jcast('int', jadd(Code03_SphereCenter.n, 1))):
            j = jcast('int', 1)
            while (j <= Code03_SphereCenter.n):
                jcall(in_, 'nextToken')
                jset(Code03_SphereCenter.data[i], j, jcast('double', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SphereCenter.n):
            j = jcast('int', 1)
            while (j <= Code03_SphereCenter.n):
                jset(Code03_SphereCenter.mat[i], j, (2 * (Code03_SphereCenter.data[i][j] - Code03_SphereCenter.data[jcast('int', jadd(i, 1))][j])))
                ((_java_obj_7 := Code03_SphereCenter.mat[i]), (_java_key_8 := jcast('int', jadd(Code03_SphereCenter.n, 1))), jset(_java_obj_7, _java_key_8, jadd(jget(_java_obj_7, _java_key_8), ((Code03_SphereCenter.data[i][j] * Code03_SphereCenter.data[i][j]) - (Code03_SphereCenter.data[jcast('int', jadd(i, 1))][j] * Code03_SphereCenter.data[jcast('int', jadd(i, 1))][j])))))[2]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        Code03_SphereCenter.gauss(Code03_SphereCenter.n)
        i = jcast('int', 1)
        while (i <= Code03_SphereCenter.n):
            jcall(out, 'printf', '%.3f ', Code03_SphereCenter.mat[i][jcast('int', jadd(Code03_SphereCenter.n, 1))])
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SphereCenter.MAXN = jcast('int', 12)
Code03_SphereCenter.data = jarray('double', [Code03_SphereCenter.MAXN, Code03_SphereCenter.MAXN])
Code03_SphereCenter.mat = jarray('double', [Code03_SphereCenter.MAXN, Code03_SphereCenter.MAXN])
Code03_SphereCenter.n = jcast('int', 0)
Code03_SphereCenter.sml = jcast('double', 1e-07)

if __name__ == '__main__':
    Code03_SphereCenter.main([])

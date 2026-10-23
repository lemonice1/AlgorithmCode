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

# 装备购买
# 一共有n个物品，每个物品都有m个属性值
# 下面定义什么是不必要的物品：如果已经选择了k个物品，此时又有一件当前物品
# 如果给已经选择的物品分配一组相乘的系数，并把属性值相加，就能得到当前物品
# 那么就说当前物品是不必要的，比如下面的例子
# a = { 4, 6, 2 }, b = { 2, 8, 4 }, c = { 6, 19, 9 }
# a * 0.5 + b * 2 = c，那么c物品是不必要的
# 每个物品都有价格，现在希望尽量多的购买物品，但不能出现不必要的物品
# 返回最多能买几件物品和最少的花费
# 1 <= n、m <= 500
# 0 <= 属性值 <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/P3265
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_BuyEquipment:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'sml': 'sml', 'mat': 'mat', 'basis': 'basis', 'n': 'n', 'm': 'm', 'cnt': 'cnt', 'cost': 'cost'}
    MAXN = 0
    MAXM = 0
    sml = 0.0
    mat = None
    # 记录的是物品编号
    basis = None
    n = 0
    m = 0
    cnt = 0
    cost = 0
    @staticmethod
    def compute():
        Code01_BuyEquipment.cnt = jcast('int', jset(Code01_BuyEquipment, 'cost', 0))
        jstatic('Arrays', 'sort', Code01_BuyEquipment.mat, 1, jcast('int', jadd(Code01_BuyEquipment.n, 1)), (lambda a, b: (jcast('int', (-1)) if (a[jcast('int', jadd(Code01_BuyEquipment.m, 1))] <= b[jcast('int', jadd(Code01_BuyEquipment.m, 1))]) else 1)))
        i = jcast('int', 1)
        while (i <= Code01_BuyEquipment.n):
            if Code01_BuyEquipment.insert(i):
                Code01_BuyEquipment.cnt = jcast('int', (Code01_BuyEquipment.cnt + 1))
                Code01_BuyEquipment.cost = jcast('int', jcast('int', jadd(Code01_BuyEquipment.cost, jcast('int', Code01_BuyEquipment.mat[i][jcast('int', jadd(Code01_BuyEquipment.m, 1))]))))
            i = jcast('int', (i + 1))

    @staticmethod
    def insert(i):
        i = jcast('int', i)
        j = jcast('int', 1)
        while (j <= Code01_BuyEquipment.m):
            if (jstatic('Math', 'abs', Code01_BuyEquipment.mat[i][j]) >= Code01_BuyEquipment.sml):
                if (Code01_BuyEquipment.basis[j] == 0):
                    Code01_BuyEquipment.basis[j] = jcast('int', i)
                    return jcast('boolean', True)
                rate = jcast('double', jdiv(Code01_BuyEquipment.mat[i][j], Code01_BuyEquipment.mat[Code01_BuyEquipment.basis[j]][j]))
                k = jcast('int', j)
                while (k <= Code01_BuyEquipment.m):
                    ((_java_obj_1 := Code01_BuyEquipment.mat[i]), (_java_key_2 := k), jset(_java_obj_1, _java_key_2, (jget(_java_obj_1, _java_key_2) - (rate * Code01_BuyEquipment.mat[Code01_BuyEquipment.basis[j]][k]))))[2]
                    k = jcast('int', (k + 1))
            j = jcast('int', (j + 1))
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_BuyEquipment.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_BuyEquipment.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_BuyEquipment.n):
            j = jcast('int', 1)
            while (j <= Code01_BuyEquipment.m):
                jcall(in_, 'nextToken')
                jset(Code01_BuyEquipment.mat[i], j, jcast('double', jget(in_, 'nval')))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_BuyEquipment.n):
            jcall(in_, 'nextToken')
            jset(Code01_BuyEquipment.mat[i], jcast('int', jadd(Code01_BuyEquipment.m, 1)), jcast('double', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_BuyEquipment.compute()
        jcall(out, 'println', jadd(jadd(Code01_BuyEquipment.cnt, ' '), Code01_BuyEquipment.cost))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_BuyEquipment.MAXN = jcast('int', 502)
Code01_BuyEquipment.MAXM = jcast('int', 502)
Code01_BuyEquipment.sml = jcast('double', 1e-05)
Code01_BuyEquipment.mat = jarray('double', [Code01_BuyEquipment.MAXN, Code01_BuyEquipment.MAXM])
Code01_BuyEquipment.basis = jarray('int', [Code01_BuyEquipment.MAXN])
Code01_BuyEquipment.n = jcast('int', 0)
Code01_BuyEquipment.m = jcast('int', 0)
Code01_BuyEquipment.cnt = jcast('int', 0)
Code01_BuyEquipment.cost = jcast('int', 0)

if __name__ == '__main__':
    Code01_BuyEquipment.main([])

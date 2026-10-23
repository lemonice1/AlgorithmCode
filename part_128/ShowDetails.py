# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课上讲述高斯消元解决同余方程组的例子
class ShowDetails:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'mat': 'mat', 'inv': 'inv_data'}
    # 题目会保证取模的数字为质数
    MOD = 0
    MAXN = 0
    mat = None
    # 逆元线性递推公式求逆元表，讲解099 - 除法同余
    inv_data = None
    @staticmethod
    def inv():
        ShowDetails.inv_data[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i < ShowDetails.MOD):
            ShowDetails.inv_data[i] = jcast('int', jcast('int', jcast('long', (ShowDetails.MOD - jcast('long', jmod(jcast('long', (jcast('long', ShowDetails.inv_data[jcast('int', jmod(ShowDetails.MOD, i))]) * jcast('int', jdiv(ShowDetails.MOD, i)))), ShowDetails.MOD))))))
            i = jcast('int', (i + 1))

    # 求a和b的最大公约数，保证a和b都不等于0
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else ShowDetails.gcd(b, jcast('int', jmod(a, b)))))

    # 高斯消元解决同余方程组模版，保证初始系数没有负数
    # ((系数 % MOD) + MOD) % MOD
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        # 已经成为主元的行不参与
                        if ((j < i) and (ShowDetails.mat[j][j] != 0)):
                            raise JContinue(None)
                        # 找到系数不等于0的行做主元即可
                        if (ShowDetails.mat[j][i] != 0):
                            ShowDetails.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (ShowDetails.mat[i][i] != 0):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (ShowDetails.mat[j][i] != 0)):
                            gcd = jcast('int', ShowDetails.gcd(ShowDetails.mat[j][i], ShowDetails.mat[i][i]))
                            a = jcast('int', jcast('int', jdiv(ShowDetails.mat[i][i], gcd)))
                            b = jcast('int', jcast('int', jdiv(ShowDetails.mat[j][i], gcd)))
                            if ((j < i) and (ShowDetails.mat[j][j] != 0)):
                                # 如果j行有主元，那么从j列到i-1列的所有系数 * a
                                # 正确更新主元和自由元之间的关系
                                k = jcast('int', j)
                                while (k < i):
                                    jset(ShowDetails.mat[j], k, jcast('int', jmod(jcast('int', (ShowDetails.mat[j][k] * a)), ShowDetails.MOD)))
                                    k = jcast('int', (k + 1))
                            # 正常消元
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                jset(ShowDetails.mat[j], k, jcast('int', jmod(jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', (ShowDetails.mat[j][k] * a)) - jcast('int', (ShowDetails.mat[i][k] * b)))), ShowDetails.MOD)), ShowDetails.MOD)), ShowDetails.MOD)))
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
        i = jcast('int', 1)
        while (i <= n):
            try:
                if (ShowDetails.mat[i][i] != 0):
                    # 检查当前主元是否被若干自由元影响
                    # 如果当前主元不受自由元影响，那么可以确定当前主元的值
                    # 否则保留这种影响，正确显示主元和自由元的关系
                    flag = jcast('boolean', False)
                    j = jcast('int', jcast('int', jadd(i, 1)))
                    while (j <= n):
                        try:
                            if (ShowDetails.mat[i][j] != 0):
                                flag = jcast('boolean', True)
                                raise JBreak(None)
                        except JContinue as _java_control_4:
                            if _java_control_4.label not in (None,):
                                raise
                        except JBreak as _java_control_4:
                            if _java_control_4.label not in (None,):
                                raise
                            break
                        j = jcast('int', (j + 1))
                    if (not flag):
                        # 本来应该是，mat[i][n + 1] = mat[i][n + 1] / mat[i][i]
                        # 但是在模意义下应该求逆元，(a / b) % MOD = (a * b的逆元) % MOD
                        # 如果不会，去看讲解099 - 除法同余
                        jset(ShowDetails.mat[i], jcast('int', jadd(n, 1)), jcast('int', jmod(jcast('int', (ShowDetails.mat[i][jcast('int', jadd(n, 1))] * ShowDetails.inv_data[ShowDetails.mat[i][i]])), ShowDetails.MOD)))
                        jset(ShowDetails.mat[i], i, 1)
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = ShowDetails.mat[a]
        ShowDetails.mat[a] = ShowDetails.mat[b]
        ShowDetails.mat[b] = tmp

    @staticmethod
    def print(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(n, 1))):
                jprint(jadd(ShowDetails.mat[i][j], ' '), newline=False)
                j = jcast('int', (j + 1))
            jprint(newline=True)
            i = jcast('int', (i + 1))
        jprint('========================', newline=True)

    @staticmethod
    def main(args):
        # 逆元表建立好
        ShowDetails.inv()
        jprint('课上图解的例子，唯一解', newline=True)
        # 4*x1 + 2*x2 + 4*x3 同余 3
        # 2*x1 + 5*x2 + 2*x3 同余 2
        # 6*x1 + 3*x2 + 4*x3 同余 5
        jset(ShowDetails.mat[1], 1, 4)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, 4)
        jset(ShowDetails.mat[1], 4, 3)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 5)
        jset(ShowDetails.mat[2], 3, 2)
        jset(ShowDetails.mat[2], 4, 2)
        jset(ShowDetails.mat[3], 1, 6)
        jset(ShowDetails.mat[3], 2, 3)
        jset(ShowDetails.mat[3], 3, 4)
        jset(ShowDetails.mat[3], 4, 5)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('表达式存在矛盾的例子', newline=True)
        # 1*x1 + 2*x2 + 3*x3 同余 2
        # 2*x1 + 4*x2 + 6*x3 同余 5
        # 0*x1 + 3*x2 + 4*x3 同余 2
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, 3)
        jset(ShowDetails.mat[1], 4, 2)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, 6)
        jset(ShowDetails.mat[2], 4, 5)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 3)
        jset(ShowDetails.mat[3], 3, 4)
        jset(ShowDetails.mat[3], 4, 2)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('课上图解的例子，多解', newline=True)
        jprint('只有确定了自由元，才能确定主元的值', newline=True)
        jprint('如果是多解的情况，那么在消元结束后', newline=True)
        jprint('二维矩阵中主元和自由元的关系是正确的', newline=True)
        jprint('课上也进行了验证', newline=True)
        # 1*x1 + 2*x2 + 3*x3 同余 2
        # 2*x1 + 4*x2 + 6*x3 同余 4
        # 0*x1 + 3*x2 + 4*x3 同余 2
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 2)
        jset(ShowDetails.mat[1], 3, 3)
        jset(ShowDetails.mat[1], 4, 2)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 4)
        jset(ShowDetails.mat[2], 3, 6)
        jset(ShowDetails.mat[2], 4, 4)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 3)
        jset(ShowDetails.mat[3], 3, 4)
        jset(ShowDetails.mat[3], 4, 2)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('注意下面这个多解的例子', newline=True)
        # 1*x1 + 1*x2 + 1*x3 同余 3
        # 2*x1 + 1*x2 + 1*x3 同余 5
        # 0*x1 + 3*x2 + 3*x3 同余 3
        jset(ShowDetails.mat[1], 1, 1)
        jset(ShowDetails.mat[1], 2, 1)
        jset(ShowDetails.mat[1], 3, 1)
        jset(ShowDetails.mat[1], 4, 3)
        jset(ShowDetails.mat[2], 1, 2)
        jset(ShowDetails.mat[2], 2, 1)
        jset(ShowDetails.mat[2], 3, 1)
        jset(ShowDetails.mat[2], 4, 5)
        jset(ShowDetails.mat[3], 1, 0)
        jset(ShowDetails.mat[3], 2, 3)
        jset(ShowDetails.mat[3], 3, 3)
        jset(ShowDetails.mat[3], 4, 3)
        ShowDetails.gauss(3)
        ShowDetails.print(3)
        jprint('最后一个例子里', newline=True)
        jprint('主元x1，不受其他自由元影响，值可以直接确定', newline=True)
        jprint('但是主元x2，受到自由元x3的影响，6*x2 + 6*x3 同余 6', newline=True)
        jprint('只有自由元x3确定了值，主元x2的值才能确定', newline=True)
        jprint('本节课提供的模版，对于能求出的主元可以得到正确结果', newline=True)
        jprint('对于不能求出的主元，该模版也能给出，主元和自由元的正确关系', newline=True)
        jprint('有些题目需要这种多解情况下，主元和自由元之间的正确关系', newline=True)
        jprint('绝大多数模版和讲解都没有考虑这个，但值得引起重视', newline=True)
        jprint('如果有些题目不需要这种正确关系', newline=True)
        jprint('那么逻辑可以化简，让常数时间更快，比如本节课的题目1', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetails.MOD = jcast('int', 7)
ShowDetails.MAXN = jcast('int', 101)
ShowDetails.mat = jarray('int', [ShowDetails.MAXN, ShowDetails.MAXN])
ShowDetails.inv_data = jarray('int', [ShowDetails.MOD])

if __name__ == '__main__':
    ShowDetails.main([])

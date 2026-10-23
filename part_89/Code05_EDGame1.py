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

# 计算两堆石子的SG值
# 桌上有两堆石子，石头数量分别为a、b
# 任取一堆石子，将其移走，然后分割同一组的另一堆石子
# 从中取出若干个石子放在被移走的位置，组成新的一堆
# 操作完成后，组内每堆的石子数必须保证大于0
# 显然，被分割的一堆的石子数至少要为2
# 两个人轮流进行分割操作，如果轮到某人进行操作时，两堆石子数均为1，判此人输掉比赛
# 计算sg[a][b]的值并找到简洁规律
# 本文件仅为题目5打表找规律的代码
class Code05_EDGame1:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp'}
    MAXN = 0
    dp = None
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i < Code05_EDGame1.MAXN):
            j = jcast('int', 0)
            while (j < Code05_EDGame1.MAXN):
                jset(Code05_EDGame1.dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def sg(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if ((a == 1) and (b == 1)):
            return jcast('int', 0)
        if (Code05_EDGame1.dp[a][b] != jcast('int', (-1))):
            return jcast('int', Code05_EDGame1.dp[a][b])
        appear = jarray('boolean', [jcast('int', jadd(jstatic('Math', 'max', a, b), 1))])
        if (a > 1):
            l = jcast('int', 1)
            r = jcast('int', jcast('int', (a - 1)))
            while (l < a):
                jset(appear, Code05_EDGame1.sg(l, r), True)
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
        if (b > 1):
            l = jcast('int', 1)
            r = jcast('int', jcast('int', (b - 1)))
            while (l < b):
                jset(appear, Code05_EDGame1.sg(l, r), True)
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
        ans = jcast('int', 0)
        s = jcast('int', 0)
        while (s <= jstatic('Math', 'max', a, b)):
            try:
                if (not appear[s]):
                    ans = jcast('int', s)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            s = jcast('int', (s + 1))
        jset(Code05_EDGame1.dp[a], b, ans)
        return jcast('int', ans)

    @staticmethod
    def f1():
        jprint('石子数9以内所有组合的sg值', newline=True)
        jprint(newline=True)
        jprint('    ', newline=False)
        i = jcast('int', 1)
        while (i <= 9):
            jprint(jadd(i, ' '), newline=False)
            i = jcast('int', (i + 1))
        jprint(newline=True)
        jprint(newline=True)
        a = jcast('int', 1)
        while (a <= 9):
            jprint(jadd(a, '   '), newline=False)
            b = jcast('int', 1)
            while (b < a):
                jprint('X ', newline=False)
                b = jcast('int', (b + 1))
            b = jcast('int', a)
            while (b <= 9):
                sg = jcast('int', Code05_EDGame1.sg(a, b))
                jprint(jadd(sg, ' '), newline=False)
                b = jcast('int', (b + 1))
            jprint(newline=True)
            a = jcast('int', (a + 1))

    @staticmethod
    def f2():
        jprint('石子数9以内所有组合的sg值，但是行列都-1', newline=True)
        jprint(newline=True)
        jprint('    ', newline=False)
        i = jcast('int', 0)
        while (i <= 8):
            jprint(jadd(i, ' '), newline=False)
            i = jcast('int', (i + 1))
        jprint(newline=True)
        jprint(newline=True)
        a = jcast('int', 1)
        while (a <= 9):
            jprint(jadd(jcast('int', (a - 1)), '   '), newline=False)
            b = jcast('int', 1)
            while (b < a):
                jprint('X ', newline=False)
                b = jcast('int', (b + 1))
            b = jcast('int', a)
            while (b <= 9):
                sg = jcast('int', Code05_EDGame1.sg(a, b))
                jprint(jadd(sg, ' '), newline=False)
                b = jcast('int', (b + 1))
            jprint(newline=True)
            a = jcast('int', (a + 1))

    @staticmethod
    def f3():
        jprint('测试开始', newline=True)
        a = jcast('int', 1)
        while (a < Code05_EDGame1.MAXN):
            b = jcast('int', 1)
            while (b < Code05_EDGame1.MAXN):
                sg1 = jcast('int', Code05_EDGame1.sg(a, b))
                sg2 = jcast('int', Code05_EDGame1.lowZero(jcast('int', (jcast('int', (a - 1)) | jcast('int', (b - 1))))))
                if (sg1 != sg2):
                    jprint('出错了!', newline=True)
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        jprint('测试结束', newline=True)

    # 返回status最低位的0在第几位
    @staticmethod
    def lowZero(status):
        status = jcast('int', status)
        cnt = jcast('int', 0)
        while (status > 0):
            try:
                if (jcast('int', (status & 1)) == 0):
                    raise JBreak(None)
                status = jcast('int', jcast('int', (status >> (1 & 31))))
                cnt = jcast('int', (cnt + 1))
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
        return jcast('int', cnt)

    @staticmethod
    def main(args):
        Code05_EDGame1.build()
        Code05_EDGame1.f1()
        jprint(newline=True)
        jprint(newline=True)
        Code05_EDGame1.f2()
        jprint(newline=True)
        jprint(newline=True)
        Code05_EDGame1.f3()

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_EDGame1.MAXN = jcast('int', 1001)
Code05_EDGame1.dp = jarray('int', [Code05_EDGame1.MAXN, Code05_EDGame1.MAXN])

if __name__ == '__main__':
    Code05_EDGame1.main([])

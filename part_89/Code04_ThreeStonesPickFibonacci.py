# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 三堆石头拿取斐波那契数博弈
# 有三堆石头，数量分别为a、b、c
# 两个人轮流拿，每次可以选择其中一堆石头，拿取斐波那契数的石头
# 拿到最后一颗石子的人获胜，根据a、b、c返回谁赢
# 来自真实大厂笔试，每堆石子的数量在10^5以内
# 没有在线测试，对数器验证
class Code04_ThreeStonesPickFibonacci:
    __java_fields__ = {'MAXN': 'MAXN', 'f': 'f', 'dp': 'dp', 'sg': 'sg', 'appear': 'appear'}
    # 如果MAXN变大
    # 相应的要修改f数组
    MAXN = 0
    # MAXN以内的斐波那契数
    f = None
    dp = None
    # 动态规划方法彻底尝试
    # 为了验证
    @staticmethod
    def win1(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        # 假设当前的先手来行动
        # 注意不是全局的先手，是当前的先手来行动！
        # 当前！当前！当前！
        if (jcast('int', jadd(jcast('int', jadd(a, b)), c)) == 0):
            # 当前的先手，面对这个局面
            # 返回当前的后手赢
            return '后手'
        if (Code04_ThreeStonesPickFibonacci.dp[a][b][c] != None):
            return Code04_ThreeStonesPickFibonacci.dp[a][b][c]
        # ans : 赢的是当前的先手，还是当前的后手
        ans = '后手'
        i = jcast('int', 0)
        while (i < jget(Code04_ThreeStonesPickFibonacci.f, 'length')):
            try:
                if (Code04_ThreeStonesPickFibonacci.f[i] <= a):
                    if jcall(Code04_ThreeStonesPickFibonacci.win1(jcast('int', (a - Code04_ThreeStonesPickFibonacci.f[i])), b, c), 'equals', '后手'):
                        # 后续过程的赢家是后续过程的后手
                        # 那就表示当前的先手，通过这个后续过程，能赢
                        ans = '先手'
                        raise JBreak(None)
                if (Code04_ThreeStonesPickFibonacci.f[i] <= b):
                    if jcall(Code04_ThreeStonesPickFibonacci.win1(a, jcast('int', (b - Code04_ThreeStonesPickFibonacci.f[i])), c), 'equals', '后手'):
                        # 后续过程的赢家是后续过程的后手
                        # 那就表示当前的先手，通过这个后续过程，能赢
                        ans = '先手'
                        raise JBreak(None)
                if (Code04_ThreeStonesPickFibonacci.f[i] <= c):
                    if jcall(Code04_ThreeStonesPickFibonacci.win1(a, b, jcast('int', (c - Code04_ThreeStonesPickFibonacci.f[i]))), 'equals', '后手'):
                        # 后续过程的赢家是后续过程的后手
                        # 那就表示当前的先手，通过这个后续过程，能赢
                        ans = '先手'
                        raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jset(Code04_ThreeStonesPickFibonacci.dp[a][b], c, ans)
        return ans

    # sg定理
    sg = None
    appear = None
    # O(10^5 * 24 * 2)
    @staticmethod
    def build():
        i = jcast('int', 1)
        while (i < Code04_ThreeStonesPickFibonacci.MAXN):
            try:
                jstatic('Arrays', 'fill', Code04_ThreeStonesPickFibonacci.appear, False)
                j = jcast('int', 0)
                while ((j < jget(Code04_ThreeStonesPickFibonacci.f, 'length')) and (jcast('int', (i - Code04_ThreeStonesPickFibonacci.f[j])) >= 0)):
                    jset(Code04_ThreeStonesPickFibonacci.appear, Code04_ThreeStonesPickFibonacci.sg[jcast('int', (i - Code04_ThreeStonesPickFibonacci.f[j]))], True)
                    j = jcast('int', (j + 1))
                s = jcast('int', 0)
                while (s < Code04_ThreeStonesPickFibonacci.MAXN):
                    try:
                        if (not Code04_ThreeStonesPickFibonacci.appear[s]):
                            Code04_ThreeStonesPickFibonacci.sg[i] = jcast('int', s)
                            raise JBreak(None)
                    except JContinue as _java_control_3:
                        if _java_control_3.label not in (None,):
                            raise
                    except JBreak as _java_control_3:
                        if _java_control_3.label not in (None,):
                            raise
                        break
                    s = jcast('int', (s + 1))
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def win2(a, b, c):
        a = jcast('int', a)
        b = jcast('int', b)
        c = jcast('int', c)
        return ('先手' if (jcast('int', (jcast('int', (Code04_ThreeStonesPickFibonacci.sg[a] ^ Code04_ThreeStonesPickFibonacci.sg[b])) ^ Code04_ThreeStonesPickFibonacci.sg[c])) != 0) else '后手')

    @staticmethod
    def main(args):
        Code04_ThreeStonesPickFibonacci.build()
        jprint('测试开始', newline=True)
        a = jcast('int', 0)
        while (a < Code04_ThreeStonesPickFibonacci.MAXN):
            b = jcast('int', 0)
            while (b < Code04_ThreeStonesPickFibonacci.MAXN):
                c = jcast('int', 0)
                while (c < Code04_ThreeStonesPickFibonacci.MAXN):
                    ans1 = Code04_ThreeStonesPickFibonacci.win1(a, b, c)
                    ans2 = Code04_ThreeStonesPickFibonacci.win2(a, b, c)
                    if (not jcall(ans1, 'equals', ans2)):
                        jprint('出错了！', newline=True)
                    c = jcast('int', (c + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        jprint('测试结束', newline=True)
        # 试图找到简洁规律，想通过O(1)的过程就得到sg(x)
        # 于是打印200以内的sg值，开始观察
        # 刚开始有规律，但是在sg(138)之后开始发生异常波动
        # 原题数据规模下可以比较不同复杂度的方案，O(1) 优化可进一步减少开销
        # 那就用build方法计算sg值，不再找寻简洁规律
        # 考试时一切根据题目数据量来决定是否继续优化
        i = jcast('int', 0)
        while (i < Code04_ThreeStonesPickFibonacci.MAXN):
            jprint(jadd(jadd(jadd('sg(', i), ') : '), Code04_ThreeStonesPickFibonacci.sg[i]), newline=True)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ThreeStonesPickFibonacci.MAXN = jcast('int', 201)
Code04_ThreeStonesPickFibonacci.f = jarray('int', [None], [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
Code04_ThreeStonesPickFibonacci.dp = jarray('String', [Code04_ThreeStonesPickFibonacci.MAXN, Code04_ThreeStonesPickFibonacci.MAXN, Code04_ThreeStonesPickFibonacci.MAXN])
Code04_ThreeStonesPickFibonacci.sg = jarray('int', [Code04_ThreeStonesPickFibonacci.MAXN])
Code04_ThreeStonesPickFibonacci.appear = jarray('boolean', [Code04_ThreeStonesPickFibonacci.MAXN])

if __name__ == '__main__':
    Code04_ThreeStonesPickFibonacci.main([])

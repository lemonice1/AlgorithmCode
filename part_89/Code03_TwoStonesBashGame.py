# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 两堆石头的巴什博弈
# 有两堆石头，数量分别为a、b
# 两个人轮流拿，每次可以选择其中一堆石头，拿1~m颗
# 拿到最后一颗石子的人获胜，根据a、b、m返回谁赢
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code03_TwoStonesBashGame:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp'}
    MAXN = 0
    dp = None
    # 动态规划方法彻底尝试
    # 为了验证
    @staticmethod
    def win1(a, b, m):
        a = jcast('int', a)
        b = jcast('int', b)
        m = jcast('int', m)
        if (m >= jstatic('Math', 'max', a, b)):
            return ('先手' if (a != b) else '后手')
        if (a == b):
            return '后手'
        if (Code03_TwoStonesBashGame.dp[a][b][m] != None):
            return Code03_TwoStonesBashGame.dp[a][b][m]
        ans = '后手'
        pick = jcast('int', 1)
        while (pick <= jstatic('Math', 'min', a, m)):
            try:
                if jcall(Code03_TwoStonesBashGame.win1(jcast('int', (a - pick)), b, m), 'equals', '后手'):
                    # 后续过程的赢家是后续过程的后手
                    # 那就表示此时的先手，通过这个后续过程，能赢
                    ans = '先手'
                if jcall(ans, 'equals', '先手'):
                    # 后续过程的赢家是后续过程的后手
                    # 那就表示此时的先手，通过这个后续过程，能赢
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            pick = jcast('int', (pick + 1))
        pick = jcast('int', 1)
        while (pick <= jstatic('Math', 'min', b, m)):
            try:
                if jcall(Code03_TwoStonesBashGame.win1(a, jcast('int', (b - pick)), m), 'equals', '后手'):
                    # 后续过程的赢家是后续过程的后手
                    # 那就表示此时的先手，通过这个后续过程，能赢
                    ans = '先手'
                if jcall(ans, 'equals', '先手'):
                    raise JBreak(None)
            except JContinue as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
            except JBreak as _java_control_2:
                if _java_control_2.label not in (None,):
                    raise
                break
            pick = jcast('int', (pick + 1))
        jset(Code03_TwoStonesBashGame.dp[a][b], m, ans)
        return ans

    # sg定理
    @staticmethod
    def win2(a, b, m):
        a = jcast('int', a)
        b = jcast('int', b)
        m = jcast('int', m)
        n = jcast('int', jstatic('Math', 'max', a, b))
        sg = jarray('int', [jcast('int', jadd(n, 1))])
        appear = jarray('boolean', [jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            try:
                jstatic('Arrays', 'fill', appear, False)
                j = jcast('int', 1)
                while ((j <= m) and (jcast('int', (i - j)) >= 0)):
                    jset(appear, sg[jcast('int', (i - j))], True)
                    j = jcast('int', (j + 1))
                s = jcast('int', 0)
                while (s <= m):
                    try:
                        if (not appear[s]):
                            sg[i] = jcast('int', s)
                            raise JBreak(None)
                    except JContinue as _java_control_4:
                        if _java_control_4.label not in (None,):
                            raise
                    except JBreak as _java_control_4:
                        if _java_control_4.label not in (None,):
                            raise
                        break
                    s = jcast('int', (s + 1))
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        return ('先手' if (jcast('int', (sg[a] ^ sg[b])) != 0) else '后手')

    # 时间复杂度O(1)的最优解
    # 其实是根据方法2中的sg表观察出来的
    @staticmethod
    def win3(a, b, m):
        a = jcast('int', a)
        b = jcast('int', b)
        m = jcast('int', m)
        return ('先手' if (jcast('int', jmod(a, jcast('int', jadd(m, 1)))) != jcast('int', jmod(b, jcast('int', jadd(m, 1))))) else '后手')

    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        a = jcast('int', 0)
        while (a < Code03_TwoStonesBashGame.MAXN):
            b = jcast('int', 0)
            while (b < Code03_TwoStonesBashGame.MAXN):
                m = jcast('int', 1)
                while (m < Code03_TwoStonesBashGame.MAXN):
                    ans1 = Code03_TwoStonesBashGame.win1(a, b, m)
                    ans2 = Code03_TwoStonesBashGame.win2(a, b, m)
                    ans3 = Code03_TwoStonesBashGame.win3(a, b, m)
                    if ((not jcall(ans1, 'equals', ans2)) or (not jcall(ans1, 'equals', ans3))):
                        jprint('出错了！', newline=True)
                    m = jcast('int', (m + 1))
                b = jcast('int', (b + 1))
            a = jcast('int', (a + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TwoStonesBashGame.MAXN = jcast('int', 101)
Code03_TwoStonesBashGame.dp = jarray('String', [Code03_TwoStonesBashGame.MAXN, Code03_TwoStonesBashGame.MAXN, Code03_TwoStonesBashGame.MAXN])

if __name__ == '__main__':
    Code03_TwoStonesBashGame.main([])

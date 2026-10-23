# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 巴什博弈(Bash Game)
# 一共有n颗石子，两个人轮流拿，每次可以拿1~m颗石子
# 拿到最后一颗石子的人获胜，根据n、m返回谁赢
class Code01_BashGame:
    __java_fields__ = {'MAXN': 'MAXN', 'dp': 'dp'}
    # 动态规划进行所有尝试
    # 为了验证
    MAXN = 0
    dp = None
    @staticmethod
    def bashGame1(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        if (n == 0):
            return '后手'
        if (Code01_BashGame.dp[n][m] != None):
            return Code01_BashGame.dp[n][m]
        ans = '后手'
        pick = jcast('int', 1)
        while (pick <= m):
            try:
                if jcall(Code01_BashGame.bashGame1(jcast('int', (n - pick)), m), 'equals', '后手'):
                    # 后续过程的赢家是后续过程的后手
                    # 那就表示此时的先手，通过这个后续过程，能赢
                    ans = '先手'
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            pick = jcast('int', (pick + 1))
        jset(Code01_BashGame.dp[n], m, ans)
        return ans

    # 正式方法
    @staticmethod
    def bashGame2(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        return ('先手' if (jcast('int', jmod(n, jcast('int', jadd(m, 1)))) != 0) else '后手')

    # 为了验证
    @staticmethod
    def main(args):
        # 需要比MAXN小
        V = jcast('int', 500)
        testTimes = jcast('int', 5000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            n = jcast('int', jcast('int', (jstatic('Math', 'random') * V)))
            m = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * V)), 1)))
            ans1 = Code01_BashGame.bashGame1(n, m)
            ans2 = Code01_BashGame.bashGame2(n, m)
            if (not jcall(ans1, 'equals', ans2)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_BashGame.MAXN = jcast('int', 1001)
Code01_BashGame.dp = jarray('String', [Code01_BashGame.MAXN, Code01_BashGame.MAXN])

if __name__ == '__main__':
    Code01_BashGame.main([])

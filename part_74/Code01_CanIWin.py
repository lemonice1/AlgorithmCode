# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 我能赢吗
# 给定两个整数n和m
# 两个玩家可以轮流从公共整数池中抽取从1到n的整数（不放回）
# 抽取的整数会累加起来（两个玩家都算）
# 谁在自己的回合让累加和 >= m，谁获胜
# 若先出手的玩家能稳赢则返回true，否则返回false
# 假设两位玩家游戏时都绝顶聪明，可以全盘为自己打算
# 测试链接 : https://leetcode.cn/problems/can-i-win/
class Code01_CanIWin:
    __java_fields__ = {}
    @staticmethod
    def canIWin(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        if (m == 0):
            # 来自题目规定
            return jcast('boolean', True)
        if (jcast('int', jdiv(jcast('int', (n * jcast('int', jadd(n, 1)))), 2)) < m):
            # 如果1~n数字全加起来
            # 累加和和是n * (n+1) / 2，都小于m
            # 那么不会有赢家，也就意味着先手不会获胜
            return jcast('boolean', False)
        # dp[status] == 0 代表没算过
        # dp[status] == 1 算过，答案是true
        # dp[status] == -1 算过，答案是false
        dp = jarray('int', [jcast('int', (1 << (jcast('int', jadd(n, 1)) & 31)))])
        return jcast('boolean', Code01_CanIWin.f(n, jcast('int', (jcast('int', (1 << (jcast('int', jadd(n, 1)) & 31))) - 1)), m, dp))

    # 如果1~7范围的数字都能选，那么status的状态为：
    # 1 1 1 1 1 1 1 1
    # 7 6 5 4 3 2 1 0
    # 0位弃而不用
    # 如果1~7范围的数字，4、2已经选了不能再选，那么status的状态为：
    # 1 1 1 0 1 0 1 1
    # 7 6 5 4 3 2 1 0
    # 0位弃而不用
    # f的含义 :
    # 数字范围1~n，当前的先手，面对status给定的数字状态
    # 在累加和还剩rest的情况下
    # 返回当前的先手能不能赢，能赢返回true，不能赢返回false
    @staticmethod
    def f(n, status, rest, dp):
        n = jcast('int', n)
        status = jcast('int', status)
        rest = jcast('int', rest)
        if (rest <= 0):
            return jcast('boolean', False)
        if (dp[status] != 0):
            return jcast('boolean', (dp[status] == 1))
        # rest > 0
        ans = jcast('boolean', False)
        i = jcast('int', 1)
        while (i <= n):
            try:
                # 考察所有数字，但是不能选择之前选了的数字
                if ((jcast('int', (status & jcast('int', (1 << (i & 31))))) != 0) and (not Code01_CanIWin.f(n, jcast('int', (status ^ jcast('int', (1 << (i & 31))))), jcast('int', (rest - i)), dp))):
                    ans = jcast('boolean', True)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        dp[status] = jcast('int', (1 if ans else jcast('int', (-1))))
        return jcast('boolean', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



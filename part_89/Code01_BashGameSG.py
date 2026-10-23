# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 巴什博弈(SG函数求解过程展示)
# 一共有n颗石子，两个人轮流拿，每次可以拿1~m颗石子
# 拿到最后一颗石子的人获胜，根据n、m返回谁赢
# 对数器验证
class Code01_BashGameSG:
    __java_fields__ = {}
    # 发现结论去求解，时间复杂度O(1)
    # 充分研究了性质
    @staticmethod
    def bash1(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        return ('先手' if (jcast('int', jmod(n, jcast('int', jadd(m, 1)))) != 0) else '后手')

    # sg函数去求解，时间复杂度O(n*m)
    # 不用研究性质
    # 其实把sg表打印之后，也可以发现性质，也就是打表找规律
    @staticmethod
    def bash2(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
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
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    s = jcast('int', (s + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        # print("打印 n = " + n + ", m = " + m + " 的sg表")
        # for (int i = 0; i <= n; i++) {
        # print("sg(" + i + ") : " + sg[i])
        # }
        return ('先手' if (sg[n] != 0) else '后手')

    # 为了验证
    @staticmethod
    def main(args):
        V = jcast('int', 1000)
        testTimes = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            n = jcast('int', jcast('int', (jstatic('Math', 'random') * V)))
            m = jcast('int', jcast('int', (jstatic('Math', 'random') * V)))
            ans1 = Code01_BashGameSG.bash1(n, m)
            ans2 = Code01_BashGameSG.bash2(n, m)
            if (not jcall(ans1, 'equals', ans2)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)
        n = jcast('int', 100)
        m = jcast('int', 6)
        Code01_BashGameSG.bash2(n, m)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_BashGameSG.main([])

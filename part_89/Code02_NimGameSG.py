# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 尼姆博弈(SG定理简单用法展示)
# 一共有 n 堆石头，两人轮流进行游戏
# 在每个玩家的回合中，玩家需要 选择任一 非空 石头堆，从中移除任意 非零 数量的石头
# 如果不能移除任意的石头，就输掉游戏
# 返回先手是否一定获胜
# 对数器验证
class Code02_NimGameSG:
    __java_fields__ = {}
    # 时间复杂度O(n)
    # 充分研究了性质
    @staticmethod
    def nim1(arr):
        eor = jcast('int', 0)
        for num in arr:
            eor = jcast('int', jcast('int', (eor ^ num)))
        return ('先手' if (eor != 0) else '后手')

    # sg函数去求解
    # 过程时间复杂度高，但是可以轻易发现规律，进而优化成最优解
    # 证明不好想，但是从sg表出发，去观察最终的解，要好做很多
    @staticmethod
    def nim2(arr):
        max = jcast('int', 0)
        for num in arr:
            max = jcast('int', jstatic('Math', 'max', max, num))
        sg = jarray('int', [jcast('int', jadd(max, 1))])
        appear = jarray('boolean', [jcast('int', jadd(max, 1))])
        i = jcast('int', 1)
        while (i <= max):
            try:
                jstatic('Arrays', 'fill', appear, False)
                j = jcast('int', 0)
                while (j < i):
                    appear[j] = jcast('boolean', True)
                    j = jcast('int', (j + 1))
                s = jcast('int', 0)
                while (s <= max):
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
        # 打印sg表之后，可以发现，sg[x] = x
        # 那么eor ^= sg[num] 等同于 eor ^= num
        # 从sg定理发现了最优解
        eor = jcast('int', 0)
        for num in arr:
            eor = jcast('int', jcast('int', (eor ^ sg[num])))
        return ('先手' if (eor != 0) else '后手')

    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    @staticmethod
    def main(args):
        N = jcast('int', 200)
        V = jcast('int', 1000)
        testTimes = jcast('int', 10000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            arr = Code02_NimGameSG.randomArray(n, V)
            ans1 = Code02_NimGameSG.nim1(arr)
            ans2 = Code02_NimGameSG.nim2(arr)
            if (not jcall(ans1, 'equals', ans2)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_NimGameSG.main([])

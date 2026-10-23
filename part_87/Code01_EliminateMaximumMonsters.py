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

# 消灭怪物的最大数量
# 你正在玩一款电子游戏，在游戏中你需要保护城市免受怪物侵袭
# 给定两个大小为n的整数数组dist、speed
# 其中dist[i]是第i个怪物与城市的初始距离
# 其中speed[i]是第i个怪物的速度
# 你有一种武器，一旦充满电，就可以消灭一个怪物，但是，武器需要1的时间才能充电完成
# 武器在游戏开始时是充满电的状态，怪物从0时刻开始移动，一旦任何怪物到达城市，就输掉了这场游戏
# 如果某个怪物恰好在某一分钟开始时到达城市，这也会被视为输掉游戏
# 返回在你输掉游戏前可以消灭的怪物的最大数量，如果消灭所有怪兽了返回n
# 测试链接 : https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/
class Code01_EliminateMaximumMonsters:
    __java_fields__ = {}
    @staticmethod
    def eliminateMaximum(dist, speed):
        n = jcast('int', jget(dist, 'length'))
        time = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            # a / b 向上取整 -> (a + b - 1) / b
            time[i] = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(dist[i], speed[i])) - 1)), speed[i])))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', time)
        i = jcast('int', 0)
        while (i < n):
            # 当前来到i的时刻
            if (time[i] <= i):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', n)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



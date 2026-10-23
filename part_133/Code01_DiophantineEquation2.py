# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 二元一次不定方程模版
# 给定a、b、c，求解方程ax + by = c
# 如果方程无解打印-1
# 如果方程无正整数解，但是有整数解
# 打印这些整数解中，x的最小正数值，y的最小正数值
# 如果方程有正整数解，打印正整数解的数量，同时打印所有正整数解中，
# x的最小正数值，y的最小正数值，x的最大正数值，y的最大正数值
# 1 <= a、b、c <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P5656
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DiophantineEquation2:
    __java_fields__ = {'d': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py', 'a': 'a', 'b': 'b', 'c': 'c', 'xd': 'xd', 'yd': 'yd', 'times': 'times'}
    # 扩展欧几里得算法
    d = 0
    x = 0
    y = 0
    px = 0
    py = 0
    @staticmethod
    def exgcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        if (b == 0):
            Code01_DiophantineEquation2.d = jcast('long', a)
            Code01_DiophantineEquation2.x = jcast('long', 1)
            Code01_DiophantineEquation2.y = jcast('long', 0)
        else:
            Code01_DiophantineEquation2.exgcd(b, jcast('long', jmod(a, b)))
            Code01_DiophantineEquation2.px = jcast('long', Code01_DiophantineEquation2.x)
            Code01_DiophantineEquation2.py = jcast('long', Code01_DiophantineEquation2.y)
            Code01_DiophantineEquation2.x = jcast('long', Code01_DiophantineEquation2.py)
            Code01_DiophantineEquation2.y = jcast('long', jcast('long', (Code01_DiophantineEquation2.px - jcast('long', (Code01_DiophantineEquation2.py * jcast('long', jdiv(a, b)))))))

    a = 0
    b = 0
    c = 0
    xd = 0
    yd = 0
    times = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        while (t <= cases):
            jcall(in_, 'nextToken')
            Code01_DiophantineEquation2.a = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_DiophantineEquation2.b = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code01_DiophantineEquation2.c = jcast('long', jcast('long', jget(in_, 'nval')))
            Code01_DiophantineEquation2.exgcd(Code01_DiophantineEquation2.a, Code01_DiophantineEquation2.b)
            # 无整数解
            if (jcast('long', jmod(Code01_DiophantineEquation2.c, Code01_DiophantineEquation2.d)) != 0):
                jcall(out, 'println', jcast('int', (-1)))
                # 有整数解
            else:
                Code01_DiophantineEquation2.x = jcast('long', jcast('long', (Code01_DiophantineEquation2.x * jcast('long', jdiv(Code01_DiophantineEquation2.c, Code01_DiophantineEquation2.d)))))
                Code01_DiophantineEquation2.y = jcast('long', jcast('long', (Code01_DiophantineEquation2.y * jcast('long', jdiv(Code01_DiophantineEquation2.c, Code01_DiophantineEquation2.d)))))
                Code01_DiophantineEquation2.xd = jcast('long', jcast('long', jdiv(Code01_DiophantineEquation2.b, Code01_DiophantineEquation2.d)))
                Code01_DiophantineEquation2.yd = jcast('long', jcast('long', jdiv(Code01_DiophantineEquation2.a, Code01_DiophantineEquation2.d)))
                if (Code01_DiophantineEquation2.x < 0):
                    # x要想增长到>=1且最小的值，差几个xd，算出来就是k的值
                    # 那应该是(1-x)/xd，结果向上取整
                    Code01_DiophantineEquation2.times = jcast('long', jcast('long', jdiv(jcast('long', (jcast('long', jadd(jcast('long', (1 - Code01_DiophantineEquation2.x)), Code01_DiophantineEquation2.xd)) - 1)), Code01_DiophantineEquation2.xd)))
                    Code01_DiophantineEquation2.x = jcast('long', jcast('long', jadd(Code01_DiophantineEquation2.x, jcast('long', (Code01_DiophantineEquation2.xd * Code01_DiophantineEquation2.times)))))
                    Code01_DiophantineEquation2.y = jcast('long', jcast('long', (Code01_DiophantineEquation2.y - jcast('long', (Code01_DiophantineEquation2.yd * Code01_DiophantineEquation2.times)))))
                else:
                    # x要想减少到>=1且最小的值，差几个xd，算出来就是k的值，向下取整
                    Code01_DiophantineEquation2.times = jcast('long', jcast('long', jdiv(jcast('long', (Code01_DiophantineEquation2.x - 1)), Code01_DiophantineEquation2.xd)))
                    Code01_DiophantineEquation2.x = jcast('long', jcast('long', (Code01_DiophantineEquation2.x - jcast('long', (Code01_DiophantineEquation2.xd * Code01_DiophantineEquation2.times)))))
                    Code01_DiophantineEquation2.y = jcast('long', jcast('long', jadd(Code01_DiophantineEquation2.y, jcast('long', (Code01_DiophantineEquation2.yd * Code01_DiophantineEquation2.times)))))
                # 此时得到的(x, y)，是x为最小正整数时的一组解
                # 然后继续讨论
                # 无正整数解
                if (Code01_DiophantineEquation2.y <= 0):
                    # x能取得的最小正数
                    jcall(out, 'print', jadd(Code01_DiophantineEquation2.x, ' '))
                    # y能取得的最小正数
                    jcall(out, 'println', jcast('long', jadd(Code01_DiophantineEquation2.y, jcast('long', (Code01_DiophantineEquation2.yd * jcast('long', jdiv(jcast('long', (jcast('long', jadd(jcast('long', (1 - Code01_DiophantineEquation2.y)), Code01_DiophantineEquation2.yd)) - 1)), Code01_DiophantineEquation2.yd)))))))
                    # 有正整数解
                else:
                    # y减少到1以下，能减几次，就是正整数解的个数
                    jcall(out, 'print', jadd(jcast('long', jadd(jcast('long', jdiv(jcast('long', (Code01_DiophantineEquation2.y - 1)), Code01_DiophantineEquation2.yd)), 1)), ' '))
                    # x能取得的最小正数
                    jcall(out, 'print', jadd(Code01_DiophantineEquation2.x, ' '))
                    # y能取得的最小正数
                    jcall(out, 'print', jadd(jcast('long', (Code01_DiophantineEquation2.y - jcast('long', (jcast('long', jdiv(jcast('long', (Code01_DiophantineEquation2.y - 1)), Code01_DiophantineEquation2.yd)) * Code01_DiophantineEquation2.yd)))), ' '))
                    # x能取得的最大正数
                    jcall(out, 'print', jadd(jcast('long', jadd(Code01_DiophantineEquation2.x, jcast('long', (jcast('long', jdiv(jcast('long', (Code01_DiophantineEquation2.y - 1)), Code01_DiophantineEquation2.yd)) * Code01_DiophantineEquation2.xd)))), ' '))
                    # y能取得的最大正数
                    jcall(out, 'println', Code01_DiophantineEquation2.y)
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DiophantineEquation2.d = jcast('long', 0)
Code01_DiophantineEquation2.x = jcast('long', 0)
Code01_DiophantineEquation2.y = jcast('long', 0)
Code01_DiophantineEquation2.px = jcast('long', 0)
Code01_DiophantineEquation2.py = jcast('long', 0)
Code01_DiophantineEquation2.a = jcast('long', 0)
Code01_DiophantineEquation2.b = jcast('long', 0)
Code01_DiophantineEquation2.c = jcast('long', 0)
Code01_DiophantineEquation2.xd = jcast('long', 0)
Code01_DiophantineEquation2.yd = jcast('long', 0)
Code01_DiophantineEquation2.times = jcast('long', 0)

if __name__ == '__main__':
    Code01_DiophantineEquation2.main([])

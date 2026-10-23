# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 机器人的移动区域
# 二维网格中只有x和y的值都为整数的坐标，才叫格点
# 某个机器人从格点(0,0)出发，每次机器人都走直线到达(x + dx, y + dy)的格点
# 一共移动n次，每次的(dx, dy)都给定，途中路线不会交叉，输入保证机器人最终回到(0,0)
# 机器人走的路线所围成的区域一定是多边形，输入保证机器人一定沿着逆时针方向行动
# 返回多边形的内部一共几个格点，多边形的边上一共几个格点，多边形的面积
# 3 <= n <= 100
# -100 <= dx、dy <= 100
# 测试链接 : http://poj.org/problem?id=1265
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Area:
    __java_fields__ = {}
    @staticmethod
    def gcd(a, b):
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', (a if (b == 0) else Code04_Area.gcd(b, jcast('long', jmod(a, b)))))

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
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            edges = jcast('int', 0)
            area = jcast('double', 0)
            i = jcast('int', 1)
            x = jcast('int', 0)
            y = jcast('int', 0)
            dx = 0
            dy = 0
            while (i <= n):
                jcall(in_, 'nextToken')
                dx = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                dy = jcast('int', jcast('int', jget(in_, 'nval')))
                # 题目3的重要结论
                edges = jcast('int', jcast('long', jadd(edges, Code04_Area.gcd(jstatic('Math', 'abs', dx), jstatic('Math', 'abs', dy)))))
                # 逆时针方向转动的鞋带公式
                area = jcast('double', jadd(area, jcast('int', (jcast('int', (x * jcast('int', jadd(y, dy)))) - jcast('int', (jcast('int', jadd(x, dx)) * y))))))
                x = jcast('int', jcast('int', jadd(x, dx)))
                y = jcast('int', jcast('int', jadd(y, dy)))
                i = jcast('int', (i + 1))
            # 鞋带公式最后要/2
            area = jcast('double', jdiv(area, 2))
            # pick定理
            # 多边形面积 = 边界上格点数/2 + 内部格点数 - 1
            # 内部格点数 = 多边形面积 - 边界上格点数/2 + 1
            inners = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', jcast('area', jcast('int', (-edges)))), 2)), 1)))
            jcall(out, 'println', jadd(jadd('Scenario #', t), ':'))
            jcall(out, 'print', jadd(inners, ' '))
            jcall(out, 'print', jadd(edges, ' '))
            jcall(out, 'printf', '%.1f', area)
            jcall(out, 'println')
            jcall(out, 'println')
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_Area.main([])

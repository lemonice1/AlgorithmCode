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

# 青蛙的约会
# 有一个周长为l的环，从环的0位置开始，规定只能沿着顺时针方向不停转圈
# 青蛙A在环的x1位置，每秒跳m个单位，青蛙B在x2位置，每秒跳n个单位
# 只有在某时刻，青蛙A和青蛙B来到环的同一个位置，才算相遇
# 如果两只青蛙相遇不了，打印"Impossible"
# 如果可以相遇，打印两只青蛙至少多久才能相遇
# 1 <= l <= 3 * 10^9
# 1 <= x1、x2、m、n <= 2 * 10^9
# x1 != x2
# 测试链接 : https://www.luogu.com.cn/problem/P1516
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_FrogsMeeting:
    __java_fields__ = {'d': 'd', 'x': 'x', 'y': 'y', 'px': 'px', 'py': 'py'}
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
            Code02_FrogsMeeting.d = jcast('long', a)
            Code02_FrogsMeeting.x = jcast('long', 1)
            Code02_FrogsMeeting.y = jcast('long', 0)
        else:
            Code02_FrogsMeeting.exgcd(b, jcast('long', jmod(a, b)))
            Code02_FrogsMeeting.px = jcast('long', Code02_FrogsMeeting.x)
            Code02_FrogsMeeting.py = jcast('long', Code02_FrogsMeeting.y)
            Code02_FrogsMeeting.x = jcast('long', Code02_FrogsMeeting.py)
            Code02_FrogsMeeting.y = jcast('long', jcast('long', (Code02_FrogsMeeting.px - jcast('long', (Code02_FrogsMeeting.py * jcast('long', jdiv(a, b)))))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        x1 = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        x2 = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        n = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        l = jcast('long', jcast('long', jget(in_, 'nval')))
        a = 0
        c = 0
        if (x1 < x2):
            a = jcast('long', jcast('long', (m - n)))
            c = jcast('long', jcast('long', (x2 - x1)))
        else:
            a = jcast('long', jcast('long', (n - m)))
            c = jcast('long', jcast('long', (x1 - x2)))
        if (a < 0):
            a = jcast('long', jcast('long', (-a)))
            c = jcast('long', jcast('long', (l - c)))
        Code02_FrogsMeeting.exgcd(a, l)
        if (jcast('long', jmod(c, Code02_FrogsMeeting.d)) != 0):
            jcall(out, 'println', 'Impossible')
        else:
            # 解出的特解
            x0 = jcast('long', jcast('long', jdiv(jcast('long', (Code02_FrogsMeeting.x * c)), Code02_FrogsMeeting.d)))
            # 单次幅度
            xd = jcast('long', jcast('long', jdiv(l, Code02_FrogsMeeting.d)))
            # x0调整成>=1的最小正整数，处理办法和上一题一样
            if (x0 < 0):
                x0 = jcast('long', jcast('long', jadd(x0, jcast('long', (jcast('long', jdiv(jcast('long', (jcast('long', jadd(jcast('long', (1 - x0)), xd)) - 1)), xd)) * xd)))))
            else:
                x0 = jcast('long', jcast('long', (x0 - jcast('long', (jcast('long', jdiv(jcast('long', (x0 - 1)), xd)) * xd)))))
            jcall(out, 'println', x0)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_FrogsMeeting.d = jcast('long', 0)
Code02_FrogsMeeting.x = jcast('long', 0)
Code02_FrogsMeeting.y = jcast('long', 0)
Code02_FrogsMeeting.px = jcast('long', 0)
Code02_FrogsMeeting.py = jcast('long', 0)

if __name__ == '__main__':
    Code02_FrogsMeeting.main([])

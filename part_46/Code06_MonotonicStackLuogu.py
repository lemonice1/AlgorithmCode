# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课上没讲的代码，单调栈在洛谷上的测试，原理是一样的
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 建议看看就好，现在的笔试和比赛时，不会这么极限的
# 给定一个长度为n的数组，打印每个位置的右侧，大于该位置数字的最近位置
# 测试链接 : https://www.luogu.com.cn/problem/P5788
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_MonotonicStackLuogu:
    __java_fields__ = {'in': 'in_', 'out': 'out'}
    @staticmethod
    def main(args):
        n = jcast('int', Code06_MonotonicStackLuogu.nextInt())
        arr = jarray('int', [jcast('int', jadd(n, 1))])
        i = jcast('int', 1)
        while (i <= n):
            jset(arr, i, Code06_MonotonicStackLuogu.nextInt())
            i = jcast('int', (i + 1))
        # 单调栈中保证 : 左 >= 右
        stack = jarray('int', [jcast('int', jadd(n, 1))])
        r = jcast('int', 0)
        # 注意，这里为了省空间，直接复用了arr
        # 比如一个位置x，如果从stack中弹出，并且是当前的i位置让其弹出的
        # 那么令arr[x] = i，也就是代码36行
        # 此时arr[x]不再表示原始数组x位置的值
        # 而去表示，原始数组中，x的右边，大于arr[x]，最近的位置
        # 也就是说，重新复用arr，让其变成答案数组
        # 为啥这么节省？为啥不单独弄一个答案数组
        # 没办法，不这么节省通过不了测试，空间卡的非常极限
        i = jcast('int', 1)
        while (i <= n):
            while ((r > 0) and (arr[stack[jcast('int', (r - 1))]] < arr[i])):
                jset(arr, stack[(r := jcast('int', (r + (-1))))], i)
            jset(stack, ((_java_old_1 := r), (r := jcast('int', (r + (1)))), _java_old_1)[2], i)
            i = jcast('int', (i + 1))
        while (r > 0):
            jset(arr, stack[(r := jcast('int', (r + (-1))))], 0)
        jcall(Code06_MonotonicStackLuogu.out, 'print', arr[1])
        i = jcast('int', 2)
        while (i <= n):
            jcall(Code06_MonotonicStackLuogu.out, 'print', jadd(' ', arr[i]))
            i = jcast('int', (i + 1))
        jcall(Code06_MonotonicStackLuogu.out, 'println')
        jcall(Code06_MonotonicStackLuogu.out, 'flush')

    # 用如下的方式读数据其实并不推荐
    # 但是这道题特别卡空间
    # 需要这么读数据让内存开销最小
    # 一般笔试、比赛时不需要这么写
    in_ = None
    out = None
    @staticmethod
    def nextInt():
        ch = 0
        sign = jcast('int', 1)
        ans = jcast('int', 0)
        while (not jstatic('Character', 'isDigit', (ch := jcall(Code06_MonotonicStackLuogu.in_, 'read')))):
            if (ch == jchar('-')):
                sign = jcast('int', jcast('int', (-1)))
        while True:
            ans = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (ans * 10)), ch)) - jchar('0'))))
            if not (jstatic('Character', 'isDigit', (ch := jcall(Code06_MonotonicStackLuogu.in_, 'read')))):
                break
        return jcast('int', jcast('int', (ans * sign)))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_MonotonicStackLuogu.in_ = jnew('BufferedInputStream', jget(System, 'in'))
Code06_MonotonicStackLuogu.out = jnew('PrintWriter', jget(System, 'out'))

if __name__ == '__main__':
    Code06_MonotonicStackLuogu.main([])

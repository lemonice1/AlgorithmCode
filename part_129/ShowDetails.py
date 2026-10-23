# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 课上讲述普通消元、高斯消元构建异或空间线性基的例子
class ShowDetails:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'arr': 'arr', 'n': 'n', 'basis1': 'basis1', 'zero1': 'zero1', 'basis2': 'basis2', 'len': 'len', 'zero2': 'zero2'}
    MAXN = 0
    # 最高位从哪开始
    BIT = 0
    arr = None
    n = 0
    # 普通消元
    basis1 = None
    zero1 = False
    @staticmethod
    def compute1():
        ShowDetails.zero1 = jcast('boolean', False)
        i = jcast('int', 1)
        while (i <= ShowDetails.n):
            if (not ShowDetails.insert(ShowDetails.arr[i])):
                ShowDetails.zero1 = jcast('boolean', True)
            i = jcast('int', (i + 1))

    # 线性基里插入num，如果线性基增加了返回true，否则返回false
    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', ShowDetails.BIT)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (ShowDetails.basis1[i] == 0):
                    ShowDetails.basis1[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ ShowDetails.basis1[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    # 高斯消元
    # 因为不需要维护主元和自由元的依赖关系
    # 所以高斯消元的写法可以得到简化
    basis2 = None
    len = 0
    zero2 = False
    @staticmethod
    def compute2():
        ShowDetails.len = jcast('int', 1)
        i = jcast('long', ShowDetails.BIT)
        while (i >= 0):
            try:
                j = jcast('int', ShowDetails.len)
                while (j <= ShowDetails.n):
                    try:
                        if (jcast('long', (ShowDetails.basis2[j] & jcast('long', (1 << (i & 63))))) != 0):
                            ShowDetails.swap(j, ShowDetails.len)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (jcast('long', (ShowDetails.basis2[ShowDetails.len] & jcast('long', (1 << (i & 63))))) != 0):
                    j = jcast('int', 1)
                    while (j <= ShowDetails.n):
                        if ((j != ShowDetails.len) and (jcast('long', (ShowDetails.basis2[j] & jcast('long', (1 << (i & 63))))) != 0)):
                            ShowDetails.basis2[j] = jcast('long', jcast('long', (ShowDetails.basis2[j] ^ ShowDetails.basis2[ShowDetails.len])))
                        j = jcast('int', (j + 1))
                    ShowDetails.len = jcast('int', (ShowDetails.len + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('long', (i - 1))
        ShowDetails.len = jcast('int', (ShowDetails.len - 1))
        ShowDetails.zero2 = jcast('boolean', (ShowDetails.len != ShowDetails.n))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = jcast('long', ShowDetails.basis2[a])
        ShowDetails.basis2[a] = jcast('long', ShowDetails.basis2[b])
        ShowDetails.basis2[b] = jcast('long', tmp)

    @staticmethod
    def main(args):
        # 课上讲的普通消元，例子1
        # 12, 9, 14, 11
        jprint('例子1', newline=True)
        jstatic('Arrays', 'fill', ShowDetails.basis1, 0)
        ShowDetails.arr[1] = jcast('long', 12)
        ShowDetails.arr[2] = jcast('long', 9)
        ShowDetails.arr[3] = jcast('long', 14)
        ShowDetails.arr[4] = jcast('long', 11)
        ShowDetails.n = jcast('int', 4)
        jprint('原始数组得到的异或结果如下', newline=True)
        ShowDetails.printXor(ShowDetails.arr, ShowDetails.n)
        jprint('===========================', newline=True)
        jprint('普通消元得到的线性基 : ', newline=True)
        ShowDetails.compute1()
        b1 = jarray('long', [ShowDetails.MAXN])
        s1 = jcast('int', 0)
        i = jcast('int', ShowDetails.BIT)
        while (i >= 0):
            if (ShowDetails.basis1[i] != 0):
                jprint(jadd(ShowDetails.basis1[i], ' '), newline=False)
                jset(b1, (s1 := jcast('int', (s1 + (1)))), ShowDetails.basis1[i])
            i = jcast('int', (i - 1))
        jprint(newline=True)
        jprint(jadd('是否能异或出0 : ', ShowDetails.zero1), newline=True)
        jprint('普通消元得到的异或结果如下', newline=True)
        ShowDetails.printXor(b1, s1)
        jprint('===========================', newline=True)
        jprint(newline=True)
        jprint(newline=True)
        # 课上讲的普通消元，例子2
        # 2, 5, 11, 6
        jprint('例子2', newline=True)
        jstatic('Arrays', 'fill', ShowDetails.basis1, 0)
        ShowDetails.arr[1] = jcast('long', 2)
        ShowDetails.arr[2] = jcast('long', 5)
        ShowDetails.arr[3] = jcast('long', 11)
        ShowDetails.arr[4] = jcast('long', 6)
        ShowDetails.n = jcast('int', 4)
        jprint('原始数组得到的异或结果如下', newline=True)
        ShowDetails.printXor(ShowDetails.arr, ShowDetails.n)
        jprint('===========================', newline=True)
        jprint('普通消元得到的线性基 : ', newline=True)
        ShowDetails.compute1()
        b2 = jarray('long', [ShowDetails.MAXN])
        s2 = jcast('int', 0)
        i = jcast('int', ShowDetails.BIT)
        while (i >= 0):
            if (ShowDetails.basis1[i] != 0):
                jprint(jadd(ShowDetails.basis1[i], ' '), newline=False)
                jset(b2, (s2 := jcast('int', (s2 + (1)))), ShowDetails.basis1[i])
            i = jcast('int', (i - 1))
        jprint(newline=True)
        jprint(jadd('是否能异或出0 : ', ShowDetails.zero1), newline=True)
        jprint('普通消元得到的异或结果如下', newline=True)
        ShowDetails.printXor(b2, s2)
        jprint('===========================', newline=True)
        jprint(newline=True)
        jprint(newline=True)
        # 课上讲的高斯消元的例子，例子3
        # 6, 37, 35, 33
        jprint('例子3', newline=True)
        jstatic('Arrays', 'fill', ShowDetails.basis2, 0)
        jset(ShowDetails.arr, 1, jset(ShowDetails.basis2, 1, 6))
        jset(ShowDetails.arr, 2, jset(ShowDetails.basis2, 2, 37))
        jset(ShowDetails.arr, 3, jset(ShowDetails.basis2, 3, 35))
        jset(ShowDetails.arr, 4, jset(ShowDetails.basis2, 4, 33))
        ShowDetails.n = jcast('int', 4)
        jprint('原始数组得到的异或结果如下', newline=True)
        ShowDetails.printXor(ShowDetails.arr, ShowDetails.n)
        jprint('===========================', newline=True)
        jprint('高斯消元得到的线性基 : ', newline=True)
        ShowDetails.compute2()
        i = jcast('int', 1)
        while (i <= ShowDetails.len):
            jprint(jadd(ShowDetails.basis2[i], ' '), newline=False)
            i = jcast('int', (i + 1))
        jprint(newline=True)
        jprint(jadd('是否能异或出0 : ', ShowDetails.zero2), newline=True)
        jprint('高斯消元得到的异或结果如下', newline=True)
        ShowDetails.printXor(ShowDetails.basis2, ShowDetails.len)
        jprint('===========================', newline=True)
        jprint(newline=True)
        jprint(newline=True)
        # 课上讲的高斯消元的例子，例子4
        # 如果想得到第k小的非0异或和
        # 必须用高斯消元，不能用普通消元，比如
        # arr = { 7, 10, 4 }
        # 普通消元得到的异或空间线性基是 : 10 7 3
        # 第三小异或和是4，第四小异或和是10，这是错误的
        # 高斯消元可以得到正确结果
        # 高斯消元得到的异或空间线性基是 : 9 4 3
        # 第三小异或和是7，第四小异或和是9，这是正确的
        jprint('例子4', newline=True)
        jstatic('Arrays', 'fill', ShowDetails.basis1, 0)
        jstatic('Arrays', 'fill', ShowDetails.basis2, 0)
        jset(ShowDetails.arr, 1, jset(ShowDetails.basis2, 1, 7))
        jset(ShowDetails.arr, 2, jset(ShowDetails.basis2, 2, 10))
        jset(ShowDetails.arr, 3, jset(ShowDetails.basis2, 3, 4))
        ShowDetails.n = jcast('int', 3)
        jprint('原始数组得到的异或结果如下', newline=True)
        ShowDetails.printXor(ShowDetails.arr, ShowDetails.n)
        jprint('===========================', newline=True)
        jprint('普通消元', newline=True)
        ShowDetails.compute1()
        i = jcast('int', ShowDetails.BIT)
        while (i >= 0):
            if (ShowDetails.basis1[i] != 0):
                jprint(jadd(ShowDetails.basis1[i], ' '), newline=False)
            i = jcast('int', (i - 1))
        jprint(newline=True)
        jprint(jadd('是否能异或出0 : ', ShowDetails.zero1), newline=True)
        jprint('===========================', newline=True)
        jprint('高斯消元', newline=True)
        ShowDetails.compute2()
        i = jcast('int', 1)
        while (i <= ShowDetails.len):
            jprint(jadd(ShowDetails.basis2[i], ' '), newline=False)
            i = jcast('int', (i + 1))
        jprint(newline=True)
        jprint(jadd('是否能异或出0 : ', ShowDetails.zero2), newline=True)

    # nums中1~n的范围
    # 所有可能的异或和打印出来
    # 要求去重并且至少选择一个数字
    @staticmethod
    def printXor(nums, n):
        n = jcast('int', n)
        set = jnew('HashSet')
        ShowDetails.dfs(nums, n, 1, False, 0, set)
        jprint('至少选择一个数字所有可能的异或和:', newline=True)
        for s in set:
            jprint(jadd(s, ', '), newline=False)
        jprint(newline=True)

    # 当前来到i位置
    # 之前是否选择过数字用pick表示
    # 之前做的决定形成的异或和是path
    # 当前i位置的数字要或者不要全决策
    # 收集所有可能的异或和
    @staticmethod
    def dfs(nums, n, i, pick, path, set):
        n = jcast('int', n)
        i = jcast('int', i)
        pick = jcast('boolean', pick)
        path = jcast('long', path)
        if (i > n):
            if pick:
                jcall(set, 'add', path)
        else:
            ShowDetails.dfs(nums, n, jcast('int', jadd(i, 1)), pick, path, set)
            ShowDetails.dfs(nums, n, jcast('int', jadd(i, 1)), True, jcast('long', (path ^ nums[i])), set)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


ShowDetails.MAXN = jcast('int', 101)
ShowDetails.BIT = jcast('int', 60)
ShowDetails.arr = jarray('long', [ShowDetails.MAXN])
ShowDetails.n = jcast('int', 0)
ShowDetails.basis1 = jarray('long', [jcast('int', jadd(ShowDetails.BIT, 1))])
ShowDetails.zero1 = jcast('boolean', False)
ShowDetails.basis2 = jarray('long', [ShowDetails.MAXN])
ShowDetails.len = jcast('int', 0)
ShowDetails.zero2 = jcast('boolean', False)

if __name__ == '__main__':
    ShowDetails.main([])

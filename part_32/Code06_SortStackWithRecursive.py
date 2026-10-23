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

# 用递归函数排序栈
# 栈只提供push、pop、isEmpty三个方法
# 请完成无序栈的排序，要求排完序之后，从栈顶到栈底从小到大
# 只能使用栈提供的push、pop、isEmpty三个方法、以及递归函数
# 除此之外不能使用任何的容器，数组也不行
# 就是排序过程中只能用：
# 1) 栈提供的push、pop、isEmpty三个方法
# 2) 递归函数，并且返回值最多为单个整数
class Code06_SortStackWithRecursive:
    __java_fields__ = {}
    @staticmethod
    def sort(stack):
        deep = jcast('int', Code06_SortStackWithRecursive.deep(stack))
        while (deep > 0):
            max = jcast('int', Code06_SortStackWithRecursive.max(stack, deep))
            k = jcast('int', Code06_SortStackWithRecursive.times(stack, deep, max))
            Code06_SortStackWithRecursive.down(stack, deep, max, k)
            deep = jcast('int', jcast('int', (deep - k)))

    # 返回栈的深度
    # 不改变栈的数据状况
    @staticmethod
    def deep(stack):
        if jcall(stack, 'isEmpty'):
            return jcast('int', 0)
        num = jcast('int', jcall(stack, 'pop'))
        deep = jcast('int', jcast('int', jadd(Code06_SortStackWithRecursive.deep(stack), 1)))
        jcall(stack, 'push', num)
        return jcast('int', deep)

    # 从栈当前的顶部开始，往下数deep层
    # 返回这deep层里的最大值
    @staticmethod
    def max(stack, deep):
        deep = jcast('int', deep)
        if (deep == 0):
            return jcast('int', jget(Integer, 'MIN_VALUE'))
        num = jcast('int', jcall(stack, 'pop'))
        restMax = jcast('int', Code06_SortStackWithRecursive.max(stack, jcast('int', (deep - 1))))
        max = jcast('int', jstatic('Math', 'max', num, restMax))
        jcall(stack, 'push', num)
        return jcast('int', max)

    # 从栈当前的顶部开始，往下数deep层，已知最大值是max了
    # 返回，max出现了几次，不改变栈的数据状况
    @staticmethod
    def times(stack, deep, max):
        deep = jcast('int', deep)
        max = jcast('int', max)
        if (deep == 0):
            return jcast('int', 0)
        num = jcast('int', jcall(stack, 'pop'))
        restTimes = jcast('int', Code06_SortStackWithRecursive.times(stack, jcast('int', (deep - 1)), max))
        times = jcast('int', jcast('int', jadd(restTimes, (1 if (num == max) else 0))))
        jcall(stack, 'push', num)
        return jcast('int', times)

    # 从栈当前的顶部开始，往下数deep层，已知最大值是max，出现了k次
    # 请把这k个最大值沉底，剩下的数据状况不变
    @staticmethod
    def down(stack, deep, max, k):
        deep = jcast('int', deep)
        max = jcast('int', max)
        k = jcast('int', k)
        if (deep == 0):
            i = jcast('int', 0)
            while (i < k):
                jcall(stack, 'push', max)
                i = jcast('int', (i + 1))
        else:
            num = jcast('int', jcall(stack, 'pop'))
            Code06_SortStackWithRecursive.down(stack, jcast('int', (deep - 1)), max, k)
            if (num != max):
                jcall(stack, 'push', num)

    # 为了测试
    # 生成随机栈
    @staticmethod
    def randomStack(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jnew('Stack')
        i = jcast('int', 0)
        while (i < n):
            jcall(ans, 'add', jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    # 检测栈是不是从顶到底依次有序
    @staticmethod
    def isSorted(stack):
        step = jcast('int', jget(Integer, 'MIN_VALUE'))
        while (not jcall(stack, 'isEmpty')):
            if (step > jcall(stack, 'peek')):
                return jcast('boolean', False)
            step = jcast('int', jcall(stack, 'pop'))
        return jcast('boolean', True)

    # 为了测试
    @staticmethod
    def main(args):
        test = jnew('Stack')
        jcall(test, 'add', 1)
        jcall(test, 'add', 5)
        jcall(test, 'add', 4)
        jcall(test, 'add', 5)
        jcall(test, 'add', 3)
        jcall(test, 'add', 2)
        jcall(test, 'add', 3)
        jcall(test, 'add', 1)
        jcall(test, 'add', 4)
        jcall(test, 'add', 2)
        Code06_SortStackWithRecursive.sort(test)
        while (not jcall(test, 'isEmpty')):
            jprint(jcall(test, 'pop'), newline=True)
        # 随机测试
        N = jcast('int', 20)
        V = jcast('int', 20)
        testTimes = jcast('int', 20000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            try:
                n = jcast('int', jcast('int', (jstatic('Math', 'random') * N)))
                stack = Code06_SortStackWithRecursive.randomStack(n, V)
                Code06_SortStackWithRecursive.sort(stack)
                if (not Code06_SortStackWithRecursive.isSorted(stack)):
                    jprint('出错了!', newline=True)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_SortStackWithRecursive.main([])

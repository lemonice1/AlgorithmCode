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

# 用递归函数逆序栈
class Code05_ReverseStackWithRecursive:
    __java_fields__ = {}
    @staticmethod
    def reverse(stack):
        if jcall(stack, 'isEmpty'):
            return
        num = jcast('int', Code05_ReverseStackWithRecursive.bottomOut(stack))
        Code05_ReverseStackWithRecursive.reverse(stack)
        jcall(stack, 'push', num)

    # 栈底元素移除掉，上面的元素盖下来
    # 返回移除掉的栈底元素
    @staticmethod
    def bottomOut(stack):
        ans = jcast('int', jcall(stack, 'pop'))
        if jcall(stack, 'isEmpty'):
            return jcast('int', ans)
        else:
            last = jcast('int', Code05_ReverseStackWithRecursive.bottomOut(stack))
            jcall(stack, 'push', ans)
            return jcast('int', last)

    @staticmethod
    def main(args):
        stack = jnew('Stack')
        jcall(stack, 'push', 1)
        jcall(stack, 'push', 2)
        jcall(stack, 'push', 3)
        jcall(stack, 'push', 4)
        jcall(stack, 'push', 5)
        Code05_ReverseStackWithRecursive.reverse(stack)
        while (not jcall(stack, 'isEmpty')):
            jprint(jcall(stack, 'pop'), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_ReverseStackWithRecursive.main([])

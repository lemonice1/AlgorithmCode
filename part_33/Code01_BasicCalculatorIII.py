# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 含有嵌套的表达式求值
# 力扣上本题为会员题，所以额外提供了牛客网的测试链接
# 如果在牛客网上提交，请将函数名从calculate改为solve
# 测试链接 : https://leetcode.cn/problems/basic-calculator-iii/
# 测试链接 : https://www.nowcoder.com/practice/c215ba61c8b1443b996351df929dc4d4
class Code01_BasicCalculatorIII:
    __java_fields__ = {'where': 'where'}
    @staticmethod
    def calculate(str):
        Code01_BasicCalculatorIII.where = jcast('int', 0)
        return jcast('int', Code01_BasicCalculatorIII.f(jcall(str, 'toCharArray'), 0))

    where = 0
    # s[i....]开始计算，遇到字符串终止 或者 遇到)停止
    # 返回 : 自己负责的这一段，计算的结果
    # 返回之间，更新全局变量where，为了上游函数知道从哪继续！
    @staticmethod
    def f(s, i):
        i = jcast('int', i)
        cur = jcast('int', 0)
        numbers = jnew('ArrayList')
        ops = jnew('ArrayList')
        while ((i < jget(s, 'length')) and (s[i] != jchar(')'))):
            if ((s[i] >= jchar('0')) and (s[i] <= jchar('9'))):
                cur = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (cur * 10)), s[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]])) - jchar('0'))))
            else:
                if (s[i] != jchar('(')):
                    # 遇到了运算符 + - * /
                    Code01_BasicCalculatorIII.push(numbers, ops, cur, s[((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2]])
                    cur = jcast('int', 0)
                else:
                    # i (.....)
                    # 遇到了左括号！
                    cur = jcast('int', Code01_BasicCalculatorIII.f(s, jcast('int', jadd(i, 1))))
                    i = jcast('int', jcast('int', jadd(Code01_BasicCalculatorIII.where, 1)))
        Code01_BasicCalculatorIII.push(numbers, ops, cur, jchar('+'))
        Code01_BasicCalculatorIII.where = jcast('int', i)
        return jcast('int', Code01_BasicCalculatorIII.compute(numbers, ops))

    @staticmethod
    def push(numbers, ops, cur, op):
        cur = jcast('int', cur)
        op = jcast('char', op)
        n = jcast('int', jcall(numbers, 'size'))
        if (((n == 0) or (jcall(ops, 'get', jcast('int', (n - 1))) == jchar('+'))) or (jcall(ops, 'get', jcast('int', (n - 1))) == jchar('-'))):
            jcall(numbers, 'add', cur)
            jcall(ops, 'add', op)
        else:
            topNumber = jcast('int', jcall(numbers, 'get', jcast('int', (n - 1))))
            topOp = jcast('char', jcall(ops, 'get', jcast('int', (n - 1))))
            if (topOp == jchar('*')):
                jcall(numbers, 'set', jcast('int', (n - 1)), jcast('int', (topNumber * cur)))
            else:
                jcall(numbers, 'set', jcast('int', (n - 1)), jcast('int', jdiv(topNumber, cur)))
            jcall(ops, 'set', jcast('int', (n - 1)), op)

    @staticmethod
    def compute(numbers, ops):
        n = jcast('int', jcall(numbers, 'size'))
        ans = jcast('int', jcall(numbers, 'get', 0))
        i = jcast('int', 1)
        while (i < n):
            ans = jcast('int', jadd(ans, (jcall(numbers, 'get', i) if (jcall(ops, 'get', jcast('int', (i - 1))) == jchar('+')) else (-jcall(numbers, 'get', i)))))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_BasicCalculatorIII.where = jcast('int', 0)

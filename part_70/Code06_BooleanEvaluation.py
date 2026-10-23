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

# 布尔运算
# 给定一个布尔表达式和一个期望的布尔结果 result
# 布尔表达式由 0 (false)、1 (true)、& (AND)、 | (OR) 和 ^ (XOR) 符号组成
# 布尔表达式一定是正确的，不需要检查有效性
# 但是其中没有任何括号来表示优先级
# 你可以随意添加括号来改变逻辑优先级
# 目的是让表达式能够最终得出result的结果
# 返回最终得出result有多少种不同的逻辑计算顺序
# 测试链接 : https://leetcode.cn/problems/boolean-evaluation-lcci/
class Code06_BooleanEvaluation:
    __java_fields__ = {}
    # 记忆化搜索
    @staticmethod
    def countEval(str, result):
        result = jcast('int', result)
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n, None])
        ft = Code06_BooleanEvaluation.f(s, 0, jcast('int', (n - 1)), dp)
        return jcast('int', ft[result])

    # s[l...r]是表达式的一部分，且一定符合范式
    # 0/1  逻  0/1   逻       0/1
    # l  l+1  l+2  l+3........r
    # s[l...r]  0 : ?
    # 1 : ?
    # ans : int[2] ans[0] = false方法数 ans[0] = true方法数
    @staticmethod
    def f(s, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (dp[l][r] != None):
            return dp[l][r]
        f = jcast('int', 0)
        t = jcast('int', 0)
        if (l == r):
            # 只剩一个字符，0/1
            f = jcast('int', (1 if (s[l] == jchar('0')) else 0))
            t = jcast('int', (1 if (s[l] == jchar('1')) else 0))
        else:
            tmp = None
            k = jcast('int', jcast('int', jadd(l, 1)))
            a = 0
            b = 0
            c = 0
            d = 0
            while (k < r):
                # l ... r
                # 枚举每一个逻辑符号最后执行 k = l+1 ... r-1  k+=2
                tmp = Code06_BooleanEvaluation.f(s, l, jcast('int', (k - 1)), dp)
                a = jcast('int', tmp[0])
                b = jcast('int', tmp[1])
                tmp = Code06_BooleanEvaluation.f(s, jcast('int', jadd(k, 1)), r, dp)
                c = jcast('int', tmp[0])
                d = jcast('int', tmp[1])
                if (s[k] == jchar('&')):
                    f = jcast('int', jcast('int', jadd(f, jcast('int', jadd(jcast('int', jadd(jcast('int', (a * c)), jcast('int', (a * d)))), jcast('int', (b * c)))))))
                    t = jcast('int', jcast('int', jadd(t, jcast('int', (b * d)))))
                else:
                    if (s[k] == jchar('|')):
                        f = jcast('int', jcast('int', jadd(f, jcast('int', (a * c)))))
                        t = jcast('int', jcast('int', jadd(t, jcast('int', jadd(jcast('int', jadd(jcast('int', (a * d)), jcast('int', (b * c)))), jcast('int', (b * d)))))))
                    else:
                        f = jcast('int', jcast('int', jadd(f, jcast('int', jadd(jcast('int', (a * c)), jcast('int', (b * d)))))))
                        t = jcast('int', jcast('int', jadd(t, jcast('int', jadd(jcast('int', (a * d)), jcast('int', (b * c)))))))
                k = jcast('int', jcast('int', jadd(k, 2)))
        ft = jarray('int', [None], [f, t])
        jset(dp[l], r, ft)
        return ft

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



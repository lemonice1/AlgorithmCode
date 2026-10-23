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

# 可以用r、e、d三种字符拼接字符串，如果拼出来的字符串中
# 有且仅有1个长度>=2的回文子串，那么这个字符串定义为"好串"
# 返回长度为n的所有可能的字符串中，好串有多少个
# 结果对 1000000007 取模， 1 <= n <= 10^9
# 示例：
# n = 1, 输出0
# n = 2, 输出3
# n = 3, 输出18
class Code04_RedPalindromeGoodStrings:
    __java_fields__ = {}
    # 暴力方法
    # 为了观察规律
    @staticmethod
    def num1(n):
        n = jcast('int', n)
        path = jarray('char', [n])
        return jcast('int', Code04_RedPalindromeGoodStrings.f(path, 0))

    @staticmethod
    def f(path, i):
        i = jcast('int', i)
        if (i == jget(path, 'length')):
            cnt = jcast('int', 0)
            l = jcast('int', 0)
            while (l < jget(path, 'length')):
                r = jcast('int', jcast('int', jadd(l, 1)))
                while (r < jget(path, 'length')):
                    if Code04_RedPalindromeGoodStrings.is_(path, l, r):
                        cnt = jcast('int', (cnt + 1))
                    if (cnt > 1):
                        return jcast('int', 0)
                    r = jcast('int', (r + 1))
                l = jcast('int', (l + 1))
            return jcast('int', (1 if (cnt == 1) else 0))
        else:
            # i正常位置
            ans = jcast('int', 0)
            path[i] = jcast('char', jchar('r'))
            ans = jcast('int', jcast('int', jadd(ans, Code04_RedPalindromeGoodStrings.f(path, jcast('int', jadd(i, 1))))))
            path[i] = jcast('char', jchar('e'))
            ans = jcast('int', jcast('int', jadd(ans, Code04_RedPalindromeGoodStrings.f(path, jcast('int', jadd(i, 1))))))
            path[i] = jcast('char', jchar('d'))
            ans = jcast('int', jcast('int', jadd(ans, Code04_RedPalindromeGoodStrings.f(path, jcast('int', jadd(i, 1))))))
            return jcast('int', ans)

    @staticmethod
    def is_(s, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        while (l < r):
            if (s[l] != s[r]):
                return jcast('boolean', False)
            l = jcast('int', (l + 1))
            r = jcast('int', (r - 1))
        return jcast('boolean', True)

    # 正式方法
    # 观察规律之后变成代码
    @staticmethod
    def num2(n):
        n = jcast('int', n)
        if (n == 1):
            return jcast('int', 0)
        if (n == 2):
            return jcast('int', 3)
        if (n == 3):
            return jcast('int', 18)
        return jcast('int', jcast('int', jcast('long', jmod(jcast('long', (jcast('long', 6) * jcast('int', jadd(n, 1)))), 1000000007))))

    @staticmethod
    def main(args):
        i = jcast('int', 1)
        while (i <= 10):
            jprint(jadd(jadd(jadd('长度为', i), ', 答案:'), Code04_RedPalindromeGoodStrings.num1(i)), newline=True)
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_RedPalindromeGoodStrings.main([])

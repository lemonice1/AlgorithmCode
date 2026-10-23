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

# 完成配对需要的最少字符数量
# 给定一个由'['、']'、'('，')'组成的字符串
# 请问最少插入多少个括号就能使这个字符串的所有括号正确配对
# 例如当前串是 "([[])"，那么插入一个']'即可满足
# 输出最少需要插入多少个字符
# 测试链接 : https://www.nowcoder.com/practice/e391767d80d942d29e6095a935a5b96b
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MinimumInsertionsToMatch:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        str = jcall(br, 'readLine')
        jcall(out, 'println', Code01_MinimumInsertionsToMatch.compute(str))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(n^3)
    @staticmethod
    def compute(str):
        s = jcall(str, 'toCharArray')
        n = jcast('int', jget(s, 'length'))
        dp = jarray('int', [n, n])
        i = jcast('int', 0)
        while (i < n):
            j = jcast('int', 0)
            while (j < n):
                jset(dp[i], j, jcast('int', (-1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code01_MinimumInsertionsToMatch.f(s, 0, jcast('int', (jget(s, 'length') - 1)), dp))

    # 让s[l...r]配对至少需要几个字符
    @staticmethod
    def f(s, l, r, dp):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('int', 1)
        if (l == jcast('int', (r - 1))):
            if (((s[l] == jchar('(')) and (s[r] == jchar(')'))) or ((s[l] == jchar('[')) and (s[r] == jchar(']')))):
                return jcast('int', 0)
            return jcast('int', 2)
        # l...r字符数量 >= 3
        if (dp[l][r] != jcast('int', (-1))):
            return jcast('int', dp[l][r])
        # 可能性1 : [l]、[r]本来就是配对的
        p1 = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (((s[l] == jchar('(')) and (s[r] == jchar(')'))) or ((s[l] == jchar('[')) and (s[r] == jchar(']')))):
            p1 = jcast('int', Code01_MinimumInsertionsToMatch.f(s, jcast('int', jadd(l, 1)), jcast('int', (r - 1)), dp))
        # 可能性2 : 基于每个可能的划分点，做左右划分
        p2 = jcast('int', jget(Integer, 'MAX_VALUE'))
        m = jcast('int', l)
        while (m < r):
            p2 = jcast('int', jstatic('Math', 'min', p2, jcast('int', jadd(Code01_MinimumInsertionsToMatch.f(s, l, m, dp), Code01_MinimumInsertionsToMatch.f(s, jcast('int', jadd(m, 1)), r, dp)))))
            m = jcast('int', (m + 1))
        ans = jcast('int', jstatic('Math', 'min', p1, p2))
        jset(dp[l], r, ans)
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_MinimumInsertionsToMatch.main([])

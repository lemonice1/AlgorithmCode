# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 统计有多少个不同的字符串
# 测试链接 : https://www.luogu.com.cn/problem/P3370
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DifferentStrings:
    __java_fields__ = {'MAXN': 'MAXN', 'base': 'base', 'nums': 'nums', 'n': 'n'}
    MAXN = 0
    base = 0
    nums = None
    n = 0
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_DifferentStrings.n = jcast('int', jstatic('Integer', 'valueOf', jcall(in_, 'readLine')))
        i = jcast('int', 0)
        while (i < Code01_DifferentStrings.n):
            jset(Code01_DifferentStrings.nums, i, Code01_DifferentStrings.value(jcall(jcall(in_, 'readLine'), 'toCharArray')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_DifferentStrings.cnt())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def value(s):
        ans = jcast('long', Code01_DifferentStrings.v(s[0]))
        i = jcast('int', 1)
        while (i < jget(s, 'length')):
            ans = jcast('long', jcast('long', jadd(jcast('long', (ans * Code01_DifferentStrings.base)), Code01_DifferentStrings.v(s[i]))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 数字 + 大写 + 小写
    # '0' -> 1
    # '1' -> 2
    # ...
    # '9' -> 10
    # 'A' -> 11
    # 'B' -> 12
    # ...
    # 'Z' -> 36
    # 'a' -> 37
    # ...
    # 'z' -> 62
    @staticmethod
    def v(c):
        c = jcast('char', c)
        if ((c >= jchar('0')) and (c <= jchar('9'))):
            return jcast('int', jcast('int', jadd(jcast('int', (c - jchar('0'))), 1)))
        else:
            if ((c >= jchar('A')) and (c <= jchar('Z'))):
                return jcast('int', jcast('int', jadd(jcast('int', (c - jchar('A'))), 11)))
            else:
                return jcast('int', jcast('int', jadd(jcast('int', (c - jchar('a'))), 37)))

    @staticmethod
    def cnt():
        jstatic('Arrays', 'sort', Code01_DifferentStrings.nums, 0, Code01_DifferentStrings.n)
        ans = jcast('int', 1)
        i = jcast('int', 1)
        while (i < Code01_DifferentStrings.n):
            if (Code01_DifferentStrings.nums[i] != Code01_DifferentStrings.nums[jcast('int', (i - 1))]):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DifferentStrings.MAXN = jcast('int', 10001)
Code01_DifferentStrings.base = jcast('int', 499)
Code01_DifferentStrings.nums = jarray('long', [Code01_DifferentStrings.MAXN])
Code01_DifferentStrings.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_DifferentStrings.main([])

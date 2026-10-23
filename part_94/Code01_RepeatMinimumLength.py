# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最短循环节的长度
# 给你一个字符串s，它一定是由某个循环节不断自我连接形成的
# 题目保证至少重复2次，但是最后一个循环节不一定完整
# 现在想知道s的最短循环节是多长
# 测试链接 : https://www.luogu.com.cn/problem/P4391
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_RepeatMinimumLength:
    __java_fields__ = {'MAXN': 'MAXN', 'next': 'next', 'n': 'n', 's': 's'}
    MAXN = 0
    next = None
    n = 0
    s = None
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_RepeatMinimumLength.n = jcast('int', jstatic('Integer', 'valueOf', jcall(in_, 'readLine')))
        Code01_RepeatMinimumLength.s = jcall(jcall(in_, 'readLine'), 'toCharArray')
        jcall(out, 'println', Code01_RepeatMinimumLength.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def compute():
        Code01_RepeatMinimumLength.nextArray()
        return jcast('int', jcast('int', (Code01_RepeatMinimumLength.n - Code01_RepeatMinimumLength.next[Code01_RepeatMinimumLength.n])))

    @staticmethod
    def nextArray():
        Code01_RepeatMinimumLength.next[0] = jcast('int', jcast('int', (-1)))
        Code01_RepeatMinimumLength.next[1] = jcast('int', 0)
        i = jcast('int', 2)
        cn = jcast('int', 0)
        while (i <= Code01_RepeatMinimumLength.n):
            if (Code01_RepeatMinimumLength.s[jcast('int', (i - 1))] == Code01_RepeatMinimumLength.s[cn]):
                jset(Code01_RepeatMinimumLength.next, ((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], (cn := jcast('int', (cn + (1)))))
            else:
                if (cn > 0):
                    cn = jcast('int', Code01_RepeatMinimumLength.next[cn])
                else:
                    jset(Code01_RepeatMinimumLength.next, ((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2], 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_RepeatMinimumLength.MAXN = jcast('int', 1000001)
Code01_RepeatMinimumLength.next = jarray('int', [Code01_RepeatMinimumLength.MAXN])
Code01_RepeatMinimumLength.n = jcast('int', 0)
Code01_RepeatMinimumLength.s = None

if __name__ == '__main__':
    Code01_RepeatMinimumLength.main([])

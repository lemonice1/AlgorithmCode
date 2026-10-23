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

# 无法组成的最大值
# 一共有a、b两种面值的硬币，a和b一定互质，每种硬币都有无限个
# 返回a和b无法组成的钱数中，最大值是多少
# 题目的输入保证存在最大的无法组成的钱数
# 1 <= a、b <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3951
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_LargestUnattainable:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        a = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        b = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(out, 'println', jcast('long', (jcast('long', (jcast('long', (a * b)) - a)) - b)))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_LargestUnattainable.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 判断较大的数字是否是质数(Miller-Rabin测试)
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 核心在于第11行，整型成了128位
# 测试链接 : https://www.luogu.com.cn/problem/U148828
class Code02_LargeNumberIsPrime3:
    __java_fields__ = {'s': 's'}
    # 测试次数，次数越多失误率越低，但速度也越慢
    s = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        t = jcast('int', jstatic('Integer', 'valueOf', jcall(br, 'readLine')))
        i = jcast('int', 0)
        while (i < t):
            n = jnew('BigInteger', jcall(br, 'readLine'))
            # isProbablePrime方法包含MillerRabin和LucasLehmer测试
            # 给定测试次数s即可
            jcall(out, 'println', ('Yes' if jcall(n, 'isProbablePrime', Code02_LargeNumberIsPrime3.s) else 'No'))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LargeNumberIsPrime3.s = jcast('int', 10)

if __name__ == '__main__':
    Code02_LargeNumberIsPrime3.main([])

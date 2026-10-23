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

# 修理宝塔
# 一共有编号1~n的宝塔，其中a号和b号宝塔已经修好了
# Yuwgna和Iaka两个人轮流修塔，Yuwgna先手，Iaka后手，谁先修完所有的塔谁赢
# 每次可以选择j+k号或者j-k号塔进行修理，其中j和k是任意两个已经修好的塔
# 也就是输入n、a、b，如果先手赢打印"Yuwgna"，后手赢打印"Iaka"
# 2 <= n <= 2 * 10^4
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=5512
# 测试链接 : https://vjudge.net/problem/HDU-5512
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Pagodas:
    __java_fields__ = {}
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code02_Pagodas.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        cases = jcast('int', jcast('int', jget(in_, 'nval')))
        t = jcast('int', 1)
        n = 0
        a = 0
        b = 0
        while (t <= cases):
            jcall(in_, 'nextToken')
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'print', jadd(jadd('Case #', t), ': '))
            if (jcast('int', (jcast('int', jdiv(n, Code02_Pagodas.gcd(a, b))) & 1)) == 1):
                jcall(out, 'println', 'Yuwgna')
            else:
                jcall(out, 'println', 'Iaka')
            t = jcast('int', (t + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_Pagodas.main([])

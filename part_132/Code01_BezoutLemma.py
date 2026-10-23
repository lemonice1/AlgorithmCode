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

# 裴蜀定理模版题
# 给定长度为n的一组整数值[a1, a2, a3...]，你找到一组数值[x1, x2, x3...]
# 要让a1*x1 + a2*x2 + a3*x3...得到的结果为最小正整数
# 返回能得到的最小正整数是多少
# 1 <= n <= 20
# 1 <= ai <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4549
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_BezoutLemma:
    __java_fields__ = {}
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code01_BezoutLemma.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            ans = jcast('int', Code01_BezoutLemma.gcd(jstatic('Math', 'abs', jcast('int', jget(in_, 'nval'))), ans))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_BezoutLemma.main([])

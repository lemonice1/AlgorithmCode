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

# 任意前缀上红多于黑
# 有n个红和n个黑，要组成2n长度的数列，保证任意前缀上，红的数量 >= 黑的数量
# 返回有多少种排列方法，答案对 100 取模
# 1 <= n <= 100
# 测试链接 : https://www.luogu.com.cn/problem/P1722
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_RedMore:
    __java_fields__ = {'MOD': 'MOD'}
    MOD = 0
    # 因为取模的数字含有很多因子
    # 无法用费马小定理或者扩展欧几里得求逆元
    # 同时注意到n的范围并不大，直接使用公式4
    @staticmethod
    def compute(n):
        n = jcast('int', n)
        f = jarray('long', [jcast('int', jadd(n, 1))])
        jset(f, 0, jset(f, 1, 1))
        i = jcast('int', 2)
        while (i <= n):
            l = jcast('int', 0)
            r = jcast('int', jcast('int', (i - 1)))
            while (l < i):
                f[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(f[i], jcast('long', jmod(jcast('long', (f[l] * f[r])), Code03_RedMore.MOD)))), Code03_RedMore.MOD)))
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
            i = jcast('int', (i + 1))
        return jcast('long', f[n])

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code03_RedMore.compute(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_RedMore.MOD = jcast('int', 100)

if __name__ == '__main__':
    Code03_RedMore.main([])

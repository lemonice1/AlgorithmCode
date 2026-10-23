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

# 不含递增三元组的排列方法数
# 数字从1到n，可以形成很多排列，要求任意从左往右的三个位置，不能出现依次递增的样子
# 返回排列的方法数，答案对 1000000 取模
# 1 <= n <= 1000
# 测试链接 : https://www.luogu.com.cn/problem/SP7897
# 测试链接 : https://www.spoj.com/problems/SKYLINE
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Skyline:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'f': 'f'}
    MOD = 0
    MAXN = 0
    f = None
    # 因为取模的数字含有很多因子
    # 无法用费马小定理或者扩展欧几里得求逆元
    # 同时注意到n的范围并不大，直接使用公式4
    @staticmethod
    def build():
        jset(Code07_Skyline.f, 0, jset(Code07_Skyline.f, 1, 1))
        i = jcast('int', 2)
        while (i < Code07_Skyline.MAXN):
            l = jcast('int', 0)
            r = jcast('int', jcast('int', (i - 1)))
            while (l < i):
                Code07_Skyline.f[i] = jcast('long', jcast('long', jmod(jcast('long', jadd(Code07_Skyline.f[i], jcast('long', jmod(jcast('long', (Code07_Skyline.f[l] * Code07_Skyline.f[r])), Code07_Skyline.MOD)))), Code07_Skyline.MOD)))
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Skyline.build()
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            try:
                n = jcast('int', jcast('int', jget(in_, 'nval')))
                if (n == 0):
                    raise JBreak(None)
                jcall(out, 'println', Code07_Skyline.f[n])
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Skyline.MOD = jcast('int', 1000000)
Code07_Skyline.MAXN = jcast('int', 1001)
Code07_Skyline.f = jarray('long', [Code07_Skyline.MAXN])

if __name__ == '__main__':
    Code07_Skyline.main([])

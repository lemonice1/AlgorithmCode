# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 两个排列的最长公共子序列长度
# 给出由1~n这些数字组成的两个排列
# 求它们的最长公共子序列长度
# n <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1439
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_PermutationLCS:
    __java_fields__ = {'MAXN': 'MAXN', 'a': 'a', 'b': 'b', 'where': 'where', 'ends': 'ends', 'n': 'n'}
    MAXN = 0
    a = None
    b = None
    where = None
    ends = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_PermutationLCS.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_PermutationLCS.n):
                jcall(in_, 'nextToken')
                Code03_PermutationLCS.a[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 0)
            while (i < Code03_PermutationLCS.n):
                jcall(in_, 'nextToken')
                Code03_PermutationLCS.b[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_PermutationLCS.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        i = jcast('int', 0)
        while (i < Code03_PermutationLCS.n):
            jset(Code03_PermutationLCS.where, Code03_PermutationLCS.a[i], i)
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code03_PermutationLCS.n):
            Code03_PermutationLCS.b[i] = jcast('int', Code03_PermutationLCS.where[Code03_PermutationLCS.b[i]])
            i = jcast('int', (i + 1))
        return jcast('int', Code03_PermutationLCS.lis())

    # 讲解072 - 最长递增子序列及其扩展
    @staticmethod
    def lis():
        len = jcast('int', 0)
        i = jcast('int', 0)
        find = 0
        while (i < Code03_PermutationLCS.n):
            find = jcast('int', Code03_PermutationLCS.bs(len, Code03_PermutationLCS.b[i]))
            if (find == jcast('int', (-1))):
                jset(Code03_PermutationLCS.ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], Code03_PermutationLCS.b[i])
            else:
                Code03_PermutationLCS.ends[find] = jcast('int', Code03_PermutationLCS.b[i])
            i = jcast('int', (i + 1))
        return jcast('int', len)

    @staticmethod
    def bs(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code03_PermutationLCS.ends[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_PermutationLCS.MAXN = jcast('int', 100001)
Code03_PermutationLCS.a = jarray('int', [Code03_PermutationLCS.MAXN])
Code03_PermutationLCS.b = jarray('int', [Code03_PermutationLCS.MAXN])
Code03_PermutationLCS.where = jarray('int', [Code03_PermutationLCS.MAXN])
Code03_PermutationLCS.ends = jarray('int', [Code03_PermutationLCS.MAXN])
Code03_PermutationLCS.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_PermutationLCS.main([])

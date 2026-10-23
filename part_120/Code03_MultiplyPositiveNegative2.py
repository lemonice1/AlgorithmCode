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

# 感谢热心的同学，找到了题目3的在线测试
# 测试链接 : https://codeforces.com/problemset/problem/1215/B
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_MultiplyPositiveNegative2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'arr': 'arr', 'ans1': 'ans1', 'ans2': 'ans2'}
    MAXN = 0
    n = 0
    arr = None
    # 结果可能很大，所以用long类型
    ans1 = 0
    ans2 = 0
    @staticmethod
    def compute():
        cnt = jarray('int', [2])
        cnt[0] = jcast('int', 1)
        cnt[1] = jcast('int', 0)
        Code03_MultiplyPositiveNegative2.ans1 = jcast('long', jset(Code03_MultiplyPositiveNegative2, 'ans2', 0))
        i = jcast('int', 1)
        cur = jcast('int', 0)
        while (i <= Code03_MultiplyPositiveNegative2.n):
            cur = jcast('int', jcast('int', (cur ^ (0 if (Code03_MultiplyPositiveNegative2.arr[i] > 0) else 1))))
            Code03_MultiplyPositiveNegative2.ans1 = jcast('long', jcast('long', jadd(Code03_MultiplyPositiveNegative2.ans1, cnt[cur])))
            Code03_MultiplyPositiveNegative2.ans2 = jcast('long', jcast('long', jadd(Code03_MultiplyPositiveNegative2.ans2, cnt[jcast('int', (cur ^ 1))])))
            cnt[cur] = jcast('int', (cnt[cur] + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_MultiplyPositiveNegative2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code03_MultiplyPositiveNegative2.n):
            jcall(in_, 'nextToken')
            Code03_MultiplyPositiveNegative2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code03_MultiplyPositiveNegative2.compute()
        jcall(out, 'println', jadd(jadd(Code03_MultiplyPositiveNegative2.ans2, ' '), Code03_MultiplyPositiveNegative2.ans1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_MultiplyPositiveNegative2.MAXN = jcast('int', 200001)
Code03_MultiplyPositiveNegative2.n = jcast('int', 0)
Code03_MultiplyPositiveNegative2.arr = jarray('int', [Code03_MultiplyPositiveNegative2.MAXN])
Code03_MultiplyPositiveNegative2.ans1 = jcast('long', 0)
Code03_MultiplyPositiveNegative2.ans2 = jcast('long', 0)

if __name__ == '__main__':
    Code03_MultiplyPositiveNegative2.main([])

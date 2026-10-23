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

# 笛卡尔树模版(Python版)
# 给定一个长度为n的数组arr，下标从1开始
# 构建一棵二叉树，下标按照搜索二叉树组织，值按照小根堆组织
# 建树的过程要求时间复杂度O(n)
# 建树之后，为了验证
# 打印，i * (left[i] + 1)，所有信息异或起来的值
# 打印，i * (right[i] + 1)，所有信息异或起来的值
# 1 <= n <= 10^7
# 测试链接 : https://www.luogu.com.cn/problem/P5854
# 下面为对应算法的 Python 实现，保留原算法逻辑
# 这是洛谷平台没有照顾各种语言的实现所导致的
# 对应实现可参考 Code01_DescartesTree2.py
# 对应实现保留相同的算法逻辑
# 在真正笔试、比赛时，一定是兼顾各种语言的，该实现是一定正确的
class Code01_DescartesTree1:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'left': 'left', 'right': 'right', 'stack': 'stack', 'n': 'n'}
    MAXN = 0
    arr = None
    left = None
    right = None
    stack = None
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 1)
        top = jcast('int', 0)
        pos = jcast('int', 0)
        while (i <= Code01_DescartesTree1.n):
            pos = jcast('int', top)
            while ((pos > 0) and (Code01_DescartesTree1.arr[Code01_DescartesTree1.stack[pos]] > Code01_DescartesTree1.arr[i])):
                pos = jcast('int', (pos - 1))
            if (pos > 0):
                jset(Code01_DescartesTree1.right, Code01_DescartesTree1.stack[pos], i)
            if (pos < top):
                Code01_DescartesTree1.left[i] = jcast('int', Code01_DescartesTree1.stack[jcast('int', jadd(pos, 1))])
            jset(Code01_DescartesTree1.stack, (pos := jcast('int', (pos + (1)))), i)
            top = jcast('int', pos)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_DescartesTree1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code01_DescartesTree1.n):
            jcall(in_, 'nextToken')
            Code01_DescartesTree1.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_DescartesTree1.build()
        ans1 = jcast('long', 0)
        ans2 = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code01_DescartesTree1.n):
            ans1 = jcast('long', jcast('long', (ans1 ^ jcast('long', (jcast('long', i) * jcast('int', jadd(Code01_DescartesTree1.left[i], 1)))))))
            ans2 = jcast('long', jcast('long', (ans2 ^ jcast('long', (jcast('long', i) * jcast('int', jadd(Code01_DescartesTree1.right[i], 1)))))))
            i = jcast('int', (i + 1))
        jcall(out, 'println', jadd(jadd(ans1, ' '), ans2))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DescartesTree1.MAXN = jcast('int', 10000001)
Code01_DescartesTree1.arr = jarray('int', [Code01_DescartesTree1.MAXN])
Code01_DescartesTree1.left = jarray('int', [Code01_DescartesTree1.MAXN])
Code01_DescartesTree1.right = jarray('int', [Code01_DescartesTree1.MAXN])
Code01_DescartesTree1.stack = jarray('int', [Code01_DescartesTree1.MAXN])
Code01_DescartesTree1.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_DescartesTree1.main([])

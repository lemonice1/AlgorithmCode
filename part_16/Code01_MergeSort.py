# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 归并排序，acm练习风格
# 测试链接 : https://www.luogu.com.cn/problem/P1177
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MergeSort:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'help': 'help', 'n': 'n'}
    MAXN = 0
    arr = None
    help = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_MergeSort.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code01_MergeSort.n):
            jcall(in_, 'nextToken')
            Code01_MergeSort.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # mergeSort1(0, n - 1);
        Code01_MergeSort.mergeSort2()
        i = jcast('int', 0)
        while (i < jcast('int', (Code01_MergeSort.n - 1))):
            jcall(out, 'print', jadd(Code01_MergeSort.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_MergeSort.arr[jcast('int', (Code01_MergeSort.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 归并排序递归版
    # 假设l...r一共n个数
    # T(n) = 2 * T(n/2) + O(n)
    # a = 2, b = 2, c = 1
    # 根据master公式，时间复杂度O(n * logn)
    # 空间复杂度O(n)
    @staticmethod
    def mergeSort1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code01_MergeSort.mergeSort1(l, m)
        Code01_MergeSort.mergeSort1(jcast('int', jadd(m, 1)), r)
        Code01_MergeSort.merge(l, m, r)

    # 归并排序非递归版
    # 时间复杂度O(n * logn)
    # 空间复杂度O(n)
    @staticmethod
    def mergeSort2():
        # 一共发生O(logn)次
        l = 0
        m = 0
        r = 0
        step = jcast('int', 1)
        while (step < Code01_MergeSort.n):
            try:
                # 内部分组merge，时间复杂度O(n)
                l = jcast('int', 0)
                while (l < Code01_MergeSort.n):
                    try:
                        m = jcast('int', jcast('int', (jcast('int', jadd(l, step)) - 1)))
                        if (jcast('int', jadd(m, 1)) >= Code01_MergeSort.n):
                            raise JBreak(None)
                        r = jcast('int', jstatic('Math', 'min', jcast('int', (jcast('int', jadd(l, jcast('int', (step << (1 & 31))))) - 1)), jcast('int', (Code01_MergeSort.n - 1))))
                        Code01_MergeSort.merge(l, m, r)
                        l = jcast('int', jcast('int', jadd(r, 1)))
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            step = jcast('int', jcast('int', (step << (1 & 31))))

    # l....r 一共有n个数
    # O(n)
    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code01_MergeSort.help, ((_java_old_5 := i), (i := jcast('int', (i + (1)))), _java_old_5)[2], (Code01_MergeSort.arr[((_java_old_3 := a), (a := jcast('int', (a + (1)))), _java_old_3)[2]] if (Code01_MergeSort.arr[a] <= Code01_MergeSort.arr[b]) else Code01_MergeSort.arr[((_java_old_4 := b), (b := jcast('int', (b + (1)))), _java_old_4)[2]]))
        # 左侧指针、右侧指针，必有一个越界、另一个不越界
        while (a <= m):
            jset(Code01_MergeSort.help, ((_java_old_7 := i), (i := jcast('int', (i + (1)))), _java_old_7)[2], Code01_MergeSort.arr[((_java_old_6 := a), (a := jcast('int', (a + (1)))), _java_old_6)[2]])
        while (b <= r):
            jset(Code01_MergeSort.help, ((_java_old_9 := i), (i := jcast('int', (i + (1)))), _java_old_9)[2], Code01_MergeSort.arr[((_java_old_8 := b), (b := jcast('int', (b + (1)))), _java_old_8)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code01_MergeSort.arr[i] = jcast('int', Code01_MergeSort.help[i])
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MergeSort.MAXN = jcast('int', 100001)
Code01_MergeSort.arr = jarray('int', [Code01_MergeSort.MAXN])
Code01_MergeSort.help = jarray('int', [Code01_MergeSort.MAXN])
Code01_MergeSort.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_MergeSort.main([])

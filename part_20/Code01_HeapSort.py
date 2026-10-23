# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 堆结构和堆排序，acm练习风格
# 测试链接 : https://www.luogu.com.cn/problem/P1177
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_HeapSort:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n'}
    MAXN = 0
    arr = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_HeapSort.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code01_HeapSort.n):
            jcall(in_, 'nextToken')
            Code01_HeapSort.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # heapSort1();
        Code01_HeapSort.heapSort2()
        i = jcast('int', 0)
        while (i < jcast('int', (Code01_HeapSort.n - 1))):
            jcall(out, 'print', jadd(Code01_HeapSort.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_HeapSort.arr[jcast('int', (Code01_HeapSort.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # i位置的数，向上调整大根堆
    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code01_HeapSort.arr[i] > Code01_HeapSort.arr[jcast('int', jdiv(jcast('int', (i - 1)), 2))]):
            Code01_HeapSort.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    # i位置的数，向下调整大根堆
    # 当前堆的大小为size
    @staticmethod
    def heapify(i, size):
        i = jcast('int', i)
        size = jcast('int', size)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < size):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < size) and (Code01_HeapSort.arr[jcast('int', jadd(l, 1))] > Code01_HeapSort.arr[l])) else l))
                best = jcast('int', (best if (Code01_HeapSort.arr[best] > Code01_HeapSort.arr[i]) else i))
                if (best == i):
                    raise JBreak(None)
                Code01_HeapSort.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_HeapSort.arr[i])
        Code01_HeapSort.arr[i] = jcast('int', Code01_HeapSort.arr[j])
        Code01_HeapSort.arr[j] = jcast('int', tmp)

    # 从顶到底建立大根堆，O(n * logn)
    # 依次弹出堆内最大值并排好序，O(n * logn)
    # 整体时间复杂度O(n * logn)
    @staticmethod
    def heapSort1():
        i = jcast('int', 0)
        while (i < Code01_HeapSort.n):
            Code01_HeapSort.heapInsert(i)
            i = jcast('int', (i + 1))
        size = jcast('int', Code01_HeapSort.n)
        while (size > 1):
            Code01_HeapSort.swap(0, (size := jcast('int', (size + (-1)))))
            Code01_HeapSort.heapify(0, size)

    # 从底到顶建立大根堆，O(n)
    # 依次弹出堆内最大值并排好序，O(n * logn)
    # 整体时间复杂度O(n * logn)
    @staticmethod
    def heapSort2():
        i = jcast('int', jcast('int', (Code01_HeapSort.n - 1)))
        while (i >= 0):
            Code01_HeapSort.heapify(i, Code01_HeapSort.n)
            i = jcast('int', (i - 1))
        size = jcast('int', Code01_HeapSort.n)
        while (size > 1):
            Code01_HeapSort.swap(0, (size := jcast('int', (size + (-1)))))
            Code01_HeapSort.heapify(0, size)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_HeapSort.MAXN = jcast('int', 100001)
Code01_HeapSort.arr = jarray('int', [Code01_HeapSort.MAXN])
Code01_HeapSort.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_HeapSort.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 随机快速排序，acm练习风格
# 测试链接 : https://www.luogu.com.cn/problem/P1177
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_QuickSort:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'first': 'first', 'last': 'last'}
    MAXN = 0
    arr = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_QuickSort.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code01_QuickSort.n):
            jcall(in_, 'nextToken')
            Code01_QuickSort.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_QuickSort.quickSort2(0, jcast('int', (Code01_QuickSort.n - 1)))
        i = jcast('int', 0)
        while (i < jcast('int', (Code01_QuickSort.n - 1))):
            jcall(out, 'print', jadd(Code01_QuickSort.arr[i], ' '))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code01_QuickSort.arr[jcast('int', (Code01_QuickSort.n - 1))])
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 随机快速排序经典版(不推荐)
    # 甚至在洛谷上测试因为递归开太多层会爆栈导致出错
    @staticmethod
    def quickSort1(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        # l == r，只有一个数
        # l > r，范围不存在，不用管
        if (l >= r):
            return
        # 随机这一下，常数时间比较大
        # 但只有这一下随机，才能在概率上把快速排序的时间复杂度收敛到O(n * logn)
        # l......r 随机选一个位置，x这个值，做划分
        x = jcast('int', Code01_QuickSort.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
        mid = jcast('int', Code01_QuickSort.partition1(l, r, x))
        Code01_QuickSort.quickSort1(l, jcast('int', (mid - 1)))
        Code01_QuickSort.quickSort1(jcast('int', jadd(mid, 1)), r)

    # 已知arr[l....r]范围上一定有x这个值
    # 划分数组 <=x放左边，>x放右边
    # 并且确保划分完成后<=x区域的最后一个数字是x
    @staticmethod
    def partition1(l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        # a : arr[l....a-1]范围是<=x的区域
        # xi : 记录在<=x的区域上任何一个x的位置，哪一个都可以
        a = jcast('int', l)
        xi = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code01_QuickSort.arr[i] <= x):
                Code01_QuickSort.swap(a, i)
                if (Code01_QuickSort.arr[a] == x):
                    xi = jcast('int', a)
                a = jcast('int', (a + 1))
            i = jcast('int', (i + 1))
        Code01_QuickSort.swap(xi, jcast('int', (a - 1)))
        return jcast('int', jcast('int', (a - 1)))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_QuickSort.arr[i])
        Code01_QuickSort.arr[i] = jcast('int', Code01_QuickSort.arr[j])
        Code01_QuickSort.arr[j] = jcast('int', tmp)

    # 随机快速排序改进版(推荐)
    #
    @staticmethod
    def quickSort2(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        # 随机这一下，常数时间比较大
        # 但只有这一下随机，才能在概率上把快速排序的时间复杂度收敛到O(n * logn)
        x = jcast('int', Code01_QuickSort.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
        Code01_QuickSort.partition2(l, r, x)
        # 为了防止底层的递归过程覆盖全局变量
        # 这里用临时变量记录first、last
        left = jcast('int', Code01_QuickSort.first)
        right = jcast('int', Code01_QuickSort.last)
        Code01_QuickSort.quickSort2(l, jcast('int', (left - 1)))
        Code01_QuickSort.quickSort2(jcast('int', jadd(right, 1)), r)

    # 荷兰国旗问题
    first = 0
    last = 0
    # 已知arr[l....r]范围上一定有x这个值
    # 划分数组 <x放左边，==x放中间，>x放右边
    # 把全局变量first, last，更新成==x区域的左右边界
    @staticmethod
    def partition2(l, r, x):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        Code01_QuickSort.first = jcast('int', l)
        Code01_QuickSort.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code01_QuickSort.last):
            if (Code01_QuickSort.arr[i] == x):
                i = jcast('int', (i + 1))
            else:
                if (Code01_QuickSort.arr[i] < x):
                    Code01_QuickSort.swap(((_java_obj_1 := Code01_QuickSort), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code01_QuickSort.swap(i, ((_java_obj_5 := Code01_QuickSort), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_QuickSort.MAXN = jcast('int', 100001)
Code01_QuickSort.arr = jarray('int', [Code01_QuickSort.MAXN])
Code01_QuickSort.n = jcast('int', 0)
Code01_QuickSort.first = jcast('int', 0)
Code01_QuickSort.last = jcast('int', 0)

if __name__ == '__main__':
    Code01_QuickSort.main([])

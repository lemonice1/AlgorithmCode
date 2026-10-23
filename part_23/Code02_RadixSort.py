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

# 基数排序
# 测试链接 : https://leetcode.cn/problems/sort-an-array/
class Code02_RadixSort:
    __java_fields__ = {'BASE': 'BASE', 'MAXN': 'MAXN', 'help': 'help', 'cnts': 'cnts'}
    # 可以设置进制，不一定10进制，随你设置
    BASE = 0
    MAXN = 0
    help = None
    cnts = None
    @staticmethod
    def sortArray(arr):
        if (jget(arr, 'length') > 1):
            # 如果会溢出，那么要改用long类型数组来排序
            n = jcast('int', jget(arr, 'length'))
            # 找到数组中的最小值
            min = jcast('int', arr[0])
            i = jcast('int', 1)
            while (i < n):
                min = jcast('int', jstatic('Math', 'min', min, arr[i]))
                i = jcast('int', (i + 1))
            max = jcast('int', 0)
            i = jcast('int', 0)
            while (i < n):
                # 数组中的每个数字，减去数组中的最小值，就把arr转成了非负数组
                arr[i] = jcast('int', jcast('int', (arr[i] - min)))
                # 记录数组中的最大值
                max = jcast('int', jstatic('Math', 'max', max, arr[i]))
                i = jcast('int', (i + 1))
            # 根据最大值在BASE进制下的位数，决定基数排序做多少轮
            Code02_RadixSort.radixSort(arr, n, Code02_RadixSort.bits(max))
            # 数组中所有数都减去了最小值，所以最后不要忘了还原
            i = jcast('int', 0)
            while (i < n):
                arr[i] = jcast('int', jcast('int', jadd(arr[i], min)))
                i = jcast('int', (i + 1))
        return arr

    # 返回number在BASE进制下有几位
    @staticmethod
    def bits(number):
        number = jcast('int', number)
        ans = jcast('int', 0)
        while (number > 0):
            ans = jcast('int', (ans + 1))
            number = jcast('int', jcast('int', jdiv(number, Code02_RadixSort.BASE)))
        return jcast('int', ans)

    # 基数排序核心代码
    # arr内要保证没有负数
    # n是arr的长度
    # bits是arr中最大值在BASE进制下有几位
    @staticmethod
    def radixSort(arr, n, bits):
        n = jcast('int', n)
        bits = jcast('int', bits)
        # 理解的时候可以假设BASE = 10
        offset = jcast('int', 1)
        while (bits > 0):
            jstatic('Arrays', 'fill', Code02_RadixSort.cnts, 0)
            i = jcast('int', 0)
            while (i < n):
                # 数字提取某一位的技巧
                ((_java_obj_1 := Code02_RadixSort.cnts), (_java_key_2 := jcast('int', jmod(jcast('int', jdiv(arr[i], offset)), Code02_RadixSort.BASE))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                i = jcast('int', (i + 1))
            # 处理成前缀次数累加的形式
            i = jcast('int', 1)
            while (i < Code02_RadixSort.BASE):
                Code02_RadixSort.cnts[i] = jcast('int', jcast('int', jadd(Code02_RadixSort.cnts[i], Code02_RadixSort.cnts[jcast('int', (i - 1))])))
                i = jcast('int', (i + 1))
            i = jcast('int', jcast('int', (n - 1)))
            while (i >= 0):
                # 前缀数量分区的技巧
                # 数字提取某一位的技巧
                jset(Code02_RadixSort.help, ((_java_obj_4 := Code02_RadixSort.cnts), (_java_key_5 := jcast('int', jmod(jcast('int', jdiv(arr[i], offset)), Code02_RadixSort.BASE))), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3], arr[i])
                i = jcast('int', (i - 1))
            i = jcast('int', 0)
            while (i < n):
                arr[i] = jcast('int', Code02_RadixSort.help[i])
                i = jcast('int', (i + 1))
            offset = jcast('int', jcast('int', (offset * Code02_RadixSort.BASE)))
            bits = jcast('int', (bits - 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_RadixSort.BASE = jcast('int', 10)
Code02_RadixSort.MAXN = jcast('int', 50001)
Code02_RadixSort.help = jarray('int', [Code02_RadixSort.MAXN])
Code02_RadixSort.cnts = jarray('int', [Code02_RadixSort.BASE])

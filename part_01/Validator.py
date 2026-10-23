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

class Validator:
    __java_fields__ = {}
    # 为了验证
    @staticmethod
    def main(args):
        # 随机数组最大长度
        N = jcast('int', 200)
        # 随机数组每个值，在1~V之间等概率随机
        V = jcast('int', 1000)
        # testTimes : 测试次数
        testTimes = jcast('int', 50000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            # 随机得到一个长度，长度在[0~N-1]
            n = jcast('int', jcast('int', (jstatic('Math', 'random') * N)))
            # 得到随机数组
            arr = Validator.randomArray(n, V)
            arr1 = Validator.copyArray(arr)
            arr2 = Validator.copyArray(arr)
            arr3 = Validator.copyArray(arr)
            Validator.selectionSort(arr1)
            Validator.bubbleSort(arr2)
            Validator.insertionSort(arr3)
            if ((not Validator.sameArray(arr1, arr2)) or (not Validator.sameArray(arr1, arr3))):
                jprint('出错了!', newline=True)
                # 当有错了
                # 打印是什么例子，出错的
                # 打印三个功能，各自排序成了什么样
                # 可能要把例子带入，每个方法，去debug！
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 为了验证
    # 得到一个随机数组，长度是n
    # 数组中每个数，都在1~v之间，随机得到
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        arr = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            # random.random() -> double -> [0,1)范围山的一个小数，0.37463473126、0.001231231，等概率！
            # random.random() * v -> double -> [0,v)一个小数，依然等概率
            # (int)(random.random() * v) -> int -> 0 1 2 3 ... v-1，等概率的！
            # (int) (random.random() * v) + 1 -> int -> 1 2 3 .... v，等概率的！
            jset(arr, i, jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * v)), 1)))
            i = jcast('int', (i + 1))
        return arr

    # 为了验证
    @staticmethod
    def copyArray(arr):
        n = jcast('int', jget(arr, 'length'))
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            ans[i] = jcast('int', arr[i])
            i = jcast('int', (i + 1))
        return ans

    # 为了验证
    @staticmethod
    def sameArray(arr1, arr2):
        n = jcast('int', jget(arr1, 'length'))
        i = jcast('int', 0)
        while (i < n):
            if (arr1[i] != arr2[i]):
                return jcast('boolean', False)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    # 数组中交换i和j位置的数
    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    # 选择排序
    @staticmethod
    def selectionSort(arr):
        if ((arr == None) or (jget(arr, 'length') < 2)):
            return
        minIndex = 0
        i = jcast('int', 0)
        while (i < jcast('int', (jget(arr, 'length') - 1))):
            minIndex = jcast('int', i)
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j < jget(arr, 'length')):
                if (arr[j] < arr[minIndex]):
                    minIndex = jcast('int', j)
                j = jcast('int', (j + 1))
            Validator.swap(arr, i, minIndex)
            i = jcast('int', (i + 1))

    # 冒泡排序
    @staticmethod
    def bubbleSort(arr):
        if ((arr == None) or (jget(arr, 'length') < 2)):
            return
        end = jcast('int', jcast('int', (jget(arr, 'length') - 1)))
        while (end > 0):
            i = jcast('int', 0)
            while (i < end):
                if (arr[i] > arr[jcast('int', jadd(i, 1))]):
                    Validator.swap(arr, i, jcast('int', jadd(i, 1)))
                i = jcast('int', (i + 1))
            end = jcast('int', (end - 1))

    # 插入排序
    @staticmethod
    def insertionSort(arr):
        if ((arr == None) or (jget(arr, 'length') < 2)):
            return
        i = jcast('int', 1)
        while (i < jget(arr, 'length')):
            j = jcast('int', jcast('int', (i - 1)))
            while ((j >= 0) and (arr[j] > arr[jcast('int', jadd(j, 1))])):
                Validator.swap(arr, j, jcast('int', jadd(j, 1)))
                j = jcast('int', (j - 1))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Validator.main([])

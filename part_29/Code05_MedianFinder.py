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

# 快速获得数据流的中位数的结构
class Code05_MedianFinder:
    __java_fields__ = {}
    # 测试链接 : https://leetcode.cn/problems/find-median-from-data-stream/
    class MedianFinder:
        __java_fields__ = {'maxHeap': 'maxHeap', 'minHeap': 'minHeap'}
        # maxHeap：实例字段，在构造函数中初始化。
        # minHeap：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.maxHeap = jnew('PriorityQueue', (lambda a, b: (b - a)))
            self.minHeap = jnew('PriorityQueue', (lambda a, b: (a - b)))

        def addNum(self, num):
            num = jcast('int', num)
            if (jcall(self.maxHeap, 'isEmpty') or (jcall(self.maxHeap, 'peek') >= num)):
                jcall(self.maxHeap, 'add', num)
            else:
                jcall(self.minHeap, 'add', num)
            self.balance()

        def findMedian(self):
            if (jcall(self.maxHeap, 'size') == jcall(self.minHeap, 'size')):
                return jcast('double', jdiv(jcast('double', jadd(jcall(self.maxHeap, 'peek'), jcall(self.minHeap, 'peek'))), 2))
            else:
                return jcast('double', (jcall(self.maxHeap, 'peek') if (jcall(self.maxHeap, 'size') > jcall(self.minHeap, 'size')) else jcall(self.minHeap, 'peek')))

        def balance(self):
            if (jstatic('Math', 'abs', jcast('int', (jcall(self.maxHeap, 'size') - jcall(self.minHeap, 'size')))) == 2):
                if (jcall(self.maxHeap, 'size') > jcall(self.minHeap, 'size')):
                    jcall(self.minHeap, 'add', jcall(self.maxHeap, 'poll'))
                else:
                    jcall(self.maxHeap, 'add', jcall(self.minHeap, 'poll'))

        def __init__(self, *args, _java_ctor=None):
            self.maxHeap = None
            self.minHeap = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code05_MedianFinder.MedianFinder.MedianFinder")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



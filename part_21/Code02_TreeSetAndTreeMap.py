# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

class Code02_TreeSetAndTreeMap:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        # TreeSet 和 TreeMap 兼容层使用随机化平衡搜索树，操作的期望复杂度为 O(log n)
        treeMap = jnew('TreeMap')
        jcall(treeMap, 'put', 5, '这是5')
        jcall(treeMap, 'put', 7, '这是7')
        jcall(treeMap, 'put', 1, '这是1')
        jcall(treeMap, 'put', 2, '这是2')
        jcall(treeMap, 'put', 3, '这是3')
        jcall(treeMap, 'put', 4, '这是4')
        jcall(treeMap, 'put', 8, '这是8')
        jprint(jcall(treeMap, 'containsKey', 1), newline=True)
        jprint(jcall(treeMap, 'containsKey', 10), newline=True)
        jprint(jcall(treeMap, 'get', 4), newline=True)
        jcall(treeMap, 'put', 4, '张三是4')
        jprint(jcall(treeMap, 'get', 4), newline=True)
        jcall(treeMap, 'remove', 4)
        jprint((jcall(treeMap, 'get', 4) == None), newline=True)
        jprint(jcall(treeMap, 'firstKey'), newline=True)
        jprint(jcall(treeMap, 'lastKey'), newline=True)
        # TreeMap中，所有的key，<= 4且最近的key是什么
        jprint(jcall(treeMap, 'floorKey', 4), newline=True)
        # TreeMap中，所有的key，>= 4且最近的key是什么
        jprint(jcall(treeMap, 'ceilingKey', 4), newline=True)
        jprint('========', newline=True)
        set = jnew('TreeSet')
        jcall(set, 'add', 3)
        jcall(set, 'add', 3)
        jcall(set, 'add', 4)
        jcall(set, 'add', 4)
        jprint(jadd('有序表大小 : ', jcall(set, 'size')), newline=True)
        while (not jcall(set, 'isEmpty')):
            jprint(jcall(set, 'pollFirst'), newline=True)
            # print(set.pollLast())
        # 堆，默认小根堆、如果要大根堆，定制比较器！
        heap1 = jnew('PriorityQueue')
        jcall(heap1, 'add', 3)
        jcall(heap1, 'add', 3)
        jcall(heap1, 'add', 4)
        jcall(heap1, 'add', 4)
        jprint(jadd('堆大小 : ', jcall(heap1, 'size')), newline=True)
        while (not jcall(heap1, 'isEmpty')):
            jprint(jcall(heap1, 'poll'), newline=True)
        # 定制的大根堆，用比较器！
        heap2 = jnew('PriorityQueue', (lambda a, b: (b - a)))
        jcall(heap2, 'add', 3)
        jcall(heap2, 'add', 3)
        jcall(heap2, 'add', 4)
        jcall(heap2, 'add', 4)
        jprint(jadd('堆大小 : ', jcall(heap2, 'size')), newline=True)
        while (not jcall(heap2, 'isEmpty')):
            jprint(jcall(heap2, 'poll'), newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_TreeSetAndTreeMap.main([])

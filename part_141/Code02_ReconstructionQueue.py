# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 重建队列(做到最优时间复杂度)
# 一共n个人，每个人有(a, b)两个数据，数据a表示该人的身高
# 数据b表示该人的要求，站在自己左边的人中，正好有b个人的身高大于等于自己的身高
# 请你把n个人从左到右进行排列，要求每个人的要求都可以满足
# 返回其中一种排列即可，本题的数据保证一定存在这样的排列
# 题解中的绝大多数方法，时间复杂度O(n平方)，但是时间复杂度能做到O(n * log n)
# 测试链接 : https://leetcode.cn/problems/queue-reconstruction-by-height/
class Code02_ReconstructionQueue:
    __java_fields__ = {'MAXN': 'MAXN', 'cnt': 'cnt', 'head': 'head', 'key': 'key', 'height': 'height', 'left': 'left', 'right': 'right', 'value': 'value', 'size': 'size', 'fi': 'fi'}
    @staticmethod
    def reconstructQueue(people):
        jstatic('Arrays', 'sort', people, (lambda a, b: ((b[0] - a[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
        for p in people:
            Code02_ReconstructionQueue._java_add_0(p[0], p[1])
        Code02_ReconstructionQueue.fill(people)
        Code02_ReconstructionQueue.clear()
        return people

    MAXN = 0
    cnt = 0
    head = 0
    key = None
    height = None
    left = None
    right = None
    value = None
    size = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_ReconstructionQueue.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code02_ReconstructionQueue.size[Code02_ReconstructionQueue.left[i]], Code02_ReconstructionQueue.size[Code02_ReconstructionQueue.right[i]])), 1)))
        jset(Code02_ReconstructionQueue.height, i, jcast('int', jadd(jstatic('Math', 'max', Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.left[i]], Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.right[i]]), 1)))

    @staticmethod
    def leftRotate(i):
        i = jcast('int', i)
        r = jcast('int', Code02_ReconstructionQueue.right[i])
        Code02_ReconstructionQueue.right[i] = jcast('int', Code02_ReconstructionQueue.left[r])
        Code02_ReconstructionQueue.left[r] = jcast('int', i)
        Code02_ReconstructionQueue.up(i)
        Code02_ReconstructionQueue.up(r)
        return jcast('int', r)

    @staticmethod
    def rightRotate(i):
        i = jcast('int', i)
        l = jcast('int', Code02_ReconstructionQueue.left[i])
        Code02_ReconstructionQueue.left[i] = jcast('int', Code02_ReconstructionQueue.right[l])
        Code02_ReconstructionQueue.right[l] = jcast('int', i)
        Code02_ReconstructionQueue.up(i)
        Code02_ReconstructionQueue.up(l)
        return jcast('int', l)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        lh = jcast('int', Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.left[i]])
        rh = jcast('int', Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.right[i]])
        if (jcast('int', (lh - rh)) > 1):
            if (Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.left[Code02_ReconstructionQueue.left[i]]] >= Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.right[Code02_ReconstructionQueue.left[i]]]):
                i = jcast('int', Code02_ReconstructionQueue.rightRotate(i))
            else:
                jset(Code02_ReconstructionQueue.left, i, Code02_ReconstructionQueue.leftRotate(Code02_ReconstructionQueue.left[i]))
                i = jcast('int', Code02_ReconstructionQueue.rightRotate(i))
        else:
            if (jcast('int', (rh - lh)) > 1):
                if (Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.right[Code02_ReconstructionQueue.right[i]]] >= Code02_ReconstructionQueue.height[Code02_ReconstructionQueue.left[Code02_ReconstructionQueue.right[i]]]):
                    i = jcast('int', Code02_ReconstructionQueue.leftRotate(i))
                else:
                    jset(Code02_ReconstructionQueue.right, i, Code02_ReconstructionQueue.rightRotate(Code02_ReconstructionQueue.right[i]))
                    i = jcast('int', Code02_ReconstructionQueue.leftRotate(i))
        return jcast('int', i)

    @staticmethod
    def _java_add_0(num, index):
        num = jcast('int', num)
        index = jcast('int', index)
        Code02_ReconstructionQueue.head = jcast('int', Code02_ReconstructionQueue._java_add_1(Code02_ReconstructionQueue.head, index, num, index))

    @staticmethod
    def _java_add_1(i, rank, num, index):
        i = jcast('int', i)
        rank = jcast('int', rank)
        num = jcast('int', num)
        index = jcast('int', index)
        if (i == 0):
            jset(Code02_ReconstructionQueue.key, ((_java_obj_1 := Code02_ReconstructionQueue), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
            Code02_ReconstructionQueue.value[Code02_ReconstructionQueue.cnt] = jcast('int', index)
            jset(Code02_ReconstructionQueue.size, Code02_ReconstructionQueue.cnt, jset(Code02_ReconstructionQueue.height, Code02_ReconstructionQueue.cnt, 1))
            return jcast('int', Code02_ReconstructionQueue.cnt)
        if (Code02_ReconstructionQueue.size[Code02_ReconstructionQueue.left[i]] >= rank):
            jset(Code02_ReconstructionQueue.left, i, Code02_ReconstructionQueue._java_add_1(Code02_ReconstructionQueue.left[i], rank, num, index))
        else:
            jset(Code02_ReconstructionQueue.right, i, Code02_ReconstructionQueue._java_add_1(Code02_ReconstructionQueue.right[i], jcast('int', (jcast('int', (rank - Code02_ReconstructionQueue.size[Code02_ReconstructionQueue.left[i]])) - 1)), num, index))
        Code02_ReconstructionQueue.up(i)
        return jcast('int', Code02_ReconstructionQueue.maintain(i))

    @staticmethod
    def fill(ans):
        Code02_ReconstructionQueue.fi = jcast('int', 0)
        Code02_ReconstructionQueue.inOrder(ans, Code02_ReconstructionQueue.head)

    fi = 0
    @staticmethod
    def inOrder(ans, i):
        i = jcast('int', i)
        if (i == 0):
            return
        Code02_ReconstructionQueue.inOrder(ans, Code02_ReconstructionQueue.left[i])
        jset(ans[Code02_ReconstructionQueue.fi], 0, Code02_ReconstructionQueue.key[i])
        jset(ans[((_java_obj_4 := Code02_ReconstructionQueue), (_java_key_5 := 'fi'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]], 1, Code02_ReconstructionQueue.value[i])
        Code02_ReconstructionQueue.inOrder(ans, Code02_ReconstructionQueue.right[i])

    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.key, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.height, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.left, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.right, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.value, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code02_ReconstructionQueue.size, 1, jcast('int', jadd(Code02_ReconstructionQueue.cnt, 1)), 0)
        Code02_ReconstructionQueue.cnt = jcast('int', 0)
        Code02_ReconstructionQueue.head = jcast('int', 0)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code02_ReconstructionQueue._java_add_0(*args)
        if _java_choice == 1:
            return Code02_ReconstructionQueue._java_add_1(*args)
        raise TypeError("No matching overload for Code02_ReconstructionQueue.add")


Code02_ReconstructionQueue.MAXN = jcast('int', 2001)
Code02_ReconstructionQueue.cnt = jcast('int', 0)
Code02_ReconstructionQueue.head = jcast('int', 0)
Code02_ReconstructionQueue.key = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.height = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.left = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.right = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.value = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.size = jarray('int', [Code02_ReconstructionQueue.MAXN])
Code02_ReconstructionQueue.fi = jcast('int', 0)

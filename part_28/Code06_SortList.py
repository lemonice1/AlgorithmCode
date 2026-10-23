# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 排序链表
# 要求时间复杂度O(n*logn)，额外空间复杂度O(1)，还要求稳定性
# 数组排序做不到，链表排序可以
# 测试链接 : https://leetcode.cn/problems/sort-list/
class Code06_SortList:
    __java_fields__ = {'start': 'start', 'end': 'end'}
    # 不要提交这个类
    class ListNode:
        __java_fields__ = {'val': 'val', 'next': 'next'}
        # val：实例字段，在构造函数中初始化。
        # next：实例字段，在构造函数中初始化。
        def __init__(self, *args, _java_ctor=None):
            self.val = jcast('int', 0)
            self.next = None
            if args:
                raise TypeError('This class has a no-argument constructor')


    # 提交如下的方法
    # 时间复杂度O(n*logn)，额外空间复杂度O(1)，有稳定性
    # 注意为了额外空间复杂度O(1)，所以不能使用递归
    # 因为mergeSort递归需要O(log n)的额外空间
    @staticmethod
    def sortList(head):
        n = jcast('int', 0)
        cur = head
        while (cur != None):
            n = jcast('int', (n + 1))
            cur = jget(cur, 'next')
        # l1...r1 每组的左部分
        # l2...r2 每组的右部分
        # next 下一组的开头
        # lastTeamEnd 上一组的结尾
        l1 = None
        r1 = None
        l2 = None
        r2 = None
        next = None
        lastTeamEnd = None
        step = jcast('int', 1)
        while (step < n):
            try:
                # 第一组很特殊，因为要决定整个链表的头，所以单独处理
                l1 = head
                r1 = Code06_SortList.findEnd(l1, step)
                l2 = jget(r1, 'next')
                r2 = Code06_SortList.findEnd(l2, step)
                next = jget(r2, 'next')
                r1.next = None
                r2.next = None
                Code06_SortList.merge(l1, r1, l2, r2)
                head = Code06_SortList.start
                lastTeamEnd = Code06_SortList.end
                while (next != None):
                    try:
                        l1 = next
                        r1 = Code06_SortList.findEnd(l1, step)
                        l2 = jget(r1, 'next')
                        if (l2 == None):
                            lastTeamEnd.next = l1
                            raise JBreak(None)
                        r2 = Code06_SortList.findEnd(l2, step)
                        next = jget(r2, 'next')
                        r1.next = None
                        r2.next = None
                        Code06_SortList.merge(l1, r1, l2, r2)
                        lastTeamEnd.next = Code06_SortList.start
                        lastTeamEnd = Code06_SortList.end
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
        return head

    # 包括s在内，往下数k个节点返回
    # 如果不够，返回最后一个数到的非空节点
    @staticmethod
    def findEnd(s, k):
        k = jcast('int', k)
        while ((jget(s, 'next') != None) and ((k := jcast('int', (k + (-1)))) != 0)):
            s = jget(s, 'next')
        return s

    start = None
    end = None
    # l1...r1 -> null : 有序的左部分
    # l2...r2 -> null : 有序的右部分
    # 整体merge在一起，保证有序
    # 并且把全局变量start设置为整体的头，全局变量end设置为整体的尾
    @staticmethod
    def merge(l1, r1, l2, r2):
        pre = None
        if (jget(l1, 'val') <= jget(l2, 'val')):
            Code06_SortList.start = l1
            pre = l1
            l1 = jget(l1, 'next')
        else:
            Code06_SortList.start = l2
            pre = l2
            l2 = jget(l2, 'next')
        while ((l1 != None) and (l2 != None)):
            if (jget(l1, 'val') <= jget(l2, 'val')):
                pre.next = l1
                pre = l1
                l1 = jget(l1, 'next')
            else:
                pre.next = l2
                pre = l2
                l2 = jget(l2, 'next')
        if (l1 != None):
            pre.next = l1
            Code06_SortList.end = r1
        else:
            pre.next = l2
            Code06_SortList.end = r2

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_SortList.start = None
Code06_SortList.end = None

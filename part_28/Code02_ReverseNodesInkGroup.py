# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 每k个节点一组翻转链表
# 测试链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/
class Code02_ReverseNodesInkGroup:
    __java_fields__ = {}
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
    @staticmethod
    def reverseKGroup(head, k):
        k = jcast('int', k)
        start = head
        end = Code02_ReverseNodesInkGroup.teamEnd(start, k)
        if (end == None):
            return head
        # 第一组很特殊因为牵扯到换头的问题
        head = end
        Code02_ReverseNodesInkGroup.reverse(start, end)
        # 翻转之后start变成了上一组的结尾节点
        lastTeamEnd = start
        while (jget(lastTeamEnd, 'next') != None):
            start = jget(lastTeamEnd, 'next')
            end = Code02_ReverseNodesInkGroup.teamEnd(start, k)
            if (end == None):
                return head
            Code02_ReverseNodesInkGroup.reverse(start, end)
            lastTeamEnd.next = end
            lastTeamEnd = start
        return head

    # 当前组的开始节点是s，往下数k个找到当前组的结束节点返回
    @staticmethod
    def teamEnd(s, k):
        k = jcast('int', k)
        while (((k := jcast('int', (k + (-1)))) != 0) and (s != None)):
            s = jget(s, 'next')
        return s

    # s -> a -> b -> c -> e -> 下一组的开始节点
    # 上面的链表通过如下的reverse方法调整成 : e -> c -> b -> a -> s -> 下一组的开始节点
    @staticmethod
    def reverse(s, e):
        e = jget(e, 'next')
        pre = None
        cur = s
        next = None
        while (cur != e):
            next = jget(cur, 'next')
            cur.next = pre
            pre = cur
            cur = next
        s.next = e

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



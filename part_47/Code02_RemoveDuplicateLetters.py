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

# 去除重复字母保证剩余字符串的字典序最小
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次
# 需保证 返回结果的字典序最小
# 要求不能打乱其他字符的相对位置
# 测试链接 : https://leetcode.cn/problems/remove-duplicate-letters/
class Code02_RemoveDuplicateLetters:
    __java_fields__ = {'MAXN': 'MAXN', 'cnts': 'cnts', 'enter': 'enter', 'stack': 'stack', 'r': 'r'}
    MAXN = 0
    # 每种字符词频
    cnts = None
    # 每种字符目前有没有进栈
    enter = None
    # 单调栈
    stack = None
    r = 0
    @staticmethod
    def removeDuplicateLetters(str):
        Code02_RemoveDuplicateLetters.r = jcast('int', 0)
        jstatic('Arrays', 'fill', Code02_RemoveDuplicateLetters.cnts, 0)
        jstatic('Arrays', 'fill', Code02_RemoveDuplicateLetters.enter, False)
        s = jcall(str, 'toCharArray')
        for cha in s:
            Code02_RemoveDuplicateLetters.cnts[jcast('int', (cha - jchar('a')))] = jcast('int', (Code02_RemoveDuplicateLetters.cnts[jcast('int', (cha - jchar('a')))] + 1))
        for cur in s:
            # 从左往右依次遍历字符，a -> 0 b -> 1 ... z -> 25
            # cur -> cur - 'a'
            if (not Code02_RemoveDuplicateLetters.enter[jcast('int', (cur - jchar('a')))]):
                while (((Code02_RemoveDuplicateLetters.r > 0) and (Code02_RemoveDuplicateLetters.stack[jcast('int', (Code02_RemoveDuplicateLetters.r - 1))] > cur)) and (Code02_RemoveDuplicateLetters.cnts[jcast('int', (Code02_RemoveDuplicateLetters.stack[jcast('int', (Code02_RemoveDuplicateLetters.r - 1))] - jchar('a')))] > 0)):
                    jset(Code02_RemoveDuplicateLetters.enter, jcast('int', (Code02_RemoveDuplicateLetters.stack[jcast('int', (Code02_RemoveDuplicateLetters.r - 1))] - jchar('a'))), False)
                    Code02_RemoveDuplicateLetters.r = jcast('int', (Code02_RemoveDuplicateLetters.r - 1))
                jset(Code02_RemoveDuplicateLetters.stack, ((_java_obj_1 := Code02_RemoveDuplicateLetters), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], cur)
                Code02_RemoveDuplicateLetters.enter[jcast('int', (cur - jchar('a')))] = jcast('boolean', True)
            Code02_RemoveDuplicateLetters.cnts[jcast('int', (cur - jchar('a')))] = jcast('int', (Code02_RemoveDuplicateLetters.cnts[jcast('int', (cur - jchar('a')))] - 1))
        return jstatic('String', 'valueOf', Code02_RemoveDuplicateLetters.stack, 0, Code02_RemoveDuplicateLetters.r)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_RemoveDuplicateLetters.MAXN = jcast('int', 26)
Code02_RemoveDuplicateLetters.cnts = jarray('int', [Code02_RemoveDuplicateLetters.MAXN])
Code02_RemoveDuplicateLetters.enter = jarray('boolean', [Code02_RemoveDuplicateLetters.MAXN])
Code02_RemoveDuplicateLetters.stack = jarray('char', [Code02_RemoveDuplicateLetters.MAXN])
Code02_RemoveDuplicateLetters.r = jcast('int', 0)

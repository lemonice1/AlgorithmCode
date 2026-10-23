# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 超级回文数中的一个小函数，本身也是一道题 : 判断一个数字是不是回文数
# 测试链接 : https://leetcode.cn/problems/palindrome-number/
class Code03_IsPalindrome:
    __java_fields__ = {}
    @staticmethod
    def isPalindrome(num):
        num = jcast('int', num)
        if (num < 0):
            return jcast('boolean', False)
        offset = jcast('int', 1)
        # 注意这么写是为了防止溢出
        while (jcast('int', jdiv(num, offset)) >= 10):
            offset = jcast('int', jcast('int', (offset * 10)))
        # 首尾判断
        while (num != 0):
            if (jcast('int', jdiv(num, offset)) != jcast('int', jmod(num, 10))):
                return jcast('boolean', False)
            num = jcast('int', jcast('int', jdiv(jcast('int', jmod(num, offset)), 10)))
            offset = jcast('int', jcast('int', jdiv(offset, 100)))
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



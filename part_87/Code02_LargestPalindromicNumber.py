# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大回文数字
# 给你一个仅由数字（0 - 9）组成的字符串num
# 请你找出能够使用num中数字形成的最大回文整数
# 并以字符串形式返回，该整数不含前导零
# 你无需使用num中的所有数字，但你必须使用至少一个数字，数字可以重新排列
# 测试链接 : https://leetcode.cn/problems/largest-palindromic-number/
class Code02_LargestPalindromicNumber:
    __java_fields__ = {}
    @staticmethod
    def largestPalindromic(num):
        n = jcast('int', jcall(num, 'length'))
        # '0' ~ '9'字符对应整数为48 ~ 57
        cnts = jarray('int', [58])
        for a in jcall(num, 'toCharArray'):
            cnts[a] = jcast('int', (cnts[a] + 1))
        ans = jarray('char', [n])
        leftSize = jcast('int', 0)
        mid = jcast('char', 0)
        i = jcast('char', jchar('9'))
        while (i >= jchar('1')):
            if ((jcast('int', (cnts[i] & 1)) == 1) and (mid == 0)):
                mid = jcast('char', i)
            j = jcast('int', jcast('int', jdiv(cnts[i], 2)))
            while (j > 0):
                jset(ans, ((_java_old_1 := leftSize), (leftSize := jcast('int', (leftSize + (1)))), _java_old_1)[2], i)
                j = jcast('int', (j - 1))
            i = jcast('char', (i - 1))
        # '1'~'9'每一种字符出现次数 <= 1
        if (leftSize == 0):
            # '1'~'9'每一种字符出现次数 == 0
            if (mid == 0):
                return '0'
                # '1'~'9'有若干字符出现次数 == 1，其中最大的字符是mid
            else:
                return jstatic('String', 'valueOf', mid)
        # '1'~'9'有若干字符出现次数 >= 2，左部分已经建立，再考虑把'0'字符填进来
        j = jcast('int', jcast('int', jdiv(cnts[jchar('0')], 2)))
        while (j > 0):
            jset(ans, ((_java_old_2 := leftSize), (leftSize := jcast('int', (leftSize + (1)))), _java_old_2)[2], jchar('0'))
            j = jcast('int', (j - 1))
        len = jcast('int', leftSize)
        # 把中点安插进去
        if ((mid == 0) and (jcast('int', (cnts[jchar('0')] & 1)) == 1)):
            mid = jcast('char', jchar('0'))
        if (mid != 0):
            jset(ans, ((_java_old_3 := len), (len := jcast('int', (len + (1)))), _java_old_3)[2], mid)
        # 左部分逆序拷贝给右部分
        i = jcast('int', jcast('int', (leftSize - 1)))
        while (i >= 0):
            jset(ans, ((_java_old_4 := len), (len := jcast('int', (len + (1)))), _java_old_4)[2], ans[i])
            i = jcast('int', (i - 1))
        return jnew('String', ans, 0, len)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



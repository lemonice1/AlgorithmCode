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

# 字符串转化
# 给出两个长度相同的字符串str1和str2
# 请你帮忙判断字符串str1能不能在 零次 或 多次 转化后变成字符串str2
# 每一次转化时，你可以将str1中出现的所有相同字母变成其他任何小写英文字母
# 只有在字符串str1能够通过上述方式顺利转化为字符串str2时才能返回true
# 测试链接 : https://leetcode.cn/problems/string-transforms-into-another-string/
# 测试链接 : https://www.lintcode.com/problem/3869
class Code03_StringTransforms:
    __java_fields__ = {}
    @staticmethod
    def canConvert(str1, str2):
        if jcall(str1, 'equals', str2):
            return jcast('boolean', True)
        # map[x] : str2中字符x的词频
        map = jarray('int', [26])
        # kinds : str2中字符的种类数
        kinds = jcast('int', 0)
        i = jcast('int', 0)
        while (i < jcall(str2, 'length')):
            if (((_java_obj_1 := map), (_java_key_2 := jcast('int', (jcall(str2, 'charAt', i) - jchar('a')))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4] == 0):
                kinds = jcast('int', (kinds + 1))
            i = jcast('int', (i + 1))
        if (kinds == 26):
            return jcast('boolean', False)
        jstatic('Arrays', 'fill', map, jcast('int', (-1)))
        # map[x] = y : str1中的字符x上次出现在str1中的y位置
        i = jcast('int', 0)
        cur = 0
        while (i < jcall(str1, 'length')):
            cur = jcast('int', jcast('int', (jcall(str1, 'charAt', i) - jchar('a'))))
            if ((map[cur] != jcast('int', (-1))) and (jcall(str2, 'charAt', map[cur]) != jcall(str2, 'charAt', i))):
                return jcast('boolean', False)
            map[cur] = jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('boolean', True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



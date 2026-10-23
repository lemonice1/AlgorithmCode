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

# 含有嵌套的字符串解码
# 测试链接 : https://leetcode.cn/problems/decode-string/
class Code02_DecodeString:
    __java_fields__ = {'where': 'where'}
    @staticmethod
    def decodeString(str):
        Code02_DecodeString.where = jcast('int', 0)
        return Code02_DecodeString.f(jcall(str, 'toCharArray'), 0)

    where = 0
    # s[i....]开始计算，遇到字符串终止 或者 遇到 ] 停止
    # 返回 : 自己负责的这一段字符串的结果
    # 返回之间，更新全局变量where，为了上游函数知道从哪继续！
    @staticmethod
    def f(s, i):
        i = jcast('int', i)
        path = jnew('StringBuilder')
        cnt = jcast('int', 0)
        while ((i < jget(s, 'length')) and (s[i] != jchar(']'))):
            if (((s[i] >= jchar('a')) and (s[i] <= jchar('z'))) or ((s[i] >= jchar('A')) and (s[i] <= jchar('Z')))):
                jcall(path, 'append', s[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]])
            else:
                if ((s[i] >= jchar('0')) and (s[i] <= jchar('9'))):
                    cnt = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (cnt * 10)), s[((_java_old_2 := i), (i := jcast('int', (i + (1)))), _java_old_2)[2]])) - jchar('0'))))
                else:
                    # 遇到 [
                    # cnt = 7 * ?
                    jcall(path, 'append', Code02_DecodeString.get(cnt, Code02_DecodeString.f(s, jcast('int', jadd(i, 1)))))
                    i = jcast('int', jcast('int', jadd(Code02_DecodeString.where, 1)))
                    cnt = jcast('int', 0)
        Code02_DecodeString.where = jcast('int', i)
        return jcall(path, 'toString')

    @staticmethod
    def get(cnt, str):
        cnt = jcast('int', cnt)
        builder = jnew('StringBuilder')
        i = jcast('int', 0)
        while (i < cnt):
            jcall(builder, 'append', str)
            i = jcast('int', (i + 1))
        return jcall(builder, 'toString')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DecodeString.where = jcast('int', 0)

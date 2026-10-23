# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长双回文串长度
# 输入字符串s，求s的最长双回文子串t的长度
# 双回文子串就是可以分成两个回文串的字符串
# 比如"aabb"，可以分成"aa"、"bb"
# 测试链接 : https://www.luogu.com.cn/problem/P4555
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_LongestDoublePalindrome:
    __java_fields__ = {'MAXN': 'MAXN', 'ss': 'ss', 'p': 'p', 'left': 'left', 'right': 'right', 'n': 'n'}
    MAXN = 0
    ss = None
    p = None
    left = None
    right = None
    n = 0
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(out, 'println', Code05_LongestDoublePalindrome.compute(jcall(in_, 'readLine')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def compute(s):
        Code05_LongestDoublePalindrome.manacher(s)
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code05_LongestDoublePalindrome.n):
            while (jcast('int', jadd(i, Code05_LongestDoublePalindrome.p[i])) > j):
                Code05_LongestDoublePalindrome.left[j] = jcast('int', jcast('int', (j - i)))
                j = jcast('int', jcast('int', jadd(j, 2)))
            i = jcast('int', (i + 1))
        i = jcast('int', jcast('int', (Code05_LongestDoublePalindrome.n - 1)))
        j = jcast('int', jcast('int', (Code05_LongestDoublePalindrome.n - 1)))
        while (i >= 0):
            while (jcast('int', (i - Code05_LongestDoublePalindrome.p[i])) < j):
                Code05_LongestDoublePalindrome.right[j] = jcast('int', jcast('int', (i - j)))
                j = jcast('int', jcast('int', (j - 2)))
            i = jcast('int', (i - 1))
        ans = jcast('int', 0)
        i = jcast('int', 2)
        while (i <= jcast('int', (Code05_LongestDoublePalindrome.n - 3))):
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(Code05_LongestDoublePalindrome.left[i], Code05_LongestDoublePalindrome.right[i]))))
            i = jcast('int', jcast('int', jadd(i, 2)))
        return jcast('int', ans)

    @staticmethod
    def manacher(str):
        Code05_LongestDoublePalindrome.manacherss(jcall(str, 'toCharArray'))
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < Code05_LongestDoublePalindrome.n):
            len = jcast('int', (jstatic('Math', 'min', Code05_LongestDoublePalindrome.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code05_LongestDoublePalindrome.n) and (jcast('int', (i - len)) >= 0)) and (Code05_LongestDoublePalindrome.ss[jcast('int', jadd(i, len))] == Code05_LongestDoublePalindrome.ss[jcast('int', (i - len))])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code05_LongestDoublePalindrome.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    @staticmethod
    def manacherss(a):
        Code05_LongestDoublePalindrome.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code05_LongestDoublePalindrome.n):
            jset(Code05_LongestDoublePalindrome.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2]]))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_LongestDoublePalindrome.MAXN = jcast('int', 100002)
Code05_LongestDoublePalindrome.ss = jarray('char', [jcast('int', (Code05_LongestDoublePalindrome.MAXN << (1 & 31)))])
Code05_LongestDoublePalindrome.p = jarray('int', [jcast('int', (Code05_LongestDoublePalindrome.MAXN << (1 & 31)))])
Code05_LongestDoublePalindrome.left = jarray('int', [jcast('int', (Code05_LongestDoublePalindrome.MAXN << (1 & 31)))])
Code05_LongestDoublePalindrome.right = jarray('int', [jcast('int', (Code05_LongestDoublePalindrome.MAXN << (1 & 31)))])
Code05_LongestDoublePalindrome.n = jcast('int', 0)

if __name__ == '__main__':
    Code05_LongestDoublePalindrome.main([])

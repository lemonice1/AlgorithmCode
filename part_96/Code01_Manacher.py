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

# Manacher算法模版
# 求字符串s中最长回文子串的长度
# 测试链接 : https://www.luogu.com.cn/problem/P3805
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Manacher:
    __java_fields__ = {'MAXN': 'MAXN', 'ss': 'ss', 'p': 'p', 'n': 'n'}
    MAXN = 0
    ss = None
    p = None
    n = 0
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(out, 'println', Code01_Manacher.manacher(jcall(in_, 'readLine')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    @staticmethod
    def manacher(str):
        Code01_Manacher.manacherss(jcall(str, 'toCharArray'))
        max = jcast('int', 0)
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < Code01_Manacher.n):
            len = jcast('int', (jstatic('Math', 'min', Code01_Manacher.p[jcast('int', (jcast('int', (2 * c)) - i))], jcast('int', (r - i))) if (r > i) else 1))
            while (((jcast('int', jadd(i, len)) < Code01_Manacher.n) and (jcast('int', (i - len)) >= 0)) and (Code01_Manacher.ss[jcast('int', jadd(i, len))] == Code01_Manacher.ss[jcast('int', (i - len))])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            max = jcast('int', jstatic('Math', 'max', max, len))
            Code01_Manacher.p[i] = jcast('int', len)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (max - 1)))

    @staticmethod
    def manacherss(a):
        Code01_Manacher.n = jcast('int', jcast('int', jadd(jcast('int', (jget(a, 'length') * 2)), 1)))
        i = jcast('int', 0)
        j = jcast('int', 0)
        while (i < Code01_Manacher.n):
            jset(Code01_Manacher.ss, i, (jchar('#') if (jcast('int', (i & 1)) == 0) else a[((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2]]))
            i = jcast('int', (i + 1))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Manacher.MAXN = jcast('int', 11000001)
Code01_Manacher.ss = jarray('char', [jcast('int', (Code01_Manacher.MAXN << (1 & 31)))])
Code01_Manacher.p = jarray('int', [jcast('int', (Code01_Manacher.MAXN << (1 & 31)))])
Code01_Manacher.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_Manacher.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 扩展KMP模版，又称Z算法或Z函数
# 给定两个字符串a、b，求出两个数组
# b与b每一个后缀串的最长公共前缀长度，z数组
# b与a每一个后缀串的最长公共前缀长度，e数组
# 计算出要求的两个数组后，输出这两个数组的权值即可
# 对于一个数组x，i位置的权值定义为 : (i * (x[i] + 1))
# 数组权值为所有位置权值的异或和
# 测试链接 : https://www.luogu.com.cn/problem/P5410
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_ExpandKMP:
    __java_fields__ = {'MAXN': 'MAXN', 'z': 'z', 'e': 'e'}
    MAXN = 0
    z = None
    e = None
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        a = jcall(jcall(in_, 'readLine'), 'toCharArray')
        b = jcall(jcall(in_, 'readLine'), 'toCharArray')
        Code02_ExpandKMP.zArray(b, jget(b, 'length'))
        Code02_ExpandKMP.eArray(a, b, jget(a, 'length'), jget(b, 'length'))
        jcall(out, 'println', Code02_ExpandKMP.eor(Code02_ExpandKMP.z, jget(b, 'length')))
        jcall(out, 'println', Code02_ExpandKMP.eor(Code02_ExpandKMP.e, jget(a, 'length')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    # 非常像Manacher算法
    @staticmethod
    def zArray(s, n):
        n = jcast('int', n)
        Code02_ExpandKMP.z[0] = jcast('int', n)
        i = jcast('int', 1)
        c = jcast('int', 1)
        r = jcast('int', 1)
        len = 0
        while (i < n):
            len = jcast('int', (jstatic('Math', 'min', jcast('int', (r - i)), Code02_ExpandKMP.z[jcast('int', (i - c))]) if (r > i) else 0))
            while ((jcast('int', jadd(i, len)) < n) and (s[jcast('int', jadd(i, len))] == s[len])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code02_ExpandKMP.z[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    # 非常像Manacher算法
    @staticmethod
    def eArray(a, b, n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', 0)
        c = jcast('int', 0)
        r = jcast('int', 0)
        len = 0
        while (i < n):
            len = jcast('int', (jstatic('Math', 'min', jcast('int', (r - i)), Code02_ExpandKMP.z[jcast('int', (i - c))]) if (r > i) else 0))
            while (((jcast('int', jadd(i, len)) < n) and (len < m)) and (a[jcast('int', jadd(i, len))] == b[len])):
                len = jcast('int', (len + 1))
            if (jcast('int', jadd(i, len)) > r):
                r = jcast('int', jcast('int', jadd(i, len)))
                c = jcast('int', i)
            Code02_ExpandKMP.e[i] = jcast('int', len)
            i = jcast('int', (i + 1))

    @staticmethod
    def eor(arr, n):
        n = jcast('int', n)
        ans = jcast('long', 0)
        i = jcast('int', 0)
        while (i < n):
            ans = jcast('long', jcast('long', (ans ^ jcast('long', (jcast('long', jcast('int', jadd(i, 1))) * jcast('int', jadd(arr[i], 1)))))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_ExpandKMP.MAXN = jcast('int', 20000001)
Code02_ExpandKMP.z = jarray('int', [Code02_ExpandKMP.MAXN])
Code02_ExpandKMP.e = jarray('int', [Code02_ExpandKMP.MAXN])

if __name__ == '__main__':
    Code02_ExpandKMP.main([])

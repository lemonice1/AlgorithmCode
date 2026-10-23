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

# 根据匹配定义求匹配子串的数量
# 给定长为n的字符串s，以及长度为m的字符串p，还有一个正数k
# s'与s匹配的定义为，s'与s长度相同，且最多有k个位置字符不同
# 要求查找字符串s中有多少子串与字符串p匹配
# 测试链接 : https://www.luogu.com.cn/problem/P3763
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_DNA:
    __java_fields__ = {'MAXN': 'MAXN', 'base': 'base', 'pow': 'pow', 'hashs': 'hashs', 'hashp': 'hashp'}
    MAXN = 0
    base = 0
    pow = None
    hashs = None
    hashp = None
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jstatic('Integer', 'valueOf', jcall(in_, 'readLine')))
        i = jcast('int', 0)
        while (i < n):
            s = jcall(in_, 'readLine')
            p = jcall(in_, 'readLine')
            jcall(out, 'println', Code06_DNA.compute(jcall(s, 'toCharArray'), jcall(p, 'toCharArray'), 3))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    # s中有多少子串修改最多k个位置的字符就可以变成p
    # s长度为n，p长度为m，时间复杂度O(n * k * logm)
    @staticmethod
    def compute(s, p, k):
        k = jcast('int', k)
        n = jcast('int', jget(s, 'length'))
        m = jcast('int', jget(p, 'length'))
        if (n < m):
            return jcast('int', 0)
        Code06_DNA.build(s, n, p, m)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= jcast('int', (n - m))):
            # s[i...i+m-1] -> m
            # p[0.....m-1]
            if Code06_DNA.check(i, jcast('int', (jcast('int', jadd(i, m)) - 1)), k):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # s[l1...r1] 和 p[0...m-1] 取等长的两段
    # 返回这两段上字符不一样的位置是不是<=k个
    @staticmethod
    def check(l1, r1, k):
        l1 = jcast('int', l1)
        r1 = jcast('int', r1)
        k = jcast('int', k)
        diff = jcast('int', 0)
        l2 = jcast('int', 0)
        while ((l1 <= r1) and (diff <= k)):
            l = jcast('int', 1)
            r = jcast('int', jcast('int', jadd(jcast('int', (r1 - l1)), 1)))
            m = 0
            len = jcast('int', 0)
            while (l <= r):
                m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
                if Code06_DNA.same(l1, l2, m):
                    len = jcast('int', m)
                    l = jcast('int', jcast('int', jadd(m, 1)))
                else:
                    r = jcast('int', jcast('int', (m - 1)))
            if (jcast('int', jadd(l1, len)) <= r1):
                diff = jcast('int', (diff + 1))
            l1 = jcast('int', jcast('int', jadd(l1, jcast('int', jadd(len, 1)))))
            l2 = jcast('int', jcast('int', jadd(l2, jcast('int', jadd(len, 1)))))
        return jcast('boolean', (diff <= k))

    @staticmethod
    def same(l1, l2, len):
        l1 = jcast('int', l1)
        l2 = jcast('int', l2)
        len = jcast('int', len)
        return jcast('boolean', (Code06_DNA.hash(Code06_DNA.hashs, l1, jcast('int', (jcast('int', jadd(l1, len)) - 1))) == Code06_DNA.hash(Code06_DNA.hashp, l2, jcast('int', (jcast('int', jadd(l2, len)) - 1)))))

    @staticmethod
    def build(s, n, p, m):
        n = jcast('int', n)
        m = jcast('int', m)
        Code06_DNA.pow[0] = jcast('long', 1)
        j = jcast('int', 1)
        while (j < Code06_DNA.MAXN):
            Code06_DNA.pow[j] = jcast('long', jcast('long', (Code06_DNA.pow[jcast('int', (j - 1))] * Code06_DNA.base)))
            j = jcast('int', (j + 1))
        Code06_DNA.hashs[0] = jcast('long', jcast('int', jadd(jcast('int', (s[0] - jchar('a'))), 1)))
        j = jcast('int', 1)
        while (j < n):
            Code06_DNA.hashs[j] = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code06_DNA.hashs[jcast('int', (j - 1))] * Code06_DNA.base)), s[j])) - jchar('a'))), 1)))
            j = jcast('int', (j + 1))
        Code06_DNA.hashp[0] = jcast('long', jcast('int', jadd(jcast('int', (p[0] - jchar('a'))), 1)))
        j = jcast('int', 1)
        while (j < m):
            Code06_DNA.hashp[j] = jcast('long', jcast('long', jadd(jcast('long', (jcast('long', jadd(jcast('long', (Code06_DNA.hashp[jcast('int', (j - 1))] * Code06_DNA.base)), p[j])) - jchar('a'))), 1)))
            j = jcast('int', (j + 1))

    @staticmethod
    def hash(hash, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', hash[r])
        ans = jcast('long', jcast('long', (ans - (0 if (l == 0) else jcast('long', (hash[jcast('int', (l - 1))] * Code06_DNA.pow[jcast('int', jadd(jcast('int', (r - l)), 1))]))))))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_DNA.MAXN = jcast('int', 100001)
Code06_DNA.base = jcast('int', 499)
Code06_DNA.pow = jarray('long', [Code06_DNA.MAXN])
Code06_DNA.hashs = jarray('long', [Code06_DNA.MAXN])
Code06_DNA.hashp = jarray('long', [Code06_DNA.MAXN])

if __name__ == '__main__':
    Code06_DNA.main([])

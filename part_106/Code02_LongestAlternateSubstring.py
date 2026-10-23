# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最长LR交替子串
# 给定一个长度为n的字符串，一开始字符串中全是'L'字符
# 有q次修改，每次指定一个位置i
# 如果i位置是'L'字符那么改成'R'字符
# 如果i位置是'R'字符那么改成'L'字符
# 如果一个子串是两种字符不停交替出现的样子，也就是LRLR... 或者RLRL...
# 那么说这个子串是有效子串
# 每次修改后，都打印当前整个字符串中最长交替子串的长度
# 测试链接 : https://www.luogu.com.cn/problem/P6492
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_LongestAlternateSubstring:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'len': 'len', 'pre': 'pre', 'suf': 'suf'}
    MAXN = 0
    # 原始数组
    arr = None
    # 交替最长子串长度
    len = None
    # 交替最长前缀长度
    pre = None
    # 交替最长后缀长度
    suf = None
    @staticmethod
    def up(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        jset(Code02_LongestAlternateSubstring.len, i, jstatic('Math', 'max', Code02_LongestAlternateSubstring.len[jcast('int', (i << (1 & 31)))], Code02_LongestAlternateSubstring.len[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))
        Code02_LongestAlternateSubstring.pre[i] = jcast('int', Code02_LongestAlternateSubstring.pre[jcast('int', (i << (1 & 31)))])
        Code02_LongestAlternateSubstring.suf[i] = jcast('int', Code02_LongestAlternateSubstring.suf[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ln = jcast('int', jcast('int', jadd(jcast('int', (mid - l)), 1)))
        rn = jcast('int', jcast('int', (r - mid)))
        if (Code02_LongestAlternateSubstring.arr[mid] != Code02_LongestAlternateSubstring.arr[jcast('int', jadd(mid, 1))]):
            jset(Code02_LongestAlternateSubstring.len, i, jstatic('Math', 'max', Code02_LongestAlternateSubstring.len[i], jcast('int', jadd(Code02_LongestAlternateSubstring.suf[jcast('int', (i << (1 & 31)))], Code02_LongestAlternateSubstring.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))))
            if (Code02_LongestAlternateSubstring.len[jcast('int', (i << (1 & 31)))] == ln):
                Code02_LongestAlternateSubstring.pre[i] = jcast('int', jcast('int', jadd(ln, Code02_LongestAlternateSubstring.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
            if (Code02_LongestAlternateSubstring.len[jcast('int', (jcast('int', (i << (1 & 31))) | 1))] == rn):
                Code02_LongestAlternateSubstring.suf[i] = jcast('int', jcast('int', jadd(rn, Code02_LongestAlternateSubstring.suf[jcast('int', (i << (1 & 31)))])))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code02_LongestAlternateSubstring.len[i] = jcast('int', 1)
            Code02_LongestAlternateSubstring.pre[i] = jcast('int', 1)
            Code02_LongestAlternateSubstring.suf[i] = jcast('int', 1)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_LongestAlternateSubstring.build(l, mid, jcast('int', (i << (1 & 31))))
            Code02_LongestAlternateSubstring.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_LongestAlternateSubstring.up(l, r, i)

    @staticmethod
    def reverse(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code02_LongestAlternateSubstring.arr[jobi] = jcast('int', jcast('int', (Code02_LongestAlternateSubstring.arr[jobi] ^ 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code02_LongestAlternateSubstring.reverse(jobi, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_LongestAlternateSubstring.reverse(jobi, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code02_LongestAlternateSubstring.up(l, r, i)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        q = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_LongestAlternateSubstring.build(1, n, 1)
        i = jcast('int', 1)
        index = 0
        while (i <= q):
            jcall(in_, 'nextToken')
            index = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_LongestAlternateSubstring.reverse(index, 1, n, 1)
            jcall(out, 'println', Code02_LongestAlternateSubstring.len[1])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_LongestAlternateSubstring.MAXN = jcast('int', 200001)
Code02_LongestAlternateSubstring.arr = jarray('int', [Code02_LongestAlternateSubstring.MAXN])
Code02_LongestAlternateSubstring.len = jarray('int', [jcast('int', (Code02_LongestAlternateSubstring.MAXN << (2 & 31)))])
Code02_LongestAlternateSubstring.pre = jarray('int', [jcast('int', (Code02_LongestAlternateSubstring.MAXN << (2 & 31)))])
Code02_LongestAlternateSubstring.suf = jarray('int', [jcast('int', (Code02_LongestAlternateSubstring.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code02_LongestAlternateSubstring.main([])

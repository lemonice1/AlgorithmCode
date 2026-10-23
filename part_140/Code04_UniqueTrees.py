# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 不同结构的二叉树数量
# 一共有n个节点，认为节点之间无差别，返回能形成多少种不同结构的二叉树
# 1 <= n <= 19
# 测试链接 : https://leetcode.cn/problems/unique-binary-search-trees/
class Code04_UniqueTrees:
    __java_fields__ = {}
    # 数据量小用哪个公式都可以
    # 不用考虑溢出、取模等问题
    # 同时注意到n的范围并不大，直接使用公式4
    @staticmethod
    def numTrees(n):
        n = jcast('int', n)
        f = jarray('int', [jcast('int', jadd(n, 1))])
        jset(f, 0, jset(f, 1, 1))
        i = jcast('int', 2)
        while (i <= n):
            l = jcast('int', 0)
            r = jcast('int', jcast('int', (i - 1)))
            while (l < i):
                f[i] = jcast('int', jcast('int', jadd(f[i], jcast('int', (f[l] * f[r])))))
                l = jcast('int', (l + 1))
                r = jcast('int', (r - 1))
            i = jcast('int', (i + 1))
        return jcast('int', f[n])

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



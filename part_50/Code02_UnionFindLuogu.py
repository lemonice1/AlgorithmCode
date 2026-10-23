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

# 并查集模版(洛谷)
# 本实现用递归函数实现路径压缩，而且省掉了小挂大的优化，一般情况下可以省略
# 测试链接 : https://www.luogu.com.cn/problem/P3367
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_UnionFindLuogu:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'n': 'n'}
    MAXN = 0
    father = None
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i <= Code02_UnionFindLuogu.n):
            Code02_UnionFindLuogu.father[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code02_UnionFindLuogu.father[i]):
            jset(Code02_UnionFindLuogu.father, i, Code02_UnionFindLuogu.find(Code02_UnionFindLuogu.father[i]))
        return jcast('int', Code02_UnionFindLuogu.father[i])

    @staticmethod
    def isSameSet(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('boolean', (Code02_UnionFindLuogu.find(x) == Code02_UnionFindLuogu.find(y)))

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code02_UnionFindLuogu.father, Code02_UnionFindLuogu.find(x), Code02_UnionFindLuogu.find(y))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code02_UnionFindLuogu.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_UnionFindLuogu.build()
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < m):
                jcall(in_, 'nextToken')
                z = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                if (z == 1):
                    Code02_UnionFindLuogu.union(x, y)
                else:
                    jcall(out, 'println', ('Y' if Code02_UnionFindLuogu.isSameSet(x, y) else 'N'))
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_UnionFindLuogu.MAXN = jcast('int', 200001)
Code02_UnionFindLuogu.father = jarray('int', [Code02_UnionFindLuogu.MAXN])
Code02_UnionFindLuogu.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_UnionFindLuogu.main([])

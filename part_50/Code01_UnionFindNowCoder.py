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

# 并查集模版(牛客)
# 路径压缩 + 小挂大
# 测试链接 : https://www.nowcoder.com/practice/e7ed657974934a30b2010046536a5372
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_UnionFindNowCoder:
    __java_fields__ = {'MAXN': 'MAXN', 'father': 'father', 'size': 'size', 'stack': 'stack', 'n': 'n'}
    MAXN = 0
    father = None
    size = None
    stack = None
    n = 0
    @staticmethod
    def build():
        i = jcast('int', 0)
        while (i <= Code01_UnionFindNowCoder.n):
            Code01_UnionFindNowCoder.father[i] = jcast('int', i)
            Code01_UnionFindNowCoder.size[i] = jcast('int', 1)
            i = jcast('int', (i + 1))

    # i号节点，往上一直找，找到代表节点返回！
    @staticmethod
    def find(i):
        i = jcast('int', i)
        # 沿途收集了几个点
        size = jcast('int', 0)
        while (i != Code01_UnionFindNowCoder.father[i]):
            jset(Code01_UnionFindNowCoder.stack, ((_java_old_1 := size), (size := jcast('int', (size + (1)))), _java_old_1)[2], i)
            i = jcast('int', Code01_UnionFindNowCoder.father[i])
        # 沿途节点收集好了，i已经跳到代表节点了
        while (size > 0):
            jset(Code01_UnionFindNowCoder.father, Code01_UnionFindNowCoder.stack[(size := jcast('int', (size + (-1))))], i)
        return jcast('int', i)

    @staticmethod
    def isSameSet(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        return jcast('boolean', (Code01_UnionFindNowCoder.find(x) == Code01_UnionFindNowCoder.find(y)))

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code01_UnionFindNowCoder.find(x))
        fy = jcast('int', Code01_UnionFindNowCoder.find(y))
        if (fx != fy):
            # fx是集合的代表：拿大小
            # fy是集合的代表：拿大小
            if (Code01_UnionFindNowCoder.size[fx] >= Code01_UnionFindNowCoder.size[fy]):
                Code01_UnionFindNowCoder.size[fx] = jcast('int', jcast('int', jadd(Code01_UnionFindNowCoder.size[fx], Code01_UnionFindNowCoder.size[fy])))
                Code01_UnionFindNowCoder.father[fy] = jcast('int', fx)
            else:
                Code01_UnionFindNowCoder.size[fy] = jcast('int', jcast('int', jadd(Code01_UnionFindNowCoder.size[fy], Code01_UnionFindNowCoder.size[fx])))
                Code01_UnionFindNowCoder.father[fx] = jcast('int', fy)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_UnionFindNowCoder.n = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_UnionFindNowCoder.build()
            jcall(in_, 'nextToken')
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < m):
                jcall(in_, 'nextToken')
                op = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                if (op == 1):
                    jcall(out, 'println', ('Yes' if Code01_UnionFindNowCoder.isSameSet(x, y) else 'No'))
                else:
                    Code01_UnionFindNowCoder.union(x, y)
                i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_UnionFindNowCoder.MAXN = jcast('int', 1000001)
Code01_UnionFindNowCoder.father = jarray('int', [Code01_UnionFindNowCoder.MAXN])
Code01_UnionFindNowCoder.size = jarray('int', [Code01_UnionFindNowCoder.MAXN])
Code01_UnionFindNowCoder.stack = jarray('int', [Code01_UnionFindNowCoder.MAXN])
Code01_UnionFindNowCoder.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_UnionFindNowCoder.main([])

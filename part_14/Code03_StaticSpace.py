# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 展示acm风格的测试方式
# 子矩阵的最大累加和问题，不要求会解题思路，后面的课会讲
# 每一组测试都给定数据规模
# 任何空间都提前生成好，一律都是静态空间，然后自己去复用，推荐这种方式
# 测试链接 : https://www.nowcoder.com/practice/cb82a97dcd0d48a7b1f4ee917e2c0409?
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_StaticSpace:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'mat': 'mat', 'arr': 'arr', 'n': 'n', 'm': 'm'}
    # 题目给定的行的最大数据量
    MAXN = 0
    # 题目给定的列的最大数据量
    MAXM = 0
    # 申请这么大的矩阵空间，一定够用了
    # 静态的空间，不停复用
    mat = None
    # 需要的所有辅助空间也提前生成
    # 静态的空间，不停复用
    arr = None
    # 当前测试数据行的数量是n
    # 当前测试数据列的数量是m
    # 这两个变量可以把代码运行的边界规定下来
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code03_StaticSpace.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code03_StaticSpace.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code03_StaticSpace.n):
                j = jcast('int', 0)
                while (j < Code03_StaticSpace.m):
                    jcall(in_, 'nextToken')
                    jset(Code03_StaticSpace.mat[i], j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code03_StaticSpace.maxSumSubmatrix())
        jcall(out, 'flush')
        jcall(br, 'close')
        jcall(out, 'close')

    # 求子矩阵的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubmatrix():
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < Code03_StaticSpace.n):
            # 因为之前的过程可能用过辅助数组
            # 为了让之前结果不干扰到这次运行，需要自己清空辅助数组需要用到的部分
            jstatic('Arrays', 'fill', Code03_StaticSpace.arr, 0, Code03_StaticSpace.m, 0)
            j = jcast('int', i)
            while (j < Code03_StaticSpace.n):
                k = jcast('int', 0)
                while (k < Code03_StaticSpace.m):
                    Code03_StaticSpace.arr[k] = jcast('int', jcast('int', jadd(Code03_StaticSpace.arr[k], Code03_StaticSpace.mat[j][k])))
                    k = jcast('int', (k + 1))
                max = jcast('int', jstatic('Math', 'max', max, Code03_StaticSpace.maxSumSubarray()))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    # 求子数组的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubarray():
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        cur = jcast('int', 0)
        i = jcast('int', 0)
        while (i < Code03_StaticSpace.m):
            cur = jcast('int', jcast('int', jadd(cur, Code03_StaticSpace.arr[i])))
            max = jcast('int', jstatic('Math', 'max', max, cur))
            cur = jcast('int', (0 if (cur < 0) else cur))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_StaticSpace.MAXN = jcast('int', 201)
Code03_StaticSpace.MAXM = jcast('int', 201)
Code03_StaticSpace.mat = jarray('int', [Code03_StaticSpace.MAXN, Code03_StaticSpace.MAXM])
Code03_StaticSpace.arr = jarray('int', [Code03_StaticSpace.MAXM])
Code03_StaticSpace.n = jcast('int', 0)
Code03_StaticSpace.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_StaticSpace.main([])

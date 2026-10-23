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
# 需要任何空间都动态生成，在大厂笔试或者比赛中，这种方式并不推荐
# 测试链接 : https://www.nowcoder.com/practice/cb82a97dcd0d48a7b1f4ee917e2c0409?
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_SpecifyAmount:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        # 把文件里的内容，load进来，保存在内存里，很高效，很经济，托管的很好
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        # 一个一个读数字
        in_ = jnew('StreamTokenizer', br)
        # 提交答案的时候用的，也是一个内存托管区
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        # 文件没有结束就继续
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            # n，二维数组的行
            n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            # m，二维数组的列
            m = jcast('int', jcast('int', jget(in_, 'nval')))
            # 装数字的矩阵，临时动态生成
            mat = jarray('int', [n, m])
            i = jcast('int', 0)
            while (i < n):
                j = jcast('int', 0)
                while (j < m):
                    jcall(in_, 'nextToken')
                    jset(mat[i], j, jcast('int', jget(in_, 'nval')))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code02_SpecifyAmount.maxSumSubmatrix(mat, n, m))
        jcall(out, 'flush')
        jcall(br, 'close')
        jcall(out, 'close')

    # 求子矩阵的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubmatrix(mat, n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        i = jcast('int', 0)
        while (i < n):
            # 需要的辅助数组，临时动态生成
            arr = jarray('int', [m])
            j = jcast('int', i)
            while (j < n):
                k = jcast('int', 0)
                while (k < m):
                    arr[k] = jcast('int', jcast('int', jadd(arr[k], mat[j][k])))
                    k = jcast('int', (k + 1))
                max = jcast('int', jstatic('Math', 'max', max, Code02_SpecifyAmount.maxSumSubarray(arr, m)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    # 求子数组的最大累加和，后面的课会讲
    @staticmethod
    def maxSumSubarray(arr, m):
        m = jcast('int', m)
        max = jcast('int', jget(Integer, 'MIN_VALUE'))
        cur = jcast('int', 0)
        i = jcast('int', 0)
        while (i < m):
            cur = jcast('int', jcast('int', jadd(cur, arr[i])))
            max = jcast('int', jstatic('Math', 'max', max, cur))
            cur = jcast('int', (0 if (cur < 0) else cur))
            i = jcast('int', (i + 1))
        return jcast('int', max)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_SpecifyAmount.main([])

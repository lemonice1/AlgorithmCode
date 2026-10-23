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

# 返回无序数组中正数和负数个数相等的最长子数组长度
# 给定一个无序数组arr，其中元素可正、可负、可0
# 求arr所有子数组中正数与负数个数相等的最长子数组的长度
# 测试链接 : https://www.nowcoder.com/practice/545544c060804eceaed0bb84fcd992fb
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_PositivesEqualsNegtivesLongestSubarray:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'n': 'n', 'map': 'map'}
    MAXN = 0
    arr = None
    n = 0
    map = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_PositivesEqualsNegtivesLongestSubarray.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            num = 0
            while (i < Code04_PositivesEqualsNegtivesLongestSubarray.n):
                jcall(in_, 'nextToken')
                num = jcast('int', jcast('int', jget(in_, 'nval')))
                Code04_PositivesEqualsNegtivesLongestSubarray.arr[i] = jcast('int', ((1 if (num > 0) else jcast('int', (-1))) if (num != 0) else 0))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_PositivesEqualsNegtivesLongestSubarray.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jcall(Code04_PositivesEqualsNegtivesLongestSubarray.map, 'clear')
        jcall(Code04_PositivesEqualsNegtivesLongestSubarray.map, 'put', 0, jcast('int', (-1)))
        ans = jcast('int', 0)
        i = jcast('int', 0)
        sum = jcast('int', 0)
        while (i < Code04_PositivesEqualsNegtivesLongestSubarray.n):
            sum = jcast('int', jcast('int', jadd(sum, Code04_PositivesEqualsNegtivesLongestSubarray.arr[i])))
            if jcall(Code04_PositivesEqualsNegtivesLongestSubarray.map, 'containsKey', sum):
                ans = jcast('int', jstatic('Math', 'max', ans, (i - jcall(Code04_PositivesEqualsNegtivesLongestSubarray.map, 'get', sum))))
            else:
                jcall(Code04_PositivesEqualsNegtivesLongestSubarray.map, 'put', sum, i)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PositivesEqualsNegtivesLongestSubarray.MAXN = jcast('int', 100001)
Code04_PositivesEqualsNegtivesLongestSubarray.arr = jarray('int', [Code04_PositivesEqualsNegtivesLongestSubarray.MAXN])
Code04_PositivesEqualsNegtivesLongestSubarray.n = jcast('int', 0)
Code04_PositivesEqualsNegtivesLongestSubarray.map = jnew('HashMap')

if __name__ == '__main__':
    Code04_PositivesEqualsNegtivesLongestSubarray.main([])

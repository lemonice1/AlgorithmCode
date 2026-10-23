# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 有一次修改机会的最长不下降子序列
# 给定一个长度为n的数组arr，和一个整数k
# 只有一次机会可以将其中连续的k个数全修改成任意一个值
# 这次机会你可以用也可以不用，请返回最长不下降子序列长度
# 1 <= k, n <= 10^5
# 1 <= arr[i] <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P8776
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_LongestNoDecreaseModifyKSubarray:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'right': 'right_data', 'ends': 'ends', 'n': 'n', 'k': 'k'}
    MAXN = 0
    arr = None
    right_data = None
    ends = None
    n = 0
    k = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code05_LongestNoDecreaseModifyKSubarray.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_LongestNoDecreaseModifyKSubarray.k = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code05_LongestNoDecreaseModifyKSubarray.n):
                jcall(in_, 'nextToken')
                Code05_LongestNoDecreaseModifyKSubarray.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            if (Code05_LongestNoDecreaseModifyKSubarray.k >= Code05_LongestNoDecreaseModifyKSubarray.n):
                jcall(out, 'println', Code05_LongestNoDecreaseModifyKSubarray.n)
            else:
                jcall(out, 'println', Code05_LongestNoDecreaseModifyKSubarray.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        Code05_LongestNoDecreaseModifyKSubarray.right()
        len = jcast('int', 0)
        ans = jcast('int', 0)
        i = jcast('int', 0)
        j = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.k)
        find = 0
        left = 0
        while (j < Code05_LongestNoDecreaseModifyKSubarray.n):
            find = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.bs2(len, Code05_LongestNoDecreaseModifyKSubarray.arr[j]))
            left = jcast('int', (len if (find == jcast('int', (-1))) else find))
            ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(jcast('int', jadd(left, Code05_LongestNoDecreaseModifyKSubarray.k)), Code05_LongestNoDecreaseModifyKSubarray.right_data[j]))))
            find = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.bs2(len, Code05_LongestNoDecreaseModifyKSubarray.arr[i]))
            if (find == jcast('int', (-1))):
                jset(Code05_LongestNoDecreaseModifyKSubarray.ends, ((_java_old_1 := len), (len := jcast('int', (len + (1)))), _java_old_1)[2], Code05_LongestNoDecreaseModifyKSubarray.arr[i])
            else:
                Code05_LongestNoDecreaseModifyKSubarray.ends[find] = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.arr[i])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        ans = jcast('int', jstatic('Math', 'max', ans, jcast('int', jadd(len, Code05_LongestNoDecreaseModifyKSubarray.k))))
        return jcast('int', ans)

    # 生成辅助数组right
    # right[j] :
    # 一定以arr[j]做开头的情况下，arr[j...]上最长不下降子序列长度是多少
    # 关键逻辑 :
    # 一定以arr[i]做开头的情况下，arr[i...]上最长不下降子序列
    # 就是！从n-1出发来看(从右往左遍历)，以arr[i]做结尾的情况下的最长不上升子序列
    @staticmethod
    def right():
        len = jcast('int', 0)
        i = jcast('int', jcast('int', (Code05_LongestNoDecreaseModifyKSubarray.n - 1)))
        find = 0
        while (i >= 0):
            find = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.bs1(len, Code05_LongestNoDecreaseModifyKSubarray.arr[i]))
            if (find == jcast('int', (-1))):
                jset(Code05_LongestNoDecreaseModifyKSubarray.ends, ((_java_old_2 := len), (len := jcast('int', (len + (1)))), _java_old_2)[2], Code05_LongestNoDecreaseModifyKSubarray.arr[i])
                Code05_LongestNoDecreaseModifyKSubarray.right_data[i] = jcast('int', len)
            else:
                Code05_LongestNoDecreaseModifyKSubarray.ends[find] = jcast('int', Code05_LongestNoDecreaseModifyKSubarray.arr[i])
                Code05_LongestNoDecreaseModifyKSubarray.right_data[i] = jcast('int', jcast('int', jadd(find, 1)))
            i = jcast('int', (i - 1))

    # 求最长不上升子序列长度的二分
    # ends[0...len-1]是降序的，找到<num的最左位置
    # 不存在返回-1
    @staticmethod
    def bs1(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code05_LongestNoDecreaseModifyKSubarray.ends[m] < num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 求最长不下降子序列长度的二分
    # ends[0...len-1]是升序的，找到>num的最左位置
    # 不存在返回-1
    @staticmethod
    def bs2(len, num):
        len = jcast('int', len)
        num = jcast('int', num)
        l = jcast('int', 0)
        r = jcast('int', jcast('int', (len - 1)))
        m = 0
        ans = jcast('int', jcast('int', (-1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code05_LongestNoDecreaseModifyKSubarray.ends[m] > num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_LongestNoDecreaseModifyKSubarray.MAXN = jcast('int', 100001)
Code05_LongestNoDecreaseModifyKSubarray.arr = jarray('int', [Code05_LongestNoDecreaseModifyKSubarray.MAXN])
Code05_LongestNoDecreaseModifyKSubarray.right_data = jarray('int', [Code05_LongestNoDecreaseModifyKSubarray.MAXN])
Code05_LongestNoDecreaseModifyKSubarray.ends = jarray('int', [Code05_LongestNoDecreaseModifyKSubarray.MAXN])
Code05_LongestNoDecreaseModifyKSubarray.n = jcast('int', 0)
Code05_LongestNoDecreaseModifyKSubarray.k = jcast('int', 0)

if __name__ == '__main__':
    Code05_LongestNoDecreaseModifyKSubarray.main([])

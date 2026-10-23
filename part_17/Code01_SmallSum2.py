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

# 小和问题，Python版
# 测试链接 : https://www.nowcoder.com/practice/edfe05a1d45c4ea89101d936cac32469
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SmallSum2:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'help': 'help', 'n': 'n'}
    MAXN = 0
    arr = None
    help = None
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code01_SmallSum2.n = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < Code01_SmallSum2.n):
                jcall(in_, 'nextToken')
                Code01_SmallSum2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code01_SmallSum2.smallSum(0, jcast('int', (Code01_SmallSum2.n - 1))))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 结果比较大，用int会溢出的，所以返回long类型
    # 特别注意溢出这个点，笔试常见坑
    # 返回arr[l...r]范围上，小和的累加和，同时请把arr[l..r]变有序
    # 时间复杂度O(n * logn)
    @staticmethod
    def smallSum(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('long', 0)
        m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('long', jcast('long', jadd(jcast('long', jadd(Code01_SmallSum2.smallSum(l, m), Code01_SmallSum2.smallSum(jcast('int', jadd(m, 1)), r))), Code01_SmallSum2.merge(l, m, r))))

    # 返回跨左右产生的小和累加和，左侧有序、右侧有序，让左右两侧整体有序
    # arr[l...m] arr[m+1...r]
    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # 统计部分
        ans = jcast('long', 0)
        j = jcast('int', jcast('int', jadd(m, 1)))
        i = jcast('int', l)
        sum = jcast('int', 0)
        while (j <= r):
            while ((i <= m) and (Code01_SmallSum2.arr[i] <= Code01_SmallSum2.arr[j])):
                sum = jcast('int', jcast('int', jadd(sum, Code01_SmallSum2.arr[((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2]])))
            ans = jcast('long', jcast('long', jadd(ans, sum)))
            j = jcast('int', (j + 1))
        # 正常merge
        i = jcast('int', l)
        a = jcast('int', l)
        b = jcast('int', jcast('int', jadd(m, 1)))
        while ((a <= m) and (b <= r)):
            jset(Code01_SmallSum2.help, ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2], (Code01_SmallSum2.arr[((_java_old_2 := a), (a := jcast('int', (a + (1)))), _java_old_2)[2]] if (Code01_SmallSum2.arr[a] <= Code01_SmallSum2.arr[b]) else Code01_SmallSum2.arr[((_java_old_3 := b), (b := jcast('int', (b + (1)))), _java_old_3)[2]]))
        while (a <= m):
            jset(Code01_SmallSum2.help, ((_java_old_6 := i), (i := jcast('int', (i + (1)))), _java_old_6)[2], Code01_SmallSum2.arr[((_java_old_5 := a), (a := jcast('int', (a + (1)))), _java_old_5)[2]])
        while (b <= r):
            jset(Code01_SmallSum2.help, ((_java_old_8 := i), (i := jcast('int', (i + (1)))), _java_old_8)[2], Code01_SmallSum2.arr[((_java_old_7 := b), (b := jcast('int', (b + (1)))), _java_old_7)[2]])
        i = jcast('int', l)
        while (i <= r):
            Code01_SmallSum2.arr[i] = jcast('int', Code01_SmallSum2.help[i])
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SmallSum2.MAXN = jcast('int', 100001)
Code01_SmallSum2.arr = jarray('int', [Code01_SmallSum2.MAXN])
Code01_SmallSum2.help = jarray('int', [Code01_SmallSum2.MAXN])
Code01_SmallSum2.n = jcast('int', 0)

if __name__ == '__main__':
    Code01_SmallSum2.main([])

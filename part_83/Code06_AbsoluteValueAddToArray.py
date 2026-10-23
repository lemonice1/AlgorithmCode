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

# 加入差值绝对值直到长度固定
# 给定一个非负数组arr，计算任何两个数差值的绝对值
# 如果arr中没有，都要加入到arr里，但是只加一份
# 然后新的arr继续计算任何两个数差值的绝对值，
# 如果arr中没有，都要加入到arr里，但是只加一份
# 一直到arr大小固定，返回arr最终的长度
# 来自真实大厂笔试，没有在线测试，对数器验证
class Code06_AbsoluteValueAddToArray:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def len1(arr):
        list = jnew('ArrayList')
        set = jnew('HashSet')
        for num in arr:
            jcall(list, 'add', num)
            jcall(set, 'add', num)
        while (not Code06_AbsoluteValueAddToArray.finish(list, set)):
            None
        return jcast('int', jcall(list, 'size'))

    @staticmethod
    def finish(list, set):
        len = jcast('int', jcall(list, 'size'))
        i = jcast('int', 0)
        while (i < len):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j < len):
                abs = jcast('int', jstatic('Math', 'abs', (jcall(list, 'get', i) - jcall(list, 'get', j))))
                if (not jcall(set, 'contains', abs)):
                    jcall(list, 'add', abs)
                    jcall(set, 'add', abs)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('boolean', (len == jcall(list, 'size')))

    # 正式方法
    # 时间复杂度O(n)
    @staticmethod
    def len2(arr):
        max = jcast('int', 0)
        # 找到任意一个非0的值
        gcd = jcast('int', 0)
        for num in arr:
            max = jcast('int', jstatic('Math', 'max', max, num))
            if (num != 0):
                gcd = jcast('int', num)
        # 数组中都是0
        if (gcd == 0):
            return jcast('int', jget(arr, 'length'))
        # 不都是0
        # 0 7次
        # 5 5次
        cnts = jnew('HashMap')
        for num in arr:
            if (num != 0):
                gcd = jcast('int', Code06_AbsoluteValueAddToArray.gcd(gcd, num))
            jcall(cnts, 'put', num, jadd(jcall(cnts, 'getOrDefault', num, 0), 1))
        ans = jcast('int', jcast('int', jdiv(max, gcd)))
        maxCnt = jcast('int', 0)
        for key in jcall(cnts, 'keySet'):
            if (key != 0):
                ans = jcast('int', jadd(ans, (jcall(cnts, 'get', key) - 1)))
            maxCnt = jcast('int', jstatic('Math', 'max', maxCnt, jcall(cnts, 'get', key)))
        ans = jcast('int', jadd(ans, jcall(cnts, 'getOrDefault', 0, (1 if (maxCnt > 1) else 0))))
        return jcast('int', ans)

    @staticmethod
    def gcd(m, n):
        m = jcast('int', m)
        n = jcast('int', n)
        return jcast('int', (m if (n == 0) else Code06_AbsoluteValueAddToArray.gcd(n, jcast('int', jmod(m, n)))))

    # 为了测试
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('int', (jstatic('Math', 'random') * v)))
            i = jcast('int', (i + 1))
        return ans

    # 为了测试
    @staticmethod
    def main(args):
        N = jcast('int', 50)
        V = jcast('int', 100)
        testTimes = jcast('int', 20000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTimes):
            n = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * N)), 1)))
            nums = Code06_AbsoluteValueAddToArray.randomArray(n, V)
            ans1 = jcast('int', Code06_AbsoluteValueAddToArray.len1(nums))
            ans2 = jcast('int', Code06_AbsoluteValueAddToArray.len2(nums))
            if (ans1 != ans2):
                jprint('出错了！', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code06_AbsoluteValueAddToArray.main([])

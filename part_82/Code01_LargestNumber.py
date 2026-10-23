# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最大数
# 给定一组非负整数nums
# 重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数
# 测试链接 : https://leetcode.cn/problems/largest-number/
class Code01_LargestNumber:
    __java_fields__ = {}
    # strs中全是非空字符串，要把所有字符串拼接起来，形成字典序最小的结果
    # 暴力方法
    # 为了验证
    # 生成所有可能的排列
    # 其中选出字典序最小的结果
    @staticmethod
    def way1(strs):
        ans = jnew('ArrayList')
        Code01_LargestNumber.f(strs, 0, ans)
        jcall(ans, 'sort', (lambda a, b: jcall(a, 'compareTo', b)))
        return jcall(ans, 'get', 0)

    # 全排列代码，讲解038，常见经典递归过程解析
    @staticmethod
    def f(strs, i, ans):
        i = jcast('int', i)
        if (i == jget(strs, 'length')):
            path = jnew('StringBuilder')
            for s in strs:
                jcall(path, 'append', s)
            jcall(ans, 'add', jcall(path, 'toString'))
        else:
            j = jcast('int', i)
            while (j < jget(strs, 'length')):
                Code01_LargestNumber.swap(strs, i, j)
                Code01_LargestNumber.f(strs, jcast('int', jadd(i, 1)), ans)
                Code01_LargestNumber.swap(strs, i, j)
                j = jcast('int', (j + 1))

    @staticmethod
    def swap(strs, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = strs[i]
        strs[i] = strs[j]
        strs[j] = tmp

    # strs中全是非空字符串，要把所有字符串拼接起来，形成字典序最小的结果
    # 正式方法
    # 时间复杂度O(n*logn)
    @staticmethod
    def way2(strs):
        jstatic('Arrays', 'sort', strs, (lambda a, b: jcall(jadd(a, b), 'compareTo', jadd(b, a))))
        path = jnew('StringBuilder')
        i = jcast('int', 0)
        while (i < jget(strs, 'length')):
            jcall(path, 'append', strs[i])
            i = jcast('int', (i + 1))
        return jcall(path, 'toString')

    # 为了验证
    # 生成长度1~n的随机字符串数组
    @staticmethod
    def randomStringArray(n, m, v):
        n = jcast('int', n)
        m = jcast('int', m)
        v = jcast('int', v)
        ans = jarray('String', [jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1))])
        i = jcast('int', 0)
        while (i < jget(ans, 'length')):
            jset(ans, i, Code01_LargestNumber.randomString(m, v))
            i = jcast('int', (i + 1))
        return ans

    # 为了验证
    # 生成长度1~m，字符种类有v种，随机字符串
    @staticmethod
    def randomString(m, v):
        m = jcast('int', m)
        v = jcast('int', v)
        len = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * m)), 1)))
        ans = jarray('char', [len])
        i = jcast('int', 0)
        while (i < len):
            jset(ans, i, jcast('char', jcast('int', jadd(jchar('a'), jcast('int', (jstatic('Math', 'random') * v))))))
            i = jcast('int', (i + 1))
        return jstatic('String', 'valueOf', ans)

    # 为了验证
    # 对数器
    @staticmethod
    def main(args):
        # 数组中最多几个字符串
        n = jcast('int', 8)
        # 字符串长度最大多长
        m = jcast('int', 5)
        # 字符的种类有几种
        v = jcast('int', 4)
        testTimes = jcast('int', 2000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        while (i <= testTimes):
            strs = Code01_LargestNumber.randomStringArray(n, m, v)
            ans1 = Code01_LargestNumber.way1(strs)
            ans2 = Code01_LargestNumber.way2(strs)
            if (not jcall(ans1, 'equals', ans2)):
                # 如果出错了
                # 可以增加打印行为找到一组出错的例子
                # 然后去debug
                jprint('出错了！', newline=True)
            if (jcast('int', jmod(i, 100)) == 0):
                jprint(jadd(jadd('测试到第', i), '组'), newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 测试链接 : https://leetcode.cn/problems/largest-number/
    @staticmethod
    def largestNumber(nums):
        n = jcast('int', jget(nums, 'length'))
        strs = jarray('String', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(strs, i, jstatic('String', 'valueOf', nums[i]))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', strs, (lambda a, b: jcall(jadd(b, a), 'compareTo', jadd(a, b))))
        if jcall(strs[0], 'equals', '0'):
            return '0'
        path = jnew('StringBuilder')
        for s in strs:
            jcall(path, 'append', s)
        return jcall(path, 'toString')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code01_LargestNumber.main([])

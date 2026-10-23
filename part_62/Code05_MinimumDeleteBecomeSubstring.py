# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 删除至少几个字符可以变成另一个字符串的子串
# 给定两个字符串s1和s2
# 返回s1至少删除多少字符可以成为s2的子串
# 对数器验证
class Code05_MinimumDeleteBecomeSubstring:
    __java_fields__ = {}
    # 暴力方法
    # 为了验证
    @staticmethod
    def minDelete1(s1, s2):
        list = jnew('ArrayList')
        Code05_MinimumDeleteBecomeSubstring.f(jcall(s1, 'toCharArray'), 0, '', list)
        # 排序 : 长度大的子序列先考虑
        # 因为如果长度大的子序列是s2的子串
        # 那么需要删掉的字符数量 = s1的长度 - s1子序列长度
        # 子序列长度越大，需要删掉的字符数量就越少
        # 所以长度大的子序列先考虑
        jcall(list, 'sort', (lambda a, b: jcast('int', (jcall(b, 'length') - jcall(a, 'length')))))
        for str in list:
            if (jcall(s2, 'indexOf', str) != jcast('int', (-1))):
                # 检查s2中，是否包含当前的s1子序列str
                return jcast('int', jcast('int', (jcall(s1, 'length') - jcall(str, 'length'))))
        return jcast('int', jcall(s1, 'length'))

    # 生成s1字符串的所有子序列串
    @staticmethod
    def f(s1, i, path, list):
        i = jcast('int', i)
        if (i == jget(s1, 'length')):
            jcall(list, 'add', path)
        else:
            Code05_MinimumDeleteBecomeSubstring.f(s1, jcast('int', jadd(i, 1)), path, list)
            Code05_MinimumDeleteBecomeSubstring.f(s1, jcast('int', jadd(i, 1)), jadd(path, s1[i]), list)

    # 正式方法，动态规划
    # 已经展示太多次从递归到动态规划了
    # 直接写动态规划吧
    # 也不做空间压缩了，因为千篇一律
    # 有兴趣的同学自己试试
    @staticmethod
    def minDelete2(str1, str2):
        s1 = jcall(str1, 'toCharArray')
        s2 = jcall(str2, 'toCharArray')
        n = jcast('int', jget(s1, 'length'))
        m = jcast('int', jget(s2, 'length'))
        # dp[len1][len2] :
        # s1[前缀长度为i]至少删除多少字符，可以变成s2[前缀长度为j]的任意后缀串
        dp = jarray('int', [jcast('int', jadd(n, 1)), jcast('int', jadd(m, 1))])
        i = jcast('int', 1)
        while (i <= n):
            jset(dp[i], 0, i)
            j = jcast('int', 1)
            while (j <= m):
                if (s1[jcast('int', (i - 1))] == s2[jcast('int', (j - 1))]):
                    jset(dp[i], j, dp[jcast('int', (i - 1))][jcast('int', (j - 1))])
                else:
                    jset(dp[i], j, jcast('int', jadd(dp[jcast('int', (i - 1))][j], 1)))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        j = jcast('int', 0)
        while (j <= m):
            ans = jcast('int', jstatic('Math', 'min', ans, dp[n][j]))
            j = jcast('int', (j + 1))
        return jcast('int', ans)

    # 为了验证
    # 生成长度为n，有v种字符的随机字符串
    @staticmethod
    def randomString(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jarray('char', [n])
        i = jcast('int', 0)
        while (i < n):
            jset(ans, i, jcast('char', jcast('int', jadd(jchar('a'), jcast('int', (jstatic('Math', 'random') * v))))))
            i = jcast('int', (i + 1))
        return jstatic('String', 'valueOf', ans)

    # 为了验证
    # 对数器
    @staticmethod
    def main(args):
        # 测试的数据量比较小
        # 那是因为数据量大了，暴力方法过不了
        # 但是这个数据量足够说明正式方法是正确的
        n = jcast('int', 12)
        v = jcast('int', 3)
        testTime = jcast('int', 20000)
        jprint('测试开始', newline=True)
        i = jcast('int', 0)
        while (i < testTime):
            len1 = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            len2 = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            s1 = Code05_MinimumDeleteBecomeSubstring.randomString(len1, v)
            s2 = Code05_MinimumDeleteBecomeSubstring.randomString(len2, v)
            ans1 = jcast('int', Code05_MinimumDeleteBecomeSubstring.minDelete1(s1, s2))
            ans2 = jcast('int', Code05_MinimumDeleteBecomeSubstring.minDelete2(s1, s2))
            if (ans1 != ans2):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_MinimumDeleteBecomeSubstring.main([])

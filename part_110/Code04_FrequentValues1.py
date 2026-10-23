# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 出现次数最多的数有几个
# 给定一个长度为n的数组arr，该数组一定是有序的
# 一共有m次查询，每次查询arr[l~r]上出现次数最多的数有几个
# 对数器验证
class Code04_FrequentValues1:
    __java_fields__ = {'MAXN': 'MAXN', 'LIMIT': 'LIMIT', 'arr': 'arr', 'log2': 'log2', 'bucket': 'bucket', 'left': 'left', 'right': 'right', 'stmax': 'stmax'}
    MAXN = 0
    LIMIT = 0
    arr = None
    log2 = None
    bucket = None
    left = None
    right = None
    stmax = None
    @staticmethod
    def build(n):
        n = jcast('int', n)
        # 题目给定的数值范围-100000 ~ +100000
        # 把arr[0]设置成不会到达的数字即可
        Code04_FrequentValues1.arr[0] = jcast('int', jcast('int', (-23333333)))
        cnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            if (Code04_FrequentValues1.arr[jcast('int', (i - 1))] != Code04_FrequentValues1.arr[i]):
                Code04_FrequentValues1.right[cnt] = jcast('int', jcast('int', (i - 1)))
                jset(Code04_FrequentValues1.left, (cnt := jcast('int', (cnt + (1)))), i)
            Code04_FrequentValues1.bucket[i] = jcast('int', cnt)
            i = jcast('int', (i + 1))
        Code04_FrequentValues1.right[cnt] = jcast('int', n)
        Code04_FrequentValues1.log2[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= cnt):
            Code04_FrequentValues1.log2[i] = jcast('int', jcast('int', jadd(Code04_FrequentValues1.log2[jcast('int', (i >> (1 & 31)))], 1)))
            jset(Code04_FrequentValues1.stmax[i], 0, jcast('int', jadd(jcast('int', (Code04_FrequentValues1.right[i] - Code04_FrequentValues1.left[i])), 1)))
            i = jcast('int', (i + 1))
        p = jcast('int', 1)
        while (p <= Code04_FrequentValues1.log2[cnt]):
            i = jcast('int', 1)
            while (jcast('int', (jcast('int', jadd(i, jcast('int', (1 << (p & 31))))) - 1)) <= cnt):
                jset(Code04_FrequentValues1.stmax[i], p, jstatic('Math', 'max', Code04_FrequentValues1.stmax[i][jcast('int', (p - 1))], Code04_FrequentValues1.stmax[jcast('int', jadd(i, jcast('int', (1 << (jcast('int', (p - 1)) & 31)))))][jcast('int', (p - 1))]))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            tmp = jcast('int', l)
            l = jcast('int', r)
            r = jcast('int', tmp)
        lbucket = jcast('int', Code04_FrequentValues1.bucket[l])
        rbucket = jcast('int', Code04_FrequentValues1.bucket[r])
        if (lbucket == rbucket):
            return jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        # a : 最左侧桶在此时l~r范围上的数字有几个
        # b : 最右侧桶在此时l~r范围上的数字有几个
        a = jcast('int', jcast('int', jadd(jcast('int', (Code04_FrequentValues1.right[lbucket] - l)), 1)))
        b = jcast('int', jcast('int', jadd(jcast('int', (r - Code04_FrequentValues1.left[rbucket])), 1)))
        c = jcast('int', 0)
        if (jcast('int', jadd(lbucket, 1)) < rbucket):
            from_ = jcast('int', jcast('int', jadd(lbucket, 1)))
            to = jcast('int', jcast('int', (rbucket - 1)))
            p = jcast('int', Code04_FrequentValues1.log2[jcast('int', jadd(jcast('int', (to - from_)), 1))])
            c = jcast('int', jstatic('Math', 'max', Code04_FrequentValues1.stmax[from_][p], Code04_FrequentValues1.stmax[jcast('int', jadd(jcast('int', (to - jcast('int', (1 << (p & 31))))), 1))][p]))
        return jcast('int', jstatic('Math', 'max', jstatic('Math', 'max', a, b), c))

    # 对数器
    # 为了验证
    @staticmethod
    def main(args):
        jprint('测试开始', newline=True)
        n = jcast('int', 10000)
        v = jcast('int', 100)
        m = jcast('int', 5000)
        Code04_FrequentValues1.randomArray(n, v)
        Code04_FrequentValues1.build(n)
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= m):
            l = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            r = jcast('int', jcast('int', jadd(jcast('int', (jstatic('Math', 'random') * n)), 1)))
            if (Code04_FrequentValues1.query(l, r) != Code04_FrequentValues1.checkQuery(l, r)):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    # 得到随机数组
    # 为了验证
    @staticmethod
    def randomArray(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        i = jcast('int', 1)
        while (i <= n):
            jset(Code04_FrequentValues1.arr, i, jcast('int', (jcast('int', ((jstatic('Math', 'random') * 2) * v)) - v)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_FrequentValues1.arr, 1, jcast('int', jadd(n, 1)))

    # 暴力方法
    # 直接遍历统计词频
    # 为了验证
    @staticmethod
    def checkQuery(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            tmp = jcast('int', l)
            l = jcast('int', r)
            r = jcast('int', tmp)
        map = jnew('HashMap')
        i = jcast('int', l)
        while (i <= r):
            jcall(map, 'put', Code04_FrequentValues1.arr[i], jadd(jcall(map, 'getOrDefault', Code04_FrequentValues1.arr[i], 0), 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        for v in jcall(map, 'values'):
            ans = jcast('int', jstatic('Math', 'max', ans, v))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_FrequentValues1.MAXN = jcast('int', 100001)
Code04_FrequentValues1.LIMIT = jcast('int', 17)
Code04_FrequentValues1.arr = jarray('int', [Code04_FrequentValues1.MAXN])
Code04_FrequentValues1.log2 = jarray('int', [Code04_FrequentValues1.MAXN])
Code04_FrequentValues1.bucket = jarray('int', [Code04_FrequentValues1.MAXN])
Code04_FrequentValues1.left = jarray('int', [Code04_FrequentValues1.MAXN])
Code04_FrequentValues1.right = jarray('int', [Code04_FrequentValues1.MAXN])
Code04_FrequentValues1.stmax = jarray('int', [Code04_FrequentValues1.MAXN, Code04_FrequentValues1.LIMIT])

if __name__ == '__main__':
    Code04_FrequentValues1.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 完美洗牌算法
# 给定数组arr，给定某个范围arr[l..r]，该范围长度为n，n是偶数
# 因为n是偶数，所以给定的范围可以分成左右两个部分，arr[l1, l2, ...lk, r1, r2, ...rk]
# 请把arr[l..r]范围上的数字调整成arr[r1, l1, r2, l2, ... rk, lk]，其他位置的数字不变
# 要求时间复杂度O(n)，额外空间复杂度O(1)，对数器验证
class Code05_PerfectShuffle:
    __java_fields__ = {'MAXN': 'MAXN', 'start': 'start', 'split': 'split', 'size': 'size'}
    # 申请额外空间的做法
    # 保证调整的范围是偶数长度
    # 为了测试
    @staticmethod
    def shuffle1(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        n = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        help = jarray('int', [n])
        l1 = jcast('int', l)
        r1 = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', jadd(l, r)), 2)), 1)))
        j = jcast('int', 0)
        while (j < n):
            jset(help, ((_java_old_1 := j), (j := jcast('int', (j + (1)))), _java_old_1)[2], arr[r1])
            jset(help, ((_java_old_2 := j), (j := jcast('int', (j + (1)))), _java_old_2)[2], arr[l1])
            l1 = jcast('int', (l1 + 1))
            r1 = jcast('int', (r1 + 1))
        i = jcast('int', l)
        j = jcast('int', 0)
        while (j < n):
            arr[i] = jcast('int', help[j])
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))

    # 正式方法
    # 完美洗牌算法
    MAXN = 0
    start = None
    split = None
    size = 0
    # 保证调整的范围是偶数长度
    @staticmethod
    def shuffle2(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        n = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        Code05_PerfectShuffle.build(n)
        i = jcast('int', Code05_PerfectShuffle.size)
        m = 0
        while (n > 0):
            if (Code05_PerfectShuffle.split[i] <= n):
                m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
                Code05_PerfectShuffle.rotate(arr, jcast('int', jadd(l, jcast('int', jdiv(Code05_PerfectShuffle.split[i], 2)))), m, jcast('int', jadd(m, jcast('int', jdiv(Code05_PerfectShuffle.split[i], 2)))))
                Code05_PerfectShuffle.circle(arr, l, jcast('int', (jcast('int', jadd(l, Code05_PerfectShuffle.split[i])) - 1)), i)
                l = jcast('int', jcast('int', jadd(l, Code05_PerfectShuffle.split[i])))
                n = jcast('int', jcast('int', (n - Code05_PerfectShuffle.split[i])))
            else:
                i = jcast('int', (i - 1))

    @staticmethod
    def build(n):
        n = jcast('int', n)
        Code05_PerfectShuffle.size = jcast('int', 0)
        s = jcast('int', 1)
        p = jcast('int', 2)
        while (p <= n):
            jset(Code05_PerfectShuffle.start, ((_java_obj_3 := Code05_PerfectShuffle), (_java_key_4 := 'size'), (_java_old_5 := jget(_java_obj_3, _java_key_4)), jset(_java_obj_3, _java_key_4, jcast('int', (_java_old_5 + (1)))))[3], s)
            Code05_PerfectShuffle.split[Code05_PerfectShuffle.size] = jcast('int', p)
            s = jcast('int', jcast('int', (s * 3)))
            p = jcast('int', jcast('int', (jcast('int', (s * 3)) - 1)))

    @staticmethod
    def rotate(arr, l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        Code05_PerfectShuffle.reverse(arr, l, m)
        Code05_PerfectShuffle.reverse(arr, jcast('int', jadd(m, 1)), r)
        Code05_PerfectShuffle.reverse(arr, l, r)

    @staticmethod
    def reverse(arr, l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        while (l < r):
            Code05_PerfectShuffle.swap(arr, ((_java_old_6 := l), (l := jcast('int', (l + (1)))), _java_old_6)[2], ((_java_old_7 := r), (r := jcast('int', (r + (-1)))), _java_old_7)[2])

    @staticmethod
    def swap(arr, i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', arr[i])
        arr[i] = jcast('int', arr[j])
        arr[j] = jcast('int', tmp)

    @staticmethod
    def circle(arr, l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        j = jcast('int', 1)
        init = 0
        cur = 0
        next = 0
        curv = 0
        nextv = 0
        while (j <= i):
            init = jcast('int', (cur := jcast('int', (jcast('int', jadd(l, Code05_PerfectShuffle.start[j])) - 1))))
            next = jcast('int', Code05_PerfectShuffle.to(cur, l, r))
            curv = jcast('int', arr[cur])
            while (next != init):
                nextv = jcast('int', arr[next])
                arr[next] = jcast('int', curv)
                curv = jcast('int', nextv)
                cur = jcast('int', next)
                next = jcast('int', Code05_PerfectShuffle.to(cur, l, r))
            arr[init] = jcast('int', curv)
            j = jcast('int', (j + 1))

    @staticmethod
    def to(i, l, r):
        i = jcast('int', i)
        l = jcast('int', l)
        r = jcast('int', r)
        if (i <= jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))):
            return jcast('int', jcast('int', jadd(i, jcast('int', jadd(jcast('int', (i - l)), 1)))))
        else:
            return jcast('int', jcast('int', (i - jcast('int', jadd(jcast('int', (r - i)), 1)))))

    # 生成随机数组
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

    # 拷贝数组
    # 为了测试
    @staticmethod
    def copyArray(arr):
        n = jcast('int', jget(arr, 'length'))
        ans = jarray('int', [n])
        i = jcast('int', 0)
        while (i < n):
            ans[i] = jcast('int', arr[i])
            i = jcast('int', (i + 1))
        return ans

    @staticmethod
    def main(args):
        n = jcast('int', 10000)
        v = jcast('int', 100000)
        arr1 = Code05_PerfectShuffle.randomArray(n, v)
        arr2 = Code05_PerfectShuffle.copyArray(arr1)
        test = jcast('int', 50000)
        jprint('测试开始', newline=True)
        i = jcast('int', 1)
        a = 0
        b = 0
        l = 0
        r = 0
        while (i <= test):
            a = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            b = jcast('int', jcast('int', (jstatic('Math', 'random') * n)))
            l = jcast('int', jstatic('Math', 'min', a, b))
            r = jcast('int', jstatic('Math', 'max', a, b))
            if (jcast('int', (jcast('int', jadd(jcast('int', (r - l)), 1)) & 1)) == 0):
                Code05_PerfectShuffle.shuffle1(arr1, l, r)
                Code05_PerfectShuffle.shuffle2(arr2, l, r)
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            if (arr1[i] != arr2[i]):
                jprint('出错了!', newline=True)
            i = jcast('int', (i + 1))
        jprint('测试结束', newline=True)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_PerfectShuffle.MAXN = jcast('int', 20)
Code05_PerfectShuffle.start = jarray('int', [Code05_PerfectShuffle.MAXN])
Code05_PerfectShuffle.split = jarray('int', [Code05_PerfectShuffle.MAXN])
Code05_PerfectShuffle.size = jcast('int', 0)

if __name__ == '__main__':
    Code05_PerfectShuffle.main([])

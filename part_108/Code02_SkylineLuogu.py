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

# 天际线问题(洛谷测试)
# 测试链接 : https://www.luogu.com.cn/problem/P1904
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 堆结构由自己实现
class Code02_SkylineLuogu:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'xsort': 'xsort', 'height': 'height', 'heap': 'heap', 'heapSize': 'heapSize'}
    MAXN = 0
    arr = None
    xsort = None
    height = None
    heap = None
    heapSize = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', 0)
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            jset(Code02_SkylineLuogu.arr[n], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_SkylineLuogu.arr[n], 2, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_SkylineLuogu.arr[n], 1, jcast('int', jget(in_, 'nval')))
            n = jcast('int', (n + 1))
        m = jcast('int', Code02_SkylineLuogu.prepare(n))
        Code02_SkylineLuogu.compute(n, m)
        jcall(out, 'print', jadd(jadd(Code02_SkylineLuogu.xsort[1], ' '), Code02_SkylineLuogu.height[1]))
        i = jcast('int', 2)
        pre = jcast('int', Code02_SkylineLuogu.height[1])
        while (i <= m):
            if (pre != Code02_SkylineLuogu.height[i]):
                jcall(out, 'print', jadd(jadd(jadd(' ', Code02_SkylineLuogu.xsort[i]), ' '), Code02_SkylineLuogu.height[i]))
            pre = jcast('int', Code02_SkylineLuogu.height[i])
            i = jcast('int', (i + 1))
        jcall(out, 'println')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n, m):
        n = jcast('int', n)
        m = jcast('int', m)
        i = jcast('int', 1)
        j = jcast('int', 0)
        while (i <= m):
            while ((j < n) and (Code02_SkylineLuogu.arr[j][0] <= i)):
                Code02_SkylineLuogu.push(Code02_SkylineLuogu.arr[j][2], Code02_SkylineLuogu.arr[j][1])
                j = jcast('int', (j + 1))
            while ((not Code02_SkylineLuogu.isEmpty()) and (Code02_SkylineLuogu.peekEnd() < i)):
                Code02_SkylineLuogu.poll()
            if (not Code02_SkylineLuogu.isEmpty()):
                jset(Code02_SkylineLuogu.height, i, Code02_SkylineLuogu.peekHeight())
            i = jcast('int', (i + 1))

    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        size = jcast('int', 0)
        i = jcast('int', 0)
        while (i < n):
            jset(Code02_SkylineLuogu.xsort, (size := jcast('int', (size + (1)))), Code02_SkylineLuogu.arr[i][0])
            jset(Code02_SkylineLuogu.xsort, (size := jcast('int', (size + (1)))), jcast('int', (Code02_SkylineLuogu.arr[i][1] - 1)))
            jset(Code02_SkylineLuogu.xsort, (size := jcast('int', (size + (1)))), Code02_SkylineLuogu.arr[i][1])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_SkylineLuogu.xsort, 1, jcast('int', jadd(size, 1)))
        m = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= size):
            if (Code02_SkylineLuogu.xsort[m] != Code02_SkylineLuogu.xsort[i]):
                jset(Code02_SkylineLuogu.xsort, (m := jcast('int', (m + (1)))), Code02_SkylineLuogu.xsort[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < n):
            jset(Code02_SkylineLuogu.arr[i], 0, Code02_SkylineLuogu.rank(m, Code02_SkylineLuogu.arr[i][0]))
            jset(Code02_SkylineLuogu.arr[i], 1, Code02_SkylineLuogu.rank(m, jcast('int', (Code02_SkylineLuogu.arr[i][1] - 1))))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_SkylineLuogu.arr, 0, n, (lambda a, b: (a[0] - b[0])))
        jstatic('Arrays', 'fill', Code02_SkylineLuogu.height, 1, jcast('int', jadd(m, 1)), 0)
        return jcast('int', m)

    @staticmethod
    def rank(n, v):
        n = jcast('int', n)
        v = jcast('int', v)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', n)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_SkylineLuogu.xsort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def isEmpty():
        return jcast('boolean', (Code02_SkylineLuogu.heapSize == 0))

    @staticmethod
    def peekHeight():
        return jcast('int', Code02_SkylineLuogu.heap[0][0])

    @staticmethod
    def peekEnd():
        return jcast('int', Code02_SkylineLuogu.heap[0][1])

    @staticmethod
    def push(h, e):
        h = jcast('int', h)
        e = jcast('int', e)
        jset(Code02_SkylineLuogu.heap[Code02_SkylineLuogu.heapSize], 0, h)
        jset(Code02_SkylineLuogu.heap[Code02_SkylineLuogu.heapSize], 1, e)
        Code02_SkylineLuogu.heapInsert(((_java_obj_1 := Code02_SkylineLuogu), (_java_key_2 := 'heapSize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4])

    @staticmethod
    def poll():
        Code02_SkylineLuogu.swap(0, ((_java_obj_4 := Code02_SkylineLuogu), (_java_key_5 := 'heapSize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))))[3])
        Code02_SkylineLuogu.heapify(0)

    @staticmethod
    def heapInsert(i):
        i = jcast('int', i)
        while (Code02_SkylineLuogu.heap[i][0] > Code02_SkylineLuogu.heap[jcast('int', jdiv(jcast('int', (i - 1)), 2))][0]):
            Code02_SkylineLuogu.swap(i, jcast('int', jdiv(jcast('int', (i - 1)), 2)))
            i = jcast('int', jcast('int', jdiv(jcast('int', (i - 1)), 2)))

    @staticmethod
    def heapify(i):
        i = jcast('int', i)
        l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
        while (l < Code02_SkylineLuogu.heapSize):
            try:
                best = jcast('int', (jcast('int', jadd(l, 1)) if ((jcast('int', jadd(l, 1)) < Code02_SkylineLuogu.heapSize) and (Code02_SkylineLuogu.heap[jcast('int', jadd(l, 1))][0] > Code02_SkylineLuogu.heap[l][0])) else l))
                best = jcast('int', (best if (Code02_SkylineLuogu.heap[best][0] > Code02_SkylineLuogu.heap[i][0]) else i))
                if (best == i):
                    raise JBreak(None)
                Code02_SkylineLuogu.swap(best, i)
                i = jcast('int', best)
                l = jcast('int', jcast('int', jadd(jcast('int', (i * 2)), 1)))
            except JContinue as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
            except JBreak as _java_control_7:
                if _java_control_7.label not in (None,):
                    raise
                break

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = Code02_SkylineLuogu.heap[i]
        Code02_SkylineLuogu.heap[i] = Code02_SkylineLuogu.heap[j]
        Code02_SkylineLuogu.heap[j] = tmp

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_SkylineLuogu.MAXN = jcast('int', 20001)
Code02_SkylineLuogu.arr = jarray('int', [Code02_SkylineLuogu.MAXN, 3])
Code02_SkylineLuogu.xsort = jarray('int', [Code02_SkylineLuogu.MAXN])
Code02_SkylineLuogu.height = jarray('int', [Code02_SkylineLuogu.MAXN])
Code02_SkylineLuogu.heap = jarray('int', [Code02_SkylineLuogu.MAXN, 2])
Code02_SkylineLuogu.heapSize = jcast('int', 0)

if __name__ == '__main__':
    Code02_SkylineLuogu.main([])

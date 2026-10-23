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

# 排队，Python版
# 给定一个长度为n的数组arr，下标1~n
# 如果有i < j，并且arr[i] > arr[j]，那么(i,j)就叫做一个逆序对
# 首先打印原始arr中有多少逆序对，然后进行如下类型的操作，一共发生m次
# 操作 a b : 交换arr中a位置的数和b位置的数，打印数组中逆序对的数量
# 1 <= n <= 2 * 10^4
# 1 <= m <= 2 * 10^3
# 1 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1975
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_LineUp2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'sorted': 'sorted', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'cnt': 'cnt', 'ans': 'ans'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    m = 0
    s = 0
    arr = None
    sorted = None
    root = None
    left = None
    right = None
    sum = None
    cnt = 0
    ans = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code06_LineUp2.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code06_LineUp2.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code06_LineUp2.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 线段树单点修改，jobi这个数字词频增加jobv
    @staticmethod
    def innerAdd(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_1 := Code06_LineUp2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        if (l == r):
            Code06_LineUp2.sum[i] = jcast('int', jcast('int', jadd(Code06_LineUp2.sum[i], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code06_LineUp2.left, i, Code06_LineUp2.innerAdd(jobi, jobv, l, mid, Code06_LineUp2.left[i]))
            else:
                jset(Code06_LineUp2.right, i, Code06_LineUp2.innerAdd(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code06_LineUp2.right[i]))
            Code06_LineUp2.sum[i] = jcast('int', jcast('int', jadd(Code06_LineUp2.sum[Code06_LineUp2.left[i]], Code06_LineUp2.sum[Code06_LineUp2.right[i]])))
        return jcast('int', i)

    # 查询的数字范围[jobl...jobr]，线段树的数字范围[l..r]，节点编号i
    # 返回有多少词频
    @staticmethod
    def innerQuery(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('int', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code06_LineUp2.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code06_LineUp2.innerQuery(jobl, jobr, l, mid, Code06_LineUp2.left[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code06_LineUp2.innerQuery(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code06_LineUp2.right[i]))))
        return jcast('int', ans)

    # arr的i位置的数字，词频增加v
    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        j = jcast('int', i)
        while (j <= Code06_LineUp2.n):
            jset(Code06_LineUp2.root, j, Code06_LineUp2.innerAdd(Code06_LineUp2.arr[i], v, 1, Code06_LineUp2.s, Code06_LineUp2.root[j]))
            j = jcast('int', jcast('int', jadd(j, Code06_LineUp2.lowbit(j))))

    # arr[al..ar]范围上，有多少数字在[numl..numr]范围上
    @staticmethod
    def query(al, ar, numl, numr):
        al = jcast('int', al)
        ar = jcast('int', ar)
        numl = jcast('int', numl)
        numr = jcast('int', numr)
        ans = jcast('int', 0)
        i = jcast('int', ar)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code06_LineUp2.innerQuery(numl, numr, 1, Code06_LineUp2.s, Code06_LineUp2.root[i]))))
            i = jcast('int', jcast('int', (i - Code06_LineUp2.lowbit(i))))
        i = jcast('int', jcast('int', (al - 1)))
        while (i > 0):
            ans = jcast('int', jcast('int', (ans - Code06_LineUp2.innerQuery(numl, numr, 1, Code06_LineUp2.s, Code06_LineUp2.root[i]))))
            i = jcast('int', jcast('int', (i - Code06_LineUp2.lowbit(i))))
        return jcast('int', ans)

    # 交换a和b位置的数字，保证a在前，b在后
    # 修正好逆序对的数量ans
    @staticmethod
    def compute(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        Code06_LineUp2.ans = jcast('int', jcast('int', (Code06_LineUp2.ans - Code06_LineUp2.query(jcast('int', jadd(a, 1)), jcast('int', (b - 1)), 1, jcast('int', (Code06_LineUp2.arr[a] - 1))))))
        Code06_LineUp2.ans = jcast('int', jcast('int', jadd(Code06_LineUp2.ans, Code06_LineUp2.query(jcast('int', jadd(a, 1)), jcast('int', (b - 1)), jcast('int', jadd(Code06_LineUp2.arr[a], 1)), Code06_LineUp2.s))))
        Code06_LineUp2.ans = jcast('int', jcast('int', (Code06_LineUp2.ans - Code06_LineUp2.query(jcast('int', jadd(a, 1)), jcast('int', (b - 1)), jcast('int', jadd(Code06_LineUp2.arr[b], 1)), Code06_LineUp2.s))))
        Code06_LineUp2.ans = jcast('int', jcast('int', jadd(Code06_LineUp2.ans, Code06_LineUp2.query(jcast('int', jadd(a, 1)), jcast('int', (b - 1)), 1, jcast('int', (Code06_LineUp2.arr[b] - 1))))))
        if (Code06_LineUp2.arr[a] < Code06_LineUp2.arr[b]):
            Code06_LineUp2.ans = jcast('int', (Code06_LineUp2.ans + 1))
        else:
            if (Code06_LineUp2.arr[a] > Code06_LineUp2.arr[b]):
                Code06_LineUp2.ans = jcast('int', (Code06_LineUp2.ans - 1))
        Code06_LineUp2.add(a, jcast('int', (-1)))
        Code06_LineUp2.add(b, jcast('int', (-1)))
        tmp = jcast('int', Code06_LineUp2.arr[a])
        Code06_LineUp2.arr[a] = jcast('int', Code06_LineUp2.arr[b])
        Code06_LineUp2.arr[b] = jcast('int', tmp)
        Code06_LineUp2.add(a, 1)
        Code06_LineUp2.add(b, 1)

    @staticmethod
    def prepare():
        Code06_LineUp2.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_LineUp2.n):
            jset(Code06_LineUp2.sorted, ((_java_obj_4 := Code06_LineUp2), (_java_key_5 := 's'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code06_LineUp2.arr[i])
            i = jcast('int', (i + 1))
        jset(Code06_LineUp2.sorted, ((_java_obj_7 := Code06_LineUp2), (_java_key_8 := 's'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], jcast('int', (-Code06_LineUp2.INF)))
        jset(Code06_LineUp2.sorted, ((_java_obj_10 := Code06_LineUp2), (_java_key_11 := 's'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3], Code06_LineUp2.INF)
        jstatic('Arrays', 'sort', Code06_LineUp2.sorted, 1, jcast('int', jadd(Code06_LineUp2.s, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code06_LineUp2.s):
            if (Code06_LineUp2.sorted[len] != Code06_LineUp2.sorted[i]):
                jset(Code06_LineUp2.sorted, (len := jcast('int', (len + (1)))), Code06_LineUp2.sorted[i])
            i = jcast('int', (i + 1))
        Code06_LineUp2.s = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code06_LineUp2.n):
            jset(Code06_LineUp2.arr, i, Code06_LineUp2.kth(Code06_LineUp2.arr[i]))
            Code06_LineUp2.add(i, 1)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_LineUp2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code06_LineUp2.n):
            jcall(in_, 'nextToken')
            Code06_LineUp2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code06_LineUp2.prepare()
        i = jcast('int', 2)
        while (i <= Code06_LineUp2.n):
            Code06_LineUp2.ans = jcast('int', jcast('int', jadd(Code06_LineUp2.ans, Code06_LineUp2.query(1, jcast('int', (i - 1)), jcast('int', jadd(Code06_LineUp2.arr[i], 1)), Code06_LineUp2.s))))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code06_LineUp2.ans)
        jcall(in_, 'nextToken')
        Code06_LineUp2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code06_LineUp2.m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            if (a > b):
                tmp = jcast('int', a)
                a = jcast('int', b)
                b = jcast('int', tmp)
            Code06_LineUp2.compute(a, b)
            jcall(out, 'println', Code06_LineUp2.ans)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_LineUp2.MAXN = jcast('int', 20001)
Code06_LineUp2.MAXT = jcast('int', jcast('int', (Code06_LineUp2.MAXN * 80)))
Code06_LineUp2.INF = jcast('int', 1000000001)
Code06_LineUp2.n = jcast('int', 0)
Code06_LineUp2.m = jcast('int', 0)
Code06_LineUp2.s = jcast('int', 0)
Code06_LineUp2.arr = jarray('int', [Code06_LineUp2.MAXN])
Code06_LineUp2.sorted = jarray('int', [jcast('int', jadd(Code06_LineUp2.MAXN, 2))])
Code06_LineUp2.root = jarray('int', [Code06_LineUp2.MAXN])
Code06_LineUp2.left = jarray('int', [Code06_LineUp2.MAXT])
Code06_LineUp2.right = jarray('int', [Code06_LineUp2.MAXT])
Code06_LineUp2.sum = jarray('int', [Code06_LineUp2.MAXT])
Code06_LineUp2.cnt = jcast('int', 0)
Code06_LineUp2.ans = jcast('int', 0)

if __name__ == '__main__':
    Code06_LineUp2.main([])

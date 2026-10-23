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

# 生成能量密度最大的宝石，Python版
# 给定一个长度为n的数组arr，数组中没有重复数字
# 你可以随意选择一个子数组，长度要求大于等于2，因为这样一来，子数组必存在次大值
# 子数组的次大值 ^ 子数组中除了次大值之外随意选一个数字
# 所能得到的最大结果，叫做子数组的能量密度
# 那么必有某个子数组，拥有最大的能量密度，打印这个最大的能量密度
# 2 <= n <= 5 * 10^4
# 0 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P4098
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_ALO2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'arr': 'arr', 'root': 'root', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt', 'last': 'last', 'next': 'next'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    arr = None
    root = None
    tree = None
    pass_ = None
    cnt = 0
    last = None
    next = None
    @staticmethod
    def insert(num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_1 := Code05_ALO2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code05_ALO2.tree[rt], 0, Code05_ALO2.tree[i][0])
        jset(Code05_ALO2.tree[rt], 1, Code05_ALO2.tree[i][1])
        Code05_ALO2.pass_[rt] = jcast('int', jcast('int', jadd(Code05_ALO2.pass_[i], 1)))
        b = jcast('int', Code05_ALO2.BIT)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            i = jcast('int', Code05_ALO2.tree[i][path])
            cur = jcast('int', ((_java_obj_4 := Code05_ALO2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            jset(Code05_ALO2.tree[cur], 0, Code05_ALO2.tree[i][0])
            jset(Code05_ALO2.tree[cur], 1, Code05_ALO2.tree[i][1])
            Code05_ALO2.pass_[cur] = jcast('int', jcast('int', jadd(Code05_ALO2.pass_[i], 1)))
            jset(Code05_ALO2.tree[pre], path, cur)
            b = jcast('int', (b - 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    @staticmethod
    def query(num, u, v):
        num = jcast('int', num)
        u = jcast('int', u)
        v = jcast('int', v)
        ans = jcast('int', 0)
        b = jcast('int', Code05_ALO2.BIT)
        path = 0
        best = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            best = jcast('int', jcast('int', (path ^ 1)))
            if (Code05_ALO2.pass_[Code05_ALO2.tree[v][best]] > Code05_ALO2.pass_[Code05_ALO2.tree[u][best]]):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (b & 31))))))
                u = jcast('int', Code05_ALO2.tree[u][best])
                v = jcast('int', Code05_ALO2.tree[v][best])
            else:
                u = jcast('int', Code05_ALO2.tree[u][path])
                v = jcast('int', Code05_ALO2.tree[v][path])
            b = jcast('int', (b - 1))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        Code05_ALO2.last[0] = jcast('int', 0)
        Code05_ALO2.next[0] = jcast('int', 1)
        Code05_ALO2.last[jcast('int', jadd(Code05_ALO2.n, 1))] = jcast('int', Code05_ALO2.n)
        Code05_ALO2.next[jcast('int', jadd(Code05_ALO2.n, 1))] = jcast('int', jcast('int', jadd(Code05_ALO2.n, 1)))
        i = jcast('int', 1)
        while (i <= Code05_ALO2.n):
            jset(Code05_ALO2.root, i, Code05_ALO2.insert(Code05_ALO2.arr[i][1], Code05_ALO2.root[jcast('int', (i - 1))]))
            Code05_ALO2.last[i] = jcast('int', jcast('int', (i - 1)))
            Code05_ALO2.next[i] = jcast('int', jcast('int', jadd(i, 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_ALO2.arr, 1, jcast('int', jadd(Code05_ALO2.n, 1)), (lambda a, b: (a[1] - b[1])))

    @staticmethod
    def compute():
        ans = jcast('int', 0)
        i = jcast('int', 1)
        index = 0
        value = 0
        l1 = 0
        l2 = 0
        r1 = 0
        r2 = 0
        while (i <= Code05_ALO2.n):
            index = jcast('int', Code05_ALO2.arr[i][0])
            value = jcast('int', Code05_ALO2.arr[i][1])
            l1 = jcast('int', Code05_ALO2.last[index])
            l2 = jcast('int', Code05_ALO2.last[l1])
            r1 = jcast('int', Code05_ALO2.next[index])
            r2 = jcast('int', Code05_ALO2.next[r1])
            if (l1 != 0):
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_ALO2.query(value, Code05_ALO2.root[l2], Code05_ALO2.root[jcast('int', (r1 - 1))])))
            if (r1 != jcast('int', jadd(Code05_ALO2.n, 1))):
                ans = jcast('int', jstatic('Math', 'max', ans, Code05_ALO2.query(value, Code05_ALO2.root[l1], Code05_ALO2.root[jcast('int', (r2 - 1))])))
            Code05_ALO2.next[l1] = jcast('int', r1)
            Code05_ALO2.last[r1] = jcast('int', l1)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_ALO2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_ALO2.n):
            jset(Code05_ALO2.arr[i], 0, i)
            jcall(in_, 'nextToken')
            jset(Code05_ALO2.arr[i], 1, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code05_ALO2.prepare()
        jcall(out, 'println', Code05_ALO2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_ALO2.MAXN = jcast('int', 50002)
Code05_ALO2.MAXT = jcast('int', jcast('int', (Code05_ALO2.MAXN * 32)))
Code05_ALO2.BIT = jcast('int', 30)
Code05_ALO2.n = jcast('int', 0)
Code05_ALO2.arr = jarray('int', [Code05_ALO2.MAXN, 2])
Code05_ALO2.root = jarray('int', [Code05_ALO2.MAXN])
Code05_ALO2.tree = jarray('int', [Code05_ALO2.MAXT, 2])
Code05_ALO2.pass_ = jarray('int', [Code05_ALO2.MAXT])
Code05_ALO2.cnt = jcast('int', 0)
Code05_ALO2.last = jarray('int', [Code05_ALO2.MAXN])
Code05_ALO2.next = jarray('int', [Code05_ALO2.MAXN])

if __name__ == '__main__':
    Code05_ALO2.main([])

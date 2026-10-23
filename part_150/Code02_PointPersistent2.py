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

# 单点修改的可持久化线段树模版题2，Python版
# 给定一个长度为n的数组arr，下标1~n，一共有m条查询
# 每条查询 l r k : 打印arr[l..r]中第k小的数字
# 1 <= n、m <= 2 * 10^5
# 0 <= arr[i] <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3834
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_PointPersistent2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 's': 's', 'arr': 'arr', 'sorted': 'sorted', 'root': 'root', 'left': 'left', 'right': 'right', 'size': 'size', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    s = 0
    # 原始数组
    arr = None
    # 收集权值排序并且去重做离散化
    sorted = None
    # 可持久化线段树需要
    # root[i] : 插入arr[i]之后形成新版本的线段树，记录头节点编号
    # 0号版本的线段树代表一个数字也没有时，每种名次的数字出现的次数
    # i号版本的线段树代表arr[1..i]范围内，每种名次的数字出现的次数
    root = None
    left = None
    right = None
    # 排名范围内收集了多少个数字
    size = None
    cnt = 0
    # 返回num在所有值中排名多少
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code02_PointPersistent2.s)
        mid = 0
        ans = jcast('int', 0)
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code02_PointPersistent2.sorted[mid] <= num):
                ans = jcast('int', mid)
                left = jcast('int', jcast('int', jadd(mid, 1)))
            else:
                right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', ans)

    # 排名范围l~r，建立线段树，返回头节点编号
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code02_PointPersistent2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code02_PointPersistent2.size[rt] = jcast('int', 0)
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code02_PointPersistent2.left, rt, Code02_PointPersistent2.build(l, mid))
            jset(Code02_PointPersistent2.right, rt, Code02_PointPersistent2.build(jcast('int', jadd(mid, 1)), r))
        return jcast('int', rt)

    # 排名范围l~r，信息在i号节点，增加一个排名为jobi的数字
    # 返回新的头节点编号
    @staticmethod
    def insert(jobi, l, r, i):
        jobi = jcast('int', jobi)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code02_PointPersistent2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        Code02_PointPersistent2.left[rt] = jcast('int', Code02_PointPersistent2.left[i])
        Code02_PointPersistent2.right[rt] = jcast('int', Code02_PointPersistent2.right[i])
        Code02_PointPersistent2.size[rt] = jcast('int', jcast('int', jadd(Code02_PointPersistent2.size[i], 1)))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobi <= mid):
                jset(Code02_PointPersistent2.left, rt, Code02_PointPersistent2.insert(jobi, l, mid, Code02_PointPersistent2.left[rt]))
            else:
                jset(Code02_PointPersistent2.right, rt, Code02_PointPersistent2.insert(jobi, jcast('int', jadd(mid, 1)), r, Code02_PointPersistent2.right[rt]))
        return jcast('int', rt)

    # 排名范围l~r，老版本信息在u号节点，新版本信息在v号节点
    # 返回，第jobk小的数字，排名多少
    @staticmethod
    def query(jobk, l, r, u, v):
        jobk = jcast('int', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        u = jcast('int', u)
        v = jcast('int', v)
        if (l == r):
            return jcast('int', l)
        lsize = jcast('int', jcast('int', (Code02_PointPersistent2.size[Code02_PointPersistent2.left[v]] - Code02_PointPersistent2.size[Code02_PointPersistent2.left[u]])))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        if (lsize >= jobk):
            return jcast('int', Code02_PointPersistent2.query(jobk, l, mid, Code02_PointPersistent2.left[u], Code02_PointPersistent2.left[v]))
        else:
            return jcast('int', Code02_PointPersistent2.query(jcast('int', (jobk - lsize)), jcast('int', jadd(mid, 1)), r, Code02_PointPersistent2.right[u], Code02_PointPersistent2.right[v]))

    # 权值做离散化并且去重 + 生成各版本的线段树
    @staticmethod
    def prepare():
        Code02_PointPersistent2.cnt = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_PointPersistent2.n):
            Code02_PointPersistent2.sorted[i] = jcast('int', Code02_PointPersistent2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_PointPersistent2.sorted, 1, jcast('int', jadd(Code02_PointPersistent2.n, 1)))
        Code02_PointPersistent2.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_PointPersistent2.n):
            if (Code02_PointPersistent2.sorted[Code02_PointPersistent2.s] != Code02_PointPersistent2.sorted[i]):
                jset(Code02_PointPersistent2.sorted, ((_java_obj_7 := Code02_PointPersistent2), (_java_key_8 := 's'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], Code02_PointPersistent2.sorted[i])
            i = jcast('int', (i + 1))
        jset(Code02_PointPersistent2.root, 0, Code02_PointPersistent2.build(1, Code02_PointPersistent2.s))
        i = jcast('int', 1)
        x = 0
        while (i <= Code02_PointPersistent2.n):
            x = jcast('int', Code02_PointPersistent2.kth(Code02_PointPersistent2.arr[i]))
            jset(Code02_PointPersistent2.root, i, Code02_PointPersistent2.insert(x, 1, Code02_PointPersistent2.s, Code02_PointPersistent2.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_PointPersistent2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_PointPersistent2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_PointPersistent2.n):
            jcall(in_, 'nextToken')
            Code02_PointPersistent2.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_PointPersistent2.prepare()
        i = jcast('int', 1)
        l = 0
        r = 0
        k = 0
        rank = 0
        while (i <= Code02_PointPersistent2.m):
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            k = jcast('int', jcast('int', jget(in_, 'nval')))
            rank = jcast('int', Code02_PointPersistent2.query(k, 1, Code02_PointPersistent2.s, Code02_PointPersistent2.root[jcast('int', (l - 1))], Code02_PointPersistent2.root[r]))
            jcall(out, 'println', Code02_PointPersistent2.sorted[rank])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_PointPersistent2.MAXN = jcast('int', 200001)
Code02_PointPersistent2.MAXT = jcast('int', jcast('int', (Code02_PointPersistent2.MAXN * 22)))
Code02_PointPersistent2.n = jcast('int', 0)
Code02_PointPersistent2.m = jcast('int', 0)
Code02_PointPersistent2.s = jcast('int', 0)
Code02_PointPersistent2.arr = jarray('int', [Code02_PointPersistent2.MAXN])
Code02_PointPersistent2.sorted = jarray('int', [Code02_PointPersistent2.MAXN])
Code02_PointPersistent2.root = jarray('int', [Code02_PointPersistent2.MAXN])
Code02_PointPersistent2.left = jarray('int', [Code02_PointPersistent2.MAXT])
Code02_PointPersistent2.right = jarray('int', [Code02_PointPersistent2.MAXT])
Code02_PointPersistent2.size = jarray('int', [Code02_PointPersistent2.MAXT])
Code02_PointPersistent2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code02_PointPersistent2.main([])

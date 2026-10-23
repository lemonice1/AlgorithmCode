# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# k大数查询，Python版
# 初始时有n个空集合，编号1~n，实现如下两种类型的操作，操作一共发生m次
# 操作 1 l r v : 数字v放入编号范围[l,r]的每一个集合中
# 操作 2 l r k : 编号范围[l,r]的所有集合，如果生成不去重的并集，返回第k大的数字
# 1 <= n、m <= 5 * 10^4
# -n <= v <= +n
# 1 <= k < 2^63，题目保证第k大的数字一定存在
# 测试链接 : https://www.luogu.com.cn/problem/P3332
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_QueryKthMaximum2:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 's': 's', 'ques': 'ques', 'sorted': 'sorted', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'lazy': 'lazy', 'cnt': 'cnt'}
    # 外部线段树的范围，一共只有m个操作，所以最多有m种数字
    MAXM = 0
    # 内部线段树的节点数上限
    MAXT = 0
    n = 0
    m = 0
    s = 0
    # 所有操作收集起来，因为牵扯到数字离散化
    ques = None
    # 所有可能的数字，收集起来去重，方便得到数字排名
    sorted = None
    # 外部(a~b) + 内部(c~d)表示：数字排名范围a~b，集合范围c~d，数字的个数
    # 外部线段树的下标表示数字的排名
    # 外部(a~b)，假设对应的节点编号为i，那么root[i]就是内部线段树的头节点编号
    root = None
    # 内部线段树是开点线段树，所以需要cnt来获得节点计数
    # 内部线段树的下标表示集合的编号
    # 内部(c~d)，假设对应的节点编号为i
    # sum[i]表示集合范围c~d，一共收集了多少数字
    # lazy[i]懒更新信息，集合范围c~d，增加了几个数字，等待懒更新的下发
    left = None
    right = None
    sum = None
    lazy = None
    cnt = 0
    @staticmethod
    def kth(num):
        num = jcast('int', num)
        left = jcast('int', 1)
        right = jcast('int', Code02_QueryKthMaximum2.s)
        mid = 0
        while (left <= right):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(left, right)), 2)))
            if (Code02_QueryKthMaximum2.sorted[mid] == num):
                return jcast('int', mid)
            else:
                if (Code02_QueryKthMaximum2.sorted[mid] < num):
                    left = jcast('int', jcast('int', jadd(mid, 1)))
                else:
                    right = jcast('int', jcast('int', (mid - 1)))
        return jcast('int', jcast('int', (-1)))

    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code02_QueryKthMaximum2.sum[i] = jcast('long', jcast('long', jadd(Code02_QueryKthMaximum2.sum[Code02_QueryKthMaximum2.left[i]], Code02_QueryKthMaximum2.sum[Code02_QueryKthMaximum2.right[i]])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code02_QueryKthMaximum2.lazy[i] != 0):
            if (Code02_QueryKthMaximum2.left[i] == 0):
                jset(Code02_QueryKthMaximum2.left, i, ((_java_obj_1 := Code02_QueryKthMaximum2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            if (Code02_QueryKthMaximum2.right[i] == 0):
                jset(Code02_QueryKthMaximum2.right, i, ((_java_obj_4 := Code02_QueryKthMaximum2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            ((_java_obj_7 := Code02_QueryKthMaximum2.sum), (_java_key_8 := Code02_QueryKthMaximum2.left[i]), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), jcast('int', (Code02_QueryKthMaximum2.lazy[i] * ln))))))[2]
            ((_java_obj_9 := Code02_QueryKthMaximum2.lazy), (_java_key_10 := Code02_QueryKthMaximum2.left[i]), jset(_java_obj_9, _java_key_10, jcast('int', jadd(jget(_java_obj_9, _java_key_10), Code02_QueryKthMaximum2.lazy[i]))))[2]
            ((_java_obj_11 := Code02_QueryKthMaximum2.sum), (_java_key_12 := Code02_QueryKthMaximum2.right[i]), jset(_java_obj_11, _java_key_12, jcast('long', jadd(jget(_java_obj_11, _java_key_12), jcast('int', (Code02_QueryKthMaximum2.lazy[i] * rn))))))[2]
            ((_java_obj_13 := Code02_QueryKthMaximum2.lazy), (_java_key_14 := Code02_QueryKthMaximum2.right[i]), jset(_java_obj_13, _java_key_14, jcast('int', jadd(jget(_java_obj_13, _java_key_14), Code02_QueryKthMaximum2.lazy[i]))))[2]
            Code02_QueryKthMaximum2.lazy[i] = jcast('int', 0)

    @staticmethod
    def innerAdd(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            i = jcast('int', ((_java_obj_15 := Code02_QueryKthMaximum2), (_java_key_16 := 'cnt'), (_java_old_17 := jget(_java_obj_15, _java_key_16)), jset(_java_obj_15, _java_key_16, jcast('int', (_java_old_17 + (1)))))[3])
        if ((jobl <= l) and (r <= jobr)):
            Code02_QueryKthMaximum2.sum[i] = jcast('long', jcast('long', jadd(Code02_QueryKthMaximum2.sum[i], jcast('int', jadd(jcast('int', (r - l)), 1)))))
            Code02_QueryKthMaximum2.lazy[i] = jcast('int', (Code02_QueryKthMaximum2.lazy[i] + 1))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            Code02_QueryKthMaximum2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                jset(Code02_QueryKthMaximum2.left, i, Code02_QueryKthMaximum2.innerAdd(jobl, jobr, l, mid, Code02_QueryKthMaximum2.left[i]))
            if (jobr > mid):
                jset(Code02_QueryKthMaximum2.right, i, Code02_QueryKthMaximum2.innerAdd(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_QueryKthMaximum2.right[i]))
            Code02_QueryKthMaximum2.up(i)
        return jcast('int', i)

    @staticmethod
    def innerQuery(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (i == 0):
            return jcast('long', 0)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code02_QueryKthMaximum2.sum[i])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code02_QueryKthMaximum2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code02_QueryKthMaximum2.innerQuery(jobl, jobr, l, mid, Code02_QueryKthMaximum2.left[i]))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code02_QueryKthMaximum2.innerQuery(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code02_QueryKthMaximum2.right[i]))))
        return jcast('long', ans)

    @staticmethod
    def outerAdd(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        jset(Code02_QueryKthMaximum2.root, i, Code02_QueryKthMaximum2.innerAdd(jobl, jobr, 1, Code02_QueryKthMaximum2.n, Code02_QueryKthMaximum2.root[i]))
        if (l < r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobv <= mid):
                Code02_QueryKthMaximum2.outerAdd(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code02_QueryKthMaximum2.outerAdd(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def outerQuery(jobl, jobr, jobk, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobk = jcast('long', jobk)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        rightsum = jcast('long', Code02_QueryKthMaximum2.innerQuery(jobl, jobr, 1, Code02_QueryKthMaximum2.n, Code02_QueryKthMaximum2.root[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))
        if (jobk > rightsum):
            return jcast('int', Code02_QueryKthMaximum2.outerQuery(jobl, jobr, jcast('long', (jobk - rightsum)), l, mid, jcast('int', (i << (1 & 31)))))
        else:
            return jcast('int', Code02_QueryKthMaximum2.outerQuery(jobl, jobr, jobk, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))

    @staticmethod
    def prepare():
        Code02_QueryKthMaximum2.s = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code02_QueryKthMaximum2.m):
            if (Code02_QueryKthMaximum2.ques[i][0] == 1):
                jset(Code02_QueryKthMaximum2.sorted, ((_java_obj_18 := Code02_QueryKthMaximum2), (_java_key_19 := 's'), (_java_old_20 := jget(_java_obj_18, _java_key_19)), jset(_java_obj_18, _java_key_19, jcast('int', (_java_old_20 + (1)))))[3], Code02_QueryKthMaximum2.ques[i][3])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_QueryKthMaximum2.sorted, 1, jcast('int', jadd(Code02_QueryKthMaximum2.s, 1)))
        len = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_QueryKthMaximum2.s):
            if (Code02_QueryKthMaximum2.sorted[len] != Code02_QueryKthMaximum2.sorted[i]):
                jset(Code02_QueryKthMaximum2.sorted, (len := jcast('int', (len + (1)))), Code02_QueryKthMaximum2.sorted[i])
            i = jcast('int', (i + 1))
        Code02_QueryKthMaximum2.s = jcast('int', len)
        i = jcast('int', 1)
        while (i <= Code02_QueryKthMaximum2.m):
            if (Code02_QueryKthMaximum2.ques[i][0] == 1):
                jset(Code02_QueryKthMaximum2.ques[i], 3, Code02_QueryKthMaximum2.kth(Code02_QueryKthMaximum2.ques[i][3]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_QueryKthMaximum2.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_QueryKthMaximum2.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_QueryKthMaximum2.m):
            jcall(in_, 'nextToken')
            jset(Code02_QueryKthMaximum2.ques[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_QueryKthMaximum2.ques[i], 1, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_QueryKthMaximum2.ques[i], 2, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code02_QueryKthMaximum2.ques[i], 3, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code02_QueryKthMaximum2.prepare()
        i = jcast('int', 1)
        while (i <= Code02_QueryKthMaximum2.m):
            if (Code02_QueryKthMaximum2.ques[i][0] == 1):
                Code02_QueryKthMaximum2.outerAdd(Code02_QueryKthMaximum2.ques[i][1], Code02_QueryKthMaximum2.ques[i][2], Code02_QueryKthMaximum2.ques[i][3], 1, Code02_QueryKthMaximum2.s, 1)
            else:
                idx = jcast('int', Code02_QueryKthMaximum2.outerQuery(Code02_QueryKthMaximum2.ques[i][1], Code02_QueryKthMaximum2.ques[i][2], Code02_QueryKthMaximum2.ques[i][3], 1, Code02_QueryKthMaximum2.s, 1))
                jcall(out, 'println', Code02_QueryKthMaximum2.sorted[idx])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_QueryKthMaximum2.MAXM = jcast('int', 50001)
Code02_QueryKthMaximum2.MAXT = jcast('int', jcast('int', (Code02_QueryKthMaximum2.MAXM * 230)))
Code02_QueryKthMaximum2.n = jcast('int', 0)
Code02_QueryKthMaximum2.m = jcast('int', 0)
Code02_QueryKthMaximum2.s = jcast('int', 0)
Code02_QueryKthMaximum2.ques = jarray('int', [Code02_QueryKthMaximum2.MAXM, 4])
Code02_QueryKthMaximum2.sorted = jarray('int', [Code02_QueryKthMaximum2.MAXM])
Code02_QueryKthMaximum2.root = jarray('int', [jcast('int', (Code02_QueryKthMaximum2.MAXM << (2 & 31)))])
Code02_QueryKthMaximum2.left = jarray('int', [Code02_QueryKthMaximum2.MAXT])
Code02_QueryKthMaximum2.right = jarray('int', [Code02_QueryKthMaximum2.MAXT])
Code02_QueryKthMaximum2.sum = jarray('long', [Code02_QueryKthMaximum2.MAXT])
Code02_QueryKthMaximum2.lazy = jarray('int', [Code02_QueryKthMaximum2.MAXT])
Code02_QueryKthMaximum2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code02_QueryKthMaximum2.main([])

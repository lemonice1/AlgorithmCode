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

# 基站选址
# 一共有n个村庄排成一排，从左往右依次出现1号、2号、3号..n号村庄
# dist[i]表示i号村庄到1号村庄的距离，该数组一定有序且无重复值
# fix[i]表示i号村庄建立基站的安装费用
# range[i]表示i号村庄的接收范围，任何基站和i号村庄的距离不超过这个数字，i号村庄就能得到服务
# warranty[i]表示如果i号村庄最终没有得到任何基站的服务，需要给多少赔偿费用
# 最多可以选择k个村庄安装基站，返回总花费最少是多少，总花费包括安装费用和赔偿费用
# 1 <= n <= 20000
# 1 <= k <= 100
# k <= n
# 1 <= dist[i] <= 10^9
# 1 <= fix[i] <= 10^4
# 1 <= range[i] <= 10^9
# 1 <= warranty[i] <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P2605
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_StationLocation:
    __java_fields__ = {'n': 'n', 'k': 'k', 'MAXN': 'MAXN', 'dist': 'dist', 'fix': 'fix', 'range': 'range', 'warranty': 'warranty', 'left': 'left', 'right': 'right', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'min': 'min', 'add': 'add_data', 'dp': 'dp'}
    n = 0
    k = 0
    # 因为要补充一个村庄(无穷远处)，所以村庄编号1~20001，那么空间为20002
    MAXN = 0
    # 和1号村庄之间的距离
    dist = None
    # 安装费用
    fix = None
    # 接收范围
    range = None
    # 赔偿费用
    warranty = None
    # left[i]表示最左在第几号村庄建基站，i号村庄依然能获得服务
    left = None
    # right[i]表示最右在第几号村庄建基站，i号村庄依然能获得服务
    right = None
    # 链式前向星
    # 保存每个村庄的预警列表，i号村庄的预警列表是指
    # 如果只有一个基站建在i号村庄，现在这个基站要移动到i+1号村庄
    # 哪些村庄会从有服务变成无服务的状态
    head = None
    next = None
    to = None
    cnt = 0
    # 线段树维护最小值信息
    min = None
    # 线段树维护加的懒更新
    add_data = None
    # 动态规划表
    # dp[t][i]表示最多建t个基站，并且最右的基站一定要建在i号村庄，1..i号村庄的最少花费
    # 因为dp[t][i]，只依赖dp[t-1][..]，所以能空间压缩变成一维数组
    dp = None
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_StationLocation.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_StationLocation.k = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 2)
        while (i <= Code06_StationLocation.n):
            jcall(in_, 'nextToken')
            Code06_StationLocation.dist[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_StationLocation.n):
            jcall(in_, 'nextToken')
            Code06_StationLocation.fix[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_StationLocation.n):
            jcall(in_, 'nextToken')
            Code06_StationLocation.range[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code06_StationLocation.n):
            jcall(in_, 'nextToken')
            Code06_StationLocation.warranty[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        # 补充了一个村庄，认为在无穷远的位置，其他数据都是0
        jset(Code06_StationLocation.dist, ((_java_obj_1 := Code06_StationLocation), (_java_key_2 := 'n'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], jget(Integer, 'MAX_VALUE'))
        jset(Code06_StationLocation.fix, Code06_StationLocation.n, jset(Code06_StationLocation.range, Code06_StationLocation.n, jset(Code06_StationLocation.warranty, Code06_StationLocation.n, 0)))
        Code06_StationLocation.prepare()
        jcall(out, 'println', Code06_StationLocation.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # n是加上补充村庄(无穷远处)之后的村子数量
    # 所以dp[t][n]的值代表
    # 最右有一个单独的基站，去负责补充村庄，这一部分的花费是0
    # 剩余有最多t-1个基站，去负责真实出现的村庄，最少的总费用
    # 所以t一定要从1枚举到k+1，对应真实村子最多分到0个~k个基站的情况
    # 这么做可以减少边界讨论，课上进行了图解
    @staticmethod
    def compute():
        # 最多建t=1个基站的情况
        i = jcast('int', 1)
        w = jcast('int', 0)
        while (i <= Code06_StationLocation.n):
            Code06_StationLocation.dp[i] = jcast('int', jcast('int', jadd(w, Code06_StationLocation.fix[i])))
            ei = jcast('int', Code06_StationLocation.head[i])
            while (ei != 0):
                w = jcast('int', jcast('int', jadd(w, Code06_StationLocation.warranty[Code06_StationLocation.to[ei]])))
                ei = jcast('int', Code06_StationLocation.next[ei])
            i = jcast('int', (i + 1))
        # 最多建t>=2个基站的情况
        t = jcast('int', 2)
        while (t <= jcast('int', jadd(Code06_StationLocation.k, 1))):
            Code06_StationLocation.build(1, Code06_StationLocation.n, 1)
            i = jcast('int', 1)
            while (i <= Code06_StationLocation.n):
                if (i >= t):
                    jset(Code06_StationLocation.dp, i, jstatic('Math', 'min', Code06_StationLocation.dp[i], jcast('int', jadd(Code06_StationLocation.query(1, jcast('int', (i - 1)), 1, Code06_StationLocation.n, 1), Code06_StationLocation.fix[i]))))
                ei = jcast('int', Code06_StationLocation.head[i])
                uncover = 0
                while (ei != 0):
                    uncover = jcast('int', Code06_StationLocation.to[ei])
                    if (Code06_StationLocation.left[uncover] > 1):
                        Code06_StationLocation.add(1, jcast('int', (Code06_StationLocation.left[uncover] - 1)), Code06_StationLocation.warranty[uncover], 1, Code06_StationLocation.n, 1)
                    ei = jcast('int', Code06_StationLocation.next[ei])
                i = jcast('int', (i + 1))
            t = jcast('int', (t + 1))
        return jcast('int', Code06_StationLocation.dp[Code06_StationLocation.n])

    # 生成left[0..n]
    # 生成right[0..n]
    # 生成预警[0..n]
    @staticmethod
    def prepare():
        Code06_StationLocation.cnt = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= Code06_StationLocation.n):
            jset(Code06_StationLocation.left, i, Code06_StationLocation.search(jcast('int', (Code06_StationLocation.dist[i] - Code06_StationLocation.range[i]))))
            jset(Code06_StationLocation.right, i, Code06_StationLocation.search(jcast('int', jadd(Code06_StationLocation.dist[i], Code06_StationLocation.range[i]))))
            if (Code06_StationLocation.dist[Code06_StationLocation.right[i]] > jcast('int', jadd(Code06_StationLocation.dist[i], Code06_StationLocation.range[i]))):
                # 如果if逻辑命中
                # 说明此时right[i]上建基站，其实i号村庄是收不到信号的
                # 此时right[i]要减1
                Code06_StationLocation.right[i] = jcast('int', (Code06_StationLocation.right[i] - 1))
            # 生成预警列表
            # 比如right[3] = 17
            # 那么17号村庄的预警列表里有3
            Code06_StationLocation.addEdge(Code06_StationLocation.right[i], i)
            i = jcast('int', (i + 1))

    # 在dist数组中二分查找>=d的最左位置
    @staticmethod
    def search(d):
        d = jcast('int', d)
        l = jcast('int', 1)
        r = jcast('int', Code06_StationLocation.n)
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code06_StationLocation.dist[m] >= d):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    # 链式前向星加边
    # 其实就是u的预警列表里增加v
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        Code06_StationLocation.next[Code06_StationLocation.cnt] = jcast('int', Code06_StationLocation.head[u])
        Code06_StationLocation.to[Code06_StationLocation.cnt] = jcast('int', v)
        jset(Code06_StationLocation.head, u, ((_java_obj_4 := Code06_StationLocation), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4])

    # 下面所有方法都是线段树维护最小值的模版，没有任何修改
    @staticmethod
    def up(i):
        i = jcast('int', i)
        jset(Code06_StationLocation.min, i, jstatic('Math', 'min', Code06_StationLocation.min[jcast('int', (i << (1 & 31)))], Code06_StationLocation.min[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code06_StationLocation.add_data[i] != 0):
            Code06_StationLocation.lazy(jcast('int', (i << (1 & 31))), Code06_StationLocation.add_data[i])
            Code06_StationLocation.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code06_StationLocation.add_data[i])
            Code06_StationLocation.add_data[i] = jcast('int', 0)

    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        Code06_StationLocation.min[i] = jcast('int', jcast('int', jadd(Code06_StationLocation.min[i], v)))
        Code06_StationLocation.add_data[i] = jcast('int', jcast('int', jadd(Code06_StationLocation.add_data[i], v)))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code06_StationLocation.min[i] = jcast('int', Code06_StationLocation.dp[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code06_StationLocation.build(l, mid, jcast('int', (i << (1 & 31))))
            Code06_StationLocation.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_StationLocation.up(i)
        Code06_StationLocation.add_data[i] = jcast('int', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code06_StationLocation.lazy(i, jobv)
        else:
            Code06_StationLocation.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code06_StationLocation.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code06_StationLocation.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code06_StationLocation.up(i)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code06_StationLocation.min[i])
        Code06_StationLocation.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', jget(Integer, 'MAX_VALUE'))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code06_StationLocation.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code06_StationLocation.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_StationLocation.n = jcast('int', 0)
Code06_StationLocation.k = jcast('int', 0)
Code06_StationLocation.MAXN = jcast('int', 20002)
Code06_StationLocation.dist = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.fix = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.range = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.warranty = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.left = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.right = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.head = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.next = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.to = jarray('int', [Code06_StationLocation.MAXN])
Code06_StationLocation.cnt = jcast('int', 0)
Code06_StationLocation.min = jarray('int', [jcast('int', (Code06_StationLocation.MAXN << (2 & 31)))])
Code06_StationLocation.add_data = jarray('int', [jcast('int', (Code06_StationLocation.MAXN << (2 & 31)))])
Code06_StationLocation.dp = jarray('int', [Code06_StationLocation.MAXN])

if __name__ == '__main__':
    Code06_StationLocation.main([])

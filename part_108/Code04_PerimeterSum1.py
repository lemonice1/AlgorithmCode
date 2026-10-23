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

# 矩形周长并(洛谷测试)
# 测试链接 : https://www.luogu.com.cn/problem/P1856
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_PerimeterSum1:
    __java_fields__ = {'MAXN': 'MAXN', 'rec': 'rec', 'line': 'line', 'vsort': 'vsort', 'length': 'length', 'cover': 'cover', 'times': 'times'}
    MAXN = 0
    rec = None
    line = None
    vsort = None
    # 线段树某范围总长度
    length = None
    # 线段树某范围覆盖长度
    cover = None
    # 线段树某范围覆盖次数
    times = None
    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        jstatic('Arrays', 'sort', Code04_PerimeterSum1.vsort, 1, jcast('int', jadd(n, 1)))
        m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= n):
            if (Code04_PerimeterSum1.vsort[m] != Code04_PerimeterSum1.vsort[i]):
                jset(Code04_PerimeterSum1.vsort, (m := jcast('int', (m + (1)))), Code04_PerimeterSum1.vsort[i])
            i = jcast('int', (i + 1))
        Code04_PerimeterSum1.vsort[jcast('int', jadd(m, 1))] = jcast('int', Code04_PerimeterSum1.vsort[m])
        return jcast('int', m)

    @staticmethod
    def rank(n, num):
        n = jcast('int', n)
        num = jcast('int', num)
        ans = jcast('int', 0)
        l = jcast('int', 1)
        r = jcast('int', n)
        mid = 0
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code04_PerimeterSum1.vsort[mid] >= num):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_PerimeterSum1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_PerimeterSum1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code04_PerimeterSum1.length[i] = jcast('int', jcast('int', (Code04_PerimeterSum1.vsort[jcast('int', jadd(r, 1))] - Code04_PerimeterSum1.vsort[l])))
        Code04_PerimeterSum1.times[i] = jcast('int', 0)
        Code04_PerimeterSum1.cover[i] = jcast('int', 0)

    @staticmethod
    def up(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (Code04_PerimeterSum1.times[i] > 0):
            Code04_PerimeterSum1.cover[i] = jcast('int', Code04_PerimeterSum1.length[i])
        else:
            if (l == r):
                # 叶节点直接设置cover不需要下层信息
                Code04_PerimeterSum1.cover[i] = jcast('int', 0)
            else:
                Code04_PerimeterSum1.cover[i] = jcast('int', jcast('int', jadd(Code04_PerimeterSum1.cover[jcast('int', (i << (1 & 31)))], Code04_PerimeterSum1.cover[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_PerimeterSum1.times[i] = jcast('int', jcast('int', jadd(Code04_PerimeterSum1.times[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code04_PerimeterSum1.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_PerimeterSum1.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code04_PerimeterSum1.up(l, r, i)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            # 左下角下标
            jcall(in_, 'nextToken')
            jset(Code04_PerimeterSum1.rec[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_PerimeterSum1.rec[i], 1, jcast('int', jget(in_, 'nval')))
            # 右上角下标
            jcall(in_, 'nextToken')
            jset(Code04_PerimeterSum1.rec[i], 2, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code04_PerimeterSum1.rec[i], 3, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code04_PerimeterSum1.compute(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('int', n)
        return jcast('long', jcast('long', jadd(Code04_PerimeterSum1.scanY(n), Code04_PerimeterSum1.scanX(n))))

    @staticmethod
    def scanY(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        j = jcast('int', jcast('int', jadd(1, n)))
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        while (i <= n):
            x1 = jcast('int', Code04_PerimeterSum1.rec[i][0])
            y1 = jcast('int', Code04_PerimeterSum1.rec[i][1])
            x2 = jcast('int', Code04_PerimeterSum1.rec[i][2])
            y2 = jcast('int', Code04_PerimeterSum1.rec[i][3])
            Code04_PerimeterSum1.vsort[i] = jcast('int', y1)
            Code04_PerimeterSum1.vsort[j] = jcast('int', y2)
            jset(Code04_PerimeterSum1.line[i], 0, x1)
            jset(Code04_PerimeterSum1.line[i], 1, y1)
            jset(Code04_PerimeterSum1.line[i], 2, y2)
            jset(Code04_PerimeterSum1.line[i], 3, 1)
            jset(Code04_PerimeterSum1.line[j], 0, x2)
            jset(Code04_PerimeterSum1.line[j], 1, y1)
            jset(Code04_PerimeterSum1.line[j], 2, y2)
            jset(Code04_PerimeterSum1.line[j], 3, jcast('int', (-1)))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jcast('long', Code04_PerimeterSum1.scan(jcast('int', (n << (1 & 31)))))

    @staticmethod
    def scanX(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        j = jcast('int', jcast('int', jadd(1, n)))
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        while (i <= n):
            x1 = jcast('int', Code04_PerimeterSum1.rec[i][0])
            y1 = jcast('int', Code04_PerimeterSum1.rec[i][1])
            x2 = jcast('int', Code04_PerimeterSum1.rec[i][2])
            y2 = jcast('int', Code04_PerimeterSum1.rec[i][3])
            Code04_PerimeterSum1.vsort[i] = jcast('int', x1)
            Code04_PerimeterSum1.vsort[j] = jcast('int', x2)
            jset(Code04_PerimeterSum1.line[i], 0, y1)
            jset(Code04_PerimeterSum1.line[i], 1, x1)
            jset(Code04_PerimeterSum1.line[i], 2, x2)
            jset(Code04_PerimeterSum1.line[i], 3, 1)
            jset(Code04_PerimeterSum1.line[j], 0, y2)
            jset(Code04_PerimeterSum1.line[j], 1, x1)
            jset(Code04_PerimeterSum1.line[j], 2, x2)
            jset(Code04_PerimeterSum1.line[j], 3, jcast('int', (-1)))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        return jcast('long', Code04_PerimeterSum1.scan(jcast('int', (n << (1 & 31)))))

    @staticmethod
    def scan(n):
        n = jcast('int', n)
        m = jcast('int', Code04_PerimeterSum1.prepare(n))
        Code04_PerimeterSum1.build(1, m, 1)
        # 这里有个坑
        # 在排序时，如果同一个位置的扫描线有多条，也就是a[0] == b[0]时
        # 应该先处理区间覆盖+1的扫描线，然后再处理区间覆盖-1的扫描线
        # 不然投影长度会频繁变化，导致答案错误
        # 不过测试数据并没有安排这方面的测试
        jstatic('Arrays', 'sort', Code04_PerimeterSum1.line, 1, jcast('int', jadd(n, 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (b[3] - a[3]))))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        pre = 0
        while (i <= n):
            pre = jcast('int', Code04_PerimeterSum1.cover[1])
            Code04_PerimeterSum1.add(Code04_PerimeterSum1.rank(m, Code04_PerimeterSum1.line[i][1]), jcast('int', (Code04_PerimeterSum1.rank(m, Code04_PerimeterSum1.line[i][2]) - 1)), Code04_PerimeterSum1.line[i][3], 1, m, 1)
            ans = jcast('long', jcast('long', jadd(ans, jstatic('Math', 'abs', jcast('int', (Code04_PerimeterSum1.cover[1] - pre))))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PerimeterSum1.MAXN = jcast('int', 10001)
Code04_PerimeterSum1.rec = jarray('int', [Code04_PerimeterSum1.MAXN, 4])
Code04_PerimeterSum1.line = jarray('int', [Code04_PerimeterSum1.MAXN, 4])
Code04_PerimeterSum1.vsort = jarray('int', [Code04_PerimeterSum1.MAXN])
Code04_PerimeterSum1.length = jarray('int', [jcast('int', (Code04_PerimeterSum1.MAXN << (2 & 31)))])
Code04_PerimeterSum1.cover = jarray('int', [jcast('int', (Code04_PerimeterSum1.MAXN << (2 & 31)))])
Code04_PerimeterSum1.times = jarray('int', [jcast('int', (Code04_PerimeterSum1.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_PerimeterSum1.main([])

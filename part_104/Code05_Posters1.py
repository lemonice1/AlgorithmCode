# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 贴海报
# 有一面墙，有固定高度，长度为n，有m张海报，所有海报的高度都和墙的高度相同
# 从第1张海报开始，一张一张往墙上贴，直到n张海报贴完
# 每张海报都给出张贴位置(xi, yi)，表示第i张海报从墙的左边界xi一直延伸到右边界yi
# 有可能发生后面的海报把前面的海报完全覆盖，导致看不到的情况
# 当所有海报贴完，返回能看到海报的数量，哪怕只漏出一点的海报都算
# 1 <= n、xi、yi <= 10^7，1 <= m <= 10^3
# 测试链接 : https://www.luogu.com.cn/problem/P3740
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_Posters1:
    __java_fields__ = {'MAXM': 'MAXM', 'pl': 'pl', 'pr': 'pr', 'num': 'num', 'poster': 'poster', 'visited': 'visited'}
    MAXM = 0
    pl = None
    pr = None
    num = None
    # 线段树的某个范围上是否被设置成了统一的海报
    # 如果poster[i] != 0，poster[i]表示统一海报的编号
    # 如果poster[i] == 0，表示该范围上没有海报或者海报编号没统一
    poster = None
    # 某种海报编号是否已经被统计过了
    # 只在最后一次查询，最后统计海报数量的阶段时候使用
    visited = None
    @staticmethod
    def collect(m):
        m = jcast('int', m)
        jstatic('Arrays', 'sort', Code05_Posters1.num, 1, jcast('int', jadd(m, 1)))
        size = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= m):
            if (Code05_Posters1.num[size] != Code05_Posters1.num[i]):
                jset(Code05_Posters1.num, (size := jcast('int', (size + (1)))), Code05_Posters1.num[i])
            i = jcast('int', (i + 1))
        cnt = jcast('int', size)
        i = jcast('int', 2)
        while (i <= size):
            if (jcast('int', jadd(Code05_Posters1.num[jcast('int', (i - 1))], 1)) < Code05_Posters1.num[i]):
                jset(Code05_Posters1.num, (cnt := jcast('int', (cnt + (1)))), jcast('int', jadd(Code05_Posters1.num[jcast('int', (i - 1))], 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_Posters1.num, 1, jcast('int', jadd(cnt, 1)))
        return jcast('int', cnt)

    @staticmethod
    def rank(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code05_Posters1.num[m] >= v):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if (Code05_Posters1.poster[i] != 0):
            Code05_Posters1.poster[jcast('int', (i << (1 & 31)))] = jcast('int', Code05_Posters1.poster[i])
            Code05_Posters1.poster[jcast('int', (jcast('int', (i << (1 & 31))) | 1))] = jcast('int', Code05_Posters1.poster[i])
            Code05_Posters1.poster[i] = jcast('int', 0)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code05_Posters1.build(l, mid, jcast('int', (i << (1 & 31))))
            Code05_Posters1.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code05_Posters1.poster[i] = jcast('int', 0)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code05_Posters1.poster[i] = jcast('int', jobv)
        else:
            Code05_Posters1.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code05_Posters1.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code05_Posters1.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            if ((Code05_Posters1.poster[i] != 0) and (not Code05_Posters1.visited[Code05_Posters1.poster[i]])):
                jset(Code05_Posters1.visited, Code05_Posters1.poster[i], True)
                return jcast('int', 1)
            else:
                return jcast('int', 0)
        else:
            Code05_Posters1.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            ans = jcast('int', 0)
            if (jobl <= mid):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Posters1.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
            if (jobr > mid):
                ans = jcast('int', jcast('int', jadd(ans, Code05_Posters1.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
            return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        size = jcast('int', 0)
        jset(Code05_Posters1.num, (size := jcast('int', (size + (1)))), n)
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= m):
            jcall(in_, 'nextToken')
            Code05_Posters1.pl[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code05_Posters1.pr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            jset(Code05_Posters1.num, (size := jcast('int', (size + (1)))), Code05_Posters1.pl[i])
            jset(Code05_Posters1.num, (size := jcast('int', (size + (1)))), Code05_Posters1.pr[i])
            i = jcast('int', (i + 1))
        size = jcast('int', Code05_Posters1.collect(size))
        Code05_Posters1.build(1, size, 1)
        i = jcast('int', 1)
        jobl = 0
        jobr = 0
        while (i <= m):
            jobl = jcast('int', Code05_Posters1.rank(1, size, Code05_Posters1.pl[i]))
            jobr = jcast('int', Code05_Posters1.rank(1, size, Code05_Posters1.pr[i]))
            Code05_Posters1.update(jobl, jobr, i, 1, size, 1)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code05_Posters1.query(1, Code05_Posters1.rank(1, size, n), 1, size, 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_Posters1.MAXM = jcast('int', 1001)
Code05_Posters1.pl = jarray('int', [Code05_Posters1.MAXM])
Code05_Posters1.pr = jarray('int', [Code05_Posters1.MAXM])
Code05_Posters1.num = jarray('int', [jcast('int', (Code05_Posters1.MAXM << (2 & 31)))])
Code05_Posters1.poster = jarray('int', [jcast('int', (Code05_Posters1.MAXM << (4 & 31)))])
Code05_Posters1.visited = jarray('boolean', [Code05_Posters1.MAXM])

if __name__ == '__main__':
    Code05_Posters1.main([])

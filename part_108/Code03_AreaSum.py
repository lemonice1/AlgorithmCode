# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 矩形面积并
# 测试链接 : https://www.luogu.com.cn/problem/P5490
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_AreaSum:
    __java_fields__ = {'MAXN': 'MAXN', 'rec': 'rec', 'line': 'line', 'ysort': 'ysort', 'length': 'length', 'cover': 'cover', 'times': 'times'}
    MAXN = 0
    rec = None
    line = None
    ysort = None
    # 线段树某范围总长度
    length = None
    # 线段树某范围覆盖长度
    cover = None
    # 线段树某范围覆盖次数
    times = None
    @staticmethod
    def prepare(n):
        n = jcast('int', n)
        jstatic('Arrays', 'sort', Code03_AreaSum.ysort, 1, jcast('int', jadd(n, 1)))
        m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= n):
            if (Code03_AreaSum.ysort[m] != Code03_AreaSum.ysort[i]):
                jset(Code03_AreaSum.ysort, (m := jcast('int', (m + (1)))), Code03_AreaSum.ysort[i])
            i = jcast('int', (i + 1))
        Code03_AreaSum.ysort[jcast('int', jadd(m, 1))] = jcast('int', Code03_AreaSum.ysort[m])
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
            if (Code03_AreaSum.ysort[mid] >= num):
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
            Code03_AreaSum.build(l, mid, jcast('int', (i << (1 & 31))))
            Code03_AreaSum.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code03_AreaSum.length[i] = jcast('int', jcast('int', (Code03_AreaSum.ysort[jcast('int', jadd(r, 1))] - Code03_AreaSum.ysort[l])))
        Code03_AreaSum.times[i] = jcast('int', 0)
        Code03_AreaSum.cover[i] = jcast('int', 0)

    @staticmethod
    def up(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (Code03_AreaSum.times[i] > 0):
            Code03_AreaSum.cover[i] = jcast('int', Code03_AreaSum.length[i])
        else:
            if (l == r):
                # 叶节点直接设置cover不需要下层信息
                Code03_AreaSum.cover[i] = jcast('int', 0)
            else:
                Code03_AreaSum.cover[i] = jcast('int', jcast('int', jadd(Code03_AreaSum.cover[jcast('int', (i << (1 & 31)))], Code03_AreaSum.cover[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 这个题的特殊性在于
    # 1) 查询操作永远查的是整个范围，不会有小范围的查询，每次都返回cover[1]
    # 2) 增加操作之后，后续一定会有等规模的减少操作
    # 根据以上两点分析出不需要懒更新机制
    # 首先当一次修改完成从下往上返回时，up方法能保证最上方的cover[1]是修改正确的
    # 同时任何一次增加操作所涉及的线段树范围，后续一定能被等规模的减少操作取消掉
    # 课上重点图解这个特殊性
    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code03_AreaSum.times[i] = jcast('int', jcast('int', jadd(Code03_AreaSum.times[i], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code03_AreaSum.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code03_AreaSum.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        Code03_AreaSum.up(l, r, i)

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
            jset(Code03_AreaSum.rec[i], 0, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code03_AreaSum.rec[i], 1, jcast('int', jget(in_, 'nval')))
            # 右上角下标
            jcall(in_, 'nextToken')
            jset(Code03_AreaSum.rec[i], 2, jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            jset(Code03_AreaSum.rec[i], 3, jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code03_AreaSum.compute(n))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        j = jcast('int', jcast('int', jadd(1, n)))
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        while (i <= n):
            x1 = jcast('int', Code03_AreaSum.rec[i][0])
            y1 = jcast('int', Code03_AreaSum.rec[i][1])
            x2 = jcast('int', Code03_AreaSum.rec[i][2])
            y2 = jcast('int', Code03_AreaSum.rec[i][3])
            Code03_AreaSum.ysort[i] = jcast('int', y1)
            Code03_AreaSum.ysort[j] = jcast('int', y2)
            jset(Code03_AreaSum.line[i], 0, x1)
            jset(Code03_AreaSum.line[i], 1, y1)
            jset(Code03_AreaSum.line[i], 2, y2)
            jset(Code03_AreaSum.line[i], 3, 1)
            jset(Code03_AreaSum.line[j], 0, x2)
            jset(Code03_AreaSum.line[j], 1, y1)
            jset(Code03_AreaSum.line[j], 2, y2)
            jset(Code03_AreaSum.line[j], 3, jcast('int', (-1)))
            i = jcast('int', (i + 1))
            j = jcast('int', (j + 1))
        n = jcast('int', jcast('int', (n << (1 & 31))))
        m = jcast('int', Code03_AreaSum.prepare(n))
        Code03_AreaSum.build(1, m, 1)
        jstatic('Arrays', 'sort', Code03_AreaSum.line, 1, jcast('int', jadd(n, 1)), (lambda a, b: (a[0] - b[0])))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        pre = jcast('int', 0)
        while (i <= n):
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (jcast('long', Code03_AreaSum.cover[1]) * jcast('int', (Code03_AreaSum.line[i][0] - pre)))))))
            pre = jcast('int', Code03_AreaSum.line[i][0])
            Code03_AreaSum.add(Code03_AreaSum.rank(m, Code03_AreaSum.line[i][1]), jcast('int', (Code03_AreaSum.rank(m, Code03_AreaSum.line[i][2]) - 1)), Code03_AreaSum.line[i][3], 1, m, 1)
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_AreaSum.MAXN = jcast('int', 200001)
Code03_AreaSum.rec = jarray('int', [Code03_AreaSum.MAXN, 4])
Code03_AreaSum.line = jarray('int', [Code03_AreaSum.MAXN, 4])
Code03_AreaSum.ysort = jarray('int', [Code03_AreaSum.MAXN])
Code03_AreaSum.length = jarray('int', [jcast('int', (Code03_AreaSum.MAXN << (2 & 31)))])
Code03_AreaSum.cover = jarray('int', [jcast('int', (Code03_AreaSum.MAXN << (2 & 31)))])
Code03_AreaSum.times = jarray('int', [jcast('int', (Code03_AreaSum.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code03_AreaSum.main([])

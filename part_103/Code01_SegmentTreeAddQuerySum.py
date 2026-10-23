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

# 线段树支持范围增加、范围查询
# 维护累加和
# 测试链接 : https://www.luogu.com.cn/problem/P3372
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SegmentTreeAddQuerySum:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum': 'sum', 'add': 'add_data'}
    MAXN = 0
    arr = None
    sum = None
    add_data = None
    # 累加和信息的汇总
    @staticmethod
    def up(i):
        i = jcast('int', i)
        # 父范围的累加和 = 左范围累加和 + 右范围累加和
        Code01_SegmentTreeAddQuerySum.sum[i] = jcast('long', jcast('long', jadd(Code01_SegmentTreeAddQuerySum.sum[jcast('int', (i << (1 & 31)))], Code01_SegmentTreeAddQuerySum.sum[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 懒信息的下发
    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code01_SegmentTreeAddQuerySum.add_data[i] != 0):
            # 发左
            Code01_SegmentTreeAddQuerySum.lazy(jcast('int', (i << (1 & 31))), Code01_SegmentTreeAddQuerySum.add_data[i], ln)
            # 发右
            Code01_SegmentTreeAddQuerySum.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code01_SegmentTreeAddQuerySum.add_data[i], rn)
            # 父范围懒信息清空
            Code01_SegmentTreeAddQuerySum.add_data[i] = jcast('long', 0)

    # 当前来到l~r范围，对应的信息下标是i，范围上数字的个数是n = r-l+1
    # 现在收到一个懒更新任务 : l~r范围上每个数字增加v
    # 这个懒更新任务有可能是任务范围把当前线段树范围全覆盖导致的
    # 也有可能是父范围的懒信息下发下来的
    # 总之把线段树当前范围的sum数组和add数组调整好
    # 就不再继续往下下发了，懒住了
    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code01_SegmentTreeAddQuerySum.sum[i] = jcast('long', jcast('long', jadd(Code01_SegmentTreeAddQuerySum.sum[i], jcast('long', (v * n)))))
        Code01_SegmentTreeAddQuerySum.add_data[i] = jcast('long', jcast('long', jadd(Code01_SegmentTreeAddQuerySum.add_data[i], v)))

    # 建树
    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code01_SegmentTreeAddQuerySum.sum[i] = jcast('long', Code01_SegmentTreeAddQuerySum.arr[l])
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_SegmentTreeAddQuerySum.build(l, mid, jcast('int', (i << (1 & 31))))
            Code01_SegmentTreeAddQuerySum.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_SegmentTreeAddQuerySum.up(i)
        Code01_SegmentTreeAddQuerySum.add_data[i] = jcast('long', 0)

    # 范围修改
    # jobl ~ jobr范围上每个数字增加jobv
    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_SegmentTreeAddQuerySum.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_SegmentTreeAddQuerySum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code01_SegmentTreeAddQuerySum.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code01_SegmentTreeAddQuerySum.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_SegmentTreeAddQuerySum.up(i)

    # 查询累加和
    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code01_SegmentTreeAddQuerySum.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_SegmentTreeAddQuerySum.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code01_SegmentTreeAddQuerySum.query(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code01_SegmentTreeAddQuerySum.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            Code01_SegmentTreeAddQuerySum.arr[i] = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code01_SegmentTreeAddQuerySum.build(1, n, 1)
        jobv = 0
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobv = jcast('long', jcast('long', jget(in_, 'nval')))
                Code01_SegmentTreeAddQuerySum.add(jobl, jobr, jobv, 1, n, 1)
            else:
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code01_SegmentTreeAddQuerySum.query(jobl, jobr, 1, n, 1))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SegmentTreeAddQuerySum.MAXN = jcast('int', 100001)
Code01_SegmentTreeAddQuerySum.arr = jarray('long', [Code01_SegmentTreeAddQuerySum.MAXN])
Code01_SegmentTreeAddQuerySum.sum = jarray('long', [jcast('int', (Code01_SegmentTreeAddQuerySum.MAXN << (2 & 31)))])
Code01_SegmentTreeAddQuerySum.add_data = jarray('long', [jcast('int', (Code01_SegmentTreeAddQuerySum.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code01_SegmentTreeAddQuerySum.main([])

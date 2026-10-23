# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 旅馆
# 一共有n个房间，编号1~n，一开始都是空房
# 实现如下两种操作，会一共调用m次
# 操作 1 x   : 找到至少有连续x个空房间的区域，返回最左编号
# 如果有多个满足条件的区域，返回其中最左区域的最左编号
# 如果找不到打印0，并且不办理入住
# 如果找到了打印最左编号，并且从最左编号开始办理x个人的入住
# 操作 2 x y : 从x号房间开始往下数y个房间，一律清空
# 操作1有打印操作，操作2没有
# 1 <= n 、m <= 50000
# 测试链接 : https://www.luogu.com.cn/problem/P2894
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Hotel:
    __java_fields__ = {'MAXN': 'MAXN', 'len': 'len', 'pre': 'pre', 'suf': 'suf', 'change': 'change', 'update': 'update_data'}
    MAXN = 0
    # 连续空房最长子串长度
    len = None
    # 连续空房最长前缀长度
    pre = None
    # 连续空房最长后缀长度
    suf = None
    # 懒更新信息，范围上所有数字被重置成了什么
    change = None
    # 懒更新信息，范围上有没有重置任务
    update_data = None
    @staticmethod
    def up(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        l = jcast('int', jcast('int', (i << (1 & 31))))
        r = jcast('int', jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        jset(Code04_Hotel.len, i, jstatic('Math', 'max', jstatic('Math', 'max', Code04_Hotel.len[l], Code04_Hotel.len[r]), jcast('int', jadd(Code04_Hotel.suf[l], Code04_Hotel.pre[r]))))
        Code04_Hotel.pre[i] = jcast('int', (Code04_Hotel.pre[l] if (Code04_Hotel.len[l] < ln) else jcast('int', jadd(Code04_Hotel.pre[l], Code04_Hotel.pre[r]))))
        Code04_Hotel.suf[i] = jcast('int', (Code04_Hotel.suf[r] if (Code04_Hotel.len[r] < rn) else jcast('int', jadd(Code04_Hotel.suf[l], Code04_Hotel.suf[r]))))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if Code04_Hotel.update_data[i]:
            Code04_Hotel.lazy(jcast('int', (i << (1 & 31))), Code04_Hotel.change[i], ln)
            Code04_Hotel.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code04_Hotel.change[i], rn)
            Code04_Hotel.update_data[i] = jcast('boolean', False)

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('int', v)
        n = jcast('int', n)
        jset(Code04_Hotel.len, i, jset(Code04_Hotel.pre, i, jset(Code04_Hotel.suf, i, (n if (v == 0) else 0))))
        Code04_Hotel.change[i] = jcast('int', v)
        Code04_Hotel.update_data[i] = jcast('boolean', True)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            jset(Code04_Hotel.len, i, jset(Code04_Hotel.pre, i, jset(Code04_Hotel.suf, i, 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_Hotel.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_Hotel.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_Hotel.up(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        Code04_Hotel.update_data[i] = jcast('boolean', False)

    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_Hotel.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_Hotel.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code04_Hotel.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_Hotel.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_Hotel.up(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))

    # 在l..r范围上，在满足空房长度>=x的情况下，返回尽量靠左的开头位置
    # 递归需要遵循的潜台词 : l..r范围上一定存在连续空房长度>=x的区域
    @staticmethod
    def queryLeft(x, l, r, i):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('int', l)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_Hotel.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            # 最先查左边
            if (Code04_Hotel.len[jcast('int', (i << (1 & 31)))] >= x):
                return jcast('int', Code04_Hotel.queryLeft(x, l, mid, jcast('int', (i << (1 & 31)))))
            # 然后查中间向两边扩展的可能区域
            if (jcast('int', jadd(Code04_Hotel.suf[jcast('int', (i << (1 & 31)))], Code04_Hotel.pre[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])) >= x):
                return jcast('int', jcast('int', jadd(jcast('int', (mid - Code04_Hotel.suf[jcast('int', (i << (1 & 31)))])), 1)))
            # 前面都没有再最后查右边
            return jcast('int', Code04_Hotel.queryLeft(x, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code04_Hotel.build(1, n, 1)
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        left = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                if (Code04_Hotel.len[1] < x):
                    left = jcast('int', 0)
                else:
                    left = jcast('int', Code04_Hotel.queryLeft(x, 1, n, 1))
                    Code04_Hotel.update(left, jcast('int', (jcast('int', jadd(left, x)) - 1)), 1, 1, n, 1)
                jcall(out, 'println', left)
            else:
                jcall(in_, 'nextToken')
                x = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                y = jcast('int', jcast('int', jget(in_, 'nval')))
                Code04_Hotel.update(x, jstatic('Math', 'min', jcast('int', (jcast('int', jadd(x, y)) - 1)), n), 0, 1, n, 1)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Hotel.MAXN = jcast('int', 50001)
Code04_Hotel.len = jarray('int', [jcast('int', (Code04_Hotel.MAXN << (2 & 31)))])
Code04_Hotel.pre = jarray('int', [jcast('int', (Code04_Hotel.MAXN << (2 & 31)))])
Code04_Hotel.suf = jarray('int', [jcast('int', (Code04_Hotel.MAXN << (2 & 31)))])
Code04_Hotel.change = jarray('int', [jcast('int', (Code04_Hotel.MAXN << (2 & 31)))])
Code04_Hotel.update_data = jarray('boolean', [jcast('int', (Code04_Hotel.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_Hotel.main([])

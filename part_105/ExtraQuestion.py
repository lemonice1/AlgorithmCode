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

# 赠送一道课上没有讲的附加练习题
# 色板游戏
# 一共有L个色板，编号1~L，一开始所有色板都是1号颜色
# 一共有T种颜色，编号1~T，可以往色板上涂色
# 一共有O次操作，操作类型有如下两种
# 操作 C A B C : A~B范围的色板都涂上C颜色
# 操作 P A B   : 查询A~B范围的色板一共有几种颜色
# L <= 10^5, T <= 30, O <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P1558
# 解法 :
# 数据很特殊，颜色种类不超过30
# 可以用位信息来表示线段树范围上的颜色状况
# 那么，父范围的颜色状况 = 左范围的颜色状况 | 右范围的颜色状况
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class ExtraQuestion:
    __java_fields__ = {'MAXN': 'MAXN', 'color': 'color', 'change': 'change', 'update': 'update_data'}
    MAXN = 0
    # 线段树范围上的颜色状况
    color = None
    # 懒更新信息，范围上重置成了什么颜色
    change = None
    # 懒更新信息，范围上是否有重置任务
    update_data = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        ExtraQuestion.color[i] = jcast('int', jcast('int', (ExtraQuestion.color[jcast('int', (i << (1 & 31)))] | ExtraQuestion.color[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    @staticmethod
    def down(i):
        i = jcast('int', i)
        if ExtraQuestion.update_data[i]:
            ExtraQuestion.lazy(jcast('int', (i << (1 & 31))), ExtraQuestion.change[i])
            ExtraQuestion.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), ExtraQuestion.change[i])
            ExtraQuestion.update_data[i] = jcast('boolean', False)

    # 整个范围的色板重置成v颜色的懒更新处理
    @staticmethod
    def lazy(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        ExtraQuestion.color[i] = jcast('int', jcast('int', (1 << (v & 31))))
        ExtraQuestion.change[i] = jcast('int', v)
        ExtraQuestion.update_data[i] = jcast('boolean', True)

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            ExtraQuestion.build(l, mid, jcast('int', (i << (1 & 31))))
            ExtraQuestion.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
        # 一开始所有色板都是1号颜色
        # 所以状态为0...0010 = 2
        ExtraQuestion.color[i] = jcast('int', 2)
        ExtraQuestion.change[i] = jcast('int', 0)
        ExtraQuestion.update_data[i] = jcast('boolean', False)

    # 范围重置颜色
    @staticmethod
    def update(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            ExtraQuestion.lazy(i, jobv)
        else:
            ExtraQuestion.down(i)
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                ExtraQuestion.update(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                ExtraQuestion.update(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            ExtraQuestion.up(i)

    # 返回l..r范围上的颜色种类
    @staticmethod
    def _java_query_0(l, r, n):
        l = jcast('int', l)
        r = jcast('int', r)
        n = jcast('int', n)
        status = jcast('int', ExtraQuestion._java_query_1(l, r, 1, n, 1))
        return jcast('int', ExtraQuestion.cntOnes(status))

    # 返回l..r范围上的颜色状况
    @staticmethod
    def _java_query_1(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', ExtraQuestion.color[i])
        ExtraQuestion.down(i)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        status = jcast('int', 0)
        if (jobl <= mid):
            status = jcast('int', jcast('int', (status | ExtraQuestion._java_query_1(jobl, jobr, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            status = jcast('int', jcast('int', (status | ExtraQuestion._java_query_1(jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', status)

    # 返回n的二进制中有几个1
    # 该实现讲解031的题目6讲过了
    # 你也可以用更简单的写法
    @staticmethod
    def cntOnes(n):
        n = jcast('int', n)
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 1431655765)), jcast('int', (jcast('int', jushr(n, 1, 32)) & 1431655765)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 858993459)), jcast('int', (jcast('int', jushr(n, 2, 32)) & 858993459)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 252645135)), jcast('int', (jcast('int', jushr(n, 4, 32)) & 252645135)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 16711935)), jcast('int', (jcast('int', jushr(n, 8, 32)) & 16711935)))))
        n = jcast('int', jcast('int', jadd(jcast('int', (n & 65535)), jcast('int', (jcast('int', jushr(n, 16, 32)) & 65535)))))
        return jcast('int', n)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        ExtraQuestion.build(1, n, 1)
        op = None
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        tmp = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            op = jget(in_, 'sval')
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            # 注意题目可能有a>b的情况需要交换
            if (a > b):
                tmp = jcast('int', a)
                a = jcast('int', b)
                b = jcast('int', tmp)
            if jcall(op, 'equals', 'C'):
                jcall(in_, 'nextToken')
                c = jcast('int', jcast('int', jget(in_, 'nval')))
                ExtraQuestion.update(a, b, c, 1, n, 1)
            else:
                jcall(out, 'println', ExtraQuestion._java_query_0(a, b, n))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['int', 'int', 'int'], ['int', 'int', 'int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return ExtraQuestion._java_query_0(*args)
        if _java_choice == 1:
            return ExtraQuestion._java_query_1(*args)
        raise TypeError("No matching overload for ExtraQuestion.query")


ExtraQuestion.MAXN = jcast('int', 100001)
ExtraQuestion.color = jarray('int', [jcast('int', (ExtraQuestion.MAXN << (2 & 31)))])
ExtraQuestion.change = jarray('int', [jcast('int', (ExtraQuestion.MAXN << (2 & 31)))])
ExtraQuestion.update_data = jarray('boolean', [jcast('int', (ExtraQuestion.MAXN << (2 & 31)))])

if __name__ == '__main__':
    ExtraQuestion.main([])

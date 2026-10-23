# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树状数组范围增加、范围查询模版
# 测试链接 : https://www.luogu.com.cn/problem/P3372
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_IndexTreeIntervalAddIntervalQuery:
    __java_fields__ = {'MAXN': 'MAXN', 'info1': 'info1', 'info2': 'info2', 'n': 'n', 'm': 'm'}
    MAXN = 0
    # 维护原始数组的差分信息：Di
    info1 = None
    # 维护原始数组的差分加工信息：(i-1) * Di
    info2 = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def _java_add_0(tree, i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        while (i <= Code03_IndexTreeIntervalAddIntervalQuery.n):
            tree[i] = jcast('long', jcast('long', jadd(tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code03_IndexTreeIntervalAddIntervalQuery.lowbit(i))))

    @staticmethod
    def sum(tree, i):
        i = jcast('int', i)
        ans = jcast('long', 0)
        while (i > 0):
            ans = jcast('long', jcast('long', jadd(ans, tree[i])))
            i = jcast('int', jcast('int', (i - Code03_IndexTreeIntervalAddIntervalQuery.lowbit(i))))
        return jcast('long', ans)

    # 原始数组中[l..r]每个数值+v
    @staticmethod
    def _java_add_1(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        Code03_IndexTreeIntervalAddIntervalQuery._java_add_0(Code03_IndexTreeIntervalAddIntervalQuery.info1, l, v)
        Code03_IndexTreeIntervalAddIntervalQuery._java_add_0(Code03_IndexTreeIntervalAddIntervalQuery.info1, jcast('int', jadd(r, 1)), jcast('long', (-v)))
        Code03_IndexTreeIntervalAddIntervalQuery._java_add_0(Code03_IndexTreeIntervalAddIntervalQuery.info2, l, jcast('long', (jcast('int', (l - 1)) * v)))
        Code03_IndexTreeIntervalAddIntervalQuery._java_add_0(Code03_IndexTreeIntervalAddIntervalQuery.info2, jcast('int', jadd(r, 1)), jcast('long', (-jcast('long', (r * v)))))

    # 原始数组中[l..r]范围上的累加和
    @staticmethod
    def range(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('long', jcast('long', jadd(jcast('long', (jcast('long', (jcast('long', (Code03_IndexTreeIntervalAddIntervalQuery.sum(Code03_IndexTreeIntervalAddIntervalQuery.info1, r) * r)) - Code03_IndexTreeIntervalAddIntervalQuery.sum(Code03_IndexTreeIntervalAddIntervalQuery.info2, r))) - jcast('long', (Code03_IndexTreeIntervalAddIntervalQuery.sum(Code03_IndexTreeIntervalAddIntervalQuery.info1, jcast('int', (l - 1))) * jcast('int', (l - 1)))))), Code03_IndexTreeIntervalAddIntervalQuery.sum(Code03_IndexTreeIntervalAddIntervalQuery.info2, jcast('int', (l - 1))))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_IndexTreeIntervalAddIntervalQuery.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code03_IndexTreeIntervalAddIntervalQuery.m = jcast('int', jcast('int', jget(in_, 'nval')))
        cur = 0
        i = jcast('int', 1)
        while (i <= Code03_IndexTreeIntervalAddIntervalQuery.n):
            jcall(in_, 'nextToken')
            cur = jcast('long', jcast('long', jget(in_, 'nval')))
            Code03_IndexTreeIntervalAddIntervalQuery._java_add_1(i, i, cur)
            i = jcast('int', (i + 1))
        v = 0
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        while (i <= Code03_IndexTreeIntervalAddIntervalQuery.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('long', jcast('long', jget(in_, 'nval')))
                Code03_IndexTreeIntervalAddIntervalQuery._java_add_1(l, r, v)
            else:
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code03_IndexTreeIntervalAddIntervalQuery.range(l, r))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['long[]', 'int', 'long'], ['int', 'int', 'long']], [False, False])
        if _java_choice == 0:
            return Code03_IndexTreeIntervalAddIntervalQuery._java_add_0(*args)
        if _java_choice == 1:
            return Code03_IndexTreeIntervalAddIntervalQuery._java_add_1(*args)
        raise TypeError("No matching overload for Code03_IndexTreeIntervalAddIntervalQuery.add")


Code03_IndexTreeIntervalAddIntervalQuery.MAXN = jcast('int', 100001)
Code03_IndexTreeIntervalAddIntervalQuery.info1 = jarray('long', [Code03_IndexTreeIntervalAddIntervalQuery.MAXN])
Code03_IndexTreeIntervalAddIntervalQuery.info2 = jarray('long', [Code03_IndexTreeIntervalAddIntervalQuery.MAXN])
Code03_IndexTreeIntervalAddIntervalQuery.n = jcast('int', 0)
Code03_IndexTreeIntervalAddIntervalQuery.m = jcast('int', 0)

if __name__ == '__main__':
    Code03_IndexTreeIntervalAddIntervalQuery.main([])

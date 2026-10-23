# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树状数组单点增加、范围查询模版
# 测试链接 : https://www.luogu.com.cn/problem/P3374
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_IndexTreeSingleAddIntervalQuery:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'n': 'n', 'm': 'm'}
    MAXN = 0
    # 原始数组的信息，根据课上说的关系，维护在树状数组中
    # 注意下标一定从1开始，不从0开始
    tree = None
    n = 0
    m = 0
    # 得到i最右侧的1的状态
    # 其他位都是0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code01_IndexTreeSingleAddIntervalQuery.n):
            Code01_IndexTreeSingleAddIntervalQuery.tree[i] = jcast('int', jcast('int', jadd(Code01_IndexTreeSingleAddIntervalQuery.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code01_IndexTreeSingleAddIntervalQuery.lowbit(i))))

    # 返回1~i范围累加和
    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code01_IndexTreeSingleAddIntervalQuery.tree[i])))
            i = jcast('int', jcast('int', (i - Code01_IndexTreeSingleAddIntervalQuery.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def range(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code01_IndexTreeSingleAddIntervalQuery.sum(r) - Code01_IndexTreeSingleAddIntervalQuery.sum(jcast('int', (l - 1))))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_IndexTreeSingleAddIntervalQuery.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_IndexTreeSingleAddIntervalQuery.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        v = 0
        while (i <= Code01_IndexTreeSingleAddIntervalQuery.n):
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code01_IndexTreeSingleAddIntervalQuery.add(i, v)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        a = 0
        b = 0
        c = 0
        while (i <= Code01_IndexTreeSingleAddIntervalQuery.m):
            jcall(in_, 'nextToken')
            a = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            c = jcast('int', jcast('int', jget(in_, 'nval')))
            if (a == 1):
                Code01_IndexTreeSingleAddIntervalQuery.add(b, c)
            else:
                jcall(out, 'println', Code01_IndexTreeSingleAddIntervalQuery.range(b, c))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_IndexTreeSingleAddIntervalQuery.MAXN = jcast('int', 500001)
Code01_IndexTreeSingleAddIntervalQuery.tree = jarray('int', [Code01_IndexTreeSingleAddIntervalQuery.MAXN])
Code01_IndexTreeSingleAddIntervalQuery.n = jcast('int', 0)
Code01_IndexTreeSingleAddIntervalQuery.m = jcast('int', 0)

if __name__ == '__main__':
    Code01_IndexTreeSingleAddIntervalQuery.main([])

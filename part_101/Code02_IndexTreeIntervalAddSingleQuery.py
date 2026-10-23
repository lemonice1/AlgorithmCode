# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树状数组范围增加、单点查询模版
# 测试链接 : https://www.luogu.com.cn/problem/P3368
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_IndexTreeIntervalAddSingleQuery:
    __java_fields__ = {'MAXN': 'MAXN', 'tree': 'tree', 'n': 'n', 'm': 'm'}
    MAXN = 0
    # 树状数组不维护原数组的信息，维护原数组的差分信息
    # 注意下标一定从1开始，不从0开始
    tree = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code02_IndexTreeIntervalAddSingleQuery.n):
            Code02_IndexTreeIntervalAddSingleQuery.tree[i] = jcast('int', jcast('int', jadd(Code02_IndexTreeIntervalAddSingleQuery.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code02_IndexTreeIntervalAddSingleQuery.lowbit(i))))

    # 返回1~i范围累加和
    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ans = jcast('int', 0)
        while (i > 0):
            ans = jcast('int', jcast('int', jadd(ans, Code02_IndexTreeIntervalAddSingleQuery.tree[i])))
            i = jcast('int', jcast('int', (i - Code02_IndexTreeIntervalAddSingleQuery.lowbit(i))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_IndexTreeIntervalAddSingleQuery.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code02_IndexTreeIntervalAddSingleQuery.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        v = 0
        while (i <= Code02_IndexTreeIntervalAddSingleQuery.n):
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_IndexTreeIntervalAddSingleQuery.add(i, v)
            Code02_IndexTreeIntervalAddSingleQuery.add(jcast('int', jadd(i, 1)), jcast('int', (-v)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_IndexTreeIntervalAddSingleQuery.m):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            if (op == 1):
                jcall(in_, 'nextToken')
                l = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                r = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                v = jcast('int', jcast('int', jget(in_, 'nval')))
                Code02_IndexTreeIntervalAddSingleQuery.add(l, v)
                Code02_IndexTreeIntervalAddSingleQuery.add(jcast('int', jadd(r, 1)), jcast('int', (-v)))
            else:
                jcall(in_, 'nextToken')
                index = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code02_IndexTreeIntervalAddSingleQuery.sum(index))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_IndexTreeIntervalAddSingleQuery.MAXN = jcast('int', 500002)
Code02_IndexTreeIntervalAddSingleQuery.tree = jarray('int', [Code02_IndexTreeIntervalAddSingleQuery.MAXN])
Code02_IndexTreeIntervalAddSingleQuery.n = jcast('int', 0)
Code02_IndexTreeIntervalAddSingleQuery.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_IndexTreeIntervalAddSingleQuery.main([])

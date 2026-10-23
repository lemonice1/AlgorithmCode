# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 升序三元组数量
# 给定一个数组arr，如果i < j < k且arr[i] < arr[j] < arr[k]
# 那么称(i, j, k)为一个升序三元组
# 返回arr中升序三元组的数量
# 测试链接 : https://www.luogu.com.cn/problem/P1637
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_IncreasingTriples:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sort': 'sort', 'tree1': 'tree1', 'tree2': 'tree2', 'n': 'n', 'm': 'm'}
    MAXN = 0
    arr = None
    sort = None
    # 维护信息 : 课上讲的up1数组
    # tree1不是up1数组，是up1数组的树状数组
    tree1 = None
    # 维护信息 : 课上讲的up2数组
    # tree2不是up2数组，是up2数组的树状数组
    tree2 = None
    n = 0
    m = 0
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(tree, i, c):
        i = jcast('int', i)
        c = jcast('long', c)
        while (i <= Code02_IncreasingTriples.m):
            tree[i] = jcast('long', jcast('long', jadd(tree[i], c)))
            i = jcast('int', jcast('int', jadd(i, Code02_IncreasingTriples.lowbit(i))))

    @staticmethod
    def sum(tree, i):
        i = jcast('int', i)
        ans = jcast('long', 0)
        while (i > 0):
            ans = jcast('long', jcast('long', jadd(ans, tree[i])))
            i = jcast('int', jcast('int', (i - Code02_IncreasingTriples.lowbit(i))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_IncreasingTriples.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code02_IncreasingTriples.n):
            jcall(in_, 'nextToken')
            Code02_IncreasingTriples.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            Code02_IncreasingTriples.sort[i] = jcast('int', Code02_IncreasingTriples.arr[i])
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_IncreasingTriples.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # 时间复杂度O(n * logn)
    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code02_IncreasingTriples.sort, 1, jcast('int', jadd(Code02_IncreasingTriples.n, 1)))
        Code02_IncreasingTriples.m = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_IncreasingTriples.n):
            if (Code02_IncreasingTriples.sort[Code02_IncreasingTriples.m] != Code02_IncreasingTriples.sort[i]):
                jset(Code02_IncreasingTriples.sort, ((_java_obj_1 := Code02_IncreasingTriples), (_java_key_2 := 'm'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_IncreasingTriples.sort[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_IncreasingTriples.n):
            jset(Code02_IncreasingTriples.arr, i, Code02_IncreasingTriples.rank(Code02_IncreasingTriples.arr[i]))
            i = jcast('int', (i + 1))
        ans = jcast('long', 0)
        i = jcast('int', 1)
        while (i <= Code02_IncreasingTriples.n):
            # 查询以当前值做结尾的升序三元组数量
            ans = jcast('long', jcast('long', jadd(ans, Code02_IncreasingTriples.sum(Code02_IncreasingTriples.tree2, jcast('int', (Code02_IncreasingTriples.arr[i] - 1))))))
            # 更新以当前值做结尾的升序一元组数量
            Code02_IncreasingTriples.add(Code02_IncreasingTriples.tree1, Code02_IncreasingTriples.arr[i], 1)
            # 更新以当前值做结尾的升序二元组数量
            Code02_IncreasingTriples.add(Code02_IncreasingTriples.tree2, Code02_IncreasingTriples.arr[i], Code02_IncreasingTriples.sum(Code02_IncreasingTriples.tree1, jcast('int', (Code02_IncreasingTriples.arr[i] - 1))))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    @staticmethod
    def rank(v):
        v = jcast('int', v)
        l = jcast('int', 1)
        r = jcast('int', Code02_IncreasingTriples.m)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code02_IncreasingTriples.sort[mid] >= v):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_IncreasingTriples.MAXN = jcast('int', 30001)
Code02_IncreasingTriples.arr = jarray('int', [Code02_IncreasingTriples.MAXN])
Code02_IncreasingTriples.sort = jarray('int', [Code02_IncreasingTriples.MAXN])
Code02_IncreasingTriples.tree1 = jarray('long', [Code02_IncreasingTriples.MAXN])
Code02_IncreasingTriples.tree2 = jarray('long', [Code02_IncreasingTriples.MAXN])
Code02_IncreasingTriples.n = jcast('int', 0)
Code02_IncreasingTriples.m = jcast('int', 0)

if __name__ == '__main__':
    Code02_IncreasingTriples.main([])

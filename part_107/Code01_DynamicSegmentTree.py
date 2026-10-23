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

# 动态开点线段树
# 一共有n个位置，编号从1~n，一开始所有位置的值为0
# 实现如下两个操作，一共会调用m次
# 操作 1 l r v : 把l~r范围的每个数增加v
# 操作 2 l r   : 返回l~r范围的累加和
# 1 <= n <= 10^9
# 1 <= m <= 10^3
# 测试链接 : https://www.luogu.com.cn/problem/P2781
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_DynamicSegmentTree:
    __java_fields__ = {'LIMIT': 'LIMIT', 'cnt': 'cnt', 'left': 'left', 'right': 'right', 'sum': 'sum', 'add': 'add_data'}
    # 范围1 ~ 10^9，线段树高度差不多30
    # 查询次数1000，每次查询都有左右两条边线
    # 所以空间占用差不多1000 * 30 * 2 = 60000
    # 适当调大即可
    LIMIT = 0
    cnt = 0
    left = None
    right = None
    sum = None
    add_data = None
    @staticmethod
    def up(h, l, r):
        h = jcast('int', h)
        l = jcast('int', l)
        r = jcast('int', r)
        Code01_DynamicSegmentTree.sum[h] = jcast('long', jcast('long', jadd(Code01_DynamicSegmentTree.sum[l], Code01_DynamicSegmentTree.sum[r])))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code01_DynamicSegmentTree.add_data[i] != 0):
            # 懒更新任务下发
            # 那左右两侧的空间需要准备好
            if (Code01_DynamicSegmentTree.left[i] == 0):
                jset(Code01_DynamicSegmentTree.left, i, ((_java_obj_1 := Code01_DynamicSegmentTree), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
            if (Code01_DynamicSegmentTree.right[i] == 0):
                jset(Code01_DynamicSegmentTree.right, i, ((_java_obj_4 := Code01_DynamicSegmentTree), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            Code01_DynamicSegmentTree.lazy(Code01_DynamicSegmentTree.left[i], Code01_DynamicSegmentTree.add_data[i], ln)
            Code01_DynamicSegmentTree.lazy(Code01_DynamicSegmentTree.right[i], Code01_DynamicSegmentTree.add_data[i], rn)
            Code01_DynamicSegmentTree.add_data[i] = jcast('long', 0)

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('long', v)
        n = jcast('int', n)
        Code01_DynamicSegmentTree.sum[i] = jcast('long', jcast('long', jadd(Code01_DynamicSegmentTree.sum[i], jcast('long', (v * n)))))
        Code01_DynamicSegmentTree.add_data[i] = jcast('long', jcast('long', jadd(Code01_DynamicSegmentTree.add_data[i], v)))

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code01_DynamicSegmentTree.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code01_DynamicSegmentTree.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                # 不得不去左侧才会申请
                if (Code01_DynamicSegmentTree.left[i] == 0):
                    jset(Code01_DynamicSegmentTree.left, i, ((_java_obj_7 := Code01_DynamicSegmentTree), (_java_key_8 := 'cnt'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                Code01_DynamicSegmentTree.add(jobl, jobr, jobv, l, mid, Code01_DynamicSegmentTree.left[i])
            if (jobr > mid):
                # 不得不去右侧才会申请
                if (Code01_DynamicSegmentTree.right[i] == 0):
                    jset(Code01_DynamicSegmentTree.right, i, ((_java_obj_10 := Code01_DynamicSegmentTree), (_java_key_11 := 'cnt'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3])
                Code01_DynamicSegmentTree.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, Code01_DynamicSegmentTree.right[i])
            Code01_DynamicSegmentTree.up(i, Code01_DynamicSegmentTree.left[i], Code01_DynamicSegmentTree.right[i])

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', Code01_DynamicSegmentTree.sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_DynamicSegmentTree.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            # 发现左侧申请过空间才有必要去查询
            # 如果左侧从来没有申请过空间那查询结果就是0
            if (Code01_DynamicSegmentTree.left[i] != 0):
                ans = jcast('long', jcast('long', jadd(ans, Code01_DynamicSegmentTree.query(jobl, jobr, l, mid, Code01_DynamicSegmentTree.left[i]))))
        if (jobr > mid):
            # 发现右侧申请过空间才有必要去查询
            # 如果右侧从来没有申请过空间那查询结果就是0
            if (Code01_DynamicSegmentTree.right[i] != 0):
                ans = jcast('long', jcast('long', jadd(ans, Code01_DynamicSegmentTree.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code01_DynamicSegmentTree.right[i]))))
        return jcast('long', ans)

    # 如果一次会执行多组测试数组
    # 那么每组测试完成后要clear空间
    @staticmethod
    def clear():
        jstatic('Arrays', 'fill', Code01_DynamicSegmentTree.left, 1, jcast('int', jadd(Code01_DynamicSegmentTree.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DynamicSegmentTree.right, 1, jcast('int', jadd(Code01_DynamicSegmentTree.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DynamicSegmentTree.sum, 1, jcast('int', jadd(Code01_DynamicSegmentTree.cnt, 1)), 0)
        jstatic('Arrays', 'fill', Code01_DynamicSegmentTree.add_data, 1, jcast('int', jadd(Code01_DynamicSegmentTree.cnt, 1)), 0)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        Code01_DynamicSegmentTree.cnt = jcast('int', 1)
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
                Code01_DynamicSegmentTree.add(jobl, jobr, jobv, 1, n, 1)
            else:
                jcall(in_, 'nextToken')
                jobl = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jobr = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(out, 'println', Code01_DynamicSegmentTree.query(jobl, jobr, 1, n, 1))
            i = jcast('int', (i + 1))
        # 本题每组测试数据都单独运行
        # 可以不写clear方法
        # 但是如果多组测试数据串行调用
        # 就需要加上清空逻辑
        Code01_DynamicSegmentTree.clear()
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_DynamicSegmentTree.LIMIT = jcast('int', 80001)
Code01_DynamicSegmentTree.cnt = jcast('int', 0)
Code01_DynamicSegmentTree.left = jarray('int', [Code01_DynamicSegmentTree.LIMIT])
Code01_DynamicSegmentTree.right = jarray('int', [Code01_DynamicSegmentTree.LIMIT])
Code01_DynamicSegmentTree.sum = jarray('long', [Code01_DynamicSegmentTree.LIMIT])
Code01_DynamicSegmentTree.add_data = jarray('long', [Code01_DynamicSegmentTree.LIMIT])

if __name__ == '__main__':
    Code01_DynamicSegmentTree.main([])

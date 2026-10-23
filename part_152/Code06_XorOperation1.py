# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 异或运算，Python版
# 给定一个长度n的数组x，还有一个长度为m的数组y
# 想象一个二维矩阵mat，数组x作为行，数组y作为列，mat[i][j] = x[i] ^ y[j]
# 一共有p条查询，每条查询格式如下
# xl xr yl yr k : 划定mat的范围是，行从xl~xr，列从yl~yr，打印其中第k大的值
# 1 <= n <= 1000
# 1 <= m <= 3 * 10^5
# 1 <= p <= 500
# 0 <= x[i]、y[i] < 2^31
# 测试链接 : https://www.luogu.com.cn/problem/P5795
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_XorOperation1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 'p': 'p', 'x': 'x', 'root': 'root', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt', 'xroad': 'xroad'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    m = 0
    p = 0
    x = None
    root = None
    tree = None
    pass_ = None
    cnt = 0
    xroad = None
    @staticmethod
    def insert(num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_1 := Code06_XorOperation1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code06_XorOperation1.tree[rt], 0, Code06_XorOperation1.tree[i][0])
        jset(Code06_XorOperation1.tree[rt], 1, Code06_XorOperation1.tree[i][1])
        Code06_XorOperation1.pass_[rt] = jcast('int', jcast('int', jadd(Code06_XorOperation1.pass_[i], 1)))
        b = jcast('int', Code06_XorOperation1.BIT)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            i = jcast('int', Code06_XorOperation1.tree[i][path])
            cur = jcast('int', ((_java_obj_4 := Code06_XorOperation1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            jset(Code06_XorOperation1.tree[cur], 0, Code06_XorOperation1.tree[i][0])
            jset(Code06_XorOperation1.tree[cur], 1, Code06_XorOperation1.tree[i][1])
            Code06_XorOperation1.pass_[cur] = jcast('int', jcast('int', jadd(Code06_XorOperation1.pass_[i], 1)))
            jset(Code06_XorOperation1.tree[pre], path, cur)
            b = jcast('int', (b - 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    @staticmethod
    def maxKth(xl, xr, yl, yr, k):
        xl = jcast('int', xl)
        xr = jcast('int', xr)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        k = jcast('int', k)
        # 基于哪两个节点的pass值查询，一开始x[xl...xr]每个数字，都是一样的
        i = jcast('int', xl)
        while (i <= xr):
            jset(Code06_XorOperation1.xroad[i], 0, Code06_XorOperation1.root[jcast('int', (yl - 1))])
            jset(Code06_XorOperation1.xroad[i], 1, Code06_XorOperation1.root[yr])
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        b = jcast('int', Code06_XorOperation1.BIT)
        path = 0
        best = 0
        sum = 0
        while (b >= 0):
            sum = jcast('int', 0)
            # 统计x[xl...xr]范围上
            # 每个数字 ^ y[yl...yr]任意一个数字，在第b位上能取得1的结果，有多少个
            # 结果数量累加起来
            i = jcast('int', xl)
            while (i <= xr):
                path = jcast('int', jcast('int', (jcast('int', (Code06_XorOperation1.x[i] >> (b & 31))) & 1)))
                best = jcast('int', jcast('int', (path ^ 1)))
                sum = jcast('int', jcast('int', jadd(sum, jcast('int', (Code06_XorOperation1.pass_[Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][1]][best]] - Code06_XorOperation1.pass_[Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][0]][best]])))))
                i = jcast('int', (i + 1))
            # 如果sum >= k
            # 说明x[xl...xr]对应y[yl...yr]，第k大的异或结果，在第b位上能是1
            # 如果sum < k
            # 说明x[xl...xr]对应y[yl...yr]，第k大的异或结果，在第b位上只能是0
            # x[xl...xr]每个数字，都有自己专属的跳转，要记录好！
            i = jcast('int', xl)
            while (i <= xr):
                path = jcast('int', jcast('int', (jcast('int', (Code06_XorOperation1.x[i] >> (b & 31))) & 1)))
                best = jcast('int', jcast('int', (path ^ 1)))
                if (sum >= k):
                    jset(Code06_XorOperation1.xroad[i], 0, Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][0]][best])
                    jset(Code06_XorOperation1.xroad[i], 1, Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][1]][best])
                else:
                    jset(Code06_XorOperation1.xroad[i], 0, Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][0]][path])
                    jset(Code06_XorOperation1.xroad[i], 1, Code06_XorOperation1.tree[Code06_XorOperation1.xroad[i][1]][path])
                i = jcast('int', (i + 1))
            if (sum >= k):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (b & 31))))))
            else:
                k = jcast('int', jcast('int', (k - sum)))
            b = jcast('int', (b - 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_XorOperation1.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_XorOperation1.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code06_XorOperation1.n):
            jcall(in_, 'nextToken')
            Code06_XorOperation1.x[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        yi = 0
        while (i <= Code06_XorOperation1.m):
            jcall(in_, 'nextToken')
            yi = jcast('int', jcast('int', jget(in_, 'nval')))
            jset(Code06_XorOperation1.root, i, Code06_XorOperation1.insert(yi, Code06_XorOperation1.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))
        jcall(in_, 'nextToken')
        Code06_XorOperation1.p = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        xl = 0
        xr = 0
        yl = 0
        yr = 0
        k = 0
        while (i <= Code06_XorOperation1.p):
            jcall(in_, 'nextToken')
            xl = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            xr = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            yl = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            yr = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            k = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code06_XorOperation1.maxKth(xl, xr, yl, yr, k))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_XorOperation1.MAXN = jcast('int', 300001)
Code06_XorOperation1.MAXT = jcast('int', jcast('int', (Code06_XorOperation1.MAXN * 32)))
Code06_XorOperation1.BIT = jcast('int', 30)
Code06_XorOperation1.n = jcast('int', 0)
Code06_XorOperation1.m = jcast('int', 0)
Code06_XorOperation1.p = jcast('int', 0)
Code06_XorOperation1.x = jarray('int', [Code06_XorOperation1.MAXN])
Code06_XorOperation1.root = jarray('int', [Code06_XorOperation1.MAXN])
Code06_XorOperation1.tree = jarray('int', [Code06_XorOperation1.MAXT, 2])
Code06_XorOperation1.pass_ = jarray('int', [Code06_XorOperation1.MAXT])
Code06_XorOperation1.cnt = jcast('int', 0)
Code06_XorOperation1.xroad = jarray('int', [Code06_XorOperation1.MAXN, 2])

if __name__ == '__main__':
    Code06_XorOperation1.main([])

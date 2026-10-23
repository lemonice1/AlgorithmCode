# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 磁力块，Python版
# 磁块有五个属性值，x、y、m、p、range，磁块在(x, y)位置、质量为m、磁力为p、吸引半径range
# 磁块A可以把磁块B吸到磁块A的位置，需要满足如下的条件
# A与B的距离不大于A的吸引半径，并且B的质量不大于A的磁力
# 你有一个初始磁块，给定初始磁块的4个属性值(不给质量，因为没用)，你永远在初始磁块的位置
# 接下来给定n个磁块各自的5个属性值，你可以用初始磁块，吸过来其中的磁块
# 吸过来的磁块可以被你随意使用，返回你最多能吸过来多少磁块
# 1 <= n <= 3 * 10^5    -10^9 <= x、y <= +10^9    1 <= m、p、range <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P10590
# 测试链接 : https://codeforces.com/problemset/problem/198/E
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 排序直接使用已有数组中的记录，避免额外封装磁块对象
# 手写了双指针快排优化常数时间，一般不需要这么做，正式比赛不卡常
class Code03_Magnet1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'x': 'x', 'y': 'y', 'm': 'm', 'p': 'p', 'range': 'range', 'dist': 'dist', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'maxm': 'maxm', 'que': 'que', 'vis': 'vis'}
    MAXN = 0
    MAXB = 0
    n = 0
    x = None
    y = None
    m = None
    p = None
    range = None
    dist = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    maxm = None
    que = None
    vis = None
    # 下标为i的磁块和下标为j的磁块交换
    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp1 = 0
        tmp1 = jcast('int', Code03_Magnet1.x[i])
        Code03_Magnet1.x[i] = jcast('int', Code03_Magnet1.x[j])
        Code03_Magnet1.x[j] = jcast('int', tmp1)
        tmp1 = jcast('int', Code03_Magnet1.y[i])
        Code03_Magnet1.y[i] = jcast('int', Code03_Magnet1.y[j])
        Code03_Magnet1.y[j] = jcast('int', tmp1)
        tmp1 = jcast('int', Code03_Magnet1.m[i])
        Code03_Magnet1.m[i] = jcast('int', Code03_Magnet1.m[j])
        Code03_Magnet1.m[j] = jcast('int', tmp1)
        tmp1 = jcast('int', Code03_Magnet1.p[i])
        Code03_Magnet1.p[i] = jcast('int', Code03_Magnet1.p[j])
        Code03_Magnet1.p[j] = jcast('int', tmp1)
        tmp2 = 0
        tmp2 = jcast('long', Code03_Magnet1.range[i])
        Code03_Magnet1.range[i] = jcast('long', Code03_Magnet1.range[j])
        Code03_Magnet1.range[j] = jcast('long', tmp2)
        tmp2 = jcast('long', Code03_Magnet1.dist[i])
        Code03_Magnet1.dist[i] = jcast('long', Code03_Magnet1.dist[j])
        Code03_Magnet1.dist[j] = jcast('long', tmp2)

    # 所有磁块根据m值排序，手写双指针快排
    @staticmethod
    def sortByM(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('int', Code03_Magnet1.m[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code03_Magnet1.m[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code03_Magnet1.m[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                Code03_Magnet1.swap(((_java_old_1 := i), (i := jcast('int', (i + (1)))), _java_old_1)[2], ((_java_old_2 := j), (j := jcast('int', (j + (-1)))), _java_old_2)[2])
        Code03_Magnet1.sortByM(l, j)
        Code03_Magnet1.sortByM(i, r)

    # 所有磁块根据dist值排序，手写双指针快排
    @staticmethod
    def sortByDist(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l >= r):
            return
        i = jcast('int', l)
        j = jcast('int', r)
        pivot = jcast('long', Code03_Magnet1.dist[jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31)))])
        while (i <= j):
            while (Code03_Magnet1.dist[i] < pivot):
                i = jcast('int', (i + 1))
            while (Code03_Magnet1.dist[j] > pivot):
                j = jcast('int', (j - 1))
            if (i <= j):
                Code03_Magnet1.swap(((_java_old_3 := i), (i := jcast('int', (i + (1)))), _java_old_3)[2], ((_java_old_4 := j), (j := jcast('int', (j + (-1)))), _java_old_4)[2])
        Code03_Magnet1.sortByDist(l, j)
        Code03_Magnet1.sortByDist(i, r)

    @staticmethod
    def bfs():
        ans = jcast('int', 0)
        Code03_Magnet1.vis[0] = jcast('boolean', True)
        l = jcast('int', 1)
        r = jcast('int', 1)
        jset(Code03_Magnet1.que, ((_java_old_5 := r), (r := jcast('int', (r + (1)))), _java_old_5)[2], 0)
        while (l < r):
            try:
                cur = jcast('int', Code03_Magnet1.que[((_java_old_7 := l), (l := jcast('int', (l + (1)))), _java_old_7)[2]])
                b = jcast('int', 1)
                while (b <= Code03_Magnet1.bnum):
                    try:
                        if (Code03_Magnet1.maxm[b] <= Code03_Magnet1.p[cur]):
                            while ((Code03_Magnet1.bl[b] <= Code03_Magnet1.br[b]) and (Code03_Magnet1.dist[Code03_Magnet1.bl[b]] <= Code03_Magnet1.range[cur])):
                                i = jcast('int', Code03_Magnet1.bl[b])
                                if (not Code03_Magnet1.vis[i]):
                                    Code03_Magnet1.vis[i] = jcast('boolean', True)
                                    jset(Code03_Magnet1.que, ((_java_old_9 := r), (r := jcast('int', (r + (1)))), _java_old_9)[2], i)
                                    ans = jcast('int', (ans + 1))
                                # 重要剪枝逻辑
                                Code03_Magnet1.bl[b] = jcast('int', (Code03_Magnet1.bl[b] + 1))
                        else:
                            j = jcast('int', Code03_Magnet1.bl[b])
                            while (j <= Code03_Magnet1.br[b]):
                                if (((Code03_Magnet1.dist[j] <= Code03_Magnet1.range[cur]) and (Code03_Magnet1.m[j] <= Code03_Magnet1.p[cur])) and (not Code03_Magnet1.vis[j])):
                                    Code03_Magnet1.vis[j] = jcast('boolean', True)
                                    jset(Code03_Magnet1.que, ((_java_old_10 := r), (r := jcast('int', (r + (1)))), _java_old_10)[2], j)
                                    ans = jcast('int', (ans + 1))
                                j = jcast('int', (j + 1))
                            raise JBreak(None)
                    except JContinue as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                    except JBreak as _java_control_8:
                        if _java_control_8.label not in (None,):
                            raise
                        break
                    b = jcast('int', (b + 1))
            except JContinue as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
            except JBreak as _java_control_6:
                if _java_control_6.label not in (None,):
                    raise
                break
        return jcast('int', ans)

    @staticmethod
    def prepare():
        Code03_Magnet1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code03_Magnet1.n)))
        Code03_Magnet1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code03_Magnet1.n, Code03_Magnet1.blen)) - 1)), Code03_Magnet1.blen)))
        i = jcast('int', 1)
        while (i <= Code03_Magnet1.n):
            Code03_Magnet1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code03_Magnet1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Magnet1.bnum):
            Code03_Magnet1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code03_Magnet1.blen)), 1)))
            jset(Code03_Magnet1.br, i, jstatic('Math', 'min', jcast('int', (i * Code03_Magnet1.blen)), Code03_Magnet1.n))
            i = jcast('int', (i + 1))
        Code03_Magnet1.sortByM(1, Code03_Magnet1.n)
        i = jcast('int', 1)
        while (i <= Code03_Magnet1.bnum):
            Code03_Magnet1.maxm[i] = jcast('int', Code03_Magnet1.m[Code03_Magnet1.br[i]])
            Code03_Magnet1.sortByDist(Code03_Magnet1.bl[i], Code03_Magnet1.br[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code03_Magnet1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jset(Code03_Magnet1.x, 0, jcall(in_, 'nextInt'))
        jset(Code03_Magnet1.y, 0, jcall(in_, 'nextInt'))
        jset(Code03_Magnet1.p, 0, jcall(in_, 'nextInt'))
        jset(Code03_Magnet1.range, 0, jcall(in_, 'nextInt'))
        Code03_Magnet1.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Magnet1.n):
            jset(Code03_Magnet1.x, i, jcall(in_, 'nextInt'))
            jset(Code03_Magnet1.y, i, jcall(in_, 'nextInt'))
            jset(Code03_Magnet1.m, i, jcall(in_, 'nextInt'))
            jset(Code03_Magnet1.p, i, jcall(in_, 'nextInt'))
            jset(Code03_Magnet1.range, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i <= Code03_Magnet1.n):
            Code03_Magnet1.range[i] = jcast('long', jcast('long', (Code03_Magnet1.range[i] * Code03_Magnet1.range[i])))
            dx = jcast('long', jcast('int', (Code03_Magnet1.x[0] - Code03_Magnet1.x[i])))
            dy = jcast('long', jcast('int', (Code03_Magnet1.y[0] - Code03_Magnet1.y[i])))
            Code03_Magnet1.dist[i] = jcast('long', jcast('long', jadd(jcast('long', (dx * dx)), jcast('long', (dy * dy)))))
            i = jcast('int', (i + 1))
        Code03_Magnet1.prepare()
        jcall(out, 'println', Code03_Magnet1.bfs())
        jcall(out, 'flush')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buf': 'buf', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buf：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buf))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buf[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buf = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Magnet1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Magnet1.MAXN = jcast('int', 300001)
Code03_Magnet1.MAXB = jcast('int', 601)
Code03_Magnet1.n = jcast('int', 0)
Code03_Magnet1.x = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.y = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.m = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.p = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.range = jarray('long', [Code03_Magnet1.MAXN])
Code03_Magnet1.dist = jarray('long', [Code03_Magnet1.MAXN])
Code03_Magnet1.blen = jcast('int', 0)
Code03_Magnet1.bnum = jcast('int', 0)
Code03_Magnet1.bi = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.bl = jarray('int', [Code03_Magnet1.MAXB])
Code03_Magnet1.br = jarray('int', [Code03_Magnet1.MAXB])
Code03_Magnet1.maxm = jarray('int', [Code03_Magnet1.MAXB])
Code03_Magnet1.que = jarray('int', [Code03_Magnet1.MAXN])
Code03_Magnet1.vis = jarray('boolean', [Code03_Magnet1.MAXN])

if __name__ == '__main__':
    Code03_Magnet1.main([])

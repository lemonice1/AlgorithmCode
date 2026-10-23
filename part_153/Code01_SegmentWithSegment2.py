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

# 线段树套线段树，Python版
# 人有三种属性，身高、活泼度、缘分值
# 身高为int类型，活泼度和缘分值为小数点后最多1位的double类型
# 实现一种结构，提供如下两种类型的操作
# 操作 I a b c   : 加入一个人，身高为a，活泼度为b，缘分值为c
# 操作 Q a b c d : 查询身高范围[a,b]，活泼度范围[c,d]，所有人中的缘分最大值
# 注意操作Q，如果a > b需要交换，如果c > d需要交换
# 100 <= 身高 <= 200
# 0.0 <= 活泼度、缘分值 <= 100.0
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=1823
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_SegmentWithSegment2:
    __java_fields__ = {'n': 'n', 'm': 'm', 'MINX': 'MINX', 'MAXX': 'MAXX', 'MINY': 'MINY', 'MAXY': 'MAXY', 'tree': 'tree'}
    # 身高范围内有多少数字
    n = 0
    # 活泼度范围内有多少数字
    m = 0
    # 身高范围对应[MINX, MAXX]，活泼度范围对应[MINY, MAXY]
    MINX = 0
    MAXX = 0
    MINY = 0
    MAXY = 0
    # 外层是身高线段树，内层是活泼度线段树
    # 每一个外层线段树的节点，对应着一棵内层线段树
    # 内层线段树收集缘分值
    tree = None
    @staticmethod
    def innerBuild(yl, yr, xi, yi):
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        xi = jcast('int', xi)
        yi = jcast('int', yi)
        jset(Code01_SegmentWithSegment2.tree[xi], yi, jcast('int', (-1)))
        if (yl < yr):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(yl, yr)), 2)))
            Code01_SegmentWithSegment2.innerBuild(yl, mid, xi, jcast('int', (yi << (1 & 31))))
            Code01_SegmentWithSegment2.innerBuild(jcast('int', jadd(mid, 1)), yr, xi, jcast('int', (jcast('int', (yi << (1 & 31))) | 1)))

    @staticmethod
    def innerUpdate(jobi, jobv, yl, yr, xi, yi):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        xi = jcast('int', xi)
        yi = jcast('int', yi)
        if (yl == yr):
            jset(Code01_SegmentWithSegment2.tree[xi], yi, jstatic('Math', 'max', Code01_SegmentWithSegment2.tree[xi][yi], jobv))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(yl, yr)), 2)))
            if (jobi <= mid):
                Code01_SegmentWithSegment2.innerUpdate(jobi, jobv, yl, mid, xi, jcast('int', (yi << (1 & 31))))
            else:
                Code01_SegmentWithSegment2.innerUpdate(jobi, jobv, jcast('int', jadd(mid, 1)), yr, xi, jcast('int', (jcast('int', (yi << (1 & 31))) | 1)))
            jset(Code01_SegmentWithSegment2.tree[xi], yi, jstatic('Math', 'max', Code01_SegmentWithSegment2.tree[xi][jcast('int', (yi << (1 & 31)))], Code01_SegmentWithSegment2.tree[xi][jcast('int', (jcast('int', (yi << (1 & 31))) | 1))]))

    @staticmethod
    def innerQuery(jobl, jobr, yl, yr, xi, yi):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        xi = jcast('int', xi)
        yi = jcast('int', yi)
        if ((jobl <= yl) and (yr <= jobr)):
            return jcast('int', Code01_SegmentWithSegment2.tree[xi][yi])
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(yl, yr)), 2)))
        ans = jcast('int', jcast('int', (-1)))
        if (jobl <= mid):
            ans = jcast('int', Code01_SegmentWithSegment2.innerQuery(jobl, jobr, yl, mid, xi, jcast('int', (yi << (1 & 31)))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_SegmentWithSegment2.innerQuery(jobl, jobr, jcast('int', jadd(mid, 1)), yr, xi, jcast('int', (jcast('int', (yi << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def outerBuild(xl, xr, xi):
        xl = jcast('int', xl)
        xr = jcast('int', xr)
        xi = jcast('int', xi)
        Code01_SegmentWithSegment2.innerBuild(Code01_SegmentWithSegment2.MINY, Code01_SegmentWithSegment2.MAXY, xi, 1)
        if (xl < xr):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(xl, xr)), 2)))
            Code01_SegmentWithSegment2.outerBuild(xl, mid, jcast('int', (xi << (1 & 31))))
            Code01_SegmentWithSegment2.outerBuild(jcast('int', jadd(mid, 1)), xr, jcast('int', (jcast('int', (xi << (1 & 31))) | 1)))

    @staticmethod
    def outerUpdate(jobx, joby, jobv, xl, xr, xi):
        jobx = jcast('int', jobx)
        joby = jcast('int', joby)
        jobv = jcast('int', jobv)
        xl = jcast('int', xl)
        xr = jcast('int', xr)
        xi = jcast('int', xi)
        Code01_SegmentWithSegment2.innerUpdate(joby, jobv, Code01_SegmentWithSegment2.MINY, Code01_SegmentWithSegment2.MAXY, xi, 1)
        if (xl < xr):
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(xl, xr)), 2)))
            if (jobx <= mid):
                Code01_SegmentWithSegment2.outerUpdate(jobx, joby, jobv, xl, mid, jcast('int', (xi << (1 & 31))))
            else:
                Code01_SegmentWithSegment2.outerUpdate(jobx, joby, jobv, jcast('int', jadd(mid, 1)), xr, jcast('int', (jcast('int', (xi << (1 & 31))) | 1)))

    @staticmethod
    def outerQuery(jobxl, jobxr, jobyl, jobyr, xl, xr, xi):
        jobxl = jcast('int', jobxl)
        jobxr = jcast('int', jobxr)
        jobyl = jcast('int', jobyl)
        jobyr = jcast('int', jobyr)
        xl = jcast('int', xl)
        xr = jcast('int', xr)
        xi = jcast('int', xi)
        if ((jobxl <= xl) and (xr <= jobxr)):
            return jcast('int', Code01_SegmentWithSegment2.innerQuery(jobyl, jobyr, Code01_SegmentWithSegment2.MINY, Code01_SegmentWithSegment2.MAXY, xi, 1))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(xl, xr)), 2)))
        ans = jcast('int', jcast('int', (-1)))
        if (jobxl <= mid):
            ans = jcast('int', Code01_SegmentWithSegment2.outerQuery(jobxl, jobxr, jobyl, jobyr, xl, mid, jcast('int', (xi << (1 & 31)))))
        if (jobxr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code01_SegmentWithSegment2.outerQuery(jobxl, jobxr, jobyl, jobyr, jcast('int', jadd(mid, 1)), xr, jcast('int', (jcast('int', (xi << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        io = Code01_SegmentWithSegment2.Kattio(_java_ctor=0)
        q = jcast('int', jcall(io, 'nextInt'))
        op = None
        a = 0
        b = 0
        c = 0
        d = 0
        while (q != 0):
            Code01_SegmentWithSegment2.outerBuild(Code01_SegmentWithSegment2.MINX, Code01_SegmentWithSegment2.MAXX, 1)
            i = jcast('int', 1)
            while (i <= q):
                op = jcall(io, 'next')
                if jcall(op, 'equals', 'I'):
                    a = jcast('int', jcall(io, 'nextInt'))
                    b = jcast('int', jcast('int', (jcall(io, 'nextDouble') * 10)))
                    c = jcast('int', jcast('int', (jcall(io, 'nextDouble') * 10)))
                    Code01_SegmentWithSegment2.outerUpdate(a, b, c, Code01_SegmentWithSegment2.MINX, Code01_SegmentWithSegment2.MAXX, 1)
                else:
                    a = jcast('int', jcall(io, 'nextInt'))
                    b = jcast('int', jcall(io, 'nextInt'))
                    c = jcast('int', jcast('int', (jcall(io, 'nextDouble') * 10)))
                    d = jcast('int', jcast('int', (jcall(io, 'nextDouble') * 10)))
                    xl = jcast('int', jstatic('Math', 'min', a, b))
                    xr = jcast('int', jstatic('Math', 'max', a, b))
                    yl = jcast('int', jstatic('Math', 'min', c, d))
                    yr = jcast('int', jstatic('Math', 'max', c, d))
                    ans = jcast('int', Code01_SegmentWithSegment2.outerQuery(xl, xr, yl, yr, Code01_SegmentWithSegment2.MINX, Code01_SegmentWithSegment2.MAXX, 1))
                    if (ans == jcast('int', (-1))):
                        jcall(io, 'println', ans)
                    else:
                        jcall(io, 'println', jdiv(jcast('double', ans), 10))
                i = jcast('int', (i + 1))
            q = jcast('int', jcall(io, 'nextInt'))
        jcall(io, 'flush')
        jcall(io, 'close')

    # 读写工具类
    class Kattio(jclass('PrintWriter')):
        __java_fields__ = {'r': 'r', 'st': 'st'}
        # r：实例字段，在构造函数中初始化。
        # st：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self._java_init_1(jget(System, 'in'), jget(System, 'out'))

        def _java_init_1(self, i, o):
            super().__init__(o)
            self.r = jnew('BufferedReader', jnew('InputStreamReader', i))

        def _java_init_2(self, intput, output):
            super().__init__(output)
            self.r = jnew('BufferedReader', jnew('FileReader', intput))

        def next(self):
            try:
                while ((self.st == None) or (not jcall(self.st, 'hasMoreTokens'))):
                    self.st = jnew('StringTokenizer', jcall(self.r, 'readLine'))
                return jcall(self.st, 'nextToken')
            except (JBreak, JContinue):
                raise
            except Exception as _java_exception_1:
                if jinstanceof(_java_exception_1, 'Exception'):
                    e = _java_exception_1
                    None
                else:
                    raise
            return None

        def nextInt(self):
            return jcast('int', jstatic('Integer', 'parseInt', self.next()))

        def nextDouble(self):
            return jcast('double', jstatic('Double', 'parseDouble', self.next()))

        def nextLong(self):
            return jcast('long', jstatic('Long', 'parseLong', self.next()))

        def __init__(self, *args, _java_ctor=None):
            self.r = None
            self.st = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[], ['InputStream', 'OutputStream'], ['String', 'String']], [False, False, False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            if _java_choice == 1:
                return self._java_init_1(*args)
            if _java_choice == 2:
                return self._java_init_2(*args)
            raise TypeError("No matching overload for Code01_SegmentWithSegment2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_SegmentWithSegment2.n = jcast('int', 101)
Code01_SegmentWithSegment2.m = jcast('int', 1001)
Code01_SegmentWithSegment2.MINX = jcast('int', 100)
Code01_SegmentWithSegment2.MAXX = jcast('int', 200)
Code01_SegmentWithSegment2.MINY = jcast('int', 0)
Code01_SegmentWithSegment2.MAXY = jcast('int', 1000)
Code01_SegmentWithSegment2.tree = jarray('int', [jcast('int', (Code01_SegmentWithSegment2.n << (2 & 31))), jcast('int', (Code01_SegmentWithSegment2.m << (2 & 31)))])

if __name__ == '__main__':
    Code01_SegmentWithSegment2.main([])

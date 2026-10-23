# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 平均数和方差
# 给定一个长度为n的数组arr，操作分为三种类型，一共调用m次
# 操作 1 l r : arr数组中[l, r]范围上每个数字加上k，k为double类型
# 操作 2 l r : 查询arr数组中[l, r]范围上所有数字的平均数，返回double类型
# 操作 3 l r : 查询arr数组中[l, r]范围上所有数字的方差，返回double类型
# 测试链接 : https://www.luogu.com.cn/problem/P1471
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_MeanVariance2:
    __java_fields__ = {'MAXN': 'MAXN', 'arr': 'arr', 'sum1': 'sum1', 'sum2': 'sum2', 'addv': 'addv'}
    MAXN = 0
    arr = None
    # 区间累加和
    sum1 = None
    # 区间平方和
    sum2 = None
    # 懒更新信息(范围内每个数字增加多少)
    addv = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code04_MeanVariance2.sum1[i] = jcast('double', jadd(Code04_MeanVariance2.sum1[jcast('int', (i << (1 & 31)))], Code04_MeanVariance2.sum1[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))
        Code04_MeanVariance2.sum2[i] = jcast('double', jadd(Code04_MeanVariance2.sum2[jcast('int', (i << (1 & 31)))], Code04_MeanVariance2.sum2[jcast('int', (jcast('int', (i << (1 & 31))) | 1))]))

    @staticmethod
    def down(i, ln, rn):
        i = jcast('int', i)
        ln = jcast('int', ln)
        rn = jcast('int', rn)
        if (Code04_MeanVariance2.addv[i] != 0):
            Code04_MeanVariance2.lazy(jcast('int', (i << (1 & 31))), Code04_MeanVariance2.addv[i], ln)
            Code04_MeanVariance2.lazy(jcast('int', (jcast('int', (i << (1 & 31))) | 1)), Code04_MeanVariance2.addv[i], rn)
            Code04_MeanVariance2.addv[i] = jcast('double', 0)

    @staticmethod
    def lazy(i, v, n):
        i = jcast('int', i)
        v = jcast('double', v)
        n = jcast('int', n)
        Code04_MeanVariance2.sum2[i] = jcast('double', jadd(Code04_MeanVariance2.sum2[i], jadd(((Code04_MeanVariance2.sum1[i] * v) * 2), ((v * v) * n))))
        Code04_MeanVariance2.sum1[i] = jcast('double', jadd(Code04_MeanVariance2.sum1[i], (v * n)))
        Code04_MeanVariance2.addv[i] = jcast('double', jadd(Code04_MeanVariance2.addv[i], v))

    @staticmethod
    def build(l, r, i):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code04_MeanVariance2.sum1[i] = jcast('double', Code04_MeanVariance2.arr[l])
            Code04_MeanVariance2.sum2[i] = jcast('double', (Code04_MeanVariance2.arr[l] * Code04_MeanVariance2.arr[l]))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_MeanVariance2.build(l, mid, jcast('int', (i << (1 & 31))))
            Code04_MeanVariance2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_MeanVariance2.up(i)
        Code04_MeanVariance2.addv[i] = jcast('double', 0)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('double', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code04_MeanVariance2.lazy(i, jobv, jcast('int', jadd(jcast('int', (r - l)), 1)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code04_MeanVariance2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
            if (jobl <= mid):
                Code04_MeanVariance2.add(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code04_MeanVariance2.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code04_MeanVariance2.up(i)

    @staticmethod
    def query(sum, jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('double', sum[i])
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code04_MeanVariance2.down(i, jcast('int', jadd(jcast('int', (mid - l)), 1)), jcast('int', (r - mid)))
        ans = jcast('double', 0)
        if (jobl <= mid):
            ans = jcast('double', jadd(ans, Code04_MeanVariance2.query(sum, jobl, jobr, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('double', jadd(ans, Code04_MeanVariance2.query(sum, jobl, jobr, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('double', ans)

    @staticmethod
    def main(args):
        io = Code04_MeanVariance2.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        m = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= n):
            jset(Code04_MeanVariance2.arr, i, jcall(io, 'nextDouble'))
            i = jcast('int', (i + 1))
        Code04_MeanVariance2.build(1, n, 1)
        jobv = 0.0
        i = jcast('int', 1)
        op = 0
        jobl = 0
        jobr = 0
        while (i <= m):
            op = jcast('int', jcall(io, 'nextInt'))
            if (op == 1):
                jobl = jcast('int', jcall(io, 'nextInt'))
                jobr = jcast('int', jcall(io, 'nextInt'))
                jobv = jcast('double', jcall(io, 'nextDouble'))
                Code04_MeanVariance2.add(jobl, jobr, jobv, 1, n, 1)
            else:
                if (op == 2):
                    jobl = jcast('int', jcall(io, 'nextInt'))
                    jobr = jcast('int', jcall(io, 'nextInt'))
                    ans = jcast('double', jdiv(Code04_MeanVariance2.query(Code04_MeanVariance2.sum1, jobl, jobr, 1, n, 1), jcast('int', jadd(jcast('int', (jobr - jobl)), 1))))
                    jcall(io, 'println', jstatic('String', 'format', '%.4f', ans))
                else:
                    jobl = jcast('int', jcall(io, 'nextInt'))
                    jobr = jcast('int', jcall(io, 'nextInt'))
                    a = jcast('double', Code04_MeanVariance2.query(Code04_MeanVariance2.sum1, jobl, jobr, 1, n, 1))
                    b = jcast('double', Code04_MeanVariance2.query(Code04_MeanVariance2.sum2, jobl, jobr, 1, n, 1))
                    size = jcast('double', jcast('int', jadd(jcast('int', (jobr - jobl)), 1)))
                    ans = jcast('double', (jdiv(b, size) - (jdiv(a, size) * jdiv(a, size))))
                    jcall(io, 'println', jstatic('String', 'format', '%.4f', ans))
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    # Kattio 与 StreamTokenizer 接口均由 Python 实现，按输入格式选择，不沿用原语言的速度比较
    # 输入包含特殊格式时，可使用本类先读取字符串，再选择 int 或 float 解析
    # Python 输入输出参考：https://docs.python.org/3/library/io.html
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
            raise TypeError("No matching overload for Code04_MeanVariance2.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_MeanVariance2.MAXN = jcast('int', 100001)
Code04_MeanVariance2.arr = jarray('double', [Code04_MeanVariance2.MAXN])
Code04_MeanVariance2.sum1 = jarray('double', [jcast('int', (Code04_MeanVariance2.MAXN << (2 & 31)))])
Code04_MeanVariance2.sum2 = jarray('double', [jcast('int', (Code04_MeanVariance2.MAXN << (2 & 31)))])
Code04_MeanVariance2.addv = jarray('double', [jcast('int', (Code04_MeanVariance2.MAXN << (2 & 31)))])

if __name__ == '__main__':
    Code04_MeanVariance2.main([])

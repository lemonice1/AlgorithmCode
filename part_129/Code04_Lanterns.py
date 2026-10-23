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

# 彩灯
# 一共有n个灯泡，开始都是不亮的状态，有m个开关
# 每个开关能改变若干灯泡的状态，改变是指，亮变不亮、不亮变亮
# 比如n=5，某个开关为XXOOO，表示这个开关只能改变后3个灯泡的状态
# 可以随意使用开关，返回有多少种亮灯的组合，全不亮也算一种组合
# 答案可能很大，对 2008 取模
# 1 <= n <= 50
# 1 <= m <= 50
# 测试链接 : https://www.luogu.com.cn/problem/P3857
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Lanterns:
    __java_fields__ = {'MAXN': 'MAXN', 'MOD': 'MOD', 'arr': 'arr', 'basis': 'basis', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MOD = 0
    arr = None
    basis = None
    n = 0
    m = 0
    # 普通消元
    # 计算线性基的大小
    @staticmethod
    def compute():
        size = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Lanterns.m):
            if Code04_Lanterns.insert(Code04_Lanterns.arr[i]):
                size = jcast('int', (size + 1))
            i = jcast('int', (i + 1))
        return jcast('int', size)

    # 线性基里插入num，如果线性基增加了返回true，否则返回false
    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', Code04_Lanterns.n)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (Code04_Lanterns.basis[i] == 0):
                    Code04_Lanterns.basis[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ Code04_Lanterns.basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        io = Code04_Lanterns.Kattio(_java_ctor=0)
        Code04_Lanterns.n = jcast('int', jcast('int', (jcall(io, 'nextInt') - 1)))
        Code04_Lanterns.m = jcast('int', jcall(io, 'nextInt'))
        s = None
        i = jcast('int', 1)
        while (i <= Code04_Lanterns.m):
            s = jcall(jcall(io, 'next'), 'toCharArray')
            num = jcast('long', 0)
            j = jcast('int', 0)
            while (j <= Code04_Lanterns.n):
                if (s[j] == jchar('O')):
                    num = jcast('long', jcast('long', (num | jcast('long', (1 << (j & 63))))))
                j = jcast('int', (j + 1))
            Code04_Lanterns.arr[i] = jcast('long', num)
            i = jcast('int', (i + 1))
        size = jcast('int', Code04_Lanterns.compute())
        jcall(io, 'println', jcast('long', jmod(jcast('long', (1 << (size & 63))), Code04_Lanterns.MOD)))
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
            raise TypeError("No matching overload for Code04_Lanterns.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Lanterns.MAXN = jcast('int', 51)
Code04_Lanterns.MOD = jcast('int', 2008)
Code04_Lanterns.arr = jarray('long', [Code04_Lanterns.MAXN])
Code04_Lanterns.basis = jarray('long', [Code04_Lanterns.MAXN])
Code04_Lanterns.n = jcast('int', 0)
Code04_Lanterns.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_Lanterns.main([])

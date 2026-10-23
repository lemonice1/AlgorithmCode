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

# 外星千足虫
# 一共有n种虫子，编号1~n，虫子腿为奇数认为是外星虫，偶数认为是地球虫
# 一共有m条虫子腿的测量记录，记录编号1~m
# 比如其中一条测量记录为，011 1，表示1号虫没参与，2号、3号虫参与了，总腿数为奇数
# 测量记录保证不会有自相矛盾的情况，但是可能有冗余的测量结果
# 也许拥有从第1号到第k号测量记录就够了，k+1~m号测量记录有或者没有都不影响测量结果
# 打印这个k，并且打印每种虫子到底是外星虫还是地球虫
# 如果使用所有的测量结果，依然无法确定每种虫子的属性，打印"Cannot Determine"
# 1 <= n <= 1000
# 1 <= m <= 2000
# 测试链接 : https://www.luogu.com.cn/problem/P2447
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_AlienInsectLegs:
    __java_fields__ = {'BIT': 'BIT', 'MAXN': 'MAXN', 'MAXM': 'MAXM', 'mat': 'mat', 'n': 'n', 'm': 'm', 's': 's', 'need': 'need'}
    BIT = 0
    MAXN = 0
    MAXM = 0
    mat = None
    n = 0
    m = 0
    s = 0
    need = 0
    # 高斯消元解决异或方程组模版 + 位图，很小的改写
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        Code03_AlienInsectLegs.need = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', i)
                while (j <= n):
                    try:
                        if (Code03_AlienInsectLegs.get(j, i) == 1):
                            Code03_AlienInsectLegs.swap(i, j)
                            Code03_AlienInsectLegs.need = jcast('int', jstatic('Math', 'max', Code03_AlienInsectLegs.need, j))
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                # 一旦没有唯一解，可以结束了
                if (Code03_AlienInsectLegs.get(i, i) == 0):
                    return
                j = jcast('int', 1)
                while (j <= n):
                    if ((i != j) and (Code03_AlienInsectLegs.get(j, i) == 1)):
                        # 因为列从1开始，所以从第1位状态开始才有用
                        # 于是1~n+1列的状态，对应1~n+1位
                        # 但是位图中永远有0位，只不过从来不使用
                        # 于是一共有n+2位状态，都需要异或
                        Code03_AlienInsectLegs.eor(i, j, jcast('int', jadd(n, 2)))
                    j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    # 把row行，col列的状态设置成v
    @staticmethod
    def set(row, col, v):
        row = jcast('int', row)
        col = jcast('int', col)
        v = jcast('int', v)
        if (v == 0):
            ((_java_obj_3 := Code03_AlienInsectLegs.mat[row]), (_java_key_4 := jcast('int', jdiv(col, Code03_AlienInsectLegs.BIT))), jset(_java_obj_3, _java_key_4, jcast('long', (jget(_java_obj_3, _java_key_4) & jcast('long', (~jcast('long', (1 << (jcast('int', jmod(col, Code03_AlienInsectLegs.BIT)) & 63)))))))))[2]
        else:
            ((_java_obj_5 := Code03_AlienInsectLegs.mat[row]), (_java_key_6 := jcast('int', jdiv(col, Code03_AlienInsectLegs.BIT))), jset(_java_obj_5, _java_key_6, jcast('long', (jget(_java_obj_5, _java_key_6) | jcast('long', (1 << (jcast('int', jmod(col, Code03_AlienInsectLegs.BIT)) & 63)))))))[2]

    # 得到row行，col列的状态
    @staticmethod
    def get(row, col):
        row = jcast('int', row)
        col = jcast('int', col)
        return jcast('int', (1 if (jcast('long', (jcast('long', (Code03_AlienInsectLegs.mat[row][jcast('int', jdiv(col, Code03_AlienInsectLegs.BIT))] >> (jcast('int', jmod(col, Code03_AlienInsectLegs.BIT)) & 63))) & 1)) == 1) else 0))

    # row2行状态 = row2行状态 ^ row1行状态
    # 状态一共有bits位
    @staticmethod
    def eor(row1, row2, bits):
        row1 = jcast('int', row1)
        row2 = jcast('int', row2)
        bits = jcast('int', bits)
        k = jcast('int', 0)
        while (k <= jcast('int', jdiv(bits, Code03_AlienInsectLegs.BIT))):
            ((_java_obj_7 := Code03_AlienInsectLegs.mat[row2]), (_java_key_8 := k), jset(_java_obj_7, _java_key_8, jcast('long', (jget(_java_obj_7, _java_key_8) ^ Code03_AlienInsectLegs.mat[row1][k]))))[2]
            k = jcast('int', (k + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code03_AlienInsectLegs.mat[a]
        Code03_AlienInsectLegs.mat[a] = Code03_AlienInsectLegs.mat[b]
        Code03_AlienInsectLegs.mat[b] = tmp

    @staticmethod
    def main(args):
        io = Code03_AlienInsectLegs.Kattio(_java_ctor=0)
        Code03_AlienInsectLegs.n = jcast('int', jcall(io, 'nextInt'))
        Code03_AlienInsectLegs.m = jcast('int', jcall(io, 'nextInt'))
        Code03_AlienInsectLegs.s = jcast('int', jstatic('Math', 'max', Code03_AlienInsectLegs.n, Code03_AlienInsectLegs.m))
        i = jcast('int', 1)
        while (i <= Code03_AlienInsectLegs.m):
            line = jcall(jcall(io, 'next'), 'toCharArray')
            j = jcast('int', 1)
            while (j <= Code03_AlienInsectLegs.n):
                Code03_AlienInsectLegs.set(i, j, jcast('int', (line[jcast('int', (j - 1))] - jchar('0'))))
                j = jcast('int', (j + 1))
            Code03_AlienInsectLegs.set(i, jcast('int', jadd(Code03_AlienInsectLegs.s, 1)), jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_AlienInsectLegs.gauss(Code03_AlienInsectLegs.s)
        sign = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= Code03_AlienInsectLegs.n):
            try:
                if (Code03_AlienInsectLegs.get(i, i) == 0):
                    sign = jcast('int', 0)
                    raise JBreak(None)
            except JContinue as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
            except JBreak as _java_control_9:
                if _java_control_9.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (sign == 0):
            jcall(io, 'println', 'Cannot Determine')
        else:
            jcall(io, 'println', Code03_AlienInsectLegs.need)
            i = jcast('int', 1)
            while (i <= Code03_AlienInsectLegs.n):
                if (Code03_AlienInsectLegs.get(i, jcast('int', jadd(Code03_AlienInsectLegs.s, 1))) == 1):
                    jcall(io, 'println', '?y7M#')
                else:
                    jcall(io, 'println', 'Earth')
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
            except Exception as _java_exception_10:
                if jinstanceof(_java_exception_10, 'Exception'):
                    e = _java_exception_10
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
            raise TypeError("No matching overload for Code03_AlienInsectLegs.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_AlienInsectLegs.BIT = jcast('int', 64)
Code03_AlienInsectLegs.MAXN = jcast('int', 2002)
Code03_AlienInsectLegs.MAXM = jcast('int', jcast('int', jadd(jcast('int', jdiv(Code03_AlienInsectLegs.MAXN, Code03_AlienInsectLegs.BIT)), 1)))
Code03_AlienInsectLegs.mat = jarray('long', [Code03_AlienInsectLegs.MAXN, Code03_AlienInsectLegs.MAXM])
Code03_AlienInsectLegs.n = jcast('int', 0)
Code03_AlienInsectLegs.m = jcast('int', 0)
Code03_AlienInsectLegs.s = jcast('int', 0)
Code03_AlienInsectLegs.need = jcast('int', 0)

if __name__ == '__main__':
    Code03_AlienInsectLegs.main([])

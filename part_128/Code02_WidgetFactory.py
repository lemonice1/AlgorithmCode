# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 工具工厂
# 一共有n种工具，编号1~n，一共有m条记录，其中一条记录格式如下：
# 4 WED SUN 13 18 1 13
# 表示有个工人一共加工了4件工具，从某个星期三开始工作，到某个星期天结束工作
# 加工的工具依次为13号、18号、1号、13号
# 每个工人在工作期间不休息，每件工具都是串行加工的，完成一件后才开始下一件
# 每种工具制作天数是固定的，并且任何工具的制作天数最少3天、最多9天
# 但该数据丢失了，所以现在需要根据记录，推断出每种工具的制作天数
# 如果记录之间存在矛盾，打印"Inconsistent data."
# 如果记录无法确定每种工具的制作天数，打印"Multiple solutions."
# 如果记录能够确定每种工具的制作天数，打印所有结果
# 1 <= n、m <= 300
# 测试链接 : http://poj.org/problem?id=2947
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_WidgetFactory:
    __java_fields__ = {'MOD': 'MOD', 'MAXN': 'MAXN', 'mat': 'mat', 'inv': 'inv_data', 'days': 'days', 'n': 'n', 'm': 'm', 's': 's'}
    MOD = 0
    MAXN = 0
    mat = None
    inv_data = None
    days = None
    n = 0
    m = 0
    s = 0
    @staticmethod
    def inv():
        Code02_WidgetFactory.inv_data[1] = jcast('int', 1)
        i = jcast('int', 2)
        while (i < Code02_WidgetFactory.MOD):
            Code02_WidgetFactory.inv_data[i] = jcast('int', jcast('int', jcast('long', (Code02_WidgetFactory.MOD - jcast('long', jmod(jcast('long', (jcast('long', Code02_WidgetFactory.inv_data[jcast('int', jmod(Code02_WidgetFactory.MOD, i))]) * jcast('int', jdiv(Code02_WidgetFactory.MOD, i)))), Code02_WidgetFactory.MOD))))))
            i = jcast('int', (i + 1))

    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code02_WidgetFactory.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_WidgetFactory.s):
            j = jcast('int', 1)
            while (j <= jcast('int', jadd(Code02_WidgetFactory.s, 1))):
                jset(Code02_WidgetFactory.mat[i], j, 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def day(str):
        i = jcast('int', 0)
        while (i < jget(Code02_WidgetFactory.days, 'length')):
            if jcall(str, 'equals', Code02_WidgetFactory.days[i]):
                return jcast('int', i)
            i = jcast('int', (i + 1))
        return jcast('int', jcast('int', (-1)))

    # 高斯消元解决同余方程组模版，保证初始系数没有负数
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (Code02_WidgetFactory.mat[j][j] != 0)):
                            raise JContinue(None)
                        if (Code02_WidgetFactory.mat[j][i] != 0):
                            Code02_WidgetFactory.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (Code02_WidgetFactory.mat[i][i] != 0):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (Code02_WidgetFactory.mat[j][i] != 0)):
                            gcd = jcast('int', Code02_WidgetFactory.gcd(Code02_WidgetFactory.mat[j][i], Code02_WidgetFactory.mat[i][i]))
                            a = jcast('int', jcast('int', jdiv(Code02_WidgetFactory.mat[i][i], gcd)))
                            b = jcast('int', jcast('int', jdiv(Code02_WidgetFactory.mat[j][i], gcd)))
                            if ((j < i) and (Code02_WidgetFactory.mat[j][j] != 0)):
                                k = jcast('int', j)
                                while (k < i):
                                    jset(Code02_WidgetFactory.mat[j], k, jcast('int', jmod(jcast('int', (Code02_WidgetFactory.mat[j][k] * a)), Code02_WidgetFactory.MOD)))
                                    k = jcast('int', (k + 1))
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                jset(Code02_WidgetFactory.mat[j], k, jcast('int', jmod(jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', (Code02_WidgetFactory.mat[j][k] * a)) - jcast('int', (Code02_WidgetFactory.mat[i][k] * b)))), Code02_WidgetFactory.MOD)), Code02_WidgetFactory.MOD)), Code02_WidgetFactory.MOD)))
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= n):
            try:
                if (Code02_WidgetFactory.mat[i][i] != 0):
                    flag = jcast('boolean', False)
                    j = jcast('int', jcast('int', jadd(i, 1)))
                    while (j <= n):
                        try:
                            if (Code02_WidgetFactory.mat[i][j] != 0):
                                flag = jcast('boolean', True)
                                raise JBreak(None)
                        except JContinue as _java_control_4:
                            if _java_control_4.label not in (None,):
                                raise
                        except JBreak as _java_control_4:
                            if _java_control_4.label not in (None,):
                                raise
                            break
                        j = jcast('int', (j + 1))
                    if (not flag):
                        jset(Code02_WidgetFactory.mat[i], jcast('int', jadd(n, 1)), jcast('int', jmod(jcast('int', (Code02_WidgetFactory.mat[i][jcast('int', jadd(n, 1))] * Code02_WidgetFactory.inv_data[Code02_WidgetFactory.mat[i][i]])), Code02_WidgetFactory.MOD)))
                        jset(Code02_WidgetFactory.mat[i], i, 1)
            except JContinue as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
            except JBreak as _java_control_3:
                if _java_control_3.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code02_WidgetFactory.mat[a]
        Code02_WidgetFactory.mat[a] = Code02_WidgetFactory.mat[b]
        Code02_WidgetFactory.mat[b] = tmp

    @staticmethod
    def main(args):
        Code02_WidgetFactory.inv()
        io = Code02_WidgetFactory.Kattio(_java_ctor=0)
        Code02_WidgetFactory.n = jcast('int', jcall(io, 'nextInt'))
        Code02_WidgetFactory.m = jcast('int', jcall(io, 'nextInt'))
        while ((Code02_WidgetFactory.n != 0) and (Code02_WidgetFactory.m != 0)):
            try:
                Code02_WidgetFactory.s = jcast('int', jstatic('Math', 'max', Code02_WidgetFactory.n, Code02_WidgetFactory.m))
                Code02_WidgetFactory.prepare()
                i = jcast('int', 1)
                while (i <= Code02_WidgetFactory.m):
                    k = jcast('int', jcall(io, 'nextInt'))
                    st = jcall(io, 'next')
                    et = jcall(io, 'next')
                    j = jcast('int', 1)
                    while (j <= k):
                        tool = jcast('int', jcall(io, 'nextInt'))
                        jset(Code02_WidgetFactory.mat[i], tool, jcast('int', jmod(jcast('int', jadd(Code02_WidgetFactory.mat[i][tool], 1)), Code02_WidgetFactory.MOD)))
                        j = jcast('int', (j + 1))
                    jset(Code02_WidgetFactory.mat[i], jcast('int', jadd(Code02_WidgetFactory.s, 1)), jcast('int', jmod(jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(jcast('int', (Code02_WidgetFactory.day(et) - Code02_WidgetFactory.day(st))), 1)), Code02_WidgetFactory.MOD)), Code02_WidgetFactory.MOD)), Code02_WidgetFactory.MOD)))
                    i = jcast('int', (i + 1))
                Code02_WidgetFactory.gauss(Code02_WidgetFactory.s)
                sign = jcast('int', 1)
                i = jcast('int', 1)
                while (i <= Code02_WidgetFactory.s):
                    try:
                        if ((Code02_WidgetFactory.mat[i][i] == 0) and (Code02_WidgetFactory.mat[i][jcast('int', jadd(Code02_WidgetFactory.s, 1))] != 0)):
                            sign = jcast('int', jcast('int', (-1)))
                            raise JBreak(None)
                        if ((i <= Code02_WidgetFactory.n) and (Code02_WidgetFactory.mat[i][i] == 0)):
                            sign = jcast('int', 0)
                    except JContinue as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                    except JBreak as _java_control_6:
                        if _java_control_6.label not in (None,):
                            raise
                        break
                    i = jcast('int', (i + 1))
                if (sign == jcast('int', (-1))):
                    jcall(io, 'println', 'Inconsistent data.')
                else:
                    if (sign == 0):
                        jcall(io, 'println', 'Multiple solutions.')
                    else:
                        i = jcast('int', 1)
                        while (i <= Code02_WidgetFactory.n):
                            if (Code02_WidgetFactory.mat[i][jcast('int', jadd(Code02_WidgetFactory.s, 1))] < 3):
                                ((_java_obj_7 := Code02_WidgetFactory.mat[i]), (_java_key_8 := jcast('int', jadd(Code02_WidgetFactory.s, 1))), jset(_java_obj_7, _java_key_8, jcast('int', jadd(jget(_java_obj_7, _java_key_8), 7))))[2]
                            i = jcast('int', (i + 1))
                        i = jcast('int', 1)
                        while (i < Code02_WidgetFactory.n):
                            jcall(io, 'print', jadd(Code02_WidgetFactory.mat[i][jcast('int', jadd(Code02_WidgetFactory.s, 1))], ' '))
                            i = jcast('int', (i + 1))
                        jcall(io, 'println', Code02_WidgetFactory.mat[Code02_WidgetFactory.n][jcast('int', jadd(Code02_WidgetFactory.s, 1))])
                # 下一组n和m
                Code02_WidgetFactory.n = jcast('int', jcall(io, 'nextInt'))
                Code02_WidgetFactory.m = jcast('int', jcall(io, 'nextInt'))
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
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
            except Exception as _java_exception_9:
                if jinstanceof(_java_exception_9, 'Exception'):
                    e = _java_exception_9
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
            raise TypeError("No matching overload for Code02_WidgetFactory.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_WidgetFactory.MOD = jcast('int', 7)
Code02_WidgetFactory.MAXN = jcast('int', 302)
Code02_WidgetFactory.mat = jarray('int', [Code02_WidgetFactory.MAXN, Code02_WidgetFactory.MAXN])
Code02_WidgetFactory.inv_data = jarray('int', [Code02_WidgetFactory.MOD])
Code02_WidgetFactory.days = jarray('String', [None], ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
Code02_WidgetFactory.n = jcast('int', 0)
Code02_WidgetFactory.m = jcast('int', 0)
Code02_WidgetFactory.s = jcast('int', 0)

if __name__ == '__main__':
    Code02_WidgetFactory.main([])

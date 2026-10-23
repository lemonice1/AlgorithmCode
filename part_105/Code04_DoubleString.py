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

# 读取科学计数法表达的double数字
# 如果输入的字符串代表double数字的科学计数法形式
# 此格式不适合 StreamTokenizer 的默认分词规则，应先读取字符串再解析
# 用StringTokenizer读取正确但比较费内存
# Python 输入输出参考：https://docs.python.org/3/library/io.html
class Code04_DoubleString:
    __java_fields__ = {}
    #
    # 输入如下
    # 5
    # 10.203E+0000
    # 5.6920E+0001
    # 30.888E-0001
    # 400.20E+0002
    # 0.2373E-0002
    #
    @staticmethod
    def main(args):
        # test1();
        Code04_DoubleString.test2()

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
            raise TypeError("No matching overload for Code04_DoubleString.Kattio.Kattio")


    # 此处需要按原始字符串解析，避免分词规则或浮点转换改变输入值
    @staticmethod
    def test1():
        jprint('测试StreamTokenizer', newline=True)
        jprint('输入 : ', newline=True)
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        num = 0.0
        i = jcast('int', 1)
        while (i <= n):
            jcall(in_, 'nextToken')
            num = jcast('double', jcast('double', jget(in_, 'nval')))
            jcall(out, 'println', num)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    # StringTokenizer可以正确读取
    @staticmethod
    def test2():
        jprint('测试StringTokenizer', newline=True)
        jprint('输入 : ', newline=True)
        io = Code04_DoubleString.Kattio(_java_ctor=0)
        n = jcast('int', jcall(io, 'nextInt'))
        num = 0.0
        i = jcast('int', 1)
        while (i <= n):
            num = jcast('double', jcall(io, 'nextDouble'))
            jcall(io, 'println', num)
            i = jcast('int', (i + 1))
        jcall(io, 'flush')
        jcall(io, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_DoubleString.main([])

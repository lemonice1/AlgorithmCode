# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 演示 Kattio 接口在 Python 中的字符串分词读入方式
# 兼容分词器保留原分词规则；特殊输入应先读取完整字符串再解析
# 可使用本文件的 Kattio 接口读取字符串，再按题目格式转换
# 比如，就是需要依次读取一个一个的字符串进行处理
# StreamTokenizer 兼容层的 nval 使用 float；大整数应读取字符串后用 int 解析，避免浮点舍入
# 科学计数法应先读取完整字符串，再使用 float 解析，避免默认分词规则拆开指数部分
# Kattio 先按空白读取完整字符串，可再用 int 或 float 解析对应数值
# 可以直接运行本文件的main函数，根据提示输入给定的数字，能清晰的看到这一点
# 输入接口的选择取决于分词规则、数值精度和实际数据规模
# 本版本不沿用原语言的速度比较；应按 Python 实现的实际开销选择输入方式
# 需要保留原始数值文本时，可用 Kattio 读取字符串，再选择 int 或 float 解析
# Python 使用对应的整数、容器与输入输出接口，语言差异由兼容层处理
class Code05_Kattio:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        jprint('请输入 : 131237128371723187', newline=True)
        jprint('并按回车', newline=True)
        jcall(in_, 'nextToken')
        long1 = jcast('long', jcast('long', jget(in_, 'nval')))
        jprint('StreamTokenizer读取到的数字 : ', newline=True)
        jprint(long1, newline=True)
        jprint(newline=True)
        jprint('请输入 : 5.6920E+0001', newline=True)
        jprint('并按回车', newline=True)
        jcall(in_, 'nextToken')
        double1 = jcast('double', jget(in_, 'nval'))
        jprint('StreamTokenizer读取到的数字 : ', newline=True)
        jprint(double1, newline=True)
        jprint('============================', newline=True)
        io = Code05_Kattio.Kattio(_java_ctor=0)
        jprint('请输入 : 131237128371723187', newline=True)
        jprint('并按回车', newline=True)
        long2 = jcast('long', jcall(io, 'nextLong'))
        jprint('Kattio读取到的数字 : ', newline=True)
        jprint(long2, newline=True)
        jprint(newline=True)
        jprint('请输入 : 5.6920E+0001', newline=True)
        jprint('并按回车', newline=True)
        double2 = jcast('double', jcall(io, 'nextDouble'))
        jprint('Kattio读取到的数字 : ', newline=True)
        jprint(double2, newline=True)
        jcall(io, 'close')

    # Kattio 字符串分词接口的 Python 使用示例
    # 可以找个一些具体题目试一试
    # 这里就是罗列了一下
    @staticmethod
    def show():
        # 自动接入输入输出流
        io = Code05_Kattio.Kattio(_java_ctor=0)
        # 读取下一个字符串，注意不是整行，是以空格或回车分割的字符串，一个一个读取
        jcall(io, 'next')
        # 读取下一个int
        jcall(io, 'nextInt')
        # 读取下一个double
        jcall(io, 'nextDouble')
        # 读取下一个long
        jcall(io, 'nextLong')
        # 答案进入输出流
        jcall(io, 'println', 'ans')
        # 答案刷给后台
        jcall(io, 'flush')
        # 关闭io
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
            raise TypeError("No matching overload for Code05_Kattio.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code05_Kattio.main([])

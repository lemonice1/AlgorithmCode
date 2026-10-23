# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 元素
# 给定n个魔法矿石，每个矿石有状态和魔力，都是整数
# 若干矿石组成的组合能否有效，根据状态异或的结果来决定
# 如果一个矿石组合内部会产生异或和为0的子集，那么这个组合无效
# 返回有效的矿石组合中，最大的魔力和是多少
# 1 <= n <= 1000
# 1 <= 状态 <= 10^18
# 1 <= 魔力 <= 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P4570
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Elements:
    __java_fields__ = {'MAXN': 'MAXN', 'BIT': 'BIT', 'arr': 'arr', 'basis': 'basis', 'n': 'n'}
    MAXN = 0
    BIT = 0
    arr = None
    basis = None
    n = 0
    # 普通消元
    # 计算得到最大线性基的最少花费
    @staticmethod
    def compute():
        ans = jcast('long', 0)
        jstatic('Arrays', 'sort', Code03_Elements.arr, 1, jcast('int', jadd(Code03_Elements.n, 1)), (lambda a, b: (jcast('int', (-1)) if (a[1] >= b[1]) else 1)))
        i = jcast('int', 1)
        while (i <= Code03_Elements.n):
            if Code03_Elements.insert(Code03_Elements.arr[i][0]):
                ans = jcast('long', jcast('long', jadd(ans, Code03_Elements.arr[i][1])))
            i = jcast('int', (i + 1))
        return jcast('long', ans)

    # 线性基里插入num，如果线性基增加了返回true，否则返回false
    @staticmethod
    def insert(num):
        num = jcast('long', num)
        i = jcast('int', Code03_Elements.BIT)
        while (i >= 0):
            if (jcast('long', (num >> (i & 63))) == 1):
                if (Code03_Elements.basis[i] == 0):
                    Code03_Elements.basis[i] = jcast('long', num)
                    return jcast('boolean', True)
                num = jcast('long', jcast('long', (num ^ Code03_Elements.basis[i])))
            i = jcast('int', (i - 1))
        return jcast('boolean', False)

    @staticmethod
    def main(args):
        # 题目会读取10^18范围内的long类型数字
        # StreamTokenizer 兼容层的 nval 使用 float；大整数应读取字符串后用 int 解析，避免浮点舍入
        # 这里使用 Kattio 分词接口，Python 示例见 part_14/Code05_Kattio.py
        # 有详细的说明
        io = Code03_Elements.Kattio(_java_ctor=0)
        Code03_Elements.n = jcast('int', jcall(io, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Elements.n):
            jset(Code03_Elements.arr[i], 0, jcall(io, 'nextLong'))
            jset(Code03_Elements.arr[i], 1, jcall(io, 'nextInt'))
            i = jcast('int', (i + 1))
        jcall(io, 'println', Code03_Elements.compute())
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
            raise TypeError("No matching overload for Code03_Elements.Kattio.Kattio")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Elements.MAXN = jcast('int', 1001)
Code03_Elements.BIT = jcast('int', 60)
Code03_Elements.arr = jarray('long', [Code03_Elements.MAXN, 2])
Code03_Elements.basis = jarray('long', [jcast('int', jadd(Code03_Elements.BIT, 1))])
Code03_Elements.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_Elements.main([])

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

# 展示acm风格的测试方式
# 测试链接 : https://www.nowcoder.com/exam/test/70070648/detail?pid=27976983
# 其中，7.A+B(7)，就是一个没有给定数据规模，只能按行读数据的例子
# 此时需要自己切分出数据来计算
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_ReadByLine:
    __java_fields__ = {'line': 'line', 'parts': 'parts', 'sum': 'sum'}
    line = None
    parts = None
    sum = 0
    @staticmethod
    def main(args):
        in_ = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jset(Code04_ReadByLine, 'line', jcall(in_, 'readLine')) != None):
            Code04_ReadByLine.parts = jcall(Code04_ReadByLine.line, 'split', ' ')
            Code04_ReadByLine.sum = jcast('int', 0)
            for num in Code04_ReadByLine.parts:
                Code04_ReadByLine.sum = jcast('int', jadd(Code04_ReadByLine.sum, jstatic('Integer', 'valueOf', num)))
            jcall(out, 'println', Code04_ReadByLine.sum)
        jcall(out, 'flush')
        jcall(in_, 'close')
        jcall(out, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_ReadByLine.line = None
Code04_ReadByLine.parts = None
Code04_ReadByLine.sum = jcast('int', 0)

if __name__ == '__main__':
    Code04_ReadByLine.main([])

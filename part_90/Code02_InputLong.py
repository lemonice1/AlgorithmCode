# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 读入long类型数字的注意点
# 讲解019的扩展，没有看过讲解019的同学去看一下
class Code02_InputLong:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        Code02_InputLong.f1()
        Code02_InputLong.f2()

    @staticmethod
    def f1():
        jprint('f1函数测试读入', newline=True)
        # 尝试读入 : 131237128371723187
        # in.nval读出的是double类型
        # double类型64位
        # long类型也是64位
        # double的64位会分配若干位去表达小数部分
        # long类型的64位全用来表达整数部分
        # 所以读入是long范围的数，如果用以下的写法
        # in.nval会先变成double类型，如果再转成long类型，就可能有精度损耗
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        num = jcast('long', jcast('long', jget(in_, 'nval')))
        jcall(out, 'println', num)
        jcall(out, 'flush')

    @staticmethod
    def f2():
        jprint('f2函数测试读入', newline=True)
        # 尝试读入 : 131237128371723187
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        # 直接读出字符串
        str = jcall(br, 'readLine')
        # 然后把字符串转成long
        # 不可能有精度损耗
        num = jcast('long', jstatic('Long', 'valueOf', str))
        jcall(out, 'println', num)
        jcall(out, 'flush')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code02_InputLong.main([])

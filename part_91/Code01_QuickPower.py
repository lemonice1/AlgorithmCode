# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 乘法快速幂模版
# 求a的b次方，对p取模的结果
# 测试链接 : https://www.luogu.com.cn/problem/P1226
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_QuickPower:
    __java_fields__ = {'a': 'a', 'b': 'b', 'p': 'p'}
    a = 0
    b = 0
    p = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code01_QuickPower.a = jcast('long', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_QuickPower.b = jcast('long', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code01_QuickPower.p = jcast('long', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', jadd(jadd(jadd(jadd(jadd(jadd(Code01_QuickPower.a, '^'), Code01_QuickPower.b), ' mod '), Code01_QuickPower.p), '='), Code01_QuickPower.power()))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def power():
        ans = jcast('long', 1)
        while (Code01_QuickPower.b > 0):
            if (jcast('long', (Code01_QuickPower.b & 1)) == 1):
                ans = jcast('long', jcast('long', jmod(jcast('long', (ans * Code01_QuickPower.a)), Code01_QuickPower.p)))
            Code01_QuickPower.a = jcast('long', jcast('long', jmod(jcast('long', (Code01_QuickPower.a * Code01_QuickPower.a)), Code01_QuickPower.p)))
            Code01_QuickPower.b = jcast('long', jcast('long', (Code01_QuickPower.b >> (1 & 63))))
        return jcast('int', jcast('int', ans))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_QuickPower.a = jcast('long', 0)
Code01_QuickPower.b = jcast('long', 0)
Code01_QuickPower.p = jcast('long', 0)

if __name__ == '__main__':
    Code01_QuickPower.main([])

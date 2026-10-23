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

# 质数次方版取石子(巴什博弈扩展)
# 一共有n颗石子，两个人轮流拿
# 每一轮当前选手可以拿 p的k次方 颗石子
# 当前选手可以随意决定p和k，但要保证p是质数、k是自然数
# 拿到最后一颗石子的人获胜
# 根据石子数返回谁赢
# 如果先手赢，返回"October wins!"
# 如果后手赢，输出"Roy wins!"
# 测试链接 : https://www.luogu.com.cn/problem/P4018
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_PrimePowerStones:
    __java_fields__ = {'t': 't', 'n': 'n'}
    t = 0
    n = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_PrimePowerStones.t = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 0)
        while (i < Code02_PrimePowerStones.t):
            jcall(in_, 'nextToken')
            Code02_PrimePowerStones.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'println', Code02_PrimePowerStones.compute(Code02_PrimePowerStones.n))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute(n):
        n = jcast('int', n)
        return ('October wins!' if (jcast('int', jmod(n, 6)) != 0) else 'Roy wins!')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_PrimePowerStones.t = jcast('int', 0)
Code02_PrimePowerStones.n = jcast('int', 0)

if __name__ == '__main__':
    Code02_PrimePowerStones.main([])

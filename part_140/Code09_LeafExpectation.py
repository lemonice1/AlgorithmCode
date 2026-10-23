# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 叶子节点数的期望
# 一共有n个节点，认为节点之间无差别，能形成很多不同结构的二叉树
# 假设所有不同结构的二叉树，等概率出现一棵，返回叶子节点的期望
# 1 <= n <= 10^9
# 答案误差小于10的-9次方
# 测试链接 : https://www.luogu.com.cn/problem/P3978
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_LeafExpectation:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('double', jget(in_, 'nval'))
        jcall(out, 'printf', '%.9f', jdiv((n * jadd(n, 1)), (((2 * n) - 1) * 2)))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code09_LeafExpectation.main([])

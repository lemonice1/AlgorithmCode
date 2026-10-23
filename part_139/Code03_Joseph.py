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

# 约瑟夫环问题
# 一共有1~n这些点，组成首尾相接的环
# 从1号点从数字1开始报数，哪个节点报到数字k，就删除该节点
# 然后下一个节点从数字1开始重新报数，最终环上会剩下一个节点
# 返回该节点的编号
# 1 <= n, k <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P8671
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Joseph:
    __java_fields__ = {}
    @staticmethod
    def compute(n, k):
        n = jcast('int', n)
        k = jcast('int', k)
        ans = jcast('int', 1)
        c = jcast('int', 2)
        while (c <= n):
            ans = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', (jcast('int', jadd(ans, k)) - 1)), c)), 1)))
            c = jcast('int', (c + 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        k = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code03_Joseph.compute(n, k))
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_Joseph.main([])

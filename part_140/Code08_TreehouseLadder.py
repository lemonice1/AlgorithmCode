# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 树屋阶梯
# 地面高度是0，想搭建一个阶梯，要求每一个台阶上升1的高度，最终到达高度n
# 有无穷多任意规格的矩形材料，但是必须选择n个矩形，希望能搭建出阶梯的样子
# 返回搭建阶梯的不同方法数，答案可能很大，不取模！就打印真实答案
# 1 <= n <= 500
# 测试链接 : https://www.luogu.com.cn/problem/P2532
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_TreehouseLadder:
    __java_fields__ = {}
    # 这里用公式2
    # BigInteger 接口由基于 Python int 的任意精度整数实现兼容
    # 精确大整数乘法可使用 Python int，兼容接口保留原算法的调用方式
    @staticmethod
    def compute(n):
        n = jcast('int', n)
        a = jnew('BigInteger', '1')
        b = jnew('BigInteger', '1')
        cur = None
        i = jcast('int', 1)
        while (i <= jcast('int', (2 * n))):
            cur = jnew('BigInteger', jstatic('String', 'valueOf', i))
            a = jcall(a, 'multiply', cur)
            if (i <= n):
                b = jcall(b, 'multiply', cur)
            i = jcast('int', (i + 1))
        return jcall(jcall(a, 'divide', jcall(b, 'multiply', b)), 'divide', jnew('BigInteger', jstatic('String', 'valueOf', jcast('int', jadd(n, 1)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        n = jcast('int', jcast('int', jget(in_, 'nval')))
        ans = Code08_TreehouseLadder.compute(n)
        jcall(out, 'println', jcall(ans, 'toString'))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code08_TreehouseLadder.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 均匀生成器
# 如果有两个数字step和mod，那么可以由以下方式生成很多数字
# seed(1) = 0，seed(i+1) = (seed(i) + step) % mod
# 比如，step = 3、mod = 5
# seed(1) = 0，seed(2) = 3，seed(3) = 1，seed(4) = 4，seed(5) = 2
# 如果能产生0 ~ mod-1所有数字，step和mod的组合叫  "Good Choice"
# 如果无法产生0 ~ mod-1所有数字，step和mod的组合叫 "Bad Choice"
# 根据step和mod，打印结果
# 1 <= step、mod <= 10^5
# 测试链接 : http://poj.org/problem?id=1597
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_UniformGenerator:
    __java_fields__ = {}
    @staticmethod
    def gcd(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        return jcast('int', (a if (b == 0) else Code03_UniformGenerator.gcd(b, jcast('int', jmod(a, b)))))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            step = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            mod = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(out, 'print', jadd(jadd(jstatic('String', 'format', '%10d', step), jstatic('String', 'format', '%10d', mod)), '    '))
            jcall(out, 'println', ('Good Choice' if (Code03_UniformGenerator.gcd(step, mod) == 1) else 'Bad Choice'))
            jcall(out, 'println', ' ')
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code03_UniformGenerator.main([])

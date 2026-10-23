# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 范围内的数字计数
# 给定两个正整数a和b，求在[a,b]范围上的所有整数中
# 每个数码(digit)各出现了多少次
# 1 <= a, b
# 测试链接 : https://www.luogu.com.cn/problem/P2602
# 请同学们务必参考如下代码中关于输入、输出的处理
# 这是输入输出处理效率很高的写法
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_DigitCount2:
    __java_fields__ = {}
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            a = jcast('long', jcast('long', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            b = jcast('long', jcast('long', jget(in_, 'nval')))
            i = jcast('int', 0)
            while (i < 9):
                jcall(out, 'print', jadd(Code04_DigitCount2.digitsCount(i, a, b), ' '))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_DigitCount2.digitsCount(9, a, b))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def digitsCount(d, a, b):
        d = jcast('int', d)
        a = jcast('long', a)
        b = jcast('long', b)
        return jcast('long', jcast('long', (Code04_DigitCount2.count(b, d) - Code04_DigitCount2.count(jcast('long', (a - 1)), d))))

    @staticmethod
    def count(num, d):
        num = jcast('long', num)
        d = jcast('int', d)
        ans = jcast('long', 0)
        right = jcast('long', 1)
        tmp = jcast('long', num)
        left = 0
        cur = 0
        while (tmp != 0):
            left = jcast('long', jcast('long', jdiv(tmp, 10)))
            if (d == 0):
                left = jcast('long', (left - 1))
            ans = jcast('long', jcast('long', jadd(ans, jcast('long', (left * right)))))
            cur = jcast('long', jcast('long', jmod(tmp, 10)))
            if (cur > d):
                ans = jcast('long', jcast('long', jadd(ans, right)))
            else:
                if (cur == d):
                    ans = jcast('long', jcast('long', jadd(ans, jcast('long', jadd(jcast('long', jmod(num, right)), 1)))))
            right = jcast('long', jcast('long', (right * 10)))
            tmp = jcast('long', jcast('long', jdiv(tmp, 10)))
        return jcast('long', ans)

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')



if __name__ == '__main__':
    Code04_DigitCount2.main([])

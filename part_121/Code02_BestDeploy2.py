# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 感谢热心的同学，找到了题目2的在线测试
# 最好的部署
# 一共有n台机器，编号1 ~ n，所有机器排成一排
# 你只能一台一台的部署机器，你可以决定部署的顺序，最终所有机器都要部署
# 给定三个长度为n的数组a[]、b[]、c[]
# a[i] : 如果i号机器部署时，相邻有0台机器部署，此时能获得的收益
# b[i] : 如果i号机器部署时，相邻有1台机器部署，此时能获得的收益
# c[i] : 如果i号机器部署时，相邻有2台机器部署，此时能获得的收益
# 第1号机器、第n号机器当然不会有两台相邻的机器
# 返回部署的最大收益
# 1 <= n、a[i]、b[i]、c[i] <= 10^4
# 测试链接 : https://vjudge.net/problem/OpenJ_Bailian-4150
# 测试链接 : http://bailian.openjudge.cn/practice/4150/
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BestDeploy2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'a': 'a', 'b': 'b', 'c': 'c'}
    MAXN = 0
    n = 0
    a = None
    b = None
    c = None
    # 课上讲的时间复杂度O(n)的方法
    # 逻辑没有任何修改
    @staticmethod
    def compute():
        dp = jarray('int', [jcast('int', jadd(Code02_BestDeploy2.n, 1)), 2])
        jset(dp[Code02_BestDeploy2.n], 0, Code02_BestDeploy2.a[Code02_BestDeploy2.n])
        jset(dp[Code02_BestDeploy2.n], 1, Code02_BestDeploy2.b[Code02_BestDeploy2.n])
        i = jcast('int', jcast('int', (Code02_BestDeploy2.n - 1)))
        while (i >= 1):
            jset(dp[i], 0, jstatic('Math', 'max', jcast('int', jadd(Code02_BestDeploy2.a[i], dp[jcast('int', jadd(i, 1))][1])), jcast('int', jadd(Code02_BestDeploy2.b[i], dp[jcast('int', jadd(i, 1))][0]))))
            jset(dp[i], 1, jstatic('Math', 'max', jcast('int', jadd(Code02_BestDeploy2.b[i], dp[jcast('int', jadd(i, 1))][1])), jcast('int', jadd(Code02_BestDeploy2.c[i], dp[jcast('int', jadd(i, 1))][0]))))
            i = jcast('int', (i - 1))
        return jcast('int', dp[1][0])

    @staticmethod
    def main(args):
        in_ = Code02_BestDeploy2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_BestDeploy2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_BestDeploy2.n):
            jset(Code02_BestDeploy2.a, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_BestDeploy2.n):
            jset(Code02_BestDeploy2.b, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_BestDeploy2.n):
            jset(Code02_BestDeploy2.c, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code02_BestDeploy2.compute())
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len', 'in': 'in_'}
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        def _java_init_0(self, in_):
            self.in_ = in_

        def readByte(self):
            if (self.ptr >= self.len):
                self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
                self.ptr = jcast('int', 0)
                if (self.len <= 0):
                    return jcast('int', jcast('int', (-1)))
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

        def nextInt(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('int', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('int', jcast('int', jadd(jcast('int', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('int', (jcast('int', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_BestDeploy2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BestDeploy2.MAXN = jcast('int', 10002)
Code02_BestDeploy2.n = jcast('int', 0)
Code02_BestDeploy2.a = jarray('int', [Code02_BestDeploy2.MAXN])
Code02_BestDeploy2.b = jarray('int', [Code02_BestDeploy2.MAXN])
Code02_BestDeploy2.c = jarray('int', [Code02_BestDeploy2.MAXN])

if __name__ == '__main__':
    Code02_BestDeploy2.main([])

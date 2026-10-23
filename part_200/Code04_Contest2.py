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

# 确定能力，Python版
# 一共n头奶牛，编号为1~n，每头奶牛的能力互不相同
# 给定m条已知关系，格式 a b，表示a的能力强于b
# 能力关系具有传递性，如果a强于b，b强于c，那么a强于c
# 题目保证没有矛盾，根据已知关系，希望确定奶牛的排名
# 计算有多少头奶牛的具体名次已经能够确定，打印这个数量
# 1 <= n <= 100
# 1 <= m <= 4500
# 测试链接 : https://www.luogu.com.cn/problem/P2419
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Contest2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'dp': 'dp', 'cnt': 'cnt'}
    MAXN = 0
    n = 0
    m = 0
    dp = None
    cnt = None
    @staticmethod
    def floyd():
        bridge = jcast('int', 1)
        while (bridge <= Code04_Contest2.n):
            i = jcast('int', 1)
            while (i <= Code04_Contest2.n):
                if jcall(Code04_Contest2.dp[i], 'get', bridge):
                    jcall(Code04_Contest2.dp[i], 'or', Code04_Contest2.dp[bridge])
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    @staticmethod
    def main(args):
        in_ = Code04_Contest2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Contest2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Contest2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Contest2.n):
            jset(Code04_Contest2.dp, i, jnew('BitSet', jcast('int', jadd(Code04_Contest2.n, 1))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        a = 0
        b = 0
        while (i <= Code04_Contest2.m):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            jcall(Code04_Contest2.dp[a], 'set', b)
            i = jcast('int', (i + 1))
        Code04_Contest2.floyd()
        i = jcast('int', 1)
        while (i <= Code04_Contest2.n):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j <= Code04_Contest2.n):
                if (jcall(Code04_Contest2.dp[i], 'get', j) or jcall(Code04_Contest2.dp[j], 'get', i)):
                    Code04_Contest2.cnt[i] = jcast('int', (Code04_Contest2.cnt[i] + 1))
                    Code04_Contest2.cnt[j] = jcast('int', (Code04_Contest2.cnt[j] + 1))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Contest2.n):
            if (Code04_Contest2.cnt[i] == jcast('int', (Code04_Contest2.n - 1))):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        jcall(out, 'println', ans)
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
            raise TypeError("No matching overload for Code04_Contest2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Contest2.MAXN = jcast('int', 101)
Code04_Contest2.n = jcast('int', 0)
Code04_Contest2.m = jcast('int', 0)
Code04_Contest2.dp = jarray('BitSet', [Code04_Contest2.MAXN])
Code04_Contest2.cnt = jarray('int', [Code04_Contest2.MAXN])

if __name__ == '__main__':
    Code04_Contest2.main([])

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

# 排序步骤的实际开销取决于数据规模与 Python 实现，应结合算法复杂度评估
# 一共n个元素，用大写字母 A、B、C... 表示，元素的值互不相同
# 给定m条大小关系，格式为 A<B，表示A的值小于B，大小关系具有传递性
# 按输入顺序逐条考虑这些关系，判断以下情况
# 如果首次在前k条关系后，已经能唯一确定完整排名，输出k和升序序列，然后结束
# 输出 Sorted sequence determined after {k} relations: {升序序列}.
# 如果首次在前k条关系后，发现了矛盾，那么停止判断，不再考虑后续的关系
# 输出 Inconsistency found after {k} relations.
# 如果考察完所有m条关系，仍然没有矛盾，但无法唯一确定完整排名
# 输出 Sorted sequence cannot be determined.
# 2 <= n <= 26    1 <= m <= 600
# 测试链接 : https://www.luogu.com.cn/problem/P1347
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Sorting1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'dp': 'dp', 'ans': 'ans', 'kth': 'kth', 'order': 'order'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    a = None
    b = None
    dp = None
    ans = 0
    kth = 0
    order = None
    @staticmethod
    def floyd():
        bridge = jcast('int', 1)
        while (bridge <= Code07_Sorting1.n):
            i = jcast('int', 1)
            while (i <= Code07_Sorting1.n):
                if jcall(Code07_Sorting1.dp[i], 'get', bridge):
                    jcall(Code07_Sorting1.dp[i], 'or', Code07_Sorting1.dp[bridge])
                i = jcast('int', (i + 1))
            bridge = jcast('int', (bridge + 1))

    # 顺序未确定返回0，顺序确定返回1，出现矛盾返回2
    @staticmethod
    def check():
        i = jcast('int', 1)
        while (i <= Code07_Sorting1.n):
            if jcall(Code07_Sorting1.dp[i], 'get', i):
                return jcast('int', 2)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Sorting1.n):
            j = jcast('int', jcast('int', jadd(i, 1)))
            while (j <= Code07_Sorting1.n):
                if ((not jcall(Code07_Sorting1.dp[i], 'get', j)) and (not jcall(Code07_Sorting1.dp[j], 'get', i))):
                    return jcast('int', 0)
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', 1)

    @staticmethod
    def compute():
        Code07_Sorting1.ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code07_Sorting1.m):
            try:
                jcall(Code07_Sorting1.dp[Code07_Sorting1.a[i]], 'set', Code07_Sorting1.b[i])
                Code07_Sorting1.floyd()
                Code07_Sorting1.ans = jcast('int', Code07_Sorting1.check())
                if ((Code07_Sorting1.ans == 1) or (Code07_Sorting1.ans == 2)):
                    Code07_Sorting1.kth = jcast('int', i)
                    raise JBreak(None)
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (Code07_Sorting1.ans == 1):
            i = jcast('int', 1)
            while (i <= Code07_Sorting1.n):
                jset(Code07_Sorting1.order, (Code07_Sorting1.n - jcall(Code07_Sorting1.dp[i], 'cardinality')), jcast('char', jcast('int', (jcast('int', jadd(jchar('A'), i)) - 1))))
                i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_Sorting1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Sorting1.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Sorting1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Sorting1.n):
            jset(Code07_Sorting1.dp, i, jnew('BitSet', jcast('int', jadd(Code07_Sorting1.n, 1))))
            i = jcast('int', (i + 1))
        s1 = jchar(0)
        s2 = jchar(0)
        i = jcast('int', 1)
        while (i <= Code07_Sorting1.m):
            s1 = jcast('char', jcall(in_, 'nextChar'))
            jcall(in_, 'nextChar')
            s2 = jcast('char', jcall(in_, 'nextChar'))
            Code07_Sorting1.a[i] = jcast('int', jcast('int', jadd(jcast('int', (s1 - jchar('A'))), 1)))
            Code07_Sorting1.b[i] = jcast('int', jcast('int', jadd(jcast('int', (s2 - jchar('A'))), 1)))
            i = jcast('int', (i + 1))
        Code07_Sorting1.compute()
        if (Code07_Sorting1.ans == 0):
            jcall(out, 'println', 'Sorted sequence cannot be determined.')
        else:
            if (Code07_Sorting1.ans == 1):
                jcall(out, 'print', jadd(jadd('Sorted sequence determined after ', Code07_Sorting1.kth), ' relations: '))
                i = jcast('int', 1)
                while (i <= Code07_Sorting1.n):
                    jcall(out, 'print', Code07_Sorting1.order[i])
                    i = jcast('int', (i + 1))
                jcall(out, 'println', '.')
            else:
                jcall(out, 'println', jadd(jadd('Inconsistency found after ', Code07_Sorting1.kth), ' relations.'))
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
            return jcast('int', self.buffer[((_java_obj_2 := self), (_java_key_3 := 'ptr'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            return jcast('char', jcast('char', c))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code07_Sorting1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Sorting1.MAXN = jcast('int', 27)
Code07_Sorting1.MAXM = jcast('int', 601)
Code07_Sorting1.n = jcast('int', 0)
Code07_Sorting1.m = jcast('int', 0)
Code07_Sorting1.a = jarray('int', [Code07_Sorting1.MAXM])
Code07_Sorting1.b = jarray('int', [Code07_Sorting1.MAXM])
Code07_Sorting1.dp = jarray('BitSet', [Code07_Sorting1.MAXN])
Code07_Sorting1.ans = jcast('int', 0)
Code07_Sorting1.kth = jcast('int', 0)
Code07_Sorting1.order = jarray('char', [Code07_Sorting1.MAXN])

if __name__ == '__main__':
    Code07_Sorting1.main([])

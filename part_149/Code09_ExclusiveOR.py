# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 异或关系
# 一共n个数，编号0 ~ n-1，实现如下三种类型的操作，一共调用m次
# I x v        : 声明 第x个数 = v
# I x y v      : 声明 第x个数 ^ 第y个数 = v
# Q k a1 .. ak : 查询 一共k个数，编号为a1 .. ak，这些数字异或起来的值是多少
# 对每个Q的操作打印答案，如果根据之前的声明无法推出答案，打印"I don't know."
# 如果处理到第s条声明，发现了矛盾，打印"The first s facts are conflicting."
# 注意只有声明操作出现，s才会增加，查询操作不占用声明操作的计数
# 发现矛盾之后，所有的操作都不再处理，更多的细节可以打开测试链接查看题目
# 1 <= n <= 20000    1 <= m <= 40000    1 <= k <= 15
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=3234
# 测试链接 : https://www.luogu.com.cn/problem/UVA12232
# 测试链接 : https://vjudge.net/problem/UVA-12232
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code09_ExclusiveOR:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXK': 'MAXK', 't': 't', 'n': 'n', 'm': 'm', 'conflict': 'conflict', 'cnti': 'cnti', 'father': 'father', 'exclu': 'exclu', 'nums': 'nums', 'fas': 'fas'}
    MAXN = 0
    MAXK = 0
    t = 0
    n = 0
    m = 0
    conflict = False
    cnti = 0
    father = None
    exclu = None
    nums = None
    fas = None
    @staticmethod
    def prepare():
        Code09_ExclusiveOR.conflict = jcast('boolean', False)
        Code09_ExclusiveOR.cnti = jcast('int', 0)
        i = jcast('int', 0)
        while (i <= Code09_ExclusiveOR.n):
            Code09_ExclusiveOR.father[i] = jcast('int', i)
            Code09_ExclusiveOR.exclu[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code09_ExclusiveOR.father[i]):
            tmp = jcast('int', Code09_ExclusiveOR.father[i])
            jset(Code09_ExclusiveOR.father, i, Code09_ExclusiveOR.find(tmp))
            Code09_ExclusiveOR.exclu[i] = jcast('int', jcast('int', (Code09_ExclusiveOR.exclu[i] ^ Code09_ExclusiveOR.exclu[tmp])))
        return jcast('int', Code09_ExclusiveOR.father[i])

    @staticmethod
    def opi(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        Code09_ExclusiveOR.cnti = jcast('int', (Code09_ExclusiveOR.cnti + 1))
        lf = jcast('int', Code09_ExclusiveOR.find(l))
        rf = jcast('int', Code09_ExclusiveOR.find(r))
        if (lf == rf):
            if (jcast('int', (Code09_ExclusiveOR.exclu[l] ^ Code09_ExclusiveOR.exclu[r])) != v):
                Code09_ExclusiveOR.conflict = jcast('boolean', True)
                return jcast('boolean', False)
        else:
            if (lf == Code09_ExclusiveOR.n):
                lf = jcast('int', rf)
                rf = jcast('int', Code09_ExclusiveOR.n)
            Code09_ExclusiveOR.father[lf] = jcast('int', rf)
            Code09_ExclusiveOR.exclu[lf] = jcast('int', jcast('int', (jcast('int', (Code09_ExclusiveOR.exclu[r] ^ Code09_ExclusiveOR.exclu[l])) ^ v)))
        return jcast('boolean', True)

    @staticmethod
    def opq(k):
        k = jcast('int', k)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        fa = 0
        while (i <= k):
            fa = jcast('int', Code09_ExclusiveOR.find(Code09_ExclusiveOR.nums[i]))
            ans = jcast('int', jcast('int', (ans ^ Code09_ExclusiveOR.exclu[Code09_ExclusiveOR.nums[i]])))
            Code09_ExclusiveOR.fas[i] = jcast('int', fa)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code09_ExclusiveOR.fas, 1, jcast('int', jadd(k, 1)))
        l = jcast('int', 1)
        r = jcast('int', 1)
        while (l <= k):
            while ((jcast('int', jadd(r, 1)) <= k) and (Code09_ExclusiveOR.fas[jcast('int', jadd(r, 1))] == Code09_ExclusiveOR.fas[l])):
                r = jcast('int', (r + 1))
            if ((jcast('int', jmod(jcast('int', jadd(jcast('int', (r - l)), 1)), 2)) != 0) and (Code09_ExclusiveOR.fas[l] != Code09_ExclusiveOR.n)):
                return jcast('int', jcast('int', (-1)))
            l = jcast('int', (r := jcast('int', (r + (1)))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code09_ExclusiveOR.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code09_ExclusiveOR.t = jcast('int', 0)
        Code09_ExclusiveOR.n = jcast('int', jcall(in_, 'nextInt'))
        Code09_ExclusiveOR.m = jcast('int', jcall(in_, 'nextInt'))
        while ((Code09_ExclusiveOR.n != 0) or (Code09_ExclusiveOR.m != 0)):
            Code09_ExclusiveOR.prepare()
            jcall(out, 'println', jadd(jadd('Case ', ((_java_obj_1 := Code09_ExclusiveOR), (_java_key_2 := 't'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]), ':'))
            i = jcast('int', 1)
            while (i <= Code09_ExclusiveOR.m):
                op = jcall(in_, 'next')
                if jcall(op, 'equals', 'I'):
                    l = 0
                    r = 0
                    v = 0
                    jcall(in_, 'numbers')
                    if (not Code09_ExclusiveOR.conflict):
                        if (jget(in_, 'size') == 2):
                            l = jcast('int', jget(in_, 'a'))
                            r = jcast('int', Code09_ExclusiveOR.n)
                            v = jcast('int', jget(in_, 'b'))
                        else:
                            l = jcast('int', jget(in_, 'a'))
                            r = jcast('int', jget(in_, 'b'))
                            v = jcast('int', jget(in_, 'c'))
                        if (not Code09_ExclusiveOR.opi(l, r, v)):
                            jcall(out, 'println', jadd(jadd('The first ', Code09_ExclusiveOR.cnti), ' facts are conflicting.'))
                else:
                    k = jcast('int', jcall(in_, 'nextInt'))
                    j = jcast('int', 1)
                    while (j <= k):
                        jset(Code09_ExclusiveOR.nums, j, jcall(in_, 'nextInt'))
                        j = jcast('int', (j + 1))
                    if (not Code09_ExclusiveOR.conflict):
                        ans = jcast('int', Code09_ExclusiveOR.opq(k))
                        if (ans == jcast('int', (-1))):
                            jcall(out, 'println', "I don't know.")
                        else:
                            jcall(out, 'println', ans)
                i = jcast('int', (i + 1))
            jcall(out, 'println')
            Code09_ExclusiveOR.n = jcast('int', jcall(in_, 'nextInt'))
            Code09_ExclusiveOR.m = jcast('int', jcall(in_, 'nextInt'))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(in_, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'pointer': 'pointer', 'bytesRead': 'bytesRead', 'a': 'a', 'b': 'b', 'c': 'c', 'size': 'size'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # pointer：实例字段，在构造函数中初始化。
        # bytesRead：实例字段，在构造函数中初始化。
        # a：实例字段，在构造函数中初始化。
        # b：实例字段，在构造函数中初始化。
        # c：实例字段，在构造函数中初始化。
        # size：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.pointer = jcast('int', jset(self, 'bytesRead', 0))

        def read(self):
            if (self.pointer >= self.bytesRead):
                self.fillBuffer()
                if (self.bytesRead == jcast('int', (-1))):
                    return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'pointer'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        def fillBuffer(self):
            self.bytesRead = jcast('int', jcall(self.in_, 'read', self.buffer, 0, self.BUFFER_SIZE))
            self.pointer = jcast('int', 0)

        def skipWhiteSpace(self):
            c = 0
            while ((c := self.read()) != jcast('int', (-1))):
                try:
                    if (c > jchar(' ')):
                        self.pointer = jcast('int', (self.pointer - 1))
                        raise JBreak(None)
                except JContinue as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                except JBreak as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                    break

        def readLine(self):
            sb = jnew('StringBuilder')
            while True:
                try:
                    c = jcast('byte', self.read())
                    if ((c == jcast('int', (-1))) or (c == jchar('\n'))):
                        raise JBreak(None)
                    if (c == jchar('\r')):
                        nextc = jcast('byte', self.read())
                        if (nextc != jchar('\n')):
                            self.pointer = jcast('int', (self.pointer - 1))
                        raise JBreak(None)
                    jcall(sb, 'append', jcast('char', c))
                except JContinue as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                except JBreak as _java_control_8:
                    if _java_control_8.label not in (None,):
                        raise
                    break
            if ((jcall(sb, 'length') == 0) and (self.bytesRead == jcast('int', (-1)))):
                return None
            return jcall(sb, 'toString')

        def next(self):
            self.skipWhiteSpace()
            if (self.bytesRead == jcast('int', (-1))):
                return None
            sb = jnew('StringBuilder')
            c = jcast('byte', self.read())
            while ((c != jcast('int', (-1))) and (c > jchar(' '))):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.read())
            return jcall(sb, 'toString')

        def nextInt(self):
            self.skipWhiteSpace()
            if (self.bytesRead == jcast('int', (-1))):
                raise jnew('IOException', 'No more data to read (EOF)')
            negative = jcast('boolean', False)
            result = jcast('int', 0)
            c = jcast('byte', self.read())
            if (c == jchar('-')):
                negative = jcast('boolean', True)
                c = jcast('byte', self.read())
            while ((c >= jchar('0')) and (c <= jchar('9'))):
                result = jcast('int', jcast('int', jadd(jcast('int', (result * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('byte', self.read())
            if ((c != jcast('int', (-1))) and (c > jchar(' '))):
                self.pointer = jcast('int', (self.pointer - 1))
            return jcast('int', (jcast('int', (-result)) if negative else result))

        def numbers(self):
            self.a = jcast('int', jset(self, 'b', jset(self, 'c', jset(self, 'size', 0))))
            line = self.readLine()
            if (line == None):
                return
            parts = jcall(jcall(line, 'trim'), 'split', '\\s+')
            if (jget(parts, 'length') == 0):
                return
            self.size = jcast('int', jstatic('Math', 'min', jget(parts, 'length'), 3))
            if (self.size >= 1):
                self.a = jcast('int', jstatic('Integer', 'parseInt', parts[0]))
            if (self.size >= 2):
                self.b = jcast('int', jstatic('Integer', 'parseInt', parts[1]))
            if (self.size >= 3):
                self.c = jcast('int', jstatic('Integer', 'parseInt', parts[2]))

        def close(self):
            if (self.in_ != None):
                jcall(self.in_, 'close')

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.pointer = jcast('int', 0)
            self.bytesRead = jcast('int', 0)
            self.a = jcast('int', 0)
            self.b = jcast('int', 0)
            self.c = jcast('int', 0)
            self.size = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code09_ExclusiveOR.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code09_ExclusiveOR.MAXN = jcast('int', 20002)
Code09_ExclusiveOR.MAXK = jcast('int', 21)
Code09_ExclusiveOR.t = jcast('int', 0)
Code09_ExclusiveOR.n = jcast('int', 0)
Code09_ExclusiveOR.m = jcast('int', 0)
Code09_ExclusiveOR.conflict = jcast('boolean', False)
Code09_ExclusiveOR.cnti = jcast('int', 0)
Code09_ExclusiveOR.father = jarray('int', [Code09_ExclusiveOR.MAXN])
Code09_ExclusiveOR.exclu = jarray('int', [Code09_ExclusiveOR.MAXN])
Code09_ExclusiveOR.nums = jarray('int', [Code09_ExclusiveOR.MAXK])
Code09_ExclusiveOR.fas = jarray('int', [Code09_ExclusiveOR.MAXK])

if __name__ == '__main__':
    Code09_ExclusiveOR.main([])

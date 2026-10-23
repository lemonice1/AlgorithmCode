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

# 教主的魔法，Python版
# 给定一个长度为n的数组arr，接下来有m条操作，每条操作是如下两种类型中的一种
# 操作 A l r v : 打印arr[l..r]范围上>=v的数字个数
# 操作 M l r v : 把arr[l..r]范围上每个值都加上v
# 1 <= n <= 10^6
# 1 <= m <= 3000
# 1 <= 数组中的值 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P2801
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Magic2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'lazy': 'lazy'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    sortv = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    lazy = None
    @staticmethod
    def build():
        Code02_Magic2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_Magic2.n)))
        Code02_Magic2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code02_Magic2.n, Code02_Magic2.blen)) - 1)), Code02_Magic2.blen)))
        i = jcast('int', 1)
        while (i <= Code02_Magic2.n):
            Code02_Magic2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code02_Magic2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Magic2.bnum):
            Code02_Magic2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code02_Magic2.blen)), 1)))
            jset(Code02_Magic2.br, i, jstatic('Math', 'min', jcast('int', (i * Code02_Magic2.blen)), Code02_Magic2.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Magic2.n):
            Code02_Magic2.sortv[i] = jcast('int', Code02_Magic2.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Magic2.bnum):
            jstatic('Arrays', 'sort', Code02_Magic2.sortv, Code02_Magic2.bl[i], jcast('int', jadd(Code02_Magic2.br[i], 1)))
            i = jcast('int', (i + 1))

    @staticmethod
    def getCnt(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        v = jcast('int', jcast('int', (v - Code02_Magic2.lazy[i])))
        l = jcast('int', Code02_Magic2.bl[i])
        r = jcast('int', Code02_Magic2.br[i])
        m = 0
        ans = jcast('int', 0)
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_Magic2.sortv[m] >= v):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', jadd(jcast('int', (r - m)), 1)))))
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def innerQuery(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        v = jcast('int', jcast('int', (v - Code02_Magic2.lazy[Code02_Magic2.bi[l]])))
        ans = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code02_Magic2.arr[i] >= v):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def query(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        ans = jcast('int', 0)
        if (Code02_Magic2.bi[l] == Code02_Magic2.bi[r]):
            ans = jcast('int', Code02_Magic2.innerQuery(l, r, v))
        else:
            ans = jcast('int', jcast('int', jadd(ans, Code02_Magic2.innerQuery(l, Code02_Magic2.br[Code02_Magic2.bi[l]], v))))
            ans = jcast('int', jcast('int', jadd(ans, Code02_Magic2.innerQuery(Code02_Magic2.bl[Code02_Magic2.bi[r]], r, v))))
            i = jcast('int', jcast('int', jadd(Code02_Magic2.bi[l], 1)))
            while (i <= jcast('int', (Code02_Magic2.bi[r] - 1))):
                ans = jcast('int', jcast('int', jadd(ans, Code02_Magic2.getCnt(i, v))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def innerAdd(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        i = jcast('int', l)
        while (i <= r):
            Code02_Magic2.arr[i] = jcast('int', jcast('int', jadd(Code02_Magic2.arr[i], v)))
            i = jcast('int', (i + 1))
        i = jcast('int', Code02_Magic2.bl[Code02_Magic2.bi[l]])
        while (i <= Code02_Magic2.br[Code02_Magic2.bi[l]]):
            Code02_Magic2.sortv[i] = jcast('int', Code02_Magic2.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_Magic2.sortv, Code02_Magic2.bl[Code02_Magic2.bi[l]], jcast('int', jadd(Code02_Magic2.br[Code02_Magic2.bi[l]], 1)))

    @staticmethod
    def add(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        if (Code02_Magic2.bi[l] == Code02_Magic2.bi[r]):
            Code02_Magic2.innerAdd(l, r, v)
        else:
            Code02_Magic2.innerAdd(l, Code02_Magic2.br[Code02_Magic2.bi[l]], v)
            Code02_Magic2.innerAdd(Code02_Magic2.bl[Code02_Magic2.bi[r]], r, v)
            i = jcast('int', jcast('int', jadd(Code02_Magic2.bi[l], 1)))
            while (i <= jcast('int', (Code02_Magic2.bi[r] - 1))):
                Code02_Magic2.lazy[i] = jcast('int', jcast('int', jadd(Code02_Magic2.lazy[i], v)))
                i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_Magic2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Magic2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Magic2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Magic2.n):
            jset(Code02_Magic2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_Magic2.build()
        op = jchar(0)
        l = 0
        r = 0
        v = 0
        i = jcast('int', 1)
        while (i <= Code02_Magic2.m):
            op = jcast('char', jcall(in_, 'nextChar'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            if (op == jchar('A')):
                jcall(out, 'println', Code02_Magic2.query(l, r, v))
            else:
                Code02_Magic2.add(l, r, v)
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        # BUFFER_SIZE：实例字段，在构造函数中初始化。
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [self.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not ((c <= jchar(' '))):
                    break
            ans = jcast('char', 0)
            while (c > jchar(' ')):
                ans = jcast('char', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcast('char', ans)

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_Magic2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Magic2.MAXN = jcast('int', 1000001)
Code02_Magic2.MAXB = jcast('int', 1001)
Code02_Magic2.n = jcast('int', 0)
Code02_Magic2.m = jcast('int', 0)
Code02_Magic2.arr = jarray('int', [Code02_Magic2.MAXN])
Code02_Magic2.sortv = jarray('int', [Code02_Magic2.MAXN])
Code02_Magic2.blen = jcast('int', 0)
Code02_Magic2.bnum = jcast('int', 0)
Code02_Magic2.bi = jarray('int', [Code02_Magic2.MAXN])
Code02_Magic2.bl = jarray('int', [Code02_Magic2.MAXB])
Code02_Magic2.br = jarray('int', [Code02_Magic2.MAXB])
Code02_Magic2.lazy = jarray('int', [Code02_Magic2.MAXB])

if __name__ == '__main__':
    Code02_Magic2.main([])

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

# 最大异或和，Python版
# 非负序列arr的初始长度为n，一共有m条操作，每条操作是如下两种类型中的一种
# A x     : arr的末尾增加数字x，arr的长度n也增加1
# Q l r x : l~r这些位置中，选一个位置p，现在希望
# arr[p] ^ arr[p+1] ^ .. ^ arr[n] ^ x 这个值最大
# 打印这个最大值
# 1 <= n、m <= 3 * 10^5
# 0 <= arr[i]、x <= 10^7
# 因为练的就是可持久化前缀树，所以就用在线算法，不要使用离线算法
# 测试链接 : https://www.luogu.com.cn/problem/P4735
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_MaxXor2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'BIT': 'BIT', 'n': 'n', 'm': 'm', 'eor': 'eor', 'root': 'root', 'tree': 'tree', 'pass': 'pass_', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    BIT = 0
    n = 0
    m = 0
    eor = 0
    root = None
    tree = None
    pass_ = None
    cnt = 0
    @staticmethod
    def insert(num, i):
        num = jcast('int', num)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_1 := Code01_MaxXor2), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        jset(Code01_MaxXor2.tree[rt], 0, Code01_MaxXor2.tree[i][0])
        jset(Code01_MaxXor2.tree[rt], 1, Code01_MaxXor2.tree[i][1])
        Code01_MaxXor2.pass_[rt] = jcast('int', jcast('int', jadd(Code01_MaxXor2.pass_[i], 1)))
        b = jcast('int', Code01_MaxXor2.BIT)
        path = 0
        pre = jcast('int', rt)
        cur = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            i = jcast('int', Code01_MaxXor2.tree[i][path])
            cur = jcast('int', ((_java_obj_4 := Code01_MaxXor2), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
            jset(Code01_MaxXor2.tree[cur], 0, Code01_MaxXor2.tree[i][0])
            jset(Code01_MaxXor2.tree[cur], 1, Code01_MaxXor2.tree[i][1])
            Code01_MaxXor2.pass_[cur] = jcast('int', jcast('int', jadd(Code01_MaxXor2.pass_[i], 1)))
            jset(Code01_MaxXor2.tree[pre], path, cur)
            b = jcast('int', (b - 1))
            pre = jcast('int', cur)
        return jcast('int', rt)

    @staticmethod
    def query(num, u, v):
        num = jcast('int', num)
        u = jcast('int', u)
        v = jcast('int', v)
        ans = jcast('int', 0)
        b = jcast('int', Code01_MaxXor2.BIT)
        path = 0
        best = 0
        while (b >= 0):
            path = jcast('int', jcast('int', (jcast('int', (num >> (b & 31))) & 1)))
            best = jcast('int', jcast('int', (path ^ 1)))
            if (Code01_MaxXor2.pass_[Code01_MaxXor2.tree[v][best]] > Code01_MaxXor2.pass_[Code01_MaxXor2.tree[u][best]]):
                ans = jcast('int', jcast('int', jadd(ans, jcast('int', (1 << (b & 31))))))
                u = jcast('int', Code01_MaxXor2.tree[u][best])
                v = jcast('int', Code01_MaxXor2.tree[v][best])
            else:
                u = jcast('int', Code01_MaxXor2.tree[u][path])
                v = jcast('int', Code01_MaxXor2.tree[v][path])
            b = jcast('int', (b - 1))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code01_MaxXor2.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MaxXor2.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_MaxXor2.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_MaxXor2.eor = jcast('int', 0)
        # 其实有空版本，空版本的头节点编号是0
        jset(Code01_MaxXor2.root, 0, Code01_MaxXor2.insert(Code01_MaxXor2.eor, 0))
        i = jcast('int', 1)
        num = 0
        while (i <= Code01_MaxXor2.n):
            num = jcast('int', jcall(in_, 'nextInt'))
            Code01_MaxXor2.eor = jcast('int', jcast('int', (Code01_MaxXor2.eor ^ num)))
            jset(Code01_MaxXor2.root, i, Code01_MaxXor2.insert(Code01_MaxXor2.eor, Code01_MaxXor2.root[jcast('int', (i - 1))]))
            i = jcast('int', (i + 1))
        op = None
        x = 0
        y = 0
        z = 0
        i = jcast('int', 1)
        while (i <= Code01_MaxXor2.m):
            op = jcall(in_, 'next')
            if jcall(op, 'equals', 'A'):
                x = jcast('int', jcall(in_, 'nextInt'))
                Code01_MaxXor2.eor = jcast('int', jcast('int', (Code01_MaxXor2.eor ^ x)))
                Code01_MaxXor2.n = jcast('int', (Code01_MaxXor2.n + 1))
                jset(Code01_MaxXor2.root, Code01_MaxXor2.n, Code01_MaxXor2.insert(Code01_MaxXor2.eor, Code01_MaxXor2.root[jcast('int', (Code01_MaxXor2.n - 1))]))
            else:
                # l
                x = jcast('int', jcall(in_, 'nextInt'))
                # r
                y = jcast('int', jcall(in_, 'nextInt'))
                # x
                z = jcast('int', jcall(in_, 'nextInt'))
                if (x == 1):
                    jcall(out, 'println', Code01_MaxXor2.query(jcast('int', (Code01_MaxXor2.eor ^ z)), 0, Code01_MaxXor2.root[jcast('int', (y - 1))]))
                else:
                    jcall(out, 'println', Code01_MaxXor2.query(jcast('int', (Code01_MaxXor2.eor ^ z)), Code01_MaxXor2.root[jcast('int', (x - 2))], Code01_MaxXor2.root[jcast('int', (y - 1))]))
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
            return jcast('byte', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

        def hasNext(self):
            while self.hasNextByte():
                b = jcast('byte', self.buffer[self.ptr])
                if (not self.isWhitespace(b)):
                    return jcast('boolean', True)
                self.ptr = jcast('int', (self.ptr + 1))
            return jcast('boolean', False)

        def next(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return None
                if not ((c <= jchar(' '))):
                    break
            sb = jnew('StringBuilder')
            while (c > jchar(' ')):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

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

        def nextDouble(self):
            num = jcast('double', 0)
            div = jcast('double', 1)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while (((not self.isWhitespace(b)) and (b != jchar('.'))) and (b != jcast('int', (-1)))):
                num = jcast('double', jadd((num * 10), jcast('int', (b - jchar('0')))))
                b = jcast('byte', self.readByte())
            if (b == jchar('.')):
                b = jcast('byte', self.readByte())
                while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                    num = jcast('double', jadd(num, jdiv(jcast('int', (b - jchar('0'))), (div := (div * 10)))))
                    b = jcast('byte', self.readByte())
            return jcast('double', ((-num) if minus else num))

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
            raise TypeError("No matching overload for Code01_MaxXor2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MaxXor2.MAXN = jcast('int', 600001)
Code01_MaxXor2.MAXT = jcast('int', jcast('int', (Code01_MaxXor2.MAXN * 22)))
Code01_MaxXor2.BIT = jcast('int', 25)
Code01_MaxXor2.n = jcast('int', 0)
Code01_MaxXor2.m = jcast('int', 0)
Code01_MaxXor2.eor = jcast('int', 0)
Code01_MaxXor2.root = jarray('int', [Code01_MaxXor2.MAXN])
Code01_MaxXor2.tree = jarray('int', [Code01_MaxXor2.MAXT, 2])
Code01_MaxXor2.pass_ = jarray('int', [Code01_MaxXor2.MAXT])
Code01_MaxXor2.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code01_MaxXor2.main([])

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

# 文本编辑器，FHQ-Treap实现区间移动，Python版本
# 一开始文本为空，光标在文本开头，也就是1位置，请实现如下6种操作
# Move k     : 将光标移动到第k个字符之后，操作保证光标不会到非法位置
# Insert n s : 在光标处插入长度为n的字符串s，光标位置不变
# Delete n   : 删除光标后的n个字符，光标位置不变，操作保证有足够字符
# Get n      : 输出光标后的n个字符，光标位置不变，操作保证有足够字符
# Prev       : 光标前移一个字符，操作保证光标不会到非法位置
# Next       : 光标后移一个字符，操作保证光标不会到非法位置
# Insert操作时，字符串s中ASCII码在[32,126]范围上的字符一定有n个，其他字符请过滤掉
# 测试链接 : https://www.luogu.com.cn/problem/P4008
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 对应实现可参考 Code03_TextEditor2.py
# 两个版本保留相同的算法逻辑
# 讲解172，讲解块状链表时，本题又讲了一遍，分块的方法
class Code03_TextEditor1:
    __java_fields__ = {'MAXN': 'MAXN', 'head': 'head', 'cnt': 'cnt', 'key': 'key', 'left': 'left', 'right': 'right', 'size': 'size', 'priority': 'priority', 'ans': 'ans', 'ansi': 'ansi'}
    MAXN = 0
    head = 0
    cnt = 0
    key = None
    left = None
    right = None
    size = None
    priority = None
    ans = None
    ansi = 0
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_TextEditor1.size[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code03_TextEditor1.size[Code03_TextEditor1.left[i]], Code03_TextEditor1.size[Code03_TextEditor1.right[i]])), 1)))

    @staticmethod
    def split(l, r, i, rank):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rank = jcast('int', rank)
        if (i == 0):
            jset(Code03_TextEditor1.right, l, jset(Code03_TextEditor1.left, r, 0))
        else:
            if (jcast('int', jadd(Code03_TextEditor1.size[Code03_TextEditor1.left[i]], 1)) <= rank):
                Code03_TextEditor1.right[l] = jcast('int', i)
                Code03_TextEditor1.split(i, r, Code03_TextEditor1.right[i], jcast('int', (jcast('int', (rank - Code03_TextEditor1.size[Code03_TextEditor1.left[i]])) - 1)))
            else:
                Code03_TextEditor1.left[r] = jcast('int', i)
                Code03_TextEditor1.split(l, i, Code03_TextEditor1.left[i], rank)
            Code03_TextEditor1.up(i)

    @staticmethod
    def merge(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if ((l == 0) or (r == 0)):
            return jcast('int', jcast('int', jadd(l, r)))
        if (Code03_TextEditor1.priority[l] >= Code03_TextEditor1.priority[r]):
            jset(Code03_TextEditor1.right, l, Code03_TextEditor1.merge(Code03_TextEditor1.right[l], r))
            Code03_TextEditor1.up(l)
            return jcast('int', l)
        else:
            jset(Code03_TextEditor1.left, r, Code03_TextEditor1.merge(l, Code03_TextEditor1.left[r]))
            Code03_TextEditor1.up(r)
            return jcast('int', r)

    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if (i != 0):
            Code03_TextEditor1.inorder(Code03_TextEditor1.left[i])
            jset(Code03_TextEditor1.ans, ((_java_obj_1 := Code03_TextEditor1), (_java_key_2 := 'ansi'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_TextEditor1.key[i])
            Code03_TextEditor1.inorder(Code03_TextEditor1.right[i])

    @staticmethod
    def main(args):
        in_ = Code03_TextEditor1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        n = jcast('int', jcall(in_, 'nextInt'))
        pos = jcast('int', 0)
        op = None
        x = 0
        i = jcast('int', 1)
        while (i <= n):
            op = jcall(in_, 'nextString')
            if jcall(op, 'equals', 'Prev'):
                pos = jcast('int', (pos - 1))
            else:
                if jcall(op, 'equals', 'Next'):
                    pos = jcast('int', (pos + 1))
                else:
                    if jcall(op, 'equals', 'Move'):
                        pos = jcast('int', jcall(in_, 'nextInt'))
                    else:
                        if jcall(op, 'equals', 'Delete'):
                            x = jcast('int', jcall(in_, 'nextInt'))
                            Code03_TextEditor1.split(0, 0, Code03_TextEditor1.head, jcast('int', jadd(pos, x)))
                            r = jcast('int', Code03_TextEditor1.left[0])
                            lm = jcast('int', Code03_TextEditor1.right[0])
                            jset(Code03_TextEditor1.left, 0, jset(Code03_TextEditor1.right, 0, 0))
                            Code03_TextEditor1.split(0, 0, lm, pos)
                            l = jcast('int', Code03_TextEditor1.right[0])
                            jset(Code03_TextEditor1.left, 0, jset(Code03_TextEditor1.right, 0, 0))
                            Code03_TextEditor1.head = jcast('int', Code03_TextEditor1.merge(l, r))
                        else:
                            if jcall(op, 'equals', 'Insert'):
                                x = jcast('int', jcall(in_, 'nextInt'))
                                Code03_TextEditor1.split(0, 0, Code03_TextEditor1.head, pos)
                                l = jcast('int', Code03_TextEditor1.right[0])
                                r = jcast('int', Code03_TextEditor1.left[0])
                                jset(Code03_TextEditor1.left, 0, jset(Code03_TextEditor1.right, 0, 0))
                                j = jcast('int', 1)
                                while (j <= x):
                                    jset(Code03_TextEditor1.key, ((_java_obj_4 := Code03_TextEditor1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], jcall(in_, 'nextChar'))
                                    Code03_TextEditor1.size[Code03_TextEditor1.cnt] = jcast('int', 1)
                                    jset(Code03_TextEditor1.priority, Code03_TextEditor1.cnt, jstatic('Math', 'random'))
                                    l = jcast('int', Code03_TextEditor1.merge(l, Code03_TextEditor1.cnt))
                                    j = jcast('int', (j + 1))
                                Code03_TextEditor1.head = jcast('int', Code03_TextEditor1.merge(l, r))
                            else:
                                x = jcast('int', jcall(in_, 'nextInt'))
                                Code03_TextEditor1.split(0, 0, Code03_TextEditor1.head, jcast('int', jadd(pos, x)))
                                r = jcast('int', Code03_TextEditor1.left[0])
                                lm = jcast('int', Code03_TextEditor1.right[0])
                                jset(Code03_TextEditor1.left, 0, jset(Code03_TextEditor1.right, 0, 0))
                                Code03_TextEditor1.split(0, 0, lm, pos)
                                l = jcast('int', Code03_TextEditor1.right[0])
                                m = jcast('int', Code03_TextEditor1.left[0])
                                jset(Code03_TextEditor1.left, 0, jset(Code03_TextEditor1.right, 0, 0))
                                Code03_TextEditor1.ansi = jcast('int', 0)
                                Code03_TextEditor1.inorder(m)
                                Code03_TextEditor1.head = jcast('int', Code03_TextEditor1.merge(Code03_TextEditor1.merge(l, m), r))
                                j = jcast('int', 1)
                                while (j <= Code03_TextEditor1.ansi):
                                    jcall(out, 'print', jcast('char', Code03_TextEditor1.ans[j]))
                                    j = jcast('int', (j + 1))
                                jcall(out, 'println')
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

        def nextChar(self):
            c = 0
            while True:
                c = jcast('byte', self.readByte())
                if (c == jcast('int', (-1))):
                    return jcast('char', 0)
                if not (((c < 32) or (c > 126))):
                    break
            return jcast('char', jcast('char', c))

        def nextString(self):
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            sb = jnew('StringBuilder', 1000)
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', b))
                b = jcast('byte', self.readByte())
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
            raise TypeError("No matching overload for Code03_TextEditor1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_TextEditor1.MAXN = jcast('int', 2000001)
Code03_TextEditor1.head = jcast('int', 0)
Code03_TextEditor1.cnt = jcast('int', 0)
Code03_TextEditor1.key = jarray('char', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.left = jarray('int', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.right = jarray('int', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.size = jarray('int', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.priority = jarray('double', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.ans = jarray('char', [Code03_TextEditor1.MAXN])
Code03_TextEditor1.ansi = jcast('int', 0)

if __name__ == '__main__':
    Code03_TextEditor1.main([])

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

# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 给定一个长度为n的数组arr，下标1~n，时间戳t=0，arr认为是0版本的数组
# 一共有m条查询，每条查询为如下四种类型中的一种
# C x y z : 当前时间戳t版本的数组，[x..y]范围每个数字增加z，得到t+1版本数组，并且t++
# Q x y   : 当前时间戳t版本的数组，打印[x..y]范围累加和
# H x y z : z版本的数组，打印[x..y]范围的累加和
# B x     : 当前时间戳t设置成x
# 1 <= n、m <= 10^5
# -10^9 <= arr[i] <= +10^9
# 测试链接 : https://acm.hdu.edu.cn/showproblem.php?pid=4348
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 本实现包含较大的数组或状态集合，内存开销取决于数据规模和 Python 容器表示
# 对应实现可参考 Code05_RangePersistentLessSpace2.py
# 两个版本保留相同的算法逻辑
class Code05_RangePersistentLessSpace1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'm': 'm', 't': 't', 'arr': 'arr', 'root': 'root', 'left': 'left', 'right': 'right', 'sum': 'sum', 'addTag': 'addTag', 'cnt': 'cnt'}
    MAXN = 0
    MAXT = 0
    n = 0
    m = 0
    t = 0
    arr = None
    root = None
    left = None
    right = None
    # 不是真实累加和，而是之前的任务中
    # 不考虑被上方范围截住的任务，只考虑来到当前范围 或者 往下走的任务
    # 累加和变成了什么
    sum = None
    # 不再是懒更新信息，变成标记信息
    addTag = None
    cnt = 0
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        rt = jcast('int', ((_java_obj_1 := Code05_RangePersistentLessSpace1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3])
        Code05_RangePersistentLessSpace1.addTag[rt] = jcast('long', 0)
        if (l == r):
            Code05_RangePersistentLessSpace1.sum[rt] = jcast('long', Code05_RangePersistentLessSpace1.arr[l])
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            jset(Code05_RangePersistentLessSpace1.left, rt, Code05_RangePersistentLessSpace1.build(l, mid))
            jset(Code05_RangePersistentLessSpace1.right, rt, Code05_RangePersistentLessSpace1.build(jcast('int', jadd(mid, 1)), r))
            Code05_RangePersistentLessSpace1.sum[rt] = jcast('long', jcast('long', jadd(Code05_RangePersistentLessSpace1.sum[Code05_RangePersistentLessSpace1.left[rt]], Code05_RangePersistentLessSpace1.sum[Code05_RangePersistentLessSpace1.right[rt]])))
        return jcast('int', rt)

    @staticmethod
    def add(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('long', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_4 := Code05_RangePersistentLessSpace1), (_java_key_5 := 'cnt'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        a = jcast('int', jstatic('Math', 'max', jobl, l))
        b = jcast('int', jstatic('Math', 'min', jobr, r))
        Code05_RangePersistentLessSpace1.left[rt] = jcast('int', Code05_RangePersistentLessSpace1.left[i])
        Code05_RangePersistentLessSpace1.right[rt] = jcast('int', Code05_RangePersistentLessSpace1.right[i])
        Code05_RangePersistentLessSpace1.sum[rt] = jcast('long', jcast('long', jadd(Code05_RangePersistentLessSpace1.sum[i], jcast('long', (jobv * jcast('int', jadd(jcast('int', (b - a)), 1)))))))
        Code05_RangePersistentLessSpace1.addTag[rt] = jcast('long', Code05_RangePersistentLessSpace1.addTag[i])
        if ((jobl <= l) and (r <= jobr)):
            Code05_RangePersistentLessSpace1.addTag[rt] = jcast('long', jcast('long', jadd(Code05_RangePersistentLessSpace1.addTag[rt], jobv)))
        else:
            mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (jobl <= mid):
                jset(Code05_RangePersistentLessSpace1.left, rt, Code05_RangePersistentLessSpace1.add(jobl, jobr, jobv, l, mid, Code05_RangePersistentLessSpace1.left[rt]))
            if (jobr > mid):
                jset(Code05_RangePersistentLessSpace1.right, rt, Code05_RangePersistentLessSpace1.add(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, Code05_RangePersistentLessSpace1.right[rt]))
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, addHistory, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        addHistory = jcast('long', addHistory)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('long', jcast('long', jadd(Code05_RangePersistentLessSpace1.sum[i], jcast('long', (addHistory * jcast('int', jadd(jcast('int', (r - l)), 1)))))))
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        ans = jcast('long', 0)
        if (jobl <= mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_RangePersistentLessSpace1.query(jobl, jobr, jcast('long', jadd(addHistory, Code05_RangePersistentLessSpace1.addTag[i])), l, mid, Code05_RangePersistentLessSpace1.left[i]))))
        if (jobr > mid):
            ans = jcast('long', jcast('long', jadd(ans, Code05_RangePersistentLessSpace1.query(jobl, jobr, jcast('long', jadd(addHistory, Code05_RangePersistentLessSpace1.addTag[i])), jcast('int', jadd(mid, 1)), r, Code05_RangePersistentLessSpace1.right[i]))))
        return jcast('long', ans)

    @staticmethod
    def main(args):
        in_ = Code05_RangePersistentLessSpace1.FastReader(_java_ctor=0)
        out = jnew('BufferedWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_RangePersistentLessSpace1.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_RangePersistentLessSpace1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_RangePersistentLessSpace1.n):
            jset(Code05_RangePersistentLessSpace1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        jset(Code05_RangePersistentLessSpace1.root, 0, Code05_RangePersistentLessSpace1.build(1, Code05_RangePersistentLessSpace1.n))
        op = None
        i = jcast('int', 1)
        x = 0
        y = 0
        z = 0
        while (i <= Code05_RangePersistentLessSpace1.m):
            op = jcall(in_, 'next')
            if jcall(op, 'equals', 'C'):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                z = jcast('int', jcall(in_, 'nextInt'))
                jset(Code05_RangePersistentLessSpace1.root, jcast('int', jadd(Code05_RangePersistentLessSpace1.t, 1)), Code05_RangePersistentLessSpace1.add(x, y, z, 1, Code05_RangePersistentLessSpace1.n, Code05_RangePersistentLessSpace1.root[Code05_RangePersistentLessSpace1.t]))
                Code05_RangePersistentLessSpace1.t = jcast('int', (Code05_RangePersistentLessSpace1.t + 1))
            else:
                if jcall(op, 'equals', 'Q'):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    y = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'write', jadd(Code05_RangePersistentLessSpace1.query(x, y, 0, 1, Code05_RangePersistentLessSpace1.n, Code05_RangePersistentLessSpace1.root[Code05_RangePersistentLessSpace1.t]), '\n'))
                else:
                    if jcall(op, 'equals', 'H'):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        z = jcast('int', jcall(in_, 'nextInt'))
                        jcall(out, 'write', jadd(Code05_RangePersistentLessSpace1.query(x, y, 0, 1, Code05_RangePersistentLessSpace1.n, Code05_RangePersistentLessSpace1.root[z]), '\n'))
                    else:
                        x = jcast('int', jcall(in_, 'nextInt'))
                        Code05_RangePersistentLessSpace1.t = jcast('int', x)
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
            raise TypeError("No matching overload for Code05_RangePersistentLessSpace1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_RangePersistentLessSpace1.MAXN = jcast('int', 100001)
Code05_RangePersistentLessSpace1.MAXT = jcast('int', jcast('int', (Code05_RangePersistentLessSpace1.MAXN * 25)))
Code05_RangePersistentLessSpace1.n = jcast('int', 0)
Code05_RangePersistentLessSpace1.m = jcast('int', 0)
Code05_RangePersistentLessSpace1.t = jcast('int', 0)
Code05_RangePersistentLessSpace1.arr = jarray('int', [Code05_RangePersistentLessSpace1.MAXN])
Code05_RangePersistentLessSpace1.root = jarray('int', [Code05_RangePersistentLessSpace1.MAXN])
Code05_RangePersistentLessSpace1.left = jarray('int', [Code05_RangePersistentLessSpace1.MAXT])
Code05_RangePersistentLessSpace1.right = jarray('int', [Code05_RangePersistentLessSpace1.MAXT])
Code05_RangePersistentLessSpace1.sum = jarray('long', [Code05_RangePersistentLessSpace1.MAXT])
Code05_RangePersistentLessSpace1.addTag = jarray('long', [Code05_RangePersistentLessSpace1.MAXT])
Code05_RangePersistentLessSpace1.cnt = jcast('int', 0)

if __name__ == '__main__':
    Code05_RangePersistentLessSpace1.main([])

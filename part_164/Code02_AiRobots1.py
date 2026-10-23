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

# 机器人聊天对，Python版
# 一共有n个机器人，给定一个整数k，每个机器人给定，位置x、视野y、智商q
# 第i个机器人可以看见的范围是[xi − yi, xi + yi]
# 如果两个机器人相互之间可以看见，并且智商差距不大于k，那么它们会开始聊天
# 打印有多少对机器人可以聊天
# 1 <= n <= 10^5
# 0 <= k <= 20
# 0 <= x、y、q <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF1045G
# 测试链接 : https://codeforces.com/problemset/problem/1045/G
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_AiRobots1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 's': 's', 'arr': 'arr', 'x': 'x', 'tree': 'tree'}
    MAXN = 0
    n = 0
    k = 0
    s = 0
    # 位置x、视野y、智商q、能看到的最左位置l、能看到的最右位置r
    arr = None
    # 所有x坐标组成的数组
    x = None
    tree = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code02_AiRobots1.s):
            Code02_AiRobots1.tree[i] = jcast('int', jcast('int', jadd(Code02_AiRobots1.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code02_AiRobots1.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code02_AiRobots1.tree[i])))
            i = jcast('int', jcast('int', (i - Code02_AiRobots1.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        return jcast('int', jcast('int', (Code02_AiRobots1.sum(r) - Code02_AiRobots1.sum(jcast('int', (l - 1))))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        winl = jcast('int', l)
        winr = jcast('int', jcast('int', (l - 1)))
        ans = jcast('long', 0)
        i = jcast('int', jcast('int', jadd(m, 1)))
        while (i <= r):
            while ((winl <= m) and (Code02_AiRobots1.arr[winl][2] < jcast('int', (Code02_AiRobots1.arr[i][2] - Code02_AiRobots1.k)))):
                Code02_AiRobots1.add(Code02_AiRobots1.arr[winl][0], jcast('int', (-1)))
                winl = jcast('int', (winl + 1))
            while ((jcast('int', jadd(winr, 1)) <= m) and (Code02_AiRobots1.arr[jcast('int', jadd(winr, 1))][2] <= jcast('int', jadd(Code02_AiRobots1.arr[i][2], Code02_AiRobots1.k)))):
                winr = jcast('int', (winr + 1))
                Code02_AiRobots1.add(Code02_AiRobots1.arr[winr][0], 1)
            ans = jcast('long', jcast('long', jadd(ans, Code02_AiRobots1.query(Code02_AiRobots1.arr[i][3], Code02_AiRobots1.arr[i][4]))))
            i = jcast('int', (i + 1))
        i = jcast('int', winl)
        while (i <= winr):
            Code02_AiRobots1.add(Code02_AiRobots1.arr[i][0], jcast('int', (-1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_AiRobots1.arr, l, jcast('int', jadd(r, 1)), (lambda a, b: (a[2] - b[2])))
        return jcast('long', ans)

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return jcast('long', 0)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        return jcast('long', jcast('long', jadd(jcast('long', jadd(Code02_AiRobots1.cdq(l, mid), Code02_AiRobots1.cdq(jcast('int', jadd(mid, 1)), r))), Code02_AiRobots1.merge(l, mid, r))))

    @staticmethod
    def lower(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code02_AiRobots1.s)
        m = 0
        ans = jcast('int', 1)
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code02_AiRobots1.x[m] >= num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def upper(num):
        num = jcast('int', num)
        l = jcast('int', 1)
        r = jcast('int', Code02_AiRobots1.s)
        m = 0
        ans = jcast('int', jcast('int', jadd(Code02_AiRobots1.s, 1)))
        while (l <= r):
            m = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
            if (Code02_AiRobots1.x[m] > num):
                ans = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_AiRobots1.n):
            Code02_AiRobots1.x[i] = jcast('int', Code02_AiRobots1.arr[i][0])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_AiRobots1.x, 1, jcast('int', jadd(Code02_AiRobots1.n, 1)))
        Code02_AiRobots1.s = jcast('int', 1)
        i = jcast('int', 2)
        while (i <= Code02_AiRobots1.n):
            if (Code02_AiRobots1.x[Code02_AiRobots1.s] != Code02_AiRobots1.x[i]):
                jset(Code02_AiRobots1.x, ((_java_obj_1 := Code02_AiRobots1), (_java_key_2 := 's'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_AiRobots1.x[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_AiRobots1.n):
            jset(Code02_AiRobots1.arr[i], 3, Code02_AiRobots1.lower(jcast('int', (Code02_AiRobots1.arr[i][0] - Code02_AiRobots1.arr[i][1]))))
            jset(Code02_AiRobots1.arr[i], 4, jcast('int', (Code02_AiRobots1.upper(jcast('int', jadd(Code02_AiRobots1.arr[i][0], Code02_AiRobots1.arr[i][1]))) - 1)))
            jset(Code02_AiRobots1.arr[i], 0, Code02_AiRobots1.lower(Code02_AiRobots1.arr[i][0]))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_AiRobots1.arr, 1, jcast('int', jadd(Code02_AiRobots1.n, 1)), (lambda a, b: (b[1] - a[1])))

    @staticmethod
    def main(args):
        in_ = Code02_AiRobots1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_AiRobots1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_AiRobots1.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_AiRobots1.n):
            jset(Code02_AiRobots1.arr[i], 0, jcall(in_, 'nextInt'))
            jset(Code02_AiRobots1.arr[i], 1, jcall(in_, 'nextInt'))
            jset(Code02_AiRobots1.arr[i], 2, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_AiRobots1.prepare()
        jcall(out, 'println', Code02_AiRobots1.cdq(1, Code02_AiRobots1.n))
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_AiRobots1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_AiRobots1.MAXN = jcast('int', 100001)
Code02_AiRobots1.n = jcast('int', 0)
Code02_AiRobots1.k = jcast('int', 0)
Code02_AiRobots1.s = jcast('int', 0)
Code02_AiRobots1.arr = jarray('int', [Code02_AiRobots1.MAXN, 5])
Code02_AiRobots1.x = jarray('int', [Code02_AiRobots1.MAXN])
Code02_AiRobots1.tree = jarray('int', [Code02_AiRobots1.MAXN])

if __name__ == '__main__':
    Code02_AiRobots1.main([])

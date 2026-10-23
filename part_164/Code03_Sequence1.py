# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 序列，Python版
# 给定一个长度为n的数组arr，一共有m条操作，格式为 x v 表示x位置的数变成v
# 你可以选择不执行任何操作，或者只选择一个操作来执行，然后arr不再变动
# 请在arr中选出一组下标序列，不管你做出什么选择，下标序列所代表的数字都是不下降的
# 打印序列能达到的最大长度
# 1 <= 所有数字 <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4093
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Sequence1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'v': 'v', 'lv': 'lv', 'rv': 'rv', 'arr': 'arr', 'tree': 'tree', 'dp': 'dp'}
    MAXN = 0
    n = 0
    m = 0
    v = None
    lv = None
    rv = None
    # 位置i、数值v、最小值lv、最大值rv
    arr = None
    # 树状数组维护前缀最大值
    tree = None
    dp = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def more(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        while (i <= Code03_Sequence1.n):
            jset(Code03_Sequence1.tree, i, jstatic('Math', 'max', Code03_Sequence1.tree[i], num))
            i = jcast('int', jcast('int', jadd(i, Code03_Sequence1.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jstatic('Math', 'max', ret, Code03_Sequence1.tree[i]))
            i = jcast('int', jcast('int', (i - Code03_Sequence1.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def clear(i):
        i = jcast('int', i)
        while (i <= Code03_Sequence1.n):
            Code03_Sequence1.tree[i] = jcast('int', 0)
            i = jcast('int', jcast('int', jadd(i, Code03_Sequence1.lowbit(i))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        # 辅助数组arr拷贝l..r所有的对象
        # 接下来的排序都发生在arr中，不影响原始的次序
        i = jcast('int', l)
        while (i <= r):
            jset(Code03_Sequence1.arr[i], 0, i)
            jset(Code03_Sequence1.arr[i], 1, Code03_Sequence1.v[i])
            jset(Code03_Sequence1.arr[i], 2, Code03_Sequence1.lv[i])
            jset(Code03_Sequence1.arr[i], 3, Code03_Sequence1.rv[i])
            i = jcast('int', (i + 1))
        # 左侧根据v排序
        jstatic('Arrays', 'sort', Code03_Sequence1.arr, l, jcast('int', jadd(m, 1)), (lambda a, b: (a[1] - b[1])))
        # 右侧根据lv排序
        jstatic('Arrays', 'sort', Code03_Sequence1.arr, jcast('int', jadd(m, 1)), jcast('int', jadd(r, 1)), (lambda a, b: (a[2] - b[2])))
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            # 左侧对象.v <= 右侧对象.lv 窗口扩充
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code03_Sequence1.arr[jcast('int', jadd(p1, 1))][1] <= Code03_Sequence1.arr[p2][2])):
                p1 = jcast('int', (p1 + 1))
                # 树状数组中，下标是rv，加入的值是左侧对象的dp值
                Code03_Sequence1.more(Code03_Sequence1.arr[p1][3], Code03_Sequence1.dp[Code03_Sequence1.arr[p1][0]])
            # 右侧对象更新dp值，查出1..v范围上最大的dp值 + 1
            jset(Code03_Sequence1.dp, Code03_Sequence1.arr[p2][0], jstatic('Math', 'max', Code03_Sequence1.dp[Code03_Sequence1.arr[p2][0]], jcast('int', jadd(Code03_Sequence1.query(Code03_Sequence1.arr[p2][1]), 1))))
            p2 = jcast('int', (p2 + 1))
        # 清空树状数组
        i = jcast('int', l)
        while (i <= p1):
            Code03_Sequence1.clear(Code03_Sequence1.arr[i][3])
            i = jcast('int', (i + 1))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code03_Sequence1.cdq(l, mid)
        Code03_Sequence1.merge(l, mid, r)
        Code03_Sequence1.cdq(jcast('int', jadd(mid, 1)), r)

    @staticmethod
    def main(args):
        in_ = Code03_Sequence1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Sequence1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Sequence1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Sequence1.n):
            jset(Code03_Sequence1.v, i, jcall(in_, 'nextInt'))
            Code03_Sequence1.lv[i] = jcast('int', Code03_Sequence1.v[i])
            Code03_Sequence1.rv[i] = jcast('int', Code03_Sequence1.v[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        idx = 0
        val = 0
        while (i <= Code03_Sequence1.m):
            idx = jcast('int', jcall(in_, 'nextInt'))
            val = jcast('int', jcall(in_, 'nextInt'))
            jset(Code03_Sequence1.lv, idx, jstatic('Math', 'min', Code03_Sequence1.lv[idx], val))
            jset(Code03_Sequence1.rv, idx, jstatic('Math', 'max', Code03_Sequence1.rv[idx], val))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Sequence1.n):
            Code03_Sequence1.dp[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        Code03_Sequence1.cdq(1, Code03_Sequence1.n)
        ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code03_Sequence1.n):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_Sequence1.dp[i]))
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
            self.buffer = jarray('byte', [jcast('int', (1 << (20 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Sequence1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_Sequence1.MAXN = jcast('int', 100001)
Code03_Sequence1.n = jcast('int', 0)
Code03_Sequence1.m = jcast('int', 0)
Code03_Sequence1.v = jarray('int', [Code03_Sequence1.MAXN])
Code03_Sequence1.lv = jarray('int', [Code03_Sequence1.MAXN])
Code03_Sequence1.rv = jarray('int', [Code03_Sequence1.MAXN])
Code03_Sequence1.arr = jarray('int', [Code03_Sequence1.MAXN, 4])
Code03_Sequence1.tree = jarray('int', [Code03_Sequence1.MAXN])
Code03_Sequence1.dp = jarray('int', [Code03_Sequence1.MAXN])

if __name__ == '__main__':
    Code03_Sequence1.main([])

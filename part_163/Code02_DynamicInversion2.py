# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 动态逆序对，Python版
# 给定一个长度为n的排列，1~n所有数字都出现一次
# 如果，前面的数 > 后面的数，那么这两个数就组成一个逆序对
# 给定一个长度为m的数组，表示依次删除的数字
# 打印每次删除数字前，排列中一共有多少逆序对，一共m条打印
# 1 <= n <= 10^5
# 1 <= m <= 5 * 10^4
# 测试链接 : https://www.luogu.com.cn/problem/P3157
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_DynamicInversion2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'num': 'num', 'pos': 'pos', 'del': 'del_', 'arr': 'arr', 'cnt': 'cnt', 'tree': 'tree', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    # num : 原始序列依次的值
    # pos : 每个值在什么位置
    # del : 每一步删掉的值
    num = None
    pos = None
    del_ = None
    # 数值v、位置i、效果d、问题编号q
    arr = None
    cnt = 0
    # 树状数组
    tree = None
    # 每次逆序对的变化量
    ans = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code02_DynamicInversion2.n):
            Code02_DynamicInversion2.tree[i] = jcast('int', jcast('int', jadd(Code02_DynamicInversion2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code02_DynamicInversion2.lowbit(i))))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code02_DynamicInversion2.tree[i])))
            i = jcast('int', jcast('int', (i - Code02_DynamicInversion2.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        # 从左到右统计左侧值大的数量
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code02_DynamicInversion2.arr[jcast('int', jadd(p1, 1))][1] < Code02_DynamicInversion2.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                Code02_DynamicInversion2.add(Code02_DynamicInversion2.arr[p1][0], Code02_DynamicInversion2.arr[p1][2])
            ((_java_obj_1 := Code02_DynamicInversion2.ans), (_java_key_2 := Code02_DynamicInversion2.arr[p2][3]), jset(_java_obj_1, _java_key_2, jcast('long', jadd(jget(_java_obj_1, _java_key_2), jcast('int', (Code02_DynamicInversion2.arr[p2][2] * jcast('int', (Code02_DynamicInversion2.query(Code02_DynamicInversion2.n) - Code02_DynamicInversion2.query(Code02_DynamicInversion2.arr[p2][0])))))))))[2]
            p2 = jcast('int', (p2 + 1))
        # 清除树状数组
        i = jcast('int', l)
        while (i <= p1):
            Code02_DynamicInversion2.add(Code02_DynamicInversion2.arr[i][0], jcast('int', (-Code02_DynamicInversion2.arr[i][2])))
            i = jcast('int', (i + 1))
        # 从右到左统计右侧值小的数量
        p1 = jcast('int', jcast('int', jadd(m, 1)))
        p2 = jcast('int', r)
        while (p2 > m):
            while ((jcast('int', (p1 - 1)) >= l) and (Code02_DynamicInversion2.arr[jcast('int', (p1 - 1))][1] > Code02_DynamicInversion2.arr[p2][1])):
                p1 = jcast('int', (p1 - 1))
                Code02_DynamicInversion2.add(Code02_DynamicInversion2.arr[p1][0], Code02_DynamicInversion2.arr[p1][2])
            ((_java_obj_3 := Code02_DynamicInversion2.ans), (_java_key_4 := Code02_DynamicInversion2.arr[p2][3]), jset(_java_obj_3, _java_key_4, jcast('long', jadd(jget(_java_obj_3, _java_key_4), jcast('int', (Code02_DynamicInversion2.arr[p2][2] * Code02_DynamicInversion2.query(jcast('int', (Code02_DynamicInversion2.arr[p2][0] - 1)))))))))[2]
            p2 = jcast('int', (p2 - 1))
        # 清除树状数组
        i = jcast('int', m)
        while (i >= p1):
            Code02_DynamicInversion2.add(Code02_DynamicInversion2.arr[i][0], jcast('int', (-Code02_DynamicInversion2.arr[i][2])))
            i = jcast('int', (i - 1))
        # 直接排序
        jstatic('Arrays', 'sort', Code02_DynamicInversion2.arr, l, jcast('int', jadd(r, 1)), (lambda a, b: (a[1] - b[1])))

    # 整体按时序组织，cdq分治里根据下标重新排序
    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code02_DynamicInversion2.cdq(l, mid)
        Code02_DynamicInversion2.cdq(jcast('int', jadd(mid, 1)), r)
        Code02_DynamicInversion2.merge(l, mid, r)

    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_DynamicInversion2.n):
            jset(Code02_DynamicInversion2.arr[((_java_obj_5 := Code02_DynamicInversion2), (_java_key_6 := 'cnt'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3]], 0, Code02_DynamicInversion2.num[i])
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 1, i)
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 2, 1)
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 3, 0)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_DynamicInversion2.m):
            jset(Code02_DynamicInversion2.arr[((_java_obj_8 := Code02_DynamicInversion2), (_java_key_9 := 'cnt'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3]], 0, Code02_DynamicInversion2.del_[i])
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 1, Code02_DynamicInversion2.pos[Code02_DynamicInversion2.del_[i]])
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 2, jcast('int', (-1)))
            jset(Code02_DynamicInversion2.arr[Code02_DynamicInversion2.cnt], 3, i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code02_DynamicInversion2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_DynamicInversion2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_DynamicInversion2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_DynamicInversion2.n):
            jset(Code02_DynamicInversion2.num, i, jcall(in_, 'nextInt'))
            jset(Code02_DynamicInversion2.pos, Code02_DynamicInversion2.num[i], i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_DynamicInversion2.m):
            jset(Code02_DynamicInversion2.del_, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_DynamicInversion2.prepare()
        Code02_DynamicInversion2.cdq(1, Code02_DynamicInversion2.cnt)
        i = jcast('int', 1)
        while (i < Code02_DynamicInversion2.m):
            Code02_DynamicInversion2.ans[i] = jcast('long', jcast('long', jadd(Code02_DynamicInversion2.ans[i], Code02_DynamicInversion2.ans[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', 0)
        while (i < Code02_DynamicInversion2.m):
            jcall(out, 'println', Code02_DynamicInversion2.ans[i])
            i = jcast('int', (i + 1))
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code02_DynamicInversion2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_DynamicInversion2.MAXN = jcast('int', 100001)
Code02_DynamicInversion2.MAXM = jcast('int', 50001)
Code02_DynamicInversion2.n = jcast('int', 0)
Code02_DynamicInversion2.m = jcast('int', 0)
Code02_DynamicInversion2.num = jarray('int', [Code02_DynamicInversion2.MAXN])
Code02_DynamicInversion2.pos = jarray('int', [Code02_DynamicInversion2.MAXN])
Code02_DynamicInversion2.del_ = jarray('int', [Code02_DynamicInversion2.MAXM])
Code02_DynamicInversion2.arr = jarray('int', [jcast('int', jadd(Code02_DynamicInversion2.MAXN, Code02_DynamicInversion2.MAXM)), 4])
Code02_DynamicInversion2.cnt = jcast('int', 0)
Code02_DynamicInversion2.tree = jarray('int', [Code02_DynamicInversion2.MAXN])
Code02_DynamicInversion2.ans = jarray('long', [Code02_DynamicInversion2.MAXM])

if __name__ == '__main__':
    Code02_DynamicInversion2.main([])

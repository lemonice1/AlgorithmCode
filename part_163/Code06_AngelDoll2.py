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

# 天使玩偶，Python版
# 规定(x1, y1)和(x2, y2)之间的距离 = | x1 - x2 | + | y1 - y2 |
# 一开始先给定n个点的位置，接下来有m条操作，每种操作是如下两种类型中的一种
# 操作 1 x y : 在(x, y)位置添加一个点
# 操作 2 x y : 打印已经添加的所有点中，距离(x, y)最近的点有多远
# 1 <= n、m <= 3 * 10^5
# 0 <= x、y <= 10^6
# 测试链接 : https://www.luogu.com.cn/problem/P4169
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_AngelDoll2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'INF': 'INF', 'n': 'n', 'm': 'm', 'v': 'v', 'tim': 'tim', 'arr': 'arr', 'cnte': 'cnte', 'cntq': 'cntq', 'tree': 'tree', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    INF = 0
    n = 0
    m = 0
    v = 0
    # op == 1代表添加事件，x、y、空缺
    # op == 2代表查询事件，x、y、查询编号q
    # tim永远保持原始时序，每次变换象限都拷贝给arr，然后执行cdq分治
    tim = None
    arr = None
    cnte = 0
    cntq = 0
    # 树状数组，下标是y的值，维护前缀范围上的最大值
    tree = None
    ans = None
    @staticmethod
    def clone(a, b):
        a[0] = jcast('int', b[0])
        a[1] = jcast('int', b[1])
        a[2] = jcast('int', b[2])
        a[3] = jcast('int', b[3])

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    # 树状数组，如果i位置之前的值更大，忽略，num更大才更新
    @staticmethod
    def more(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        while (i <= Code06_AngelDoll2.v):
            jset(Code06_AngelDoll2.tree, i, jstatic('Math', 'max', Code06_AngelDoll2.tree[i], num))
            i = jcast('int', jcast('int', jadd(i, Code06_AngelDoll2.lowbit(i))))

    # 树状数组，查询1~i范围上的最大值
    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', jcast('int', (-Code06_AngelDoll2.INF)))
        while (i > 0):
            ret = jcast('int', jstatic('Math', 'max', ret, Code06_AngelDoll2.tree[i]))
            i = jcast('int', jcast('int', (i - Code06_AngelDoll2.lowbit(i))))
        return jcast('int', ret)

    # 因为本题的特殊性，树状数组一定全部清空
    # 所以当初更新时，i位置碰过哪些位置，一律设置无效值即可
    @staticmethod
    def clear(i):
        i = jcast('int', i)
        while (i <= Code06_AngelDoll2.v):
            Code06_AngelDoll2.tree[i] = jcast('int', jcast('int', (-Code06_AngelDoll2.INF)))
            i = jcast('int', jcast('int', jadd(i, Code06_AngelDoll2.lowbit(i))))

    @staticmethod
    def merge(l, m, r):
        l = jcast('int', l)
        m = jcast('int', m)
        r = jcast('int', r)
        p1 = 0
        p2 = 0
        p1 = jcast('int', jcast('int', (l - 1)))
        p2 = jcast('int', jcast('int', jadd(m, 1)))
        while (p2 <= r):
            while ((jcast('int', jadd(p1, 1)) <= m) and (Code06_AngelDoll2.arr[jcast('int', jadd(p1, 1))][1] <= Code06_AngelDoll2.arr[p2][1])):
                p1 = jcast('int', (p1 + 1))
                if (Code06_AngelDoll2.arr[p1][0] == 1):
                    Code06_AngelDoll2.more(Code06_AngelDoll2.arr[p1][2], jcast('int', jadd(Code06_AngelDoll2.arr[p1][1], Code06_AngelDoll2.arr[p1][2])))
            if (Code06_AngelDoll2.arr[p2][0] == 2):
                jset(Code06_AngelDoll2.ans, Code06_AngelDoll2.arr[p2][3], jstatic('Math', 'min', Code06_AngelDoll2.ans[Code06_AngelDoll2.arr[p2][3]], jcast('int', (jcast('int', jadd(Code06_AngelDoll2.arr[p2][1], Code06_AngelDoll2.arr[p2][2])) - Code06_AngelDoll2.query(Code06_AngelDoll2.arr[p2][2])))))
            p2 = jcast('int', (p2 + 1))
        i = jcast('int', l)
        while (i <= p1):
            if (Code06_AngelDoll2.arr[i][0] == 1):
                Code06_AngelDoll2.clear(Code06_AngelDoll2.arr[i][2])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code06_AngelDoll2.arr, l, jcast('int', jadd(r, 1)), (lambda a, b: (a[1] - b[1])))

    @staticmethod
    def cdq(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l == r):
            return
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        Code06_AngelDoll2.cdq(l, mid)
        Code06_AngelDoll2.cdq(jcast('int', jadd(mid, 1)), r)
        Code06_AngelDoll2.merge(l, mid, r)

    # 点变换到第一象限进行cdq分治
    @staticmethod
    def to1():
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cnte):
            Code06_AngelDoll2.clone(Code06_AngelDoll2.arr[i], Code06_AngelDoll2.tim[i])
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.cdq(1, Code06_AngelDoll2.cnte)

    # 点变换到第二象限进行cdq分治
    @staticmethod
    def to2():
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cnte):
            Code06_AngelDoll2.clone(Code06_AngelDoll2.arr[i], Code06_AngelDoll2.tim[i])
            jset(Code06_AngelDoll2.arr[i], 1, jcast('int', (Code06_AngelDoll2.v - Code06_AngelDoll2.arr[i][1])))
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.cdq(1, Code06_AngelDoll2.cnte)

    # 点变换到第三象限进行cdq分治
    @staticmethod
    def to3():
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cnte):
            Code06_AngelDoll2.clone(Code06_AngelDoll2.arr[i], Code06_AngelDoll2.tim[i])
            jset(Code06_AngelDoll2.arr[i], 1, jcast('int', (Code06_AngelDoll2.v - Code06_AngelDoll2.arr[i][1])))
            jset(Code06_AngelDoll2.arr[i], 2, jcast('int', (Code06_AngelDoll2.v - Code06_AngelDoll2.arr[i][2])))
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.cdq(1, Code06_AngelDoll2.cnte)

    # 点变换到第四象限进行cdq分治
    @staticmethod
    def to4():
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cnte):
            Code06_AngelDoll2.clone(Code06_AngelDoll2.arr[i], Code06_AngelDoll2.tim[i])
            jset(Code06_AngelDoll2.arr[i], 2, jcast('int', (Code06_AngelDoll2.v - Code06_AngelDoll2.arr[i][2])))
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.cdq(1, Code06_AngelDoll2.cnte)

    @staticmethod
    def main(args):
        in_ = Code06_AngelDoll2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code06_AngelDoll2.n = jcast('int', jcall(in_, 'nextInt'))
        Code06_AngelDoll2.m = jcast('int', jcall(in_, 'nextInt'))
        # 树状数组下标从1开始，所以x和y都要自增一下
        # x或y的最大值用v记录，变换象限时，防止 v - (x或y) 出现0
        # 所以最后v再自增一下
        i = jcast('int', 1)
        x = 0
        y = 0
        while (i <= Code06_AngelDoll2.n):
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            jset(Code06_AngelDoll2.tim[((_java_obj_1 := Code06_AngelDoll2), (_java_key_2 := 'cnte'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, 1)
            jset(Code06_AngelDoll2.tim[Code06_AngelDoll2.cnte], 1, (x := jcast('int', (x + (1)))))
            jset(Code06_AngelDoll2.tim[Code06_AngelDoll2.cnte], 2, (y := jcast('int', (y + (1)))))
            Code06_AngelDoll2.v = jcast('int', jstatic('Math', 'max', Code06_AngelDoll2.v, jstatic('Math', 'max', x, y)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code06_AngelDoll2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            jset(Code06_AngelDoll2.tim[((_java_obj_4 := Code06_AngelDoll2), (_java_key_5 := 'cnte'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, op)
            jset(Code06_AngelDoll2.tim[Code06_AngelDoll2.cnte], 1, (x := jcast('int', (x + (1)))))
            jset(Code06_AngelDoll2.tim[Code06_AngelDoll2.cnte], 2, (y := jcast('int', (y + (1)))))
            if (op == 2):
                jset(Code06_AngelDoll2.tim[Code06_AngelDoll2.cnte], 3, ((_java_obj_7 := Code06_AngelDoll2), (_java_key_8 := 'cntq'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
            Code06_AngelDoll2.v = jcast('int', jstatic('Math', 'max', Code06_AngelDoll2.v, jstatic('Math', 'max', x, y)))
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.v = jcast('int', (Code06_AngelDoll2.v + 1))
        # 初始化树状数组
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.v):
            Code06_AngelDoll2.tree[i] = jcast('int', jcast('int', (-Code06_AngelDoll2.INF)))
            i = jcast('int', (i + 1))
        # 初始化答案数组
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cntq):
            Code06_AngelDoll2.ans[i] = jcast('int', Code06_AngelDoll2.INF)
            i = jcast('int', (i + 1))
        Code06_AngelDoll2.to1()
        Code06_AngelDoll2.to2()
        Code06_AngelDoll2.to3()
        Code06_AngelDoll2.to4()
        i = jcast('int', 1)
        while (i <= Code06_AngelDoll2.cntq):
            jcall(out, 'println', Code06_AngelDoll2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_10 := self), (_java_key_11 := 'ptr'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]])

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
            raise TypeError("No matching overload for Code06_AngelDoll2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_AngelDoll2.MAXN = jcast('int', 300001)
Code06_AngelDoll2.MAXV = jcast('int', 1000002)
Code06_AngelDoll2.INF = jcast('int', 1000000001)
Code06_AngelDoll2.n = jcast('int', 0)
Code06_AngelDoll2.m = jcast('int', 0)
Code06_AngelDoll2.v = jcast('int', 0)
Code06_AngelDoll2.tim = jarray('int', [jcast('int', (Code06_AngelDoll2.MAXN << (1 & 31))), 4])
Code06_AngelDoll2.arr = jarray('int', [jcast('int', (Code06_AngelDoll2.MAXN << (1 & 31))), 4])
Code06_AngelDoll2.cnte = jcast('int', 0)
Code06_AngelDoll2.cntq = jcast('int', 0)
Code06_AngelDoll2.tree = jarray('int', [Code06_AngelDoll2.MAXV])
Code06_AngelDoll2.ans = jarray('int', [Code06_AngelDoll2.MAXN])

if __name__ == '__main__':
    Code06_AngelDoll2.main([])

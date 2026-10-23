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

# 混合果汁，Python版
# 一共有n种果汁，每种果汁给定，美味度d、每升价格p、添加上限l
# 制作混合果汁时每种果汁不能超过添加上限，其中美味度最低的果汁，决定混合果汁的美味度
# 一共有m个小朋友，给每位制作混合果汁时，钱数不超过money[i]，体积不少于least[i]
# 打印每个小朋友能得到的混合果汁最大美味度，如果无法满足，打印-1
# 1 <= n、m、d、p、l <= 10^5
# 1 <= money[i]、least[i] <= 10^18
# 测试链接 : https://www.luogu.com.cn/problem/P4602
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_Juice1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'juice': 'juice', 'qid': 'qid', 'money': 'money', 'least': 'least', 'maxp': 'maxp', 'suml': 'suml', 'cost': 'cost', 'used': 'used', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    # 果汁有三个参数，美味度d、每升价格p、添加上限l
    juice = None
    # 记录所有小朋友的编号
    qid = None
    # 小朋友能花的钱数
    money = None
    # 小朋友至少的果汁量
    least = None
    # 这种使用线段树的方式叫线段树二分
    # 讲解146的题目2，也涉及线段树二分
    # 果汁单价作为下标的线段树
    # maxp为最大的果汁单价
    maxp = 0
    # suml[i] : 线段树某单价区间上，允许添加的总量
    suml = None
    # cost[i] : 线段树某单价区间上，如果允许添加的总量全要，花费多少钱
    cost = None
    # 多少种果汁加入了线段树
    used = 0
    # 整体二分的过程需要
    lset = None
    rset = None
    # 每个小朋友的答案，是第几号果汁的美味度
    ans = None
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code01_Juice1.suml[i] = jcast('long', jcast('long', jadd(Code01_Juice1.suml[jcast('int', (i << (1 & 31)))], Code01_Juice1.suml[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))
        Code01_Juice1.cost[i] = jcast('long', jcast('long', jadd(Code01_Juice1.cost[jcast('int', (i << (1 & 31)))], Code01_Juice1.cost[jcast('int', (jcast('int', (i << (1 & 31))) | 1))])))

    # 单价为jobi，现在允许添加的量增加了jobv
    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            Code01_Juice1.suml[i] = jcast('long', jcast('long', jadd(Code01_Juice1.suml[i], jobv)))
            Code01_Juice1.cost[i] = jcast('long', jcast('long', (Code01_Juice1.suml[i] * l)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code01_Juice1.add(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code01_Juice1.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))
            Code01_Juice1.up(i)

    # 总体积一共volume，已知总体积一定能耗尽
    # 返回总体积耗尽的情况下，能花的最少钱数
    @staticmethod
    def query(volume, l, r, i):
        volume = jcast('long', volume)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if (l == r):
            return jcast('long', jcast('long', (volume * l)))
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (Code01_Juice1.suml[jcast('int', (i << (1 & 31)))] >= volume):
            return jcast('long', Code01_Juice1.query(volume, l, mid, jcast('int', (i << (1 & 31)))))
        else:
            return jcast('long', jcast('long', jadd(Code01_Juice1.cost[jcast('int', (i << (1 & 31)))], Code01_Juice1.query(jcast('long', (volume - Code01_Juice1.suml[jcast('int', (i << (1 & 31)))])), jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))

    @staticmethod
    def compute(ql, qr, vl, vr):
        ql = jcast('int', ql)
        qr = jcast('int', qr)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (ql > qr):
            return
        if (vl == vr):
            i = jcast('int', ql)
            while (i <= qr):
                jset(Code01_Juice1.ans, Code01_Juice1.qid[i], vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            # 线段树包含果汁的种类少就添加
            while (Code01_Juice1.used < mid):
                Code01_Juice1.used = jcast('int', (Code01_Juice1.used + 1))
                Code01_Juice1.add(Code01_Juice1.juice[Code01_Juice1.used][1], Code01_Juice1.juice[Code01_Juice1.used][2], 1, Code01_Juice1.maxp, 1)
            # 线段树包含果汁的种类多就撤销
            while (Code01_Juice1.used > mid):
                Code01_Juice1.add(Code01_Juice1.juice[Code01_Juice1.used][1], jcast('int', (-Code01_Juice1.juice[Code01_Juice1.used][2])), 1, Code01_Juice1.maxp, 1)
                Code01_Juice1.used = jcast('int', (Code01_Juice1.used - 1))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', ql)
            id = 0
            while (i <= qr):
                id = jcast('int', Code01_Juice1.qid[i])
                if ((Code01_Juice1.suml[1] >= Code01_Juice1.least[id]) and (Code01_Juice1.query(Code01_Juice1.least[id], 1, Code01_Juice1.maxp, 1) <= Code01_Juice1.money[id])):
                    jset(Code01_Juice1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                else:
                    jset(Code01_Juice1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code01_Juice1.qid[jcast('int', (jcast('int', jadd(ql, i)) - 1))] = jcast('int', Code01_Juice1.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code01_Juice1.qid[jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), i)) - 1))] = jcast('int', Code01_Juice1.rset[i])
                i = jcast('int', (i + 1))
            Code01_Juice1.compute(ql, jcast('int', (jcast('int', jadd(ql, lsiz)) - 1)), vl, mid)
            Code01_Juice1.compute(jcast('int', jadd(ql, lsiz)), qr, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code01_Juice1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_Juice1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_Juice1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_Juice1.n):
            jset(Code01_Juice1.juice[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_Juice1.juice[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_Juice1.juice[i], 2, jcall(in_, 'nextInt'))
            Code01_Juice1.maxp = jcast('int', jstatic('Math', 'max', Code01_Juice1.maxp, Code01_Juice1.juice[i][1]))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_Juice1.m):
            Code01_Juice1.qid[i] = jcast('int', i)
            jset(Code01_Juice1.money, i, jcall(in_, 'nextLong'))
            jset(Code01_Juice1.least, i, jcall(in_, 'nextLong'))
            i = jcast('int', (i + 1))
        # 所有果汁按照美味度排序，美味度大的在前，美味度小的在后
        jstatic('Arrays', 'sort', Code01_Juice1.juice, 1, jcast('int', jadd(Code01_Juice1.n, 1)), (lambda a, b: (b[0] - a[0])))
        # 答案范围就是美味度范围，从最美味的第1名，到最难喝的第n名
        # 如果小朋友答案为n+1，说明无法满足这个小朋友
        Code01_Juice1.compute(1, Code01_Juice1.m, 1, jcast('int', jadd(Code01_Juice1.n, 1)))
        i = jcast('int', 1)
        while (i <= Code01_Juice1.m):
            if (Code01_Juice1.ans[i] == jcast('int', jadd(Code01_Juice1.n, 1))):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                jcall(out, 'println', Code01_Juice1.juice[Code01_Juice1.ans[i]][0])
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

        def nextLong(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            val = jcast('long', 0)
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                val = jcast('long', jcast('long', jadd(jcast('long', (val * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            return jcast('long', (jcast('long', (-val)) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code01_Juice1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_Juice1.MAXN = jcast('int', 100001)
Code01_Juice1.n = jcast('int', 0)
Code01_Juice1.m = jcast('int', 0)
Code01_Juice1.juice = jarray('int', [Code01_Juice1.MAXN, 3])
Code01_Juice1.qid = jarray('int', [Code01_Juice1.MAXN])
Code01_Juice1.money = jarray('long', [Code01_Juice1.MAXN])
Code01_Juice1.least = jarray('long', [Code01_Juice1.MAXN])
Code01_Juice1.maxp = jcast('int', 0)
Code01_Juice1.suml = jarray('long', [jcast('int', (Code01_Juice1.MAXN << (2 & 31)))])
Code01_Juice1.cost = jarray('long', [jcast('int', (Code01_Juice1.MAXN << (2 & 31)))])
Code01_Juice1.used = jcast('int', 0)
Code01_Juice1.lset = jarray('int', [Code01_Juice1.MAXN])
Code01_Juice1.rset = jarray('int', [Code01_Juice1.MAXN])
Code01_Juice1.ans = jarray('int', [Code01_Juice1.MAXN])

if __name__ == '__main__':
    Code01_Juice1.main([])

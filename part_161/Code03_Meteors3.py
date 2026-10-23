# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 陨石雨，第一种写法，Python版
# 一共有n个国家，给定n个数字，表示每个国家希望收集到的陨石数量
# 一共有m个区域，1号区顺时针到2号区...m号区顺时针到1号区，即环形相连
# 每个区域只属于某一个国家，给定m个数字，表示每个区域归属给哪个国家
# 接下来会依次发生k场陨石雨，陨石雨格式 l r num，含义如下
# 从l号区顺时针到r号区发生了陨石雨，每个区域都增加num个陨石
# 打印每个国家经历前几场陨石雨，可以达到收集要求，如果无法满足，打印"NIE"
# 1 <= n、m、k <= 3 * 10^5    1 <= 陨石数量 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3527
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_Meteors3:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'k': 'k', 'qid': 'qid', 'need': 'need', 'rainl': 'rainl', 'rainr': 'rainr', 'num': 'num', 'head': 'head', 'next': 'next', 'to': 'to', 'cnt': 'cnt', 'tree': 'tree', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans'}
    MAXN = 0
    n = 0
    m = 0
    k = 0
    # 国家编号
    qid = None
    # 国家的需求
    need = None
    # 陨石雨的参数
    rainl = None
    rainr = None
    num = None
    # 国家拥有的区域列表
    head = None
    next = None
    to = None
    cnt = 0
    # 树状数组，支持范围修改、单点查询
    tree = None
    # 整体二分
    lset = None
    rset = None
    # 每个国家的答案
    ans = None
    @staticmethod
    def addEdge(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        jset(Code03_Meteors3.next, ((_java_obj_1 := Code03_Meteors3), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_Meteors3.head[i])
        Code03_Meteors3.to[Code03_Meteors3.cnt] = jcast('int', v)
        Code03_Meteors3.head[i] = jcast('int', Code03_Meteors3.cnt)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def _java_add_0(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        siz = jcast('int', jcast('int', (Code03_Meteors3.m * 2)))
        while (i <= siz):
            Code03_Meteors3.tree[i] = jcast('long', jcast('long', jadd(Code03_Meteors3.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code03_Meteors3.lowbit(i))))

    @staticmethod
    def _java_add_1(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        Code03_Meteors3._java_add_0(l, v)
        Code03_Meteors3._java_add_0(jcast('int', jadd(r, 1)), jcast('int', (-v)))

    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('long', 0)
        while (i > 0):
            ret = jcast('long', jcast('long', jadd(ret, Code03_Meteors3.tree[i])))
            i = jcast('int', jcast('int', (i - Code03_Meteors3.lowbit(i))))
        return jcast('long', ret)

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
                jset(Code03_Meteors3.ans, Code03_Meteors3.qid[i], vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            i = jcast('int', vl)
            while (i <= mid):
                Code03_Meteors3._java_add_1(Code03_Meteors3.rainl[i], Code03_Meteors3.rainr[i], Code03_Meteors3.num[i])
                i = jcast('int', (i + 1))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', ql)
            while (i <= qr):
                try:
                    id = jcast('int', Code03_Meteors3.qid[i])
                    satisfy = jcast('long', 0)
                    e = jcast('int', Code03_Meteors3.head[id])
                    while (e > 0):
                        try:
                            satisfy = jcast('long', jcast('long', jadd(satisfy, jcast('long', jadd(Code03_Meteors3.query(Code03_Meteors3.to[e]), Code03_Meteors3.query(jcast('int', jadd(Code03_Meteors3.to[e], Code03_Meteors3.m))))))))
                            if (satisfy >= Code03_Meteors3.need[id]):
                                raise JBreak(None)
                        except JContinue as _java_control_5:
                            if _java_control_5.label not in (None,):
                                raise
                        except JBreak as _java_control_5:
                            if _java_control_5.label not in (None,):
                                raise
                            break
                        e = jcast('int', Code03_Meteors3.next[e])
                    if (satisfy >= Code03_Meteors3.need[id]):
                        jset(Code03_Meteors3.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                    else:
                        Code03_Meteors3.need[id] = jcast('int', jcast('long', (Code03_Meteors3.need[id] - satisfy)))
                        jset(Code03_Meteors3.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                except JContinue as _java_control_4:
                    if _java_control_4.label not in (None,):
                        raise
                except JBreak as _java_control_4:
                    if _java_control_4.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= lsiz):
                Code03_Meteors3.qid[jcast('int', (jcast('int', jadd(ql, i)) - 1))] = jcast('int', Code03_Meteors3.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code03_Meteors3.qid[jcast('int', (jcast('int', jadd(jcast('int', jadd(ql, lsiz)), i)) - 1))] = jcast('int', Code03_Meteors3.rset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', vl)
            while (i <= mid):
                Code03_Meteors3._java_add_1(Code03_Meteors3.rainl[i], Code03_Meteors3.rainr[i], jcast('int', (-Code03_Meteors3.num[i])))
                i = jcast('int', (i + 1))
            Code03_Meteors3.compute(ql, jcast('int', (jcast('int', jadd(ql, lsiz)) - 1)), vl, mid)
            Code03_Meteors3.compute(jcast('int', jadd(ql, lsiz)), qr, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code03_Meteors3.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_Meteors3.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_Meteors3.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        nation = 0
        while (i <= Code03_Meteors3.m):
            nation = jcast('int', jcall(in_, 'nextInt'))
            Code03_Meteors3.addEdge(nation, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_Meteors3.n):
            Code03_Meteors3.qid[i] = jcast('int', i)
            jset(Code03_Meteors3.need, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code03_Meteors3.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_Meteors3.k):
            jset(Code03_Meteors3.rainl, i, jcall(in_, 'nextInt'))
            jset(Code03_Meteors3.rainr, i, jcall(in_, 'nextInt'))
            if (Code03_Meteors3.rainr[i] < Code03_Meteors3.rainl[i]):
                Code03_Meteors3.rainr[i] = jcast('int', jcast('int', jadd(Code03_Meteors3.rainr[i], Code03_Meteors3.m)))
            jset(Code03_Meteors3.num, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        # 答案范围[1..k+1]，第k+1场陨石雨认为满足不了要求
        Code03_Meteors3.compute(1, Code03_Meteors3.n, 1, jcast('int', jadd(Code03_Meteors3.k, 1)))
        i = jcast('int', 1)
        while (i <= Code03_Meteors3.n):
            if (Code03_Meteors3.ans[i] == jcast('int', jadd(Code03_Meteors3.k, 1))):
                jcall(out, 'println', 'NIE')
            else:
                jcall(out, 'println', Code03_Meteors3.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_6 := self), (_java_key_7 := 'ptr'), (_java_old_8 := jget(_java_obj_6, _java_key_7)), jset(_java_obj_6, _java_key_7, jcast('int', (_java_old_8 + (1)))), _java_old_8)[4]])

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
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_Meteors3.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code03_Meteors3._java_add_0(*args)
        if _java_choice == 1:
            return Code03_Meteors3._java_add_1(*args)
        raise TypeError("No matching overload for Code03_Meteors3.add")


Code03_Meteors3.MAXN = jcast('int', 300001)
Code03_Meteors3.n = jcast('int', 0)
Code03_Meteors3.m = jcast('int', 0)
Code03_Meteors3.k = jcast('int', 0)
Code03_Meteors3.qid = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.need = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.rainl = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.rainr = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.num = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.head = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.next = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.to = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.cnt = jcast('int', 0)
Code03_Meteors3.tree = jarray('long', [jcast('int', (Code03_Meteors3.MAXN << (1 & 31)))])
Code03_Meteors3.lset = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.rset = jarray('int', [Code03_Meteors3.MAXN])
Code03_Meteors3.ans = jarray('int', [Code03_Meteors3.MAXN])

if __name__ == '__main__':
    Code03_Meteors3.main([])

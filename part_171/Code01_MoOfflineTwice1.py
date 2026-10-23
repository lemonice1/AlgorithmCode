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

# 莫队二次离线入门题，Python版
# 给定一个长度为n的数组arr，给定一个非负整数k，下面给出k1二元组的定义
# 位置二元组(i, j)，i和j必须是不同的，并且 arr[i]异或arr[j] 的二进制状态里有k个1
# 当i != j时，(i, j)和(j, i)认为是相同的二元组
# 一共有m条查询，格式为 l r : 打印arr[l..r]范围上，有多少k1二元组
# 1 <= n、m <= 10^5
# 0 <= arr[i]、k < 16384(2的14次方)
# 测试链接 : https://www.luogu.com.cn/problem/P4887
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code01_MoOfflineTwice2.py
# 两个版本保留相同的算法逻辑
class Code01_MoOfflineTwice1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXV': 'MAXV', 'n': 'n', 'm': 'm', 'k': 'k', 'arr': 'arr', 'bi': 'bi', 'kOneArr': 'kOneArr', 'cntk': 'cntk', 'query': 'query', 'headl': 'headl', 'headr': 'headr', 'nextq': 'nextq', 'ql': 'ql', 'qr': 'qr', 'qop': 'qop', 'qid': 'qid', 'cntq': 'cntq', 'cnt': 'cnt', 'pre': 'pre', 'suf': 'suf', 'ans': 'ans'}
    MAXN = 0
    MAXV = 0
    n = 0
    m = 0
    k = 0
    arr = None
    bi = None
    kOneArr = None
    cntk = 0
    # 莫队任务，l、r、id
    query = None
    # 离线任务，x、l、r、op、id
    # 位置x的任务列表用链式前向星表示
    # headl[x]，x在l~r左侧的离线任务列表
    # headr[x]，x在l~r右侧的离线任务列表
    headl = None
    headr = None
    nextq = None
    ql = None
    qr = None
    qop = None
    qid = None
    cntq = 0
    # cnt[v] : 当前的数字v作为第二个数，之前出现的数字作为第一个数，产生多少k1二元组
    cnt = None
    # 前缀和
    pre = None
    # 后缀和
    suf = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code01_MoOfflineTwice1.bi[a[0]] != Code01_MoOfflineTwice1.bi[b[0]]):
                return jcast('int', jcast('int', (Code01_MoOfflineTwice1.bi[a[0]] - Code01_MoOfflineTwice1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def countOne(num):
        num = jcast('int', num)
        ret = jcast('int', 0)
        while (num > 0):
            ret = jcast('int', (ret + 1))
            num = jcast('int', jcast('int', (num - Code01_MoOfflineTwice1.lowbit(num))))
        return jcast('int', ret)

    @staticmethod
    def addLeftOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code01_MoOfflineTwice1.nextq, ((_java_obj_1 := Code01_MoOfflineTwice1), (_java_key_2 := 'cntq'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code01_MoOfflineTwice1.headl[x])
        Code01_MoOfflineTwice1.headl[x] = jcast('int', Code01_MoOfflineTwice1.cntq)
        Code01_MoOfflineTwice1.ql[Code01_MoOfflineTwice1.cntq] = jcast('int', l)
        Code01_MoOfflineTwice1.qr[Code01_MoOfflineTwice1.cntq] = jcast('int', r)
        Code01_MoOfflineTwice1.qop[Code01_MoOfflineTwice1.cntq] = jcast('int', op)
        Code01_MoOfflineTwice1.qid[Code01_MoOfflineTwice1.cntq] = jcast('int', id)

    @staticmethod
    def addRightOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code01_MoOfflineTwice1.nextq, ((_java_obj_4 := Code01_MoOfflineTwice1), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code01_MoOfflineTwice1.headr[x])
        Code01_MoOfflineTwice1.headr[x] = jcast('int', Code01_MoOfflineTwice1.cntq)
        Code01_MoOfflineTwice1.ql[Code01_MoOfflineTwice1.cntq] = jcast('int', l)
        Code01_MoOfflineTwice1.qr[Code01_MoOfflineTwice1.cntq] = jcast('int', r)
        Code01_MoOfflineTwice1.qop[Code01_MoOfflineTwice1.cntq] = jcast('int', op)
        Code01_MoOfflineTwice1.qid[Code01_MoOfflineTwice1.cntq] = jcast('int', id)

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code01_MoOfflineTwice1.n)))
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.n):
            Code01_MoOfflineTwice1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_MoOfflineTwice1.query, 1, jcast('int', jadd(Code01_MoOfflineTwice1.m, 1)), Code01_MoOfflineTwice1.QueryCmp())
        v = jcast('int', 0)
        while (v < Code01_MoOfflineTwice1.MAXV):
            if (Code01_MoOfflineTwice1.countOne(v) == Code01_MoOfflineTwice1.k):
                jset(Code01_MoOfflineTwice1.kOneArr, ((_java_obj_7 := Code01_MoOfflineTwice1), (_java_key_8 := 'cntk'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], v)
            v = jcast('int', (v + 1))

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.n):
            Code01_MoOfflineTwice1.pre[i] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.pre[jcast('int', (i - 1))], Code01_MoOfflineTwice1.cnt[Code01_MoOfflineTwice1.arr[i]])))
            j = jcast('int', 1)
            while (j <= Code01_MoOfflineTwice1.cntk):
                ((_java_obj_10 := Code01_MoOfflineTwice1.cnt), (_java_key_11 := jcast('int', (Code01_MoOfflineTwice1.arr[i] ^ Code01_MoOfflineTwice1.kOneArr[j]))), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code01_MoOfflineTwice1.cnt, 0)
        i = jcast('int', Code01_MoOfflineTwice1.n)
        while (i >= 1):
            Code01_MoOfflineTwice1.suf[i] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.suf[jcast('int', jadd(i, 1))], Code01_MoOfflineTwice1.cnt[Code01_MoOfflineTwice1.arr[i]])))
            j = jcast('int', 1)
            while (j <= Code01_MoOfflineTwice1.cntk):
                ((_java_obj_13 := Code01_MoOfflineTwice1.cnt), (_java_key_14 := jcast('int', (Code01_MoOfflineTwice1.arr[i] ^ Code01_MoOfflineTwice1.kOneArr[j]))), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))), _java_old_15)[4]
                j = jcast('int', (j + 1))
            i = jcast('int', (i - 1))
        # 执行莫队
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.m):
            jobl = jcast('int', Code01_MoOfflineTwice1.query[i][0])
            jobr = jcast('int', Code01_MoOfflineTwice1.query[i][1])
            id = jcast('int', Code01_MoOfflineTwice1.query[i][2])
            if (winr < jobr):
                Code01_MoOfflineTwice1.addLeftOffline(jcast('int', (winl - 1)), jcast('int', jadd(winr, 1)), jobr, jcast('int', (-1)), id)
                Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.ans[id], jcast('long', (Code01_MoOfflineTwice1.pre[jobr] - Code01_MoOfflineTwice1.pre[winr])))))
            if (winr > jobr):
                Code01_MoOfflineTwice1.addLeftOffline(jcast('int', (winl - 1)), jcast('int', jadd(jobr, 1)), winr, 1, id)
                Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', (Code01_MoOfflineTwice1.ans[id] - jcast('long', (Code01_MoOfflineTwice1.pre[winr] - Code01_MoOfflineTwice1.pre[jobr])))))
            winr = jcast('int', jobr)
            if (winl > jobl):
                Code01_MoOfflineTwice1.addRightOffline(jcast('int', jadd(winr, 1)), jobl, jcast('int', (winl - 1)), jcast('int', (-1)), id)
                Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.ans[id], jcast('long', (Code01_MoOfflineTwice1.suf[jobl] - Code01_MoOfflineTwice1.suf[winl])))))
            if (winl < jobl):
                Code01_MoOfflineTwice1.addRightOffline(jcast('int', jadd(winr, 1)), winl, jcast('int', (jobl - 1)), 1, id)
                Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', (Code01_MoOfflineTwice1.ans[id] - jcast('long', (Code01_MoOfflineTwice1.suf[winl] - Code01_MoOfflineTwice1.suf[jobl])))))
            winl = jcast('int', jobl)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code01_MoOfflineTwice1.cnt, 0)
        x = jcast('int', 0)
        while (x <= Code01_MoOfflineTwice1.n):
            if (x >= 1):
                j = jcast('int', 1)
                while (j <= Code01_MoOfflineTwice1.cntk):
                    ((_java_obj_16 := Code01_MoOfflineTwice1.cnt), (_java_key_17 := jcast('int', (Code01_MoOfflineTwice1.arr[x] ^ Code01_MoOfflineTwice1.kOneArr[j]))), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))), _java_old_18)[4]
                    j = jcast('int', (j + 1))
            q = jcast('int', Code01_MoOfflineTwice1.headl[x])
            while (q > 0):
                l = jcast('int', Code01_MoOfflineTwice1.ql[q])
                r = jcast('int', Code01_MoOfflineTwice1.qr[q])
                op = jcast('int', Code01_MoOfflineTwice1.qop[q])
                id = jcast('int', Code01_MoOfflineTwice1.qid[q])
                j = jcast('int', l)
                while (j <= r):
                    Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.ans[id], jcast('long', (jcast('long', op) * Code01_MoOfflineTwice1.cnt[Code01_MoOfflineTwice1.arr[j]])))))
                    j = jcast('int', (j + 1))
                q = jcast('int', Code01_MoOfflineTwice1.nextq[q])
            x = jcast('int', (x + 1))
        jstatic('Arrays', 'fill', Code01_MoOfflineTwice1.cnt, 0)
        x = jcast('int', jcast('int', jadd(Code01_MoOfflineTwice1.n, 1)))
        while (x >= 1):
            if (x <= Code01_MoOfflineTwice1.n):
                j = jcast('int', 1)
                while (j <= Code01_MoOfflineTwice1.cntk):
                    ((_java_obj_19 := Code01_MoOfflineTwice1.cnt), (_java_key_20 := jcast('int', (Code01_MoOfflineTwice1.arr[x] ^ Code01_MoOfflineTwice1.kOneArr[j]))), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]
                    j = jcast('int', (j + 1))
            q = jcast('int', Code01_MoOfflineTwice1.headr[x])
            while (q > 0):
                l = jcast('int', Code01_MoOfflineTwice1.ql[q])
                r = jcast('int', Code01_MoOfflineTwice1.qr[q])
                op = jcast('int', Code01_MoOfflineTwice1.qop[q])
                id = jcast('int', Code01_MoOfflineTwice1.qid[q])
                j = jcast('int', l)
                while (j <= r):
                    Code01_MoOfflineTwice1.ans[id] = jcast('long', jcast('long', jadd(Code01_MoOfflineTwice1.ans[id], jcast('long', (jcast('long', op) * Code01_MoOfflineTwice1.cnt[Code01_MoOfflineTwice1.arr[j]])))))
                    j = jcast('int', (j + 1))
                q = jcast('int', Code01_MoOfflineTwice1.nextq[q])
            x = jcast('int', (x - 1))

    @staticmethod
    def main(args):
        in_ = Code01_MoOfflineTwice1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_MoOfflineTwice1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_MoOfflineTwice1.m = jcast('int', jcall(in_, 'nextInt'))
        Code01_MoOfflineTwice1.k = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.n):
            jset(Code01_MoOfflineTwice1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.m):
            jset(Code01_MoOfflineTwice1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_MoOfflineTwice1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_MoOfflineTwice1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code01_MoOfflineTwice1.prepare()
        Code01_MoOfflineTwice1.compute()
        # ans[i]代表答案变化量
        # 所以加工出前缀和才是每个查询的答案
        # 注意在普通莫队的顺序下，去生成前缀和
        i = jcast('int', 2)
        while (i <= Code01_MoOfflineTwice1.m):
            ((_java_obj_22 := Code01_MoOfflineTwice1.ans), (_java_key_23 := Code01_MoOfflineTwice1.query[i][2]), jset(_java_obj_22, _java_key_23, jcast('long', jadd(jget(_java_obj_22, _java_key_23), Code01_MoOfflineTwice1.ans[Code01_MoOfflineTwice1.query[jcast('int', (i - 1))][2]]))))[2]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code01_MoOfflineTwice1.m):
            jcall(out, 'println', Code01_MoOfflineTwice1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_24 := self), (_java_key_25 := 'ptr'), (_java_old_26 := jget(_java_obj_24, _java_key_25)), jset(_java_obj_24, _java_key_25, jcast('int', (_java_old_26 + (1)))), _java_old_26)[4]])

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
            raise TypeError("No matching overload for Code01_MoOfflineTwice1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_MoOfflineTwice1.MAXN = jcast('int', 100002)
Code01_MoOfflineTwice1.MAXV = jcast('int', jcast('int', (1 << (14 & 31))))
Code01_MoOfflineTwice1.n = jcast('int', 0)
Code01_MoOfflineTwice1.m = jcast('int', 0)
Code01_MoOfflineTwice1.k = jcast('int', 0)
Code01_MoOfflineTwice1.arr = jarray('int', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.bi = jarray('int', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.kOneArr = jarray('int', [Code01_MoOfflineTwice1.MAXV])
Code01_MoOfflineTwice1.cntk = jcast('int', 0)
Code01_MoOfflineTwice1.query = jarray('int', [Code01_MoOfflineTwice1.MAXN, 3])
Code01_MoOfflineTwice1.headl = jarray('int', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.headr = jarray('int', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.nextq = jarray('int', [jcast('int', (Code01_MoOfflineTwice1.MAXN << (1 & 31)))])
Code01_MoOfflineTwice1.ql = jarray('int', [jcast('int', (Code01_MoOfflineTwice1.MAXN << (1 & 31)))])
Code01_MoOfflineTwice1.qr = jarray('int', [jcast('int', (Code01_MoOfflineTwice1.MAXN << (1 & 31)))])
Code01_MoOfflineTwice1.qop = jarray('int', [jcast('int', (Code01_MoOfflineTwice1.MAXN << (1 & 31)))])
Code01_MoOfflineTwice1.qid = jarray('int', [jcast('int', (Code01_MoOfflineTwice1.MAXN << (1 & 31)))])
Code01_MoOfflineTwice1.cntq = jcast('int', 0)
Code01_MoOfflineTwice1.cnt = jarray('int', [Code01_MoOfflineTwice1.MAXV])
Code01_MoOfflineTwice1.pre = jarray('long', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.suf = jarray('long', [Code01_MoOfflineTwice1.MAXN])
Code01_MoOfflineTwice1.ans = jarray('long', [Code01_MoOfflineTwice1.MAXN])

if __name__ == '__main__':
    Code01_MoOfflineTwice1.main([])

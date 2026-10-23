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

# 区间倍数二元组，Python版
# 给定一个长度为n的数组arr，下面给出倍数二元组的定义
# 如果arr[i]是arr[j]的倍数(>=1倍)，那么(i, j)就是一个倍数二元组
# 当i != j时，(i, j)和(j, i)认为是不同的二元组，不要漏算
# 当i == j时，(i, j)和(j, i)认为是相同的二元组，不要多算
# 比如[2, 4, 2, 6]，有10个倍数二元组
# 一共有m条查询，格式为 l r : 打印arr[l..r]范围上，有多少倍数二元组
# 1 <= n、m、arr[i] <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5398
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code04_Gosick2.py
# 两个版本保留相同的算法逻辑
class Code04_Gosick1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXF': 'MAXF', 'LIMIT': 'LIMIT', 'n': 'n', 'm': 'm', 'maxv': 'maxv', 'arr': 'arr', 'bi': 'bi', 'headf': 'headf', 'nextf': 'nextf', 'fac': 'fac', 'cntf': 'cntf', 'query': 'query', 'headq': 'headq', 'nextq': 'nextq', 'qx': 'qx', 'ql': 'ql', 'qr': 'qr', 'qop': 'qop', 'qid': 'qid', 'cntq': 'cntq', 'xcnt': 'xcnt', 'vcnt': 'vcnt', 'pre': 'pre', 'ans': 'ans'}
    MAXN = 0
    MAXF = 0
    LIMIT = 0
    n = 0
    m = 0
    maxv = 0
    arr = None
    bi = None
    # 每个数的因子表，用链式前向星表达
    headf = None
    nextf = None
    fac = None
    cntf = 0
    # 莫队任务
    query = None
    # 二次离线的任务，也是链式前向星
    headq = None
    nextq = None
    qx = None
    ql = None
    qr = None
    qop = None
    qid = None
    cntq = 0
    # xcnt[v] = 之前出现的数中，有多少数是此时数字v的倍数
    xcnt = None
    # vcnt[v] = 之前出现的数中，数字v出现了多少次
    vcnt = None
    # 前缀信息
    pre = None
    ans = None
    class QueryCmp:
        __java_fields__ = {}
        def compare(self, a, b):
            if (Code04_Gosick1.bi[a[0]] != Code04_Gosick1.bi[b[0]]):
                return jcast('int', jcast('int', (Code04_Gosick1.bi[a[0]] - Code04_Gosick1.bi[b[0]])))
            return jcast('int', jcast('int', (a[1] - b[1])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    @staticmethod
    def addFactors(num):
        num = jcast('int', num)
        if (Code04_Gosick1.headf[num] == 0):
            f = jcast('int', 1)
            while (jcast('int', (f * f)) <= num):
                if (jcast('int', jmod(num, f)) == 0):
                    jset(Code04_Gosick1.nextf, ((_java_obj_1 := Code04_Gosick1), (_java_key_2 := 'cntf'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Gosick1.headf[num])
                    Code04_Gosick1.fac[Code04_Gosick1.cntf] = jcast('int', f)
                    Code04_Gosick1.headf[num] = jcast('int', Code04_Gosick1.cntf)
                f = jcast('int', (f + 1))

    @staticmethod
    def addOffline(x, l, r, op, id):
        x = jcast('int', x)
        l = jcast('int', l)
        r = jcast('int', r)
        op = jcast('int', op)
        id = jcast('int', id)
        jset(Code04_Gosick1.nextq, ((_java_obj_4 := Code04_Gosick1), (_java_key_5 := 'cntq'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], Code04_Gosick1.headq[x])
        Code04_Gosick1.headq[x] = jcast('int', Code04_Gosick1.cntq)
        Code04_Gosick1.qx[Code04_Gosick1.cntq] = jcast('int', x)
        Code04_Gosick1.ql[Code04_Gosick1.cntq] = jcast('int', l)
        Code04_Gosick1.qr[Code04_Gosick1.cntq] = jcast('int', r)
        Code04_Gosick1.qop[Code04_Gosick1.cntq] = jcast('int', op)
        Code04_Gosick1.qid[Code04_Gosick1.cntq] = jcast('int', id)

    @staticmethod
    def compute():
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.n):
            num = jcast('int', Code04_Gosick1.arr[i])
            Code04_Gosick1.pre[i] = jcast('long', Code04_Gosick1.pre[jcast('int', (i - 1))])
            Code04_Gosick1.pre[i] = jcast('long', jcast('long', jadd(Code04_Gosick1.pre[i], Code04_Gosick1.xcnt[num])))
            e = jcast('int', Code04_Gosick1.headf[num])
            f = 0
            other = 0
            while (e > 0):
                f = jcast('int', Code04_Gosick1.fac[e])
                other = jcast('int', jcast('int', jdiv(num, f)))
                Code04_Gosick1.xcnt[f] = jcast('int', (Code04_Gosick1.xcnt[f] + 1))
                Code04_Gosick1.pre[i] = jcast('long', jcast('long', jadd(Code04_Gosick1.pre[i], Code04_Gosick1.vcnt[f])))
                if (other != f):
                    Code04_Gosick1.xcnt[other] = jcast('int', (Code04_Gosick1.xcnt[other] + 1))
                    Code04_Gosick1.pre[i] = jcast('long', jcast('long', jadd(Code04_Gosick1.pre[i], Code04_Gosick1.vcnt[other])))
                e = jcast('int', Code04_Gosick1.nextf[e])
            Code04_Gosick1.vcnt[num] = jcast('int', (Code04_Gosick1.vcnt[num] + 1))
            i = jcast('int', (i + 1))
        # 第一次离线，执行莫队
        winl = jcast('int', 1)
        winr = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.m):
            jobl = jcast('int', Code04_Gosick1.query[i][0])
            jobr = jcast('int', Code04_Gosick1.query[i][1])
            id = jcast('int', Code04_Gosick1.query[i][2])
            if (winr < jobr):
                Code04_Gosick1.addOffline(jcast('int', (winl - 1)), jcast('int', jadd(winr, 1)), jobr, jcast('int', (-1)), id)
                Code04_Gosick1.ans[id] = jcast('long', jcast('long', jadd(Code04_Gosick1.ans[id], jcast('long', (Code04_Gosick1.pre[jobr] - Code04_Gosick1.pre[winr])))))
            if (winr > jobr):
                Code04_Gosick1.addOffline(jcast('int', (winl - 1)), jcast('int', jadd(jobr, 1)), winr, 1, id)
                Code04_Gosick1.ans[id] = jcast('long', jcast('long', (Code04_Gosick1.ans[id] - jcast('long', (Code04_Gosick1.pre[winr] - Code04_Gosick1.pre[jobr])))))
            winr = jcast('int', jobr)
            # 接下来是winl滑动
            # 课上重点图解了，需要考虑 (2 * 滑动长度) 的修正
            if (winl > jobl):
                Code04_Gosick1.addOffline(winr, jobl, jcast('int', (winl - 1)), 1, id)
                Code04_Gosick1.ans[id] = jcast('long', jcast('long', (Code04_Gosick1.ans[id] - jcast('long', jadd(jcast('long', (Code04_Gosick1.pre[jcast('int', (winl - 1))] - Code04_Gosick1.pre[jcast('int', (jobl - 1))])), jcast('int', (2 * jcast('int', (winl - jobl)))))))))
            if (winl < jobl):
                Code04_Gosick1.addOffline(winr, winl, jcast('int', (jobl - 1)), jcast('int', (-1)), id)
                Code04_Gosick1.ans[id] = jcast('long', jcast('long', jadd(Code04_Gosick1.ans[id], jcast('long', jadd(jcast('long', (Code04_Gosick1.pre[jcast('int', (jobl - 1))] - Code04_Gosick1.pre[jcast('int', (winl - 1))])), jcast('int', (2 * jcast('int', (jobl - winl)))))))))
            winl = jcast('int', jobl)
            i = jcast('int', (i + 1))
        # 第二次离线，num倍数的数量 + num一部分因子的数量，都计入xcnt[num]
        jstatic('Arrays', 'fill', Code04_Gosick1.xcnt, 0)
        x = jcast('int', 0)
        while (x <= Code04_Gosick1.n):
            if (x >= 1):
                num = jcast('int', Code04_Gosick1.arr[x])
                e = jcast('int', Code04_Gosick1.headf[num])
                f = 0
                other = 0
                while (e > 0):
                    f = jcast('int', Code04_Gosick1.fac[e])
                    other = jcast('int', jcast('int', jdiv(num, f)))
                    Code04_Gosick1.xcnt[f] = jcast('int', (Code04_Gosick1.xcnt[f] + 1))
                    if (other != f):
                        Code04_Gosick1.xcnt[other] = jcast('int', (Code04_Gosick1.xcnt[other] + 1))
                    e = jcast('int', Code04_Gosick1.nextf[e])
                # 只处理大于LIMIT值的num
                if (num > Code04_Gosick1.LIMIT):
                    v = jcast('int', num)
                    while (v <= Code04_Gosick1.maxv):
                        Code04_Gosick1.xcnt[v] = jcast('int', (Code04_Gosick1.xcnt[v] + 1))
                        v = jcast('int', jcast('int', jadd(v, num)))
            q = jcast('int', Code04_Gosick1.headq[x])
            while (q > 0):
                l = jcast('int', Code04_Gosick1.ql[q])
                r = jcast('int', Code04_Gosick1.qr[q])
                op = jcast('int', Code04_Gosick1.qop[q])
                id = jcast('int', Code04_Gosick1.qid[q])
                j = jcast('int', l)
                while (j <= r):
                    Code04_Gosick1.ans[id] = jcast('long', jcast('long', jadd(Code04_Gosick1.ans[id], jcast('long', (jcast('long', op) * Code04_Gosick1.xcnt[Code04_Gosick1.arr[j]])))))
                    j = jcast('int', (j + 1))
                q = jcast('int', Code04_Gosick1.nextq[q])
            x = jcast('int', (x + 1))
        # 第三次离线，1 ~ LIMIT 这些因子是少算了的，如今补回来
        v = jcast('int', 1)
        while (v <= Code04_Gosick1.LIMIT):
            # 复用vcnt和xcnt
            # vcnt[i]，当前表示，1~i范围上，v出现的次数
            # xcnt[i]，当前表示，1~i范围上，v的倍数出现的次数
            jset(Code04_Gosick1.vcnt, 0, jset(Code04_Gosick1.xcnt, 0, 0))
            i = jcast('int', 1)
            while (i <= Code04_Gosick1.n):
                Code04_Gosick1.vcnt[i] = jcast('int', jcast('int', jadd(Code04_Gosick1.vcnt[jcast('int', (i - 1))], (1 if (Code04_Gosick1.arr[i] == v) else 0))))
                Code04_Gosick1.xcnt[i] = jcast('int', jcast('int', jadd(Code04_Gosick1.xcnt[jcast('int', (i - 1))], (1 if (jcast('int', jmod(Code04_Gosick1.arr[i], v)) == 0) else 0))))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code04_Gosick1.cntq):
                x = jcast('int', Code04_Gosick1.qx[i])
                l = jcast('int', Code04_Gosick1.ql[i])
                r = jcast('int', Code04_Gosick1.qr[i])
                op = jcast('int', Code04_Gosick1.qop[i])
                id = jcast('int', Code04_Gosick1.qid[i])
                Code04_Gosick1.ans[id] = jcast('long', jcast('long', jadd(Code04_Gosick1.ans[id], jcast('long', (jcast('long', (jcast('long', op) * Code04_Gosick1.vcnt[x])) * jcast('int', (Code04_Gosick1.xcnt[r] - Code04_Gosick1.xcnt[jcast('int', (l - 1))])))))))
                i = jcast('int', (i + 1))
            v = jcast('int', (v + 1))

    @staticmethod
    def prepare():
        blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code04_Gosick1.n)))
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.n):
            Code04_Gosick1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), blen)), 1)))
            Code04_Gosick1.maxv = jcast('int', jstatic('Math', 'max', Code04_Gosick1.maxv, Code04_Gosick1.arr[i]))
            Code04_Gosick1.addFactors(Code04_Gosick1.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code04_Gosick1.query, 1, jcast('int', jadd(Code04_Gosick1.m, 1)), Code04_Gosick1.QueryCmp())

    @staticmethod
    def main(args):
        in_ = Code04_Gosick1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Gosick1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Gosick1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.n):
            jset(Code04_Gosick1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.m):
            jset(Code04_Gosick1.query[i], 0, jcall(in_, 'nextInt'))
            jset(Code04_Gosick1.query[i], 1, jcall(in_, 'nextInt'))
            jset(Code04_Gosick1.query[i], 2, i)
            i = jcast('int', (i + 1))
        Code04_Gosick1.prepare()
        Code04_Gosick1.compute()
        # 答案变化量生成前缀和
        i = jcast('int', 2)
        while (i <= Code04_Gosick1.m):
            ((_java_obj_7 := Code04_Gosick1.ans), (_java_key_8 := Code04_Gosick1.query[i][2]), jset(_java_obj_7, _java_key_8, jcast('long', jadd(jget(_java_obj_7, _java_key_8), Code04_Gosick1.ans[Code04_Gosick1.query[jcast('int', (i - 1))][2]]))))[2]
            i = jcast('int', (i + 1))
        # 贡献是重新定义的，答案需要补偿回来
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.m):
            ((_java_obj_9 := Code04_Gosick1.ans), (_java_key_10 := Code04_Gosick1.query[i][2]), jset(_java_obj_9, _java_key_10, jcast('long', jadd(jget(_java_obj_9, _java_key_10), jcast('int', jadd(jcast('int', (Code04_Gosick1.query[i][1] - Code04_Gosick1.query[i][0])), 1))))))[2]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Gosick1.m):
            jcall(out, 'println', Code04_Gosick1.ans[i])
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
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code04_Gosick1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Gosick1.MAXN = jcast('int', 500001)
Code04_Gosick1.MAXF = jcast('int', 5000001)
Code04_Gosick1.LIMIT = jcast('int', 100)
Code04_Gosick1.n = jcast('int', 0)
Code04_Gosick1.m = jcast('int', 0)
Code04_Gosick1.maxv = jcast('int', 0)
Code04_Gosick1.arr = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.bi = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.headf = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.nextf = jarray('int', [Code04_Gosick1.MAXF])
Code04_Gosick1.fac = jarray('int', [Code04_Gosick1.MAXF])
Code04_Gosick1.cntf = jcast('int', 0)
Code04_Gosick1.query = jarray('int', [Code04_Gosick1.MAXN, 3])
Code04_Gosick1.headq = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.nextq = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.qx = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.ql = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.qr = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.qop = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.qid = jarray('int', [jcast('int', (Code04_Gosick1.MAXN << (1 & 31)))])
Code04_Gosick1.cntq = jcast('int', 0)
Code04_Gosick1.xcnt = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.vcnt = jarray('int', [Code04_Gosick1.MAXN])
Code04_Gosick1.pre = jarray('long', [Code04_Gosick1.MAXN])
Code04_Gosick1.ans = jarray('long', [Code04_Gosick1.MAXN])

if __name__ == '__main__':
    Code04_Gosick1.main([])

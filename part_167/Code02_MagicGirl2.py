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

# 魔法少女网站，Python版
# 给定一个长度为n的数组arr，一共有m条操作，每条操作类型如下
# 操作 1 x v   : arr[x]的值变成v
# 操作 2 x y v : arr[x..y]范围上，查询有多少连续子数组的最大值 <= v
# 1 <= n、m <= 3 * 10^5
# 1 <= arr[i] <= n
# 测试链接 : https://www.luogu.com.cn/problem/P6578
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MagicGirl2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'POW': 'POW', 'OFFSET': 'OFFSET', 'n': 'n', 'm': 'm', 'arr': 'arr', 'op': 'op', 'x': 'x', 'y': 'y', 'v': 'v', 'pos': 'pos', 'qid': 'qid', 'cntp': 'cntp', 'cntq': 'cntq', 'cntv': 'cntv', 'help': 'help', 'last': 'last', 'next': 'next', 'pre': 'pre', 'suf': 'suf', 'len': 'len', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    POW = 0
    OFFSET = 0
    n = 0
    m = 0
    arr = None
    op = None
    x = None
    y = None
    v = None
    # pos[1..cntp]是当前序列块的下标
    # qid[1..cntq]是整包结算的查询编号
    pos = None
    qid = None
    cntp = 0
    cntq = 0
    # 基数排序
    cntv = None
    help = None
    # 双链表
    last = None
    next = None
    # 每条查询的答案信息
    pre = None
    suf = None
    len = None
    ans = None
    # 讲解028 - 基数排序，不会的话去看课
    # idx[1..siz]都是编号，编号根据val[编号]的值排序
    # val[编号]的高位 = val[编号] >> POW
    # val[编号]的低位 = val[编号] & OFFSET
    @staticmethod
    def radix(idx, val, siz):
        siz = jcast('int', siz)
        jstatic('Arrays', 'fill', Code02_MagicGirl2.cntv, 0)
        i = jcast('int', 1)
        while (i <= siz):
            ((_java_obj_1 := Code02_MagicGirl2.cntv), (_java_key_2 := jcast('int', (val[idx[i]] & Code02_MagicGirl2.OFFSET))), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code02_MagicGirl2.MAXB):
            Code02_MagicGirl2.cntv[i] = jcast('int', jcast('int', jadd(Code02_MagicGirl2.cntv[i], Code02_MagicGirl2.cntv[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', siz)
        while (i >= 1):
            jset(Code02_MagicGirl2.help, ((_java_obj_4 := Code02_MagicGirl2.cntv), (_java_key_5 := jcast('int', (val[idx[i]] & Code02_MagicGirl2.OFFSET))), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4], idx[i])
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= siz):
            idx[i] = jcast('int', Code02_MagicGirl2.help[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'fill', Code02_MagicGirl2.cntv, 0)
        i = jcast('int', 1)
        while (i <= siz):
            ((_java_obj_7 := Code02_MagicGirl2.cntv), (_java_key_8 := jcast('int', (val[idx[i]] >> (Code02_MagicGirl2.POW & 31)))), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i < Code02_MagicGirl2.MAXB):
            Code02_MagicGirl2.cntv[i] = jcast('int', jcast('int', jadd(Code02_MagicGirl2.cntv[i], Code02_MagicGirl2.cntv[jcast('int', (i - 1))])))
            i = jcast('int', (i + 1))
        i = jcast('int', siz)
        while (i >= 1):
            jset(Code02_MagicGirl2.help, ((_java_obj_10 := Code02_MagicGirl2.cntv), (_java_key_11 := jcast('int', (val[idx[i]] >> (Code02_MagicGirl2.POW & 31)))), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4], idx[i])
            i = jcast('int', (i - 1))
        i = jcast('int', 1)
        while (i <= siz):
            idx[i] = jcast('int', Code02_MagicGirl2.help[i])
            i = jcast('int', (i + 1))

    # 查询的答案信息 pre[i]、suf[i]、len[i]、ans[i]
    # 当前块答案信息 curPre、curSuf、curLen、curAns
    # 查询的答案信息 合并 当前块答案信息
    @staticmethod
    def merge(i, curPre, curSuf, curLen, curAns):
        i = jcast('int', i)
        curPre = jcast('int', curPre)
        curSuf = jcast('int', curSuf)
        curLen = jcast('int', curLen)
        curAns = jcast('int', curAns)
        Code02_MagicGirl2.ans[i] = jcast('long', jcast('long', jadd(Code02_MagicGirl2.ans[i], jcast('long', jadd(jcast('long', (jcast('long', (1 * Code02_MagicGirl2.suf[i])) * curPre)), curAns)))))
        Code02_MagicGirl2.pre[i] = jcast('int', jcast('int', jadd(Code02_MagicGirl2.pre[i], (curPre if (Code02_MagicGirl2.pre[i] == Code02_MagicGirl2.len[i]) else 0))))
        Code02_MagicGirl2.suf[i] = jcast('int', jcast('int', jadd(curSuf, (Code02_MagicGirl2.suf[i] if (curSuf == curLen) else 0))))
        Code02_MagicGirl2.len[i] = jcast('int', jcast('int', jadd(Code02_MagicGirl2.len[i], curLen)))

    # 整包结算
    # qid[1..cntq]是查询编号，每条查询整包[l..r]
    # 根据序列块的数字状况，更新每个查询的答案信息
    @staticmethod
    def calc(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            jset(Code02_MagicGirl2.pos, ((_java_obj_13 := Code02_MagicGirl2), (_java_key_14 := 'cntp'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3], i)
            Code02_MagicGirl2.last[i] = jcast('int', jcast('int', (i - 1)))
            Code02_MagicGirl2.next[i] = jcast('int', jcast('int', jadd(i, 1)))
            i = jcast('int', (i + 1))
        Code02_MagicGirl2.radix(Code02_MagicGirl2.pos, Code02_MagicGirl2.arr, Code02_MagicGirl2.cntp)
        Code02_MagicGirl2.radix(Code02_MagicGirl2.qid, Code02_MagicGirl2.v, Code02_MagicGirl2.cntq)
        curPre = jcast('int', 0)
        curSuf = jcast('int', 0)
        curLen = jcast('int', jcast('int', jadd(jcast('int', (r - l)), 1)))
        curAns = jcast('int', 0)
        i = jcast('int', 1)
        j = jcast('int', 1)
        idx = 0
        while (i <= Code02_MagicGirl2.cntq):
            while ((j <= Code02_MagicGirl2.cntp) and (Code02_MagicGirl2.arr[Code02_MagicGirl2.pos[j]] <= Code02_MagicGirl2.v[Code02_MagicGirl2.qid[i]])):
                idx = jcast('int', Code02_MagicGirl2.pos[j])
                if (Code02_MagicGirl2.last[idx] == jcast('int', (l - 1))):
                    curPre = jcast('int', jcast('int', jadd(curPre, jcast('int', (Code02_MagicGirl2.next[idx] - idx)))))
                if (Code02_MagicGirl2.next[idx] == jcast('int', jadd(r, 1))):
                    curSuf = jcast('int', jcast('int', jadd(curSuf, jcast('int', (idx - Code02_MagicGirl2.last[idx])))))
                curAns = jcast('int', jcast('long', jadd(curAns, jcast('long', (jcast('long', (1 * jcast('int', (idx - Code02_MagicGirl2.last[idx])))) * jcast('int', (Code02_MagicGirl2.next[idx] - idx)))))))
                jset(Code02_MagicGirl2.last, Code02_MagicGirl2.next[idx], Code02_MagicGirl2.last[idx])
                jset(Code02_MagicGirl2.next, Code02_MagicGirl2.last[idx], Code02_MagicGirl2.next[idx])
                j = jcast('int', (j + 1))
            Code02_MagicGirl2.merge(Code02_MagicGirl2.qid[i], curPre, curSuf, curLen, curAns)
            i = jcast('int', (i + 1))
        Code02_MagicGirl2.cntp = jcast('int', jset(Code02_MagicGirl2, 'cntq', 0))

    # 序列块[l..r]，处理一遍所有的操作(单改 + 查询)
    @staticmethod
    def compute(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        qi = jcast('int', 1)
        while (qi <= Code02_MagicGirl2.m):
            if (Code02_MagicGirl2.op[qi] == 1):
                if ((l <= Code02_MagicGirl2.x[qi]) and (Code02_MagicGirl2.x[qi] <= r)):
                    Code02_MagicGirl2.calc(l, r)
                    jset(Code02_MagicGirl2.arr, Code02_MagicGirl2.x[qi], Code02_MagicGirl2.v[qi])
            else:
                if ((Code02_MagicGirl2.x[qi] <= l) and (r <= Code02_MagicGirl2.y[qi])):
                    jset(Code02_MagicGirl2.qid, ((_java_obj_16 := Code02_MagicGirl2), (_java_key_17 := 'cntq'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], qi)
                else:
                    i = jcast('int', jstatic('Math', 'max', Code02_MagicGirl2.x[qi], l))
                    while (i <= jstatic('Math', 'min', Code02_MagicGirl2.y[qi], r)):
                        if (Code02_MagicGirl2.arr[i] <= Code02_MagicGirl2.v[qi]):
                            Code02_MagicGirl2.merge(qi, 1, 1, 1, 1)
                        else:
                            Code02_MagicGirl2.merge(qi, 0, 0, 1, 0)
                        i = jcast('int', (i + 1))
            qi = jcast('int', (qi + 1))
        Code02_MagicGirl2.calc(l, r)

    @staticmethod
    def main(args):
        in_ = Code02_MagicGirl2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_MagicGirl2.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_MagicGirl2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_MagicGirl2.n):
            jset(Code02_MagicGirl2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_MagicGirl2.m):
            jset(Code02_MagicGirl2.op, i, jcall(in_, 'nextInt'))
            jset(Code02_MagicGirl2.x, i, jcall(in_, 'nextInt'))
            if (Code02_MagicGirl2.op[i] == 1):
                jset(Code02_MagicGirl2.v, i, jcall(in_, 'nextInt'))
            else:
                jset(Code02_MagicGirl2.y, i, jcall(in_, 'nextInt'))
                jset(Code02_MagicGirl2.v, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        blen = jcast('int', jcast('int', (1 << (Code02_MagicGirl2.POW & 31))))
        bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code02_MagicGirl2.n, blen)) - 1)), blen)))
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= bnum):
            l = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * blen)), 1)))
            r = jcast('int', jstatic('Math', 'min', jcast('int', (i * blen)), Code02_MagicGirl2.n))
            Code02_MagicGirl2.compute(l, r)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_MagicGirl2.m):
            if (Code02_MagicGirl2.op[i] == 2):
                jcall(out, 'println', Code02_MagicGirl2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_19 := self), (_java_key_20 := 'ptr'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (1)))), _java_old_21)[4]])

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
            raise TypeError("No matching overload for Code02_MagicGirl2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MagicGirl2.MAXN = jcast('int', 300002)
Code02_MagicGirl2.MAXB = jcast('int', 601)
Code02_MagicGirl2.POW = jcast('int', 9)
Code02_MagicGirl2.OFFSET = jcast('int', jcast('int', (jcast('int', (1 << (Code02_MagicGirl2.POW & 31))) - 1)))
Code02_MagicGirl2.n = jcast('int', 0)
Code02_MagicGirl2.m = jcast('int', 0)
Code02_MagicGirl2.arr = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.op = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.x = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.y = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.v = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.pos = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.qid = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.cntp = jcast('int', 0)
Code02_MagicGirl2.cntq = jcast('int', 0)
Code02_MagicGirl2.cntv = jarray('int', [Code02_MagicGirl2.MAXB])
Code02_MagicGirl2.help = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.last = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.next = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.pre = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.suf = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.len = jarray('int', [Code02_MagicGirl2.MAXN])
Code02_MagicGirl2.ans = jarray('long', [Code02_MagicGirl2.MAXN])

if __name__ == '__main__':
    Code02_MagicGirl2.main([])

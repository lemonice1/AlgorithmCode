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

# 序列，Python版
# 给定一个长度为n的数组arr，初始时刻认为是第0秒
# 接下来发生m条操作，第i条操作发生在第i秒，操作类型如下
# 操作 1 l r v : arr[l..r]范围上每个数加v，v可能是负数
# 操作 2 x v   : 不包括当前这一秒，查询过去多少秒内，arr[x] >= v
# 2 <= n、m <= 10^5
# -10^9 <= 数组中的值 <= +10^9
# 测试链接 : https://www.luogu.com.cn/problem/P3863
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_Sequence1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'event': 'event', 'cnte': 'cnte', 'cntq': 'cntq', 'tim': 'tim', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'lazy': 'lazy', 'ans': 'ans'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    # op == 1 表示修改事件、位置x、时刻t、修改效果v、空缺
    # op == 2 表示查询事件、位置x、时刻t、查询标准v、问题编号q
    event = None
    cnte = 0
    cntq = 0
    # tim[i] = v，表示在i号时间点，所有数字都增加v
    tim = None
    # 时间块内的所有值要排序，方便查询 >= v的数字个数
    sortv = None
    # 时间分块
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    lazy = None
    # 每个查询的答案
    ans = None
    @staticmethod
    def innerAdd(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        i = jcast('int', l)
        while (i <= r):
            Code02_Sequence1.tim[i] = jcast('long', jcast('long', jadd(Code02_Sequence1.tim[i], v)))
            i = jcast('int', (i + 1))
        i = jcast('int', Code02_Sequence1.bl[Code02_Sequence1.bi[l]])
        while (i <= Code02_Sequence1.br[Code02_Sequence1.bi[l]]):
            Code02_Sequence1.sortv[i] = jcast('long', Code02_Sequence1.tim[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code02_Sequence1.sortv, Code02_Sequence1.bl[Code02_Sequence1.bi[l]], jcast('int', jadd(Code02_Sequence1.br[Code02_Sequence1.bi[l]], 1)))

    @staticmethod
    def add(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        if (l > r):
            return
        if (Code02_Sequence1.bi[l] == Code02_Sequence1.bi[r]):
            Code02_Sequence1.innerAdd(l, r, v)
        else:
            Code02_Sequence1.innerAdd(l, Code02_Sequence1.br[Code02_Sequence1.bi[l]], v)
            Code02_Sequence1.innerAdd(Code02_Sequence1.bl[Code02_Sequence1.bi[r]], r, v)
            i = jcast('int', jcast('int', jadd(Code02_Sequence1.bi[l], 1)))
            while (i <= jcast('int', (Code02_Sequence1.bi[r] - 1))):
                Code02_Sequence1.lazy[i] = jcast('long', jcast('long', jadd(Code02_Sequence1.lazy[i], v)))
                i = jcast('int', (i + 1))

    @staticmethod
    def innerQuery(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        v = jcast('long', jcast('long', (v - Code02_Sequence1.lazy[Code02_Sequence1.bi[l]])))
        ans = jcast('int', 0)
        i = jcast('int', l)
        while (i <= r):
            if (Code02_Sequence1.tim[i] >= v):
                ans = jcast('int', (ans + 1))
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    # 第i块内>= v的数字个数
    @staticmethod
    def getCnt(i, v):
        i = jcast('int', i)
        v = jcast('long', v)
        v = jcast('long', jcast('long', (v - Code02_Sequence1.lazy[i])))
        l = jcast('int', Code02_Sequence1.bl[i])
        r = jcast('int', Code02_Sequence1.br[i])
        m = 0
        pos = jcast('int', jcast('int', jadd(Code02_Sequence1.br[i], 1)))
        while (l <= r):
            m = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (Code02_Sequence1.sortv[m] >= v):
                pos = jcast('int', m)
                r = jcast('int', jcast('int', (m - 1)))
            else:
                l = jcast('int', jcast('int', jadd(m, 1)))
        return jcast('int', jcast('int', jadd(jcast('int', (Code02_Sequence1.br[i] - pos)), 1)))

    @staticmethod
    def query(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('long', v)
        if (l > r):
            return jcast('int', 0)
        ans = jcast('int', 0)
        if (Code02_Sequence1.bi[l] == Code02_Sequence1.bi[r]):
            ans = jcast('int', jcast('int', jadd(ans, Code02_Sequence1.innerQuery(l, r, v))))
        else:
            ans = jcast('int', jcast('int', jadd(ans, Code02_Sequence1.innerQuery(l, Code02_Sequence1.br[Code02_Sequence1.bi[l]], v))))
            ans = jcast('int', jcast('int', jadd(ans, Code02_Sequence1.innerQuery(Code02_Sequence1.bl[Code02_Sequence1.bi[r]], r, v))))
            i = jcast('int', jcast('int', jadd(Code02_Sequence1.bi[l], 1)))
            while (i <= jcast('int', (Code02_Sequence1.bi[r] - 1))):
                ans = jcast('int', jcast('int', jadd(ans, Code02_Sequence1.getCnt(i, v))))
                i = jcast('int', (i + 1))
        return jcast('int', ans)

    @staticmethod
    def addChange(x, t, v):
        x = jcast('int', x)
        t = jcast('int', t)
        v = jcast('int', v)
        jset(Code02_Sequence1.event[((_java_obj_1 := Code02_Sequence1), (_java_key_2 := 'cnte'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, 1)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 1, x)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 2, t)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 3, v)

    @staticmethod
    def addQuery(x, t, v):
        x = jcast('int', x)
        t = jcast('int', t)
        v = jcast('int', v)
        jset(Code02_Sequence1.event[((_java_obj_4 := Code02_Sequence1), (_java_key_5 := 'cnte'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]], 0, 2)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 1, x)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 2, t)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 3, v)
        jset(Code02_Sequence1.event[Code02_Sequence1.cnte], 4, ((_java_obj_7 := Code02_Sequence1), (_java_key_8 := 'cntq'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])

    @staticmethod
    def prepare():
        Code02_Sequence1.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', Code02_Sequence1.m)))
        Code02_Sequence1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code02_Sequence1.m, Code02_Sequence1.blen)) - 1)), Code02_Sequence1.blen)))
        i = jcast('int', 1)
        while (i <= Code02_Sequence1.m):
            Code02_Sequence1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code02_Sequence1.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Sequence1.bnum):
            Code02_Sequence1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code02_Sequence1.blen)), 1)))
            jset(Code02_Sequence1.br, i, jstatic('Math', 'min', jcast('int', (i * Code02_Sequence1.blen)), Code02_Sequence1.m))
            i = jcast('int', (i + 1))
        # 所有事件根据位置x排序，位置一样的事件，修改事件先执行，查询事件后执行
        jstatic('Arrays', 'sort', Code02_Sequence1.event, 1, jcast('int', jadd(Code02_Sequence1.cnte, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else (a[2] - b[2]))))

    @staticmethod
    def main(args):
        in_ = Code02_Sequence1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_Sequence1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_Sequence1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code02_Sequence1.n):
            jset(Code02_Sequence1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        # 时间轴重新定义，1是初始时刻、2、3 ... m+1
        Code02_Sequence1.m = jcast('int', (Code02_Sequence1.m + 1))
        t = jcast('int', 2)
        op = 0
        l = 0
        r = 0
        v = 0
        x = 0
        while (t <= Code02_Sequence1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                l = jcast('int', jcall(in_, 'nextInt'))
                r = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code02_Sequence1.addChange(l, t, v)
                Code02_Sequence1.addChange(jcast('int', jadd(r, 1)), t, jcast('int', (-v)))
            else:
                x = jcast('int', jcall(in_, 'nextInt'))
                v = jcast('int', jcall(in_, 'nextInt'))
                Code02_Sequence1.addQuery(x, t, v)
            t = jcast('int', (t + 1))
        Code02_Sequence1.prepare()
        i = jcast('int', 1)
        op = 0
        x = 0
        t = 0
        v = 0
        q = 0
        while (i <= Code02_Sequence1.cnte):
            op = jcast('int', Code02_Sequence1.event[i][0])
            x = jcast('int', Code02_Sequence1.event[i][1])
            t = jcast('int', Code02_Sequence1.event[i][2])
            v = jcast('int', Code02_Sequence1.event[i][3])
            q = jcast('int', Code02_Sequence1.event[i][4])
            if (op == 1):
                Code02_Sequence1.add(t, Code02_Sequence1.m, v)
            else:
                jset(Code02_Sequence1.ans, q, Code02_Sequence1.query(1, jcast('int', (t - 1)), jcast('int', (v - Code02_Sequence1.arr[x]))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code02_Sequence1.cntq):
            jcall(out, 'println', Code02_Sequence1.ans[i])
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
            raise TypeError("No matching overload for Code02_Sequence1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_Sequence1.MAXN = jcast('int', 100001)
Code02_Sequence1.MAXB = jcast('int', 501)
Code02_Sequence1.n = jcast('int', 0)
Code02_Sequence1.m = jcast('int', 0)
Code02_Sequence1.arr = jarray('int', [Code02_Sequence1.MAXN])
Code02_Sequence1.event = jarray('int', [jcast('int', (Code02_Sequence1.MAXN << (2 & 31))), 5])
Code02_Sequence1.cnte = jcast('int', 0)
Code02_Sequence1.cntq = jcast('int', 0)
Code02_Sequence1.tim = jarray('long', [Code02_Sequence1.MAXN])
Code02_Sequence1.sortv = jarray('long', [Code02_Sequence1.MAXN])
Code02_Sequence1.blen = jcast('int', 0)
Code02_Sequence1.bnum = jcast('int', 0)
Code02_Sequence1.bi = jarray('int', [Code02_Sequence1.MAXN])
Code02_Sequence1.bl = jarray('int', [Code02_Sequence1.MAXB])
Code02_Sequence1.br = jarray('int', [Code02_Sequence1.MAXB])
Code02_Sequence1.lazy = jarray('long', [Code02_Sequence1.MAXB])
Code02_Sequence1.ans = jarray('int', [Code02_Sequence1.MAXN])

if __name__ == '__main__':
    Code02_Sequence1.main([])

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

# 稳定婚姻，Python版
# 一共有n对婚姻关系，每对婚姻关系给定(女方名, 男方名)，一共2n个名字
# 一共有m对暧昧关系，每对暧昧关系给定(女方名, 男方名)，不会出现新名字
# 如果一对婚姻关系破裂，那么女方或者男方，可能会找暧昧关系的对象私奔
# 私奔会制造更多的婚姻破裂，并且产生进一步的私奔，事情好像多米诺骨牌一样展开
# 如果所有涉事男女都能重新搭配，只要存在这种可能性，那么这对婚姻关系就是不稳定的
# 比如A为女，B为男，婚姻关系(A1, B1)、(A2, B2)，同时暧昧关系(A1, B2)、(A2, B1)
# A1和B1婚姻破裂，导致B1和A2私奔了，导致A2和B2婚姻破裂，导致B2和A1私奔了，这就是重新搭配
# 检查每对婚姻关系，如果不稳定打印"Unsafe"，如果稳定打印"Safe"
# 1 <= n <= 4000    0 <= m <= 20000
# 测试链接 : https://www.luogu.com.cn/problem/P1407
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code10_SafeMarriage2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'cntn': 'cntn', 'nameId': 'nameId', 'head': 'head', 'nxt': 'nxt', 'to': 'to', 'cntg': 'cntg', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    a = None
    b = None
    cntn = 0
    nameId = None
    head = None
    nxt = None
    to = None
    cntg = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code10_SafeMarriage2.nxt, ((_java_obj_1 := Code10_SafeMarriage2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code10_SafeMarriage2.head[u])
        Code10_SafeMarriage2.to[Code10_SafeMarriage2.cntg] = jcast('int', v)
        Code10_SafeMarriage2.head[u] = jcast('int', Code10_SafeMarriage2.cntg)

    @staticmethod
    def tarjan(u):
        u = jcast('int', u)
        jset(Code10_SafeMarriage2.dfn, u, jset(Code10_SafeMarriage2.low, u, ((_java_obj_4 := Code10_SafeMarriage2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code10_SafeMarriage2.sta, ((_java_obj_7 := Code10_SafeMarriage2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code10_SafeMarriage2.head[u])
        while (e > 0):
            v = jcast('int', Code10_SafeMarriage2.to[e])
            if (Code10_SafeMarriage2.dfn[v] == 0):
                Code10_SafeMarriage2.tarjan(v)
                jset(Code10_SafeMarriage2.low, u, jstatic('Math', 'min', Code10_SafeMarriage2.low[u], Code10_SafeMarriage2.low[v]))
            else:
                if (Code10_SafeMarriage2.belong[v] == 0):
                    jset(Code10_SafeMarriage2.low, u, jstatic('Math', 'min', Code10_SafeMarriage2.low[u], Code10_SafeMarriage2.dfn[v]))
            e = jcast('int', Code10_SafeMarriage2.nxt[e])
        if (Code10_SafeMarriage2.dfn[u] == Code10_SafeMarriage2.low[u]):
            Code10_SafeMarriage2.sccCnt = jcast('int', (Code10_SafeMarriage2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code10_SafeMarriage2.sta[((_java_obj_10 := Code10_SafeMarriage2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code10_SafeMarriage2.belong[pop] = jcast('int', Code10_SafeMarriage2.sccCnt)
                if not ((pop != u)):
                    break

    @staticmethod
    def main(args):
        in_ = Code10_SafeMarriage2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code10_SafeMarriage2.n = jcast('int', jcall(in_, 'nextInt'))
        girl = None
        boy = None
        i = jcast('int', 1)
        while (i <= Code10_SafeMarriage2.n):
            girl = jcall(in_, 'nextString')
            boy = jcall(in_, 'nextString')
            jset(Code10_SafeMarriage2.a, i, ((_java_obj_13 := Code10_SafeMarriage2), (_java_key_14 := 'cntn'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3])
            jset(Code10_SafeMarriage2.b, i, ((_java_obj_16 := Code10_SafeMarriage2), (_java_key_17 := 'cntn'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3])
            jcall(Code10_SafeMarriage2.nameId, 'put', girl, Code10_SafeMarriage2.a[i])
            jcall(Code10_SafeMarriage2.nameId, 'put', boy, Code10_SafeMarriage2.b[i])
            Code10_SafeMarriage2.addEdge(Code10_SafeMarriage2.a[i], Code10_SafeMarriage2.b[i])
            i = jcast('int', (i + 1))
        Code10_SafeMarriage2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code10_SafeMarriage2.m):
            girl = jcall(in_, 'nextString')
            boy = jcall(in_, 'nextString')
            Code10_SafeMarriage2.addEdge(jcall(Code10_SafeMarriage2.nameId, 'get', boy), jcall(Code10_SafeMarriage2.nameId, 'get', girl))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code10_SafeMarriage2.cntn):
            if (Code10_SafeMarriage2.dfn[i] == 0):
                Code10_SafeMarriage2.tarjan(i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code10_SafeMarriage2.n):
            if (Code10_SafeMarriage2.belong[Code10_SafeMarriage2.a[i]] == Code10_SafeMarriage2.belong[Code10_SafeMarriage2.b[i]]):
                jcall(out, 'println', 'Unsafe')
            else:
                jcall(out, 'println', 'Safe')
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

        def isLetter(self, c):
            c = jcast('int', c)
            return jcast('boolean', (((c >= jchar('A')) and (c <= jchar('Z'))) or ((c >= jchar('a')) and (c <= jchar('z')))))

        def nextString(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if (c == jcast('int', (-1))):
                    return None
                if not ((not self.isLetter(c))):
                    break
            sb = jnew('StringBuilder')
            while self.isLetter(c):
                try:
                    jcall(sb, 'append', jcast('char', c))
                    c = jcast('int', self.readByte())
                    if (c == jcast('int', (-1))):
                        raise JBreak(None)
                except JContinue as _java_control_22:
                    if _java_control_22.label not in (None,):
                        raise
                except JBreak as _java_control_22:
                    if _java_control_22.label not in (None,):
                        raise
                    break
            return jcall(sb, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code10_SafeMarriage2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code10_SafeMarriage2.MAXN = jcast('int', 10001)
Code10_SafeMarriage2.MAXM = jcast('int', 30001)
Code10_SafeMarriage2.n = jcast('int', 0)
Code10_SafeMarriage2.m = jcast('int', 0)
Code10_SafeMarriage2.a = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.b = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.cntn = jcast('int', 0)
Code10_SafeMarriage2.nameId = jnew('HashMap')
Code10_SafeMarriage2.head = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.nxt = jarray('int', [Code10_SafeMarriage2.MAXM])
Code10_SafeMarriage2.to = jarray('int', [Code10_SafeMarriage2.MAXM])
Code10_SafeMarriage2.cntg = jcast('int', 0)
Code10_SafeMarriage2.dfn = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.low = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.cntd = jcast('int', 0)
Code10_SafeMarriage2.sta = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.top = jcast('int', 0)
Code10_SafeMarriage2.belong = jarray('int', [Code10_SafeMarriage2.MAXN])
Code10_SafeMarriage2.sccCnt = jcast('int', 0)

if __name__ == '__main__':
    Code10_SafeMarriage2.main([])

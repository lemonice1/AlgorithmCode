# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 未来日记，Python版
# 给定一个长度为n的数组arr，一共有m条操作，每条操作类型如下
# 操作 1 l r x y : arr[l..r]范围上，所有值x变成值y
# 操作 2 l r k   : arr[l..r]范围上，查询第k小的值
# 1 <= n、m、arr[i] <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P4119
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code01_FutureDiary2.py
# 两个版本保留相同的算法逻辑
class Code01_FutureDiary1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'idxset': 'idxset', 'valset': 'valset', 'setval': 'setval', 'sum1': 'sum1', 'sum2': 'sum2', 'cnt1': 'cnt1', 'cnt2': 'cnt2'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    # blen既表示序列块长，也表示值域块长
    # bnum只表示序列块的数量
    # bi[i]可以查询下标i来自哪个序列块
    # bi[v]也可查询数字v来自哪个值域块
    # bl[i]表示下标第i块的左边界
    # br[i]表示下标第i块的右边界
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # idxset[i]表示下标i，在归属的块中，来自哪个集合
    # valset[b][v]表示序列块b中的数值v，来自哪个集合
    # setval[b][s]表示序列块b中的集合s，对应的数值
    idxset = None
    valset = None
    setval = None
    # sum1[k][b]表示前k个序列块中，第b块个值域块的数字有几个
    # sum2[k][v]表示前k个序列块中，数字v有几个
    # cnt1[b]表示遍历散块之后，第b块个值域块的数字有几个
    # cnt2[v]表示遍历散块之后，数字v有几个
    sum1 = None
    sum2 = None
    cnt1 = None
    cnt2 = None
    # 序列第b块中，根据当前arr中的值，重建集合
    @staticmethod
    def build(b):
        b = jcast('int', b)
        # 根据arr中的值重建集合，需要放弃之前的信息
        # 可是数值范围很大，不能枚举数值去清空 valset
        # 注意到，一个块里集合的数量 <= 块长
        # 所以根据 setval[b][s]，可以得到每个集合之前的对应值v
        # 然后 valset[b][v] = 0，让块内之前的每个值，不再挂靠任何集合
        # 这样可以避免数值的枚举，做到快速清空 valset
        i = jcast('int', 1)
        while (i <= Code01_FutureDiary1.blen):
            jset(Code01_FutureDiary1.valset[b], Code01_FutureDiary1.setval[b][i], 0)
            i = jcast('int', (i + 1))
        # 重建集合的过程
        i = jcast('int', Code01_FutureDiary1.bl[b])
        s = jcast('int', 0)
        while (i <= Code01_FutureDiary1.br[b]):
            if (Code01_FutureDiary1.valset[b][Code01_FutureDiary1.arr[i]] == 0):
                s = jcast('int', (s + 1))
                jset(Code01_FutureDiary1.valset[b], Code01_FutureDiary1.arr[i], s)
                jset(Code01_FutureDiary1.setval[b], s, Code01_FutureDiary1.arr[i])
            Code01_FutureDiary1.idxset[i] = jcast('int', Code01_FutureDiary1.valset[b][Code01_FutureDiary1.arr[i]])
            i = jcast('int', (i + 1))

    # 命中了整块修改，有x无y的情况，序列第b块中所有x改成y
    @staticmethod
    def lazy(b, x, y):
        b = jcast('int', b)
        x = jcast('int', x)
        y = jcast('int', y)
        jset(Code01_FutureDiary1.valset[b], y, Code01_FutureDiary1.valset[b][x])
        jset(Code01_FutureDiary1.setval[b], Code01_FutureDiary1.valset[b][x], y)
        jset(Code01_FutureDiary1.valset[b], x, 0)

    # 之前命中了整块修改，有x无y的情况，导致序列第b块中有些值改动了，把改动写入arr
    @staticmethod
    def down(b):
        b = jcast('int', b)
        i = jcast('int', Code01_FutureDiary1.bl[b])
        while (i <= Code01_FutureDiary1.br[b]):
            Code01_FutureDiary1.arr[i] = jcast('int', Code01_FutureDiary1.setval[b][Code01_FutureDiary1.idxset[i]])
            i = jcast('int', (i + 1))

    # 序列[l..r]范围上，有x有y，把所有x改成y
    @staticmethod
    def innerUpdate(l, r, x, y):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_FutureDiary1.down(Code01_FutureDiary1.bi[l])
        i = jcast('int', l)
        while (i <= r):
            if (Code01_FutureDiary1.arr[i] == x):
                ((_java_obj_1 := Code01_FutureDiary1.sum1[Code01_FutureDiary1.bi[i]]), (_java_key_2 := Code01_FutureDiary1.bi[x]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (-1)))), _java_old_3)[4]
                ((_java_obj_4 := Code01_FutureDiary1.sum1[Code01_FutureDiary1.bi[i]]), (_java_key_5 := Code01_FutureDiary1.bi[y]), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]
                ((_java_obj_7 := Code01_FutureDiary1.sum2[Code01_FutureDiary1.bi[i]]), (_java_key_8 := x), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (-1)))), _java_old_9)[4]
                ((_java_obj_10 := Code01_FutureDiary1.sum2[Code01_FutureDiary1.bi[i]]), (_java_key_11 := y), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))), _java_old_12)[4]
                Code01_FutureDiary1.arr[i] = jcast('int', y)
            i = jcast('int', (i + 1))
        Code01_FutureDiary1.build(Code01_FutureDiary1.bi[l])

    @staticmethod
    def update(l, r, x, y):
        l = jcast('int', l)
        r = jcast('int', r)
        x = jcast('int', x)
        y = jcast('int', y)
        # 必要的剪枝
        if ((x == y) or (jcast('int', (Code01_FutureDiary1.sum2[Code01_FutureDiary1.bi[r]][x] - Code01_FutureDiary1.sum2[jcast('int', (Code01_FutureDiary1.bi[l] - 1))][x])) == 0)):
            return
        # 前缀统计变成当前块统计
        b = jcast('int', Code01_FutureDiary1.bi[Code01_FutureDiary1.n])
        while (b >= Code01_FutureDiary1.bi[l]):
            ((_java_obj_13 := Code01_FutureDiary1.sum1[b]), (_java_key_14 := Code01_FutureDiary1.bi[x]), jset(_java_obj_13, _java_key_14, jcast('int', (jget(_java_obj_13, _java_key_14) - Code01_FutureDiary1.sum1[jcast('int', (b - 1))][Code01_FutureDiary1.bi[x]]))))[2]
            ((_java_obj_15 := Code01_FutureDiary1.sum1[b]), (_java_key_16 := Code01_FutureDiary1.bi[y]), jset(_java_obj_15, _java_key_16, jcast('int', (jget(_java_obj_15, _java_key_16) - Code01_FutureDiary1.sum1[jcast('int', (b - 1))][Code01_FutureDiary1.bi[y]]))))[2]
            ((_java_obj_17 := Code01_FutureDiary1.sum2[b]), (_java_key_18 := x), jset(_java_obj_17, _java_key_18, jcast('int', (jget(_java_obj_17, _java_key_18) - Code01_FutureDiary1.sum2[jcast('int', (b - 1))][x]))))[2]
            ((_java_obj_19 := Code01_FutureDiary1.sum2[b]), (_java_key_20 := y), jset(_java_obj_19, _java_key_20, jcast('int', (jget(_java_obj_19, _java_key_20) - Code01_FutureDiary1.sum2[jcast('int', (b - 1))][y]))))[2]
            b = jcast('int', (b - 1))
        if (Code01_FutureDiary1.bi[l] == Code01_FutureDiary1.bi[r]):
            Code01_FutureDiary1.innerUpdate(l, r, x, y)
        else:
            Code01_FutureDiary1.innerUpdate(l, Code01_FutureDiary1.br[Code01_FutureDiary1.bi[l]], x, y)
            Code01_FutureDiary1.innerUpdate(Code01_FutureDiary1.bl[Code01_FutureDiary1.bi[r]], r, x, y)
            b = jcast('int', jcast('int', jadd(Code01_FutureDiary1.bi[l], 1)))
            while (b <= jcast('int', (Code01_FutureDiary1.bi[r] - 1))):
                if (Code01_FutureDiary1.sum2[b][x] != 0):
                    if (Code01_FutureDiary1.sum2[b][y] != 0):
                        # 整块更新时，调用innerUpdate的次数 <= 块长
                        Code01_FutureDiary1.innerUpdate(Code01_FutureDiary1.bl[b], Code01_FutureDiary1.br[b], x, y)
                    else:
                        ((_java_obj_21 := Code01_FutureDiary1.sum1[b]), (_java_key_22 := Code01_FutureDiary1.bi[y]), jset(_java_obj_21, _java_key_22, jcast('int', jadd(jget(_java_obj_21, _java_key_22), Code01_FutureDiary1.sum2[b][x]))))[2]
                        ((_java_obj_23 := Code01_FutureDiary1.sum1[b]), (_java_key_24 := Code01_FutureDiary1.bi[x]), jset(_java_obj_23, _java_key_24, jcast('int', (jget(_java_obj_23, _java_key_24) - Code01_FutureDiary1.sum2[b][x]))))[2]
                        ((_java_obj_25 := Code01_FutureDiary1.sum2[b]), (_java_key_26 := y), jset(_java_obj_25, _java_key_26, jcast('int', jadd(jget(_java_obj_25, _java_key_26), Code01_FutureDiary1.sum2[b][x]))))[2]
                        jset(Code01_FutureDiary1.sum2[b], x, 0)
                        Code01_FutureDiary1.lazy(b, x, y)
                b = jcast('int', (b + 1))
        # 当前块统计变回前缀统计
        b = jcast('int', Code01_FutureDiary1.bi[l])
        while (b <= Code01_FutureDiary1.bi[Code01_FutureDiary1.n]):
            ((_java_obj_27 := Code01_FutureDiary1.sum1[b]), (_java_key_28 := Code01_FutureDiary1.bi[x]), jset(_java_obj_27, _java_key_28, jcast('int', jadd(jget(_java_obj_27, _java_key_28), Code01_FutureDiary1.sum1[jcast('int', (b - 1))][Code01_FutureDiary1.bi[x]]))))[2]
            ((_java_obj_29 := Code01_FutureDiary1.sum1[b]), (_java_key_30 := Code01_FutureDiary1.bi[y]), jset(_java_obj_29, _java_key_30, jcast('int', jadd(jget(_java_obj_29, _java_key_30), Code01_FutureDiary1.sum1[jcast('int', (b - 1))][Code01_FutureDiary1.bi[y]]))))[2]
            ((_java_obj_31 := Code01_FutureDiary1.sum2[b]), (_java_key_32 := x), jset(_java_obj_31, _java_key_32, jcast('int', jadd(jget(_java_obj_31, _java_key_32), Code01_FutureDiary1.sum2[jcast('int', (b - 1))][x]))))[2]
            ((_java_obj_33 := Code01_FutureDiary1.sum2[b]), (_java_key_34 := y), jset(_java_obj_33, _java_key_34, jcast('int', jadd(jget(_java_obj_33, _java_key_34), Code01_FutureDiary1.sum2[jcast('int', (b - 1))][y]))))[2]
            b = jcast('int', (b + 1))

    @staticmethod
    def addCnt(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            ((_java_obj_35 := Code01_FutureDiary1.cnt1), (_java_key_36 := Code01_FutureDiary1.bi[Code01_FutureDiary1.arr[i]]), (_java_old_37 := jget(_java_obj_35, _java_key_36)), jset(_java_obj_35, _java_key_36, jcast('int', (_java_old_37 + (1)))), _java_old_37)[4]
            ((_java_obj_38 := Code01_FutureDiary1.cnt2), (_java_key_39 := Code01_FutureDiary1.arr[i]), (_java_old_40 := jget(_java_obj_38, _java_key_39)), jset(_java_obj_38, _java_key_39, jcast('int', (_java_old_40 + (1)))), _java_old_40)[4]
            i = jcast('int', (i + 1))

    @staticmethod
    def clearCnt(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', l)
        while (i <= r):
            jset(Code01_FutureDiary1.cnt1, Code01_FutureDiary1.bi[Code01_FutureDiary1.arr[i]], jset(Code01_FutureDiary1.cnt2, Code01_FutureDiary1.arr[i], 0))
            i = jcast('int', (i + 1))

    @staticmethod
    def query(l, r, k):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        ans = jcast('int', 0)
        inner = jcast('boolean', (Code01_FutureDiary1.bi[l] == Code01_FutureDiary1.bi[r]))
        # 建立散块的词频统计
        if inner:
            Code01_FutureDiary1.down(Code01_FutureDiary1.bi[l])
            Code01_FutureDiary1.addCnt(l, r)
        else:
            Code01_FutureDiary1.down(Code01_FutureDiary1.bi[l])
            Code01_FutureDiary1.down(Code01_FutureDiary1.bi[r])
            Code01_FutureDiary1.addCnt(l, Code01_FutureDiary1.br[Code01_FutureDiary1.bi[l]])
            Code01_FutureDiary1.addCnt(Code01_FutureDiary1.bl[Code01_FutureDiary1.bi[r]], r)
        sumCnt = jcast('int', 0)
        vblock = jcast('int', 0)
        # 定位第k小的数字，来自哪个值域块
        b = jcast('int', 1)
        while (b <= Code01_FutureDiary1.bi[jcast('int', (Code01_FutureDiary1.MAXN - 1))]):
            try:
                # 如果不存在中间的整块，词频 = 散块词频，否则 词频 = 散块词频 + 整块词频
                cnt = jcast('int', jcast('int', jadd(Code01_FutureDiary1.cnt1[b], (0 if inner else jcast('int', (Code01_FutureDiary1.sum1[jcast('int', (Code01_FutureDiary1.bi[r] - 1))][b] - Code01_FutureDiary1.sum1[Code01_FutureDiary1.bi[l]][b]))))))
                if (jcast('int', jadd(sumCnt, cnt)) >= k):
                    vblock = jcast('int', b)
                    raise JBreak(None)
                else:
                    sumCnt = jcast('int', jcast('int', jadd(sumCnt, cnt)))
            except JContinue as _java_control_41:
                if _java_control_41.label not in (None,):
                    raise
            except JBreak as _java_control_41:
                if _java_control_41.label not in (None,):
                    raise
                break
            b = jcast('int', (b + 1))
        # 定位第k小的数字，来自值域块的具体数字
        v = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (vblock - 1)) * Code01_FutureDiary1.blen)), 1)))
        while (v <= jcast('int', (vblock * Code01_FutureDiary1.blen))):
            try:
                # 如果不存在中间的整块，词频 = 散块词频，否则 词频 = 散块词频 + 整块词频
                cnt = jcast('int', jcast('int', jadd(Code01_FutureDiary1.cnt2[v], (0 if inner else jcast('int', (Code01_FutureDiary1.sum2[jcast('int', (Code01_FutureDiary1.bi[r] - 1))][v] - Code01_FutureDiary1.sum2[Code01_FutureDiary1.bi[l]][v]))))))
                if (jcast('int', jadd(sumCnt, cnt)) >= k):
                    ans = jcast('int', v)
                    raise JBreak(None)
                else:
                    sumCnt = jcast('int', jcast('int', jadd(sumCnt, cnt)))
            except JContinue as _java_control_42:
                if _java_control_42.label not in (None,):
                    raise
            except JBreak as _java_control_42:
                if _java_control_42.label not in (None,):
                    raise
                break
            v = jcast('int', (v + 1))
        # 清空散块的词频统计
        if inner:
            Code01_FutureDiary1.clearCnt(l, r)
        else:
            Code01_FutureDiary1.clearCnt(l, Code01_FutureDiary1.br[Code01_FutureDiary1.bi[l]])
            Code01_FutureDiary1.clearCnt(Code01_FutureDiary1.bl[Code01_FutureDiary1.bi[r]], r)
        return jcast('int', ans)

    @staticmethod
    def prepare():
        Code01_FutureDiary1.blen = jcast('int', 300)
        Code01_FutureDiary1.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code01_FutureDiary1.n, Code01_FutureDiary1.blen)) - 1)), Code01_FutureDiary1.blen)))
        # i一定要枚举[1, MAXN)
        # 因为不仅序列要分块，值域也要分块
        i = jcast('int', 1)
        while (i < Code01_FutureDiary1.MAXN):
            Code01_FutureDiary1.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code01_FutureDiary1.blen)), 1)))
            i = jcast('int', (i + 1))
        # bl、br 仅用于序列分块
        i = jcast('int', 1)
        while (i <= Code01_FutureDiary1.bnum):
            Code01_FutureDiary1.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code01_FutureDiary1.blen)), 1)))
            jset(Code01_FutureDiary1.br, i, jstatic('Math', 'min', jcast('int', (i * Code01_FutureDiary1.blen)), Code01_FutureDiary1.n))
            Code01_FutureDiary1.build(i)
            i = jcast('int', (i + 1))
        # 初始建立sum1、sum2，都表示前缀信息
        i = jcast('int', 1)
        while (i <= Code01_FutureDiary1.bnum):
            j = jcast('int', 1)
            while (j < Code01_FutureDiary1.MAXB):
                jset(Code01_FutureDiary1.sum1[i], j, Code01_FutureDiary1.sum1[jcast('int', (i - 1))][j])
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j < Code01_FutureDiary1.MAXN):
                jset(Code01_FutureDiary1.sum2[i], j, Code01_FutureDiary1.sum2[jcast('int', (i - 1))][j])
                j = jcast('int', (j + 1))
            j = jcast('int', Code01_FutureDiary1.bl[i])
            while (j <= Code01_FutureDiary1.br[i]):
                ((_java_obj_43 := Code01_FutureDiary1.sum1[i]), (_java_key_44 := Code01_FutureDiary1.bi[Code01_FutureDiary1.arr[j]]), (_java_old_45 := jget(_java_obj_43, _java_key_44)), jset(_java_obj_43, _java_key_44, jcast('int', (_java_old_45 + (1)))), _java_old_45)[4]
                ((_java_obj_46 := Code01_FutureDiary1.sum2[i]), (_java_key_47 := Code01_FutureDiary1.arr[j]), (_java_old_48 := jget(_java_obj_46, _java_key_47)), jset(_java_obj_46, _java_key_47, jcast('int', (_java_old_48 + (1)))), _java_old_48)[4]
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code01_FutureDiary1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_FutureDiary1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_FutureDiary1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_FutureDiary1.n):
            jset(Code01_FutureDiary1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code01_FutureDiary1.prepare()
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        x = 0
        y = 0
        k = 0
        while (i <= Code01_FutureDiary1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            if (op == 1):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                Code01_FutureDiary1.update(l, r, x, y)
            else:
                k = jcast('int', jcall(in_, 'nextInt'))
                jcall(out, 'println', Code01_FutureDiary1.query(l, r, k))
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
            return jcast('int', self.buffer[((_java_obj_49 := self), (_java_key_50 := 'ptr'), (_java_old_51 := jget(_java_obj_49, _java_key_50)), jset(_java_obj_49, _java_key_50, jcast('int', (_java_old_51 + (1)))), _java_old_51)[4]])

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
            raise TypeError("No matching overload for Code01_FutureDiary1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_FutureDiary1.MAXN = jcast('int', 100001)
Code01_FutureDiary1.MAXB = jcast('int', 401)
Code01_FutureDiary1.n = jcast('int', 0)
Code01_FutureDiary1.m = jcast('int', 0)
Code01_FutureDiary1.arr = jarray('int', [Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.blen = jcast('int', 0)
Code01_FutureDiary1.bnum = jcast('int', 0)
Code01_FutureDiary1.bi = jarray('int', [Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.bl = jarray('int', [Code01_FutureDiary1.MAXB])
Code01_FutureDiary1.br = jarray('int', [Code01_FutureDiary1.MAXB])
Code01_FutureDiary1.idxset = jarray('int', [Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.valset = jarray('int', [Code01_FutureDiary1.MAXB, Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.setval = jarray('int', [Code01_FutureDiary1.MAXB, Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.sum1 = jarray('int', [Code01_FutureDiary1.MAXB, Code01_FutureDiary1.MAXB])
Code01_FutureDiary1.sum2 = jarray('int', [Code01_FutureDiary1.MAXB, Code01_FutureDiary1.MAXN])
Code01_FutureDiary1.cnt1 = jarray('int', [Code01_FutureDiary1.MAXB])
Code01_FutureDiary1.cnt2 = jarray('int', [Code01_FutureDiary1.MAXN])

if __name__ == '__main__':
    Code01_FutureDiary1.main([])

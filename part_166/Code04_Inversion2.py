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

# 区间逆序对，Python版
# 给定一个长度为n的排列，接下来有m条操作，每条操作格式如下
# 操作 l r : 打印arr[l..r]范围上的逆序对数量
# 1 <= n、m <= 10^5
# 题目要求强制在线，具体规则可以打开测试链接查看
# 测试链接 : https://www.luogu.com.cn/problem/P5046
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 正式比赛不卡常
class Code04_Inversion2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXB': 'MAXB', 'n': 'n', 'm': 'm', 'arr': 'arr', 'sortv': 'sortv', 'blen': 'blen', 'bnum': 'bnum', 'bi': 'bi', 'bl': 'bl', 'br': 'br', 'tree': 'tree', 'pre': 'pre', 'suf': 'suf', 'cnt': 'cnt', 'dp': 'dp'}
    MAXN = 0
    MAXB = 0
    n = 0
    m = 0
    arr = None
    # (数值、位置)
    sortv = None
    blen = 0
    bnum = 0
    bi = None
    bl = None
    br = None
    # 树状数组，为了快速生成pre数组和suf数组
    tree = None
    # pre[i] : 从所在块最左位置到i位置，有多少逆序对
    pre = None
    # suf[i] : 从i位置到所在块最右位置，有多少逆序对
    suf = None
    # cnt[i][j] : 前i块里<=j的数字个数
    cnt = None
    # dp[i][j] : 从第i块到第j块有多少逆序对
    dp = None
    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def add(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code04_Inversion2.n):
            Code04_Inversion2.tree[i] = jcast('int', jcast('int', jadd(Code04_Inversion2.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code04_Inversion2.lowbit(i))))

    @staticmethod
    def sum(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code04_Inversion2.tree[i])))
            i = jcast('int', jcast('int', (i - Code04_Inversion2.lowbit(i))))
        return jcast('int', ret)

    # 更靠左的第x块，从xl到xr范围上，选第一个数
    # 更靠右的第y块，从yl到yr范围上，选第二个数
    # x和y可以相等，但是xl..xr需要在yl..yr的左侧
    # 返回逆序对数量
    @staticmethod
    def f(x, xl, xr, y, yl, yr):
        x = jcast('int', x)
        xl = jcast('int', xl)
        xr = jcast('int', xr)
        y = jcast('int', y)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        ans = jcast('int', 0)
        p1 = jcast('int', Code04_Inversion2.bl[x])
        p2 = jcast('int', jcast('int', (Code04_Inversion2.bl[y] - 1)))
        cnt = jcast('int', 0)
        while (p1 <= Code04_Inversion2.br[x]):
            if ((xl <= Code04_Inversion2.sortv[p1][1]) and (Code04_Inversion2.sortv[p1][1] <= xr)):
                while ((jcast('int', jadd(p2, 1)) <= Code04_Inversion2.br[y]) and (Code04_Inversion2.sortv[p1][0] > Code04_Inversion2.sortv[jcast('int', jadd(p2, 1))][0])):
                    p2 = jcast('int', (p2 + 1))
                    if ((yl <= Code04_Inversion2.sortv[p2][1]) and (Code04_Inversion2.sortv[p2][1] <= yr)):
                        cnt = jcast('int', (cnt + 1))
                ans = jcast('int', jcast('int', jadd(ans, cnt)))
            p1 = jcast('int', (p1 + 1))
        return jcast('int', ans)

    @staticmethod
    def query(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        ans = jcast('long', 0)
        lb = jcast('int', Code04_Inversion2.bi[l])
        rb = jcast('int', Code04_Inversion2.bi[r])
        if (lb == rb):
            if (l == Code04_Inversion2.bl[lb]):
                ans = jcast('long', Code04_Inversion2.pre[r])
            else:
                ans = jcast('long', jcast('int', (jcast('int', (Code04_Inversion2.pre[r] - Code04_Inversion2.pre[jcast('int', (l - 1))])) - Code04_Inversion2.f(lb, Code04_Inversion2.bl[lb], jcast('int', (l - 1)), lb, l, r))))
        else:
            # 左散块[l..]内部逆序对 + 右散块[..r]内部逆序对 + 左散块 结合 右散块 的逆序对
            ans = jcast('long', jcast('int', jadd(jcast('int', jadd(Code04_Inversion2.suf[l], Code04_Inversion2.pre[r])), Code04_Inversion2.f(lb, l, Code04_Inversion2.br[lb], rb, Code04_Inversion2.bl[rb], r))))
            # 左散块中的arr[i]，作为第一个数
            # 中间整块中的某个数字，作为第二个数
            # 计算这样的逆序对数量
            # 注意因为题目给定的是排列！所以如下这么写没问题
            i = jcast('int', l)
            while (i <= Code04_Inversion2.br[lb]):
                ans = jcast('long', jcast('long', jadd(ans, jcast('int', (Code04_Inversion2.cnt[jcast('int', (rb - 1))][Code04_Inversion2.arr[i]] - Code04_Inversion2.cnt[lb][Code04_Inversion2.arr[i]])))))
                i = jcast('int', (i + 1))
            # 中间整块中的某个数字，作为第一个数
            # 右散块中的arr[i]，作为第二个数
            # 计算这样的逆序对数量
            i = jcast('int', Code04_Inversion2.bl[rb])
            while (i <= r):
                ans = jcast('long', jcast('long', jadd(ans, jcast('int', (jcast('int', jadd(jcast('int', (Code04_Inversion2.br[jcast('int', (rb - 1))] - Code04_Inversion2.bl[jcast('int', jadd(lb, 1))])), 1)) - jcast('int', (Code04_Inversion2.cnt[jcast('int', (rb - 1))][Code04_Inversion2.arr[i]] - Code04_Inversion2.cnt[lb][Code04_Inversion2.arr[i]])))))))
                i = jcast('int', (i + 1))
            # 中间整块的逆序对
            ans = jcast('long', jcast('long', jadd(ans, Code04_Inversion2.dp[jcast('int', jadd(lb, 1))][jcast('int', (rb - 1))])))
        return jcast('long', ans)

    # 注意调整块长
    @staticmethod
    def prepare():
        Code04_Inversion2.blen = jcast('int', jcast('int', jstatic('Math', 'sqrt', jcast('int', jdiv(Code04_Inversion2.n, 4)))))
        Code04_Inversion2.bnum = jcast('int', jcast('int', jdiv(jcast('int', (jcast('int', jadd(Code04_Inversion2.n, Code04_Inversion2.blen)) - 1)), Code04_Inversion2.blen)))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.n):
            Code04_Inversion2.bi[i] = jcast('int', jcast('int', jadd(jcast('int', jdiv(jcast('int', (i - 1)), Code04_Inversion2.blen)), 1)))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.bnum):
            Code04_Inversion2.bl[i] = jcast('int', jcast('int', jadd(jcast('int', (jcast('int', (i - 1)) * Code04_Inversion2.blen)), 1)))
            jset(Code04_Inversion2.br, i, jstatic('Math', 'min', jcast('int', (i * Code04_Inversion2.blen)), Code04_Inversion2.n))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.n):
            jset(Code04_Inversion2.sortv[i], 0, Code04_Inversion2.arr[i])
            jset(Code04_Inversion2.sortv[i], 1, i)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.bnum):
            jstatic('Arrays', 'sort', Code04_Inversion2.sortv, Code04_Inversion2.bl[i], jcast('int', jadd(Code04_Inversion2.br[i], 1)), (lambda a, b: ((a[0] - b[0]) if (a[0] != b[0]) else (a[1] - b[1]))))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.bnum):
            j = jcast('int', Code04_Inversion2.bl[i])
            while (j <= Code04_Inversion2.br[i]):
                ((_java_obj_1 := Code04_Inversion2.cnt[i]), (_java_key_2 := Code04_Inversion2.arr[j]), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]
                if (j != Code04_Inversion2.bl[i]):
                    jset(Code04_Inversion2.pre, j, jcast('int', (jcast('int', jadd(Code04_Inversion2.pre[jcast('int', (j - 1))], Code04_Inversion2.sum(Code04_Inversion2.n))) - Code04_Inversion2.sum(Code04_Inversion2.arr[j]))))
                Code04_Inversion2.add(Code04_Inversion2.arr[j], 1)
                j = jcast('int', (j + 1))
            j = jcast('int', Code04_Inversion2.bl[i])
            while (j <= Code04_Inversion2.br[i]):
                Code04_Inversion2.add(Code04_Inversion2.arr[j], jcast('int', (-1)))
                j = jcast('int', (j + 1))
            j = jcast('int', Code04_Inversion2.br[i])
            while (j >= Code04_Inversion2.bl[i]):
                if (j != Code04_Inversion2.br[i]):
                    jset(Code04_Inversion2.suf, j, jcast('int', jadd(Code04_Inversion2.suf[jcast('int', jadd(j, 1))], Code04_Inversion2.sum(Code04_Inversion2.arr[j]))))
                Code04_Inversion2.add(Code04_Inversion2.arr[j], 1)
                j = jcast('int', (j - 1))
            j = jcast('int', Code04_Inversion2.bl[i])
            while (j <= Code04_Inversion2.br[i]):
                Code04_Inversion2.add(Code04_Inversion2.arr[j], jcast('int', (-1)))
                j = jcast('int', (j + 1))
            tmp = jcast('int', 0)
            j = jcast('int', 1)
            while (j <= Code04_Inversion2.n):
                tmp = jcast('int', jcast('int', jadd(tmp, Code04_Inversion2.cnt[i][j])))
                jset(Code04_Inversion2.cnt[i], j, jcast('int', jadd(tmp, Code04_Inversion2.cnt[jcast('int', (i - 1))][j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        l = jcast('int', Code04_Inversion2.bnum)
        while (l >= 1):
            jset(Code04_Inversion2.dp[l], l, Code04_Inversion2.pre[Code04_Inversion2.br[l]])
            r = jcast('int', jcast('int', jadd(l, 1)))
            while (r <= Code04_Inversion2.bnum):
                jset(Code04_Inversion2.dp[l], r, jcast('long', jadd(jcast('long', (jcast('long', jadd(Code04_Inversion2.dp[jcast('int', jadd(l, 1))][r], Code04_Inversion2.dp[l][jcast('int', (r - 1))])) - Code04_Inversion2.dp[jcast('int', jadd(l, 1))][jcast('int', (r - 1))])), Code04_Inversion2.f(l, Code04_Inversion2.bl[l], Code04_Inversion2.br[l], r, Code04_Inversion2.bl[r], Code04_Inversion2.br[r]))))
                r = jcast('int', (r + 1))
            l = jcast('int', (l - 1))

    @staticmethod
    def main(args):
        in_ = Code04_Inversion2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Inversion2.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Inversion2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code04_Inversion2.n):
            jset(Code04_Inversion2.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code04_Inversion2.prepare()
        lastAns = jcast('long', 0)
        i = jcast('int', 1)
        l = 0
        r = 0
        while (i <= Code04_Inversion2.m):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            l = jcast('int', jcast('int', jcast('long', (lastAns ^ l))))
            r = jcast('int', jcast('int', jcast('long', (lastAns ^ r))))
            lastAns = jcast('long', Code04_Inversion2.query(l, r))
            jcall(out, 'println', lastAns)
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
            return jcast('int', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

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
            raise TypeError("No matching overload for Code04_Inversion2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_Inversion2.MAXN = jcast('int', 100001)
Code04_Inversion2.MAXB = jcast('int', 701)
Code04_Inversion2.n = jcast('int', 0)
Code04_Inversion2.m = jcast('int', 0)
Code04_Inversion2.arr = jarray('int', [Code04_Inversion2.MAXN])
Code04_Inversion2.sortv = jarray('int', [Code04_Inversion2.MAXN, 2])
Code04_Inversion2.blen = jcast('int', 0)
Code04_Inversion2.bnum = jcast('int', 0)
Code04_Inversion2.bi = jarray('int', [Code04_Inversion2.MAXN])
Code04_Inversion2.bl = jarray('int', [Code04_Inversion2.MAXB])
Code04_Inversion2.br = jarray('int', [Code04_Inversion2.MAXB])
Code04_Inversion2.tree = jarray('int', [Code04_Inversion2.MAXN])
Code04_Inversion2.pre = jarray('int', [Code04_Inversion2.MAXN])
Code04_Inversion2.suf = jarray('int', [Code04_Inversion2.MAXN])
Code04_Inversion2.cnt = jarray('int', [Code04_Inversion2.MAXB, Code04_Inversion2.MAXN])
Code04_Inversion2.dp = jarray('long', [Code04_Inversion2.MAXB, Code04_Inversion2.MAXB])

if __name__ == '__main__':
    Code04_Inversion2.main([])

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

# 须臾幻境，Python版
# 无向图中有n个点、m条无向边，边的编号是1~m
# 每条询问的格式为 l r，表示保留编号[l, r]的边，打印有多少个连通块
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 1 <= n <= 10^5
# 1 <= m <= 2 * 10^5
# 1 <= q <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5385
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code07_Fairyland2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'm': 'm', 'q': 'q', 't': 't', 'eu': 'eu', 'ev': 'ev', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'val': 'val', 'minv': 'minv', 'root': 'root', 'tl': 'tl', 'tr': 'tr', 'num': 'num', 'cntt': 'cntt'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    m = 0
    q = 0
    t = 0
    eu = None
    ev = None
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # 原图的点x，在LCT中编号x，权值为INF，是无效值
    # 原图的边i，在LCT中编号n+i，权值为i，是边序号
    val = None
    # minv[x]表示以x为根的辅助splay，汇总最小的边序号
    minv = None
    # 可持久化线段树，记录每个生成的森林中，每条边是否存在
    root = None
    tl = None
    tr = None
    num = None
    cntt = 0
    @staticmethod
    def up(x):
        x = jcast('int', x)
        jset(Code07_Fairyland2.minv, x, jstatic('Math', 'min', Code07_Fairyland2.val[x], jstatic('Math', 'min', Code07_Fairyland2.minv[Code07_Fairyland2.ls[x]], Code07_Fairyland2.minv[Code07_Fairyland2.rs[x]])))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code07_Fairyland2.ls[Code07_Fairyland2.fa[x]] != x) and (Code07_Fairyland2.rs[Code07_Fairyland2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code07_Fairyland2.ls[Code07_Fairyland2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code07_Fairyland2.ls[x])
            Code07_Fairyland2.ls[x] = jcast('int', Code07_Fairyland2.rs[x])
            Code07_Fairyland2.rs[x] = jcast('int', tmp)
            Code07_Fairyland2.rev[x] = jcast('boolean', (not Code07_Fairyland2.rev[x]))

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code07_Fairyland2.rev[x]:
            Code07_Fairyland2.reverse(Code07_Fairyland2.ls[x])
            Code07_Fairyland2.reverse(Code07_Fairyland2.rs[x])
            Code07_Fairyland2.rev[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code07_Fairyland2.fa[x])
        g = jcast('int', Code07_Fairyland2.fa[f])
        if (Code07_Fairyland2.lr(x) == 0):
            Code07_Fairyland2.ls[f] = jcast('int', Code07_Fairyland2.rs[x])
            if (Code07_Fairyland2.ls[f] != 0):
                jset(Code07_Fairyland2.fa, Code07_Fairyland2.ls[f], f)
            Code07_Fairyland2.rs[x] = jcast('int', f)
        else:
            Code07_Fairyland2.rs[f] = jcast('int', Code07_Fairyland2.ls[x])
            if (Code07_Fairyland2.rs[f] != 0):
                jset(Code07_Fairyland2.fa, Code07_Fairyland2.rs[f], f)
            Code07_Fairyland2.ls[x] = jcast('int', f)
        if (not Code07_Fairyland2.isroot(f)):
            if (Code07_Fairyland2.lr(f) == 0):
                Code07_Fairyland2.ls[g] = jcast('int', x)
            else:
                Code07_Fairyland2.rs[g] = jcast('int', x)
        Code07_Fairyland2.fa[f] = jcast('int', x)
        Code07_Fairyland2.fa[x] = jcast('int', g)
        Code07_Fairyland2.up(f)
        Code07_Fairyland2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        size = jcast('int', 0)
        jset(Code07_Fairyland2.sta, (size := jcast('int', (size + (1)))), x)
        y = jcast('int', x)
        while (not Code07_Fairyland2.isroot(y)):
            jset(Code07_Fairyland2.sta, (size := jcast('int', (size + (1)))), Code07_Fairyland2.fa[y])
            y = jcast('int', Code07_Fairyland2.fa[y])
        while (size != 0):
            Code07_Fairyland2.down(Code07_Fairyland2.sta[((_java_old_1 := size), (size := jcast('int', (size + (-1)))), _java_old_1)[2]])
        while (not Code07_Fairyland2.isroot(x)):
            f = jcast('int', Code07_Fairyland2.fa[x])
            if (not Code07_Fairyland2.isroot(f)):
                if (Code07_Fairyland2.lr(x) == Code07_Fairyland2.lr(f)):
                    Code07_Fairyland2.rotate(f)
                else:
                    Code07_Fairyland2.rotate(x)
            Code07_Fairyland2.rotate(x)
        Code07_Fairyland2.up(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code07_Fairyland2.splay(x)
            Code07_Fairyland2.rs[x] = jcast('int', y)
            Code07_Fairyland2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code07_Fairyland2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code07_Fairyland2.access(x)
        Code07_Fairyland2.splay(x)
        Code07_Fairyland2.reverse(x)

    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code07_Fairyland2.access(x)
        Code07_Fairyland2.splay(x)
        Code07_Fairyland2.down(x)
        while (Code07_Fairyland2.ls[x] != 0):
            x = jcast('int', Code07_Fairyland2.ls[x])
            Code07_Fairyland2.down(x)
        Code07_Fairyland2.splay(x)
        return jcast('int', x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Fairyland2.makeroot(x)
        Code07_Fairyland2.access(y)
        Code07_Fairyland2.splay(y)

    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Fairyland2.makeroot(x)
        if (Code07_Fairyland2.findroot(y) != x):
            Code07_Fairyland2.fa[x] = jcast('int', y)

    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Fairyland2.makeroot(x)
        if ((((Code07_Fairyland2.findroot(y) == x) and (Code07_Fairyland2.fa[y] == x)) and (Code07_Fairyland2.ls[y] == 0)) and (Code07_Fairyland2.rs[x] == y)):
            jset(Code07_Fairyland2.fa, y, jset(Code07_Fairyland2.rs, x, 0))
            Code07_Fairyland2.up(x)

    # 查询x到y路径上编号最小的边
    @staticmethod
    def pathMin(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code07_Fairyland2.split(x, y)
        return jcast('int', Code07_Fairyland2.minv[y])

    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        rt = jcast('int', ((_java_obj_2 := Code07_Fairyland2), (_java_key_3 := 'cntt'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3])
        Code07_Fairyland2.tl[rt] = jcast('int', Code07_Fairyland2.tl[i])
        Code07_Fairyland2.tr[rt] = jcast('int', Code07_Fairyland2.tr[i])
        Code07_Fairyland2.num[rt] = jcast('int', Code07_Fairyland2.num[i])
        if (l == r):
            Code07_Fairyland2.num[rt] = jcast('int', jcast('int', jadd(Code07_Fairyland2.num[rt], jobv)))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                jset(Code07_Fairyland2.tl, rt, Code07_Fairyland2.add(jobi, jobv, l, mid, Code07_Fairyland2.tl[i]))
            else:
                jset(Code07_Fairyland2.tr, rt, Code07_Fairyland2.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, Code07_Fairyland2.tr[i]))
            Code07_Fairyland2.num[rt] = jcast('int', jcast('int', jadd(Code07_Fairyland2.num[Code07_Fairyland2.tl[rt]], Code07_Fairyland2.num[Code07_Fairyland2.tr[rt]])))
        return jcast('int', rt)

    @staticmethod
    def query(jobl, jobr, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code07_Fairyland2.num[i])
        ans = jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code07_Fairyland2.query(jobl, jobr, l, mid, Code07_Fairyland2.tl[i]))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code07_Fairyland2.query(jobl, jobr, jcast('int', jadd(mid, 1)), r, Code07_Fairyland2.tr[i]))))
        return jcast('int', ans)

    @staticmethod
    def prepare():
        i = jcast('int', 0)
        while (i <= Code07_Fairyland2.n):
            jset(Code07_Fairyland2.val, i, jset(Code07_Fairyland2.minv, i, Code07_Fairyland2.INF))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Fairyland2.m):
            jset(Code07_Fairyland2.val, jcast('int', jadd(Code07_Fairyland2.n, i)), jset(Code07_Fairyland2.minv, jcast('int', jadd(Code07_Fairyland2.n, i)), i))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code07_Fairyland2.m):
            x = jcast('int', Code07_Fairyland2.eu[i])
            y = jcast('int', Code07_Fairyland2.ev[i])
            Code07_Fairyland2.root[i] = jcast('int', Code07_Fairyland2.root[jcast('int', (i - 1))])
            if (x != y):
                if (Code07_Fairyland2.findroot(x) == Code07_Fairyland2.findroot(y)):
                    e = jcast('int', Code07_Fairyland2.pathMin(x, y))
                    Code07_Fairyland2.cut(Code07_Fairyland2.eu[e], jcast('int', jadd(Code07_Fairyland2.n, e)))
                    Code07_Fairyland2.cut(Code07_Fairyland2.ev[e], jcast('int', jadd(Code07_Fairyland2.n, e)))
                    jset(Code07_Fairyland2.root, i, Code07_Fairyland2.add(e, jcast('int', (-1)), 1, Code07_Fairyland2.m, Code07_Fairyland2.root[i]))
                Code07_Fairyland2.link(x, jcast('int', jadd(Code07_Fairyland2.n, i)))
                Code07_Fairyland2.link(y, jcast('int', jadd(Code07_Fairyland2.n, i)))
                jset(Code07_Fairyland2.root, i, Code07_Fairyland2.add(i, 1, 1, Code07_Fairyland2.m, Code07_Fairyland2.root[i]))
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code07_Fairyland2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code07_Fairyland2.n = jcast('int', jcall(in_, 'nextInt'))
        Code07_Fairyland2.m = jcast('int', jcall(in_, 'nextInt'))
        Code07_Fairyland2.q = jcast('int', jcall(in_, 'nextInt'))
        Code07_Fairyland2.t = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code07_Fairyland2.m):
            jset(Code07_Fairyland2.eu, i, jcall(in_, 'nextInt'))
            jset(Code07_Fairyland2.ev, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code07_Fairyland2.prepare()
        i = jcast('int', 1)
        lastAns = jcast('int', 0)
        l = 0
        r = 0
        while (i <= Code07_Fairyland2.q):
            l = jcast('int', jcall(in_, 'nextInt'))
            r = jcast('int', jcall(in_, 'nextInt'))
            if (Code07_Fairyland2.t > 0):
                l = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(l, jcast('int', (Code07_Fairyland2.t * lastAns)))), Code07_Fairyland2.m)), 1)))
                r = jcast('int', jcast('int', jadd(jcast('int', jmod(jcast('int', jadd(r, jcast('int', (Code07_Fairyland2.t * lastAns)))), Code07_Fairyland2.m)), 1)))
            if (l > r):
                tmp = jcast('int', l)
                l = jcast('int', r)
                r = jcast('int', tmp)
            lastAns = jcast('int', jcast('int', (Code07_Fairyland2.n - Code07_Fairyland2.query(l, r, 1, Code07_Fairyland2.m, Code07_Fairyland2.root[r]))))
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
            return jcast('int', self.buffer[((_java_obj_5 := self), (_java_key_6 := 'ptr'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))), _java_old_7)[4]])

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
                val = jcast('int', jcast('int', (jcast('int', jadd(jcast('int', (val * 10)), c)) - jchar('0'))))
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
            raise TypeError("No matching overload for Code07_Fairyland2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code07_Fairyland2.MAXN = jcast('int', 300001)
Code07_Fairyland2.MAXT = jcast('int', 10000001)
Code07_Fairyland2.INF = jcast('int', 1000000001)
Code07_Fairyland2.n = jcast('int', 0)
Code07_Fairyland2.m = jcast('int', 0)
Code07_Fairyland2.q = jcast('int', 0)
Code07_Fairyland2.t = jcast('int', 0)
Code07_Fairyland2.eu = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.ev = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.fa = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.ls = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.rs = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.rev = jarray('boolean', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.sta = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.val = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.minv = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.root = jarray('int', [Code07_Fairyland2.MAXN])
Code07_Fairyland2.tl = jarray('int', [Code07_Fairyland2.MAXT])
Code07_Fairyland2.tr = jarray('int', [Code07_Fairyland2.MAXT])
Code07_Fairyland2.num = jarray('int', [Code07_Fairyland2.MAXT])
Code07_Fairyland2.cntt = jcast('int', 0)

if __name__ == '__main__':
    Code07_Fairyland2.main([])

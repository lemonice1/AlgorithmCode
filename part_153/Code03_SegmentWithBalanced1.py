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

# 线段树套平衡树，Python版
# 给定一个长度为n的数组arr，下标1~n，每条操作都是如下5种类型中的一种，一共进行m次操作
# 操作 1 x y z : 查询数字z在arr[x..y]中的排名
# 操作 2 x y z : 查询arr[x..y]中排第z名的数字
# 操作 3 x y   : arr中x位置的数字改成y
# 操作 4 x y z : 查询数字z在arr[x..y]中的前驱，不存在返回-2147483647
# 操作 5 x y z : 查询数字z在arr[x..y]中的后继，不存在返回+2147483647
# 1 <= n、m <= 2 * 10^5
# 数组中的值永远在[0, 10^8]范围内
# 测试链接 : https://www.luogu.com.cn/problem/P3380
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
# 此实现展示一种非最优思路，复杂度可能不满足题目的最大数据规模
# 本实现保留原算法思路，运行开销需结合数据规模与 Python 运行环境评估
# 对应实现可参考 Code03_SegmentWithBalanced2.py
# 两个版本保留相同的算法逻辑
class Code03_SegmentWithBalanced1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'INF': 'INF', 'n': 'n', 'm': 'm', 'arr': 'arr', 'cntn': 'cntn', 'root': 'root', 'key': 'key', 'ls': 'ls', 'rs': 'rs', 'alive': 'alive', 'aliveSiz': 'aliveSiz', 'ALPHA': 'ALPHA', 'top': 'top', 'father': 'father', 'side': 'side', 'collect': 'collect', 'collectSiz': 'collectSiz'}
    MAXN = 0
    MAXT = 0
    INF = 0
    n = 0
    m = 0
    arr = None
    # 替罪羊树的节点计数
    cntn = 0
    # 线段树维护的替罪羊树根节点编号
    root = None
    # 替罪羊树，讲解150
    key = None
    ls = None
    rs = None
    alive = None
    aliveSiz = None
    ALPHA = 0.0
    top = 0
    father = 0
    side = 0
    collect = None
    collectSiz = 0
    # 初始化替罪羊树的节点，返回节点编号
    @staticmethod
    def init(num):
        num = jcast('int', num)
        jset(Code03_SegmentWithBalanced1.key, ((_java_obj_1 := Code03_SegmentWithBalanced1), (_java_key_2 := 'cntn'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], num)
        jset(Code03_SegmentWithBalanced1.ls, Code03_SegmentWithBalanced1.cntn, jset(Code03_SegmentWithBalanced1.rs, Code03_SegmentWithBalanced1.cntn, 0))
        Code03_SegmentWithBalanced1.alive[Code03_SegmentWithBalanced1.cntn] = jcast('boolean', True)
        Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.cntn] = jcast('int', 1)
        return jcast('int', Code03_SegmentWithBalanced1.cntn)

    # 汇总存活节点信息
    @staticmethod
    def up(i):
        i = jcast('int', i)
        Code03_SegmentWithBalanced1.aliveSiz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd((1 if Code03_SegmentWithBalanced1.alive[i] else 0), Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]])), Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.rs[i]])))

    # 替罪羊树判断平衡
    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code03_SegmentWithBalanced1.ALPHA * Code03_SegmentWithBalanced1.aliveSiz[i]) >= jstatic('Math', 'max', Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]], Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.rs[i]])))

    # 中序遍历收集不平衡子树的存活节点
    @staticmethod
    def inorder(i):
        i = jcast('int', i)
        if ((i != 0) and (Code03_SegmentWithBalanced1.aliveSiz[i] != 0)):
            Code03_SegmentWithBalanced1.inorder(Code03_SegmentWithBalanced1.ls[i])
            if Code03_SegmentWithBalanced1.alive[i]:
                jset(Code03_SegmentWithBalanced1.collect, ((_java_obj_4 := Code03_SegmentWithBalanced1), (_java_key_5 := 'collectSiz'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3], i)
            Code03_SegmentWithBalanced1.inorder(Code03_SegmentWithBalanced1.rs[i])

    # 替罪羊树建树
    @staticmethod
    def build(l, r):
        l = jcast('int', l)
        r = jcast('int', r)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', jdiv(jcast('int', jadd(l, r)), 2)))
        h = jcast('int', Code03_SegmentWithBalanced1.collect[mid])
        jset(Code03_SegmentWithBalanced1.ls, h, Code03_SegmentWithBalanced1.build(l, jcast('int', (mid - 1))))
        jset(Code03_SegmentWithBalanced1.rs, h, Code03_SegmentWithBalanced1.build(jcast('int', jadd(mid, 1)), r))
        Code03_SegmentWithBalanced1.up(h)
        return jcast('int', h)

    # 替罪羊树上，加入数字num，返回头节点编号
    @staticmethod
    def treeAdd(i, f, s, num):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        num = jcast('int', num)
        if ((i == 0) or (Code03_SegmentWithBalanced1.aliveSiz[i] == 0)):
            return jcast('int', Code03_SegmentWithBalanced1.init(num))
        if (num <= Code03_SegmentWithBalanced1.key[i]):
            jset(Code03_SegmentWithBalanced1.ls, i, Code03_SegmentWithBalanced1.treeAdd(Code03_SegmentWithBalanced1.ls[i], i, 1, num))
        else:
            jset(Code03_SegmentWithBalanced1.rs, i, Code03_SegmentWithBalanced1.treeAdd(Code03_SegmentWithBalanced1.rs[i], i, 2, num))
        Code03_SegmentWithBalanced1.up(i)
        if (not Code03_SegmentWithBalanced1.balance(i)):
            Code03_SegmentWithBalanced1.top = jcast('int', i)
            Code03_SegmentWithBalanced1.father = jcast('int', f)
            Code03_SegmentWithBalanced1.side = jcast('int', s)
        return jcast('int', i)

    # 替罪羊树上，查询<num的数字个数
    @staticmethod
    def treeSmall(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        if ((i == 0) or (Code03_SegmentWithBalanced1.aliveSiz[i] == 0)):
            return jcast('int', 0)
        if (num <= Code03_SegmentWithBalanced1.key[i]):
            return jcast('int', Code03_SegmentWithBalanced1.treeSmall(Code03_SegmentWithBalanced1.ls[i], num))
        else:
            return jcast('int', jcast('int', jadd(jcast('int', jadd(Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]], (1 if Code03_SegmentWithBalanced1.alive[i] else 0))), Code03_SegmentWithBalanced1.treeSmall(Code03_SegmentWithBalanced1.rs[i], num))))

    # 替罪羊树上，查询第x小的数字
    @staticmethod
    def treeIndex(i, x):
        i = jcast('int', i)
        x = jcast('int', x)
        if (x <= Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]]):
            return jcast('int', Code03_SegmentWithBalanced1.treeIndex(Code03_SegmentWithBalanced1.ls[i], x))
        else:
            less = jcast('int', jcast('int', jadd(Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]], (1 if Code03_SegmentWithBalanced1.alive[i] else 0))))
            if (less < x):
                return jcast('int', Code03_SegmentWithBalanced1.treeIndex(Code03_SegmentWithBalanced1.rs[i], jcast('int', (x - less))))
        return jcast('int', Code03_SegmentWithBalanced1.key[i])

    # 替罪羊树上，删除排名是rank的数字
    @staticmethod
    def treeRemove(i, f, s, rank):
        i = jcast('int', i)
        f = jcast('int', f)
        s = jcast('int', s)
        rank = jcast('int', rank)
        lsiz = jcast('int', Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.ls[i]])
        if (rank <= lsiz):
            Code03_SegmentWithBalanced1.treeRemove(Code03_SegmentWithBalanced1.ls[i], i, 1, rank)
        else:
            cur = jcast('int', (1 if Code03_SegmentWithBalanced1.alive[i] else 0))
            if (Code03_SegmentWithBalanced1.alive[i] and (rank == jcast('int', jadd(lsiz, cur)))):
                Code03_SegmentWithBalanced1.alive[i] = jcast('boolean', False)
            else:
                Code03_SegmentWithBalanced1.treeRemove(Code03_SegmentWithBalanced1.rs[i], i, 2, jcast('int', (jcast('int', (rank - lsiz)) - cur)))
        Code03_SegmentWithBalanced1.up(i)
        if (not Code03_SegmentWithBalanced1.balance(i)):
            Code03_SegmentWithBalanced1.top = jcast('int', i)
            Code03_SegmentWithBalanced1.father = jcast('int', f)
            Code03_SegmentWithBalanced1.side = jcast('int', s)

    # 替罪羊树的局部重构，如果整棵树换头，则修改root[version]
    @staticmethod
    def rebuild(version):
        version = jcast('int', version)
        if (Code03_SegmentWithBalanced1.top != 0):
            Code03_SegmentWithBalanced1.collectSiz = jcast('int', 0)
            Code03_SegmentWithBalanced1.inorder(Code03_SegmentWithBalanced1.top)
            newRoot = jcast('int', Code03_SegmentWithBalanced1.build(1, Code03_SegmentWithBalanced1.collectSiz))
            if (Code03_SegmentWithBalanced1.father == 0):
                Code03_SegmentWithBalanced1.root[version] = jcast('int', newRoot)
            else:
                if (Code03_SegmentWithBalanced1.side == 1):
                    Code03_SegmentWithBalanced1.ls[Code03_SegmentWithBalanced1.father] = jcast('int', newRoot)
                else:
                    Code03_SegmentWithBalanced1.rs[Code03_SegmentWithBalanced1.father] = jcast('int', newRoot)

    # 内层替罪羊树，版本是version，头节点是root[version]，加入数字num
    @staticmethod
    def innerAdd(version, num):
        version = jcast('int', version)
        num = jcast('int', num)
        Code03_SegmentWithBalanced1.top = jcast('int', jset(Code03_SegmentWithBalanced1, 'father', jset(Code03_SegmentWithBalanced1, 'side', 0)))
        jset(Code03_SegmentWithBalanced1.root, version, Code03_SegmentWithBalanced1.treeAdd(Code03_SegmentWithBalanced1.root[version], 0, 0, num))
        Code03_SegmentWithBalanced1.rebuild(version)

    # 内层替罪羊树，版本是version，头节点是root[version]，查询num的排名
    @staticmethod
    def innerRank(version, num):
        version = jcast('int', version)
        num = jcast('int', num)
        return jcast('int', jcast('int', jadd(Code03_SegmentWithBalanced1.treeSmall(Code03_SegmentWithBalanced1.root[version], num), 1)))

    # 内层替罪羊树，版本是version，头节点是root[version]，删除数字num
    @staticmethod
    def innerRemove(version, num):
        version = jcast('int', version)
        num = jcast('int', num)
        rank1 = jcast('int', Code03_SegmentWithBalanced1.innerRank(version, num))
        rank2 = jcast('int', Code03_SegmentWithBalanced1.innerRank(version, jcast('int', jadd(num, 1))))
        if (rank1 != rank2):
            Code03_SegmentWithBalanced1.top = jcast('int', jset(Code03_SegmentWithBalanced1, 'father', jset(Code03_SegmentWithBalanced1, 'side', 0)))
            Code03_SegmentWithBalanced1.treeRemove(Code03_SegmentWithBalanced1.root[version], 0, 0, rank1)
            Code03_SegmentWithBalanced1.rebuild(version)

    # 内层替罪羊树，版本是version，头节点是root[version]，查询num的前驱
    @staticmethod
    def innerPre(version, num):
        version = jcast('int', version)
        num = jcast('int', num)
        rank = jcast('int', Code03_SegmentWithBalanced1.innerRank(version, num))
        if (rank == 1):
            return jcast('int', jcast('int', (-Code03_SegmentWithBalanced1.INF)))
        else:
            return jcast('int', Code03_SegmentWithBalanced1.treeIndex(Code03_SegmentWithBalanced1.root[version], jcast('int', (rank - 1))))

    # 内层替罪羊树，版本是version，头节点是root[version]，查询num的后继
    @staticmethod
    def innerPost(version, num):
        version = jcast('int', version)
        num = jcast('int', num)
        rank = jcast('int', Code03_SegmentWithBalanced1.innerRank(version, jcast('int', jadd(num, 1))))
        if (rank == jcast('int', jadd(Code03_SegmentWithBalanced1.aliveSiz[Code03_SegmentWithBalanced1.root[version]], 1))):
            return jcast('int', Code03_SegmentWithBalanced1.INF)
        else:
            return jcast('int', Code03_SegmentWithBalanced1.treeIndex(Code03_SegmentWithBalanced1.root[version], rank))

    # 外层线段树
    @staticmethod
    def add(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        Code03_SegmentWithBalanced1.innerAdd(i, jobv)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code03_SegmentWithBalanced1.add(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code03_SegmentWithBalanced1.add(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    # 外层线段树
    @staticmethod
    def update(jobi, jobv, l, r, i):
        jobi = jcast('int', jobi)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        Code03_SegmentWithBalanced1.innerRemove(i, Code03_SegmentWithBalanced1.arr[jobi])
        Code03_SegmentWithBalanced1.innerAdd(i, jobv)
        if (l < r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobi <= mid):
                Code03_SegmentWithBalanced1.update(jobi, jobv, l, mid, jcast('int', (i << (1 & 31))))
            else:
                Code03_SegmentWithBalanced1.update(jobi, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    # 外层线段树
    @staticmethod
    def small(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_SegmentWithBalanced1.treeSmall(Code03_SegmentWithBalanced1.root[i], jobv))
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', 0)
        if (jobl <= mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_SegmentWithBalanced1.small(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31)))))))
        if (jobr > mid):
            ans = jcast('int', jcast('int', jadd(ans, Code03_SegmentWithBalanced1.small(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1))))))
        return jcast('int', ans)

    # 外层线段树
    @staticmethod
    def number(jobl, jobr, jobk):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobk = jcast('int', jobk)
        l = jcast('int', 0)
        r = jcast('int', 100000000)
        mid = 0
        ans = jcast('int', 0)
        while (l <= r):
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jcast('int', jadd(Code03_SegmentWithBalanced1.small(jobl, jobr, jcast('int', jadd(mid, 1)), 1, Code03_SegmentWithBalanced1.n, 1), 1)) > jobk):
                ans = jcast('int', mid)
                r = jcast('int', jcast('int', (mid - 1)))
            else:
                l = jcast('int', jcast('int', jadd(mid, 1)))
        return jcast('int', ans)

    # 外层线段树
    @staticmethod
    def pre(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_SegmentWithBalanced1.innerPre(i, jobv))
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', jcast('int', (-Code03_SegmentWithBalanced1.INF)))
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentWithBalanced1.pre(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'max', ans, Code03_SegmentWithBalanced1.pre(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    # 外层线段树
    @staticmethod
    def post(jobl, jobr, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            return jcast('int', Code03_SegmentWithBalanced1.innerPost(i, jobv))
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        ans = jcast('int', Code03_SegmentWithBalanced1.INF)
        if (jobl <= mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code03_SegmentWithBalanced1.post(jobl, jobr, jobv, l, mid, jcast('int', (i << (1 & 31))))))
        if (jobr > mid):
            ans = jcast('int', jstatic('Math', 'min', ans, Code03_SegmentWithBalanced1.post(jobl, jobr, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))))
        return jcast('int', ans)

    @staticmethod
    def main(args):
        in_ = Code03_SegmentWithBalanced1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_SegmentWithBalanced1.n = jcast('int', jcall(in_, 'nextInt'))
        Code03_SegmentWithBalanced1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code03_SegmentWithBalanced1.n):
            jset(Code03_SegmentWithBalanced1.arr, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code03_SegmentWithBalanced1.n):
            Code03_SegmentWithBalanced1.add(i, Code03_SegmentWithBalanced1.arr[i], 1, Code03_SegmentWithBalanced1.n, 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= Code03_SegmentWithBalanced1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 3):
                Code03_SegmentWithBalanced1.update(x, y, 1, Code03_SegmentWithBalanced1.n, 1)
                Code03_SegmentWithBalanced1.arr[x] = jcast('int', y)
            else:
                z = jcast('int', jcall(in_, 'nextInt'))
                if (op == 1):
                    jcall(out, 'println', jcast('int', jadd(Code03_SegmentWithBalanced1.small(x, y, z, 1, Code03_SegmentWithBalanced1.n, 1), 1)))
                else:
                    if (op == 2):
                        jcall(out, 'println', Code03_SegmentWithBalanced1.number(x, y, z))
                    else:
                        if (op == 4):
                            jcall(out, 'println', Code03_SegmentWithBalanced1.pre(x, y, z, 1, Code03_SegmentWithBalanced1.n, 1))
                        else:
                            jcall(out, 'println', Code03_SegmentWithBalanced1.post(x, y, z, 1, Code03_SegmentWithBalanced1.n, 1))
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
            return jcast('int', self.buffer[((_java_obj_7 := self), (_java_key_8 := 'ptr'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))), _java_old_9)[4]])

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
            raise TypeError("No matching overload for Code03_SegmentWithBalanced1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_SegmentWithBalanced1.MAXN = jcast('int', 200001)
Code03_SegmentWithBalanced1.MAXT = jcast('int', jcast('int', (Code03_SegmentWithBalanced1.MAXN * 40)))
Code03_SegmentWithBalanced1.INF = jcast('int', jget(Integer, 'MAX_VALUE'))
Code03_SegmentWithBalanced1.n = jcast('int', 0)
Code03_SegmentWithBalanced1.m = jcast('int', 0)
Code03_SegmentWithBalanced1.arr = jarray('int', [Code03_SegmentWithBalanced1.MAXN])
Code03_SegmentWithBalanced1.cntn = jcast('int', 0)
Code03_SegmentWithBalanced1.root = jarray('int', [jcast('int', (Code03_SegmentWithBalanced1.MAXN << (2 & 31)))])
Code03_SegmentWithBalanced1.key = jarray('int', [Code03_SegmentWithBalanced1.MAXT])
Code03_SegmentWithBalanced1.ls = jarray('int', [Code03_SegmentWithBalanced1.MAXT])
Code03_SegmentWithBalanced1.rs = jarray('int', [Code03_SegmentWithBalanced1.MAXT])
Code03_SegmentWithBalanced1.alive = jarray('boolean', [Code03_SegmentWithBalanced1.MAXT])
Code03_SegmentWithBalanced1.aliveSiz = jarray('int', [Code03_SegmentWithBalanced1.MAXT])
Code03_SegmentWithBalanced1.ALPHA = jcast('double', 0.7)
Code03_SegmentWithBalanced1.top = jcast('int', 0)
Code03_SegmentWithBalanced1.father = jcast('int', 0)
Code03_SegmentWithBalanced1.side = jcast('int', 0)
Code03_SegmentWithBalanced1.collect = jarray('int', [Code03_SegmentWithBalanced1.MAXN])
Code03_SegmentWithBalanced1.collectSiz = jcast('int', 0)

if __name__ == '__main__':
    Code03_SegmentWithBalanced1.main([])

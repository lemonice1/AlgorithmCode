# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 接水果，Python版
# 一共有n个点，给定n-1条无向边，所有点连成一棵树
# 一共有p个盘子，每个盘子格式 a b c : 盘子是点a到点b的路径，盘子权值为c
# 一共有q个水果，每个水果格式 u v k : 水果是点u到点v的路径，k含义如下
# 如果一个盘子路径完全在一个水果路径的内部，那么该盘子可以接住该水果
# 那么对于每个水果，可能有很多盘子都可以将其接住，打印其中第k小的权值
# 1 <= n、p、q <= 4 * 10^4
# 0 <= 盘子权值 <= 10^9
# 内存可用空间500MB
# 测试链接 : https://www.luogu.com.cn/problem/P3242
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_Fruit1:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'INF': 'INF', 'n': 'n', 'p': 'p', 'q': 'q', 'head': 'head', 'next': 'next', 'to': 'to', 'cntg': 'cntg', 'dep': 'dep', 'ldfn': 'ldfn', 'rdfn': 'rdfn', 'stjump': 'stjump', 'cntd': 'cntd', 'tree': 'tree', 'eid': 'eid', 'event': 'event', 'cnte': 'cnte', 'lset': 'lset', 'rset': 'rset', 'ans': 'ans', 'ufe': 'ufe', 'stacksize': 'stacksize', 'u': 'u', 'f': 'f', 'e': 'e'}
    MAXN = 0
    MAXP = 0
    INF = 0
    n = 0
    p = 0
    q = 0
    # 链式前向星
    head = None
    next = None
    to = None
    cntg = 0
    # 树上倍增 + 每棵子树上的ldfn和rdfn
    dep = None
    ldfn = None
    rdfn = None
    stjump = None
    cntd = 0
    # 只有y维度的树状数组
    tree = None
    # 所有事件排完序之后，依次把下标放入eid数组
    eid = None
    # 每个事件有8个属性值
    # op==1加盘子，x处加、yl、yr，盘子权值v、空缺、空缺、空缺
    # op==2删盘子，x处删、yl、yr，盘子权值v、空缺、空缺、空缺
    # op==3为水果，x、空缺、空缺、空缺、y、要求k、问题编号i
    event = None
    # 事件的总数
    cnte = 0
    # 整体二分
    lset = None
    rset = None
    # 每个水果的答案
    ans = None
    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code04_Fruit1.next, ((_java_obj_1 := Code04_Fruit1), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code04_Fruit1.head[u])
        Code04_Fruit1.to[Code04_Fruit1.cntg] = jcast('int', v)
        Code04_Fruit1.head[u] = jcast('int', Code04_Fruit1.cntg)

    # 递归版：深层遍历需考虑调用栈与内存开销，显式栈迭代可避免递归调用
    @staticmethod
    def dfs1(u, fa):
        u = jcast('int', u)
        fa = jcast('int', fa)
        Code04_Fruit1.dep[u] = jcast('int', jcast('int', jadd(Code04_Fruit1.dep[fa], 1)))
        jset(Code04_Fruit1.ldfn, u, ((_java_obj_4 := Code04_Fruit1), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3])
        jset(Code04_Fruit1.stjump[u], 0, fa)
        p = jcast('int', 1)
        while (p < Code04_Fruit1.MAXP):
            jset(Code04_Fruit1.stjump[u], p, Code04_Fruit1.stjump[Code04_Fruit1.stjump[u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
            p = jcast('int', (p + 1))
        e = jcast('int', Code04_Fruit1.head[u])
        while (e > 0):
            if (Code04_Fruit1.to[e] != fa):
                Code04_Fruit1.dfs1(Code04_Fruit1.to[e], u)
            e = jcast('int', Code04_Fruit1.next[e])
        Code04_Fruit1.rdfn[u] = jcast('int', Code04_Fruit1.cntd)

    # 不会改迭代版，去看讲解118，详解了从递归版改迭代版
    ufe = None
    stacksize = 0
    u = 0
    f = 0
    e = 0
    @staticmethod
    def push(u, f, e):
        u = jcast('int', u)
        f = jcast('int', f)
        e = jcast('int', e)
        jset(Code04_Fruit1.ufe[Code04_Fruit1.stacksize], 0, u)
        jset(Code04_Fruit1.ufe[Code04_Fruit1.stacksize], 1, f)
        jset(Code04_Fruit1.ufe[Code04_Fruit1.stacksize], 2, e)
        Code04_Fruit1.stacksize = jcast('int', (Code04_Fruit1.stacksize + 1))

    @staticmethod
    def pop():
        Code04_Fruit1.stacksize = jcast('int', (Code04_Fruit1.stacksize - 1))
        Code04_Fruit1.u = jcast('int', Code04_Fruit1.ufe[Code04_Fruit1.stacksize][0])
        Code04_Fruit1.f = jcast('int', Code04_Fruit1.ufe[Code04_Fruit1.stacksize][1])
        Code04_Fruit1.e = jcast('int', Code04_Fruit1.ufe[Code04_Fruit1.stacksize][2])

    # dfs1的迭代版
    @staticmethod
    def dfs2():
        Code04_Fruit1.stacksize = jcast('int', 0)
        Code04_Fruit1.push(1, 0, jcast('int', (-1)))
        while (Code04_Fruit1.stacksize > 0):
            Code04_Fruit1.pop()
            if (Code04_Fruit1.e == jcast('int', (-1))):
                Code04_Fruit1.dep[Code04_Fruit1.u] = jcast('int', jcast('int', jadd(Code04_Fruit1.dep[Code04_Fruit1.f], 1)))
                jset(Code04_Fruit1.ldfn, Code04_Fruit1.u, ((_java_obj_7 := Code04_Fruit1), (_java_key_8 := 'cntd'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3])
                jset(Code04_Fruit1.stjump[Code04_Fruit1.u], 0, Code04_Fruit1.f)
                p = jcast('int', 1)
                while (p < Code04_Fruit1.MAXP):
                    jset(Code04_Fruit1.stjump[Code04_Fruit1.u], p, Code04_Fruit1.stjump[Code04_Fruit1.stjump[Code04_Fruit1.u][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                    p = jcast('int', (p + 1))
                Code04_Fruit1.e = jcast('int', Code04_Fruit1.head[Code04_Fruit1.u])
            else:
                Code04_Fruit1.e = jcast('int', Code04_Fruit1.next[Code04_Fruit1.e])
            if (Code04_Fruit1.e != 0):
                Code04_Fruit1.push(Code04_Fruit1.u, Code04_Fruit1.f, Code04_Fruit1.e)
                if (Code04_Fruit1.to[Code04_Fruit1.e] != Code04_Fruit1.f):
                    Code04_Fruit1.push(Code04_Fruit1.to[Code04_Fruit1.e], Code04_Fruit1.u, jcast('int', (-1)))
            else:
                Code04_Fruit1.rdfn[Code04_Fruit1.u] = jcast('int', Code04_Fruit1.cntd)

    @staticmethod
    def lca(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_Fruit1.dep[a] < Code04_Fruit1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_Fruit1.MAXP - 1)))
        while (p >= 0):
            if (Code04_Fruit1.dep[Code04_Fruit1.stjump[a][p]] >= Code04_Fruit1.dep[b]):
                a = jcast('int', Code04_Fruit1.stjump[a][p])
            p = jcast('int', (p - 1))
        if (a == b):
            return jcast('int', a)
        p = jcast('int', jcast('int', (Code04_Fruit1.MAXP - 1)))
        while (p >= 0):
            if (Code04_Fruit1.stjump[a][p] != Code04_Fruit1.stjump[b][p]):
                a = jcast('int', Code04_Fruit1.stjump[a][p])
                b = jcast('int', Code04_Fruit1.stjump[b][p])
            p = jcast('int', (p - 1))
        return jcast('int', Code04_Fruit1.stjump[a][0])

    # 已知a和b的最低公共祖先一定是a或b
    # 假设祖先为x，后代为y，返回x的哪个儿子的子树里有y
    @staticmethod
    def lcaSon(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        if (Code04_Fruit1.dep[a] < Code04_Fruit1.dep[b]):
            tmp = jcast('int', a)
            a = jcast('int', b)
            b = jcast('int', tmp)
        p = jcast('int', jcast('int', (Code04_Fruit1.MAXP - 1)))
        while (p >= 0):
            if (Code04_Fruit1.dep[Code04_Fruit1.stjump[a][p]] > Code04_Fruit1.dep[b]):
                a = jcast('int', Code04_Fruit1.stjump[a][p])
            p = jcast('int', (p - 1))
        return jcast('int', a)

    @staticmethod
    def lowbit(i):
        i = jcast('int', i)
        return jcast('int', jcast('int', (i & jcast('int', (-i)))))

    @staticmethod
    def _java_add_0(i, v):
        i = jcast('int', i)
        v = jcast('int', v)
        while (i <= Code04_Fruit1.n):
            Code04_Fruit1.tree[i] = jcast('int', jcast('int', jadd(Code04_Fruit1.tree[i], v)))
            i = jcast('int', jcast('int', jadd(i, Code04_Fruit1.lowbit(i))))

    # 树状数组中[l..r]范围上的每个数增加v
    @staticmethod
    def _java_add_1(l, r, v):
        l = jcast('int', l)
        r = jcast('int', r)
        v = jcast('int', v)
        Code04_Fruit1._java_add_0(l, v)
        Code04_Fruit1._java_add_0(jcast('int', jadd(r, 1)), jcast('int', (-v)))

    # 树状数组中查询单点的值
    @staticmethod
    def query(i):
        i = jcast('int', i)
        ret = jcast('int', 0)
        while (i > 0):
            ret = jcast('int', jcast('int', jadd(ret, Code04_Fruit1.tree[i])))
            i = jcast('int', jcast('int', (i - Code04_Fruit1.lowbit(i))))
        return jcast('int', ret)

    @staticmethod
    def addPlate(x, yl, yr, v):
        x = jcast('int', x)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        v = jcast('int', v)
        jset(Code04_Fruit1.event[((_java_obj_10 := Code04_Fruit1), (_java_key_11 := 'cnte'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (1)))))[3]], 0, 1)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 1, x)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 2, yl)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 3, yr)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 4, v)

    @staticmethod
    def delPlate(x, yl, yr, v):
        x = jcast('int', x)
        yl = jcast('int', yl)
        yr = jcast('int', yr)
        v = jcast('int', v)
        jset(Code04_Fruit1.event[((_java_obj_13 := Code04_Fruit1), (_java_key_14 := 'cnte'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]], 0, 2)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 1, x)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 2, yl)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 3, yr)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 4, v)

    @staticmethod
    def addFruit(x, y, k, i):
        x = jcast('int', x)
        y = jcast('int', y)
        k = jcast('int', k)
        i = jcast('int', i)
        jset(Code04_Fruit1.event[((_java_obj_16 := Code04_Fruit1), (_java_key_17 := 'cnte'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3]], 0, 3)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 1, x)
        # 2、3、4位空缺
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 5, y)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 6, k)
        jset(Code04_Fruit1.event[Code04_Fruit1.cnte], 7, i)

    @staticmethod
    def compute(el, er, vl, vr):
        el = jcast('int', el)
        er = jcast('int', er)
        vl = jcast('int', vl)
        vr = jcast('int', vr)
        if (el > er):
            return
        if (vl == vr):
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code04_Fruit1.eid[i])
                if (Code04_Fruit1.event[id][0] == 3):
                    jset(Code04_Fruit1.ans, Code04_Fruit1.event[id][7], vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            lsiz = jcast('int', 0)
            rsiz = jcast('int', 0)
            i = jcast('int', el)
            while (i <= er):
                id = jcast('int', Code04_Fruit1.eid[i])
                if (Code04_Fruit1.event[id][0] == 1):
                    if (Code04_Fruit1.event[id][4] <= mid):
                        Code04_Fruit1._java_add_1(Code04_Fruit1.event[id][2], Code04_Fruit1.event[id][3], 1)
                        jset(Code04_Fruit1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                    else:
                        jset(Code04_Fruit1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                else:
                    if (Code04_Fruit1.event[id][0] == 2):
                        if (Code04_Fruit1.event[id][4] <= mid):
                            Code04_Fruit1._java_add_1(Code04_Fruit1.event[id][2], Code04_Fruit1.event[id][3], jcast('int', (-1)))
                            jset(Code04_Fruit1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                        else:
                            jset(Code04_Fruit1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                    else:
                        satisfy = jcast('int', Code04_Fruit1.query(Code04_Fruit1.event[id][5]))
                        if (satisfy >= Code04_Fruit1.event[id][6]):
                            jset(Code04_Fruit1.lset, (lsiz := jcast('int', (lsiz + (1)))), id)
                        else:
                            ((_java_obj_19 := Code04_Fruit1.event[id]), (_java_key_20 := 6), jset(_java_obj_19, _java_key_20, jcast('int', (jget(_java_obj_19, _java_key_20) - satisfy))))[2]
                            jset(Code04_Fruit1.rset, (rsiz := jcast('int', (rsiz + (1)))), id)
                i = jcast('int', (i + 1))
            # 这里为什么不用做撤销？
            # 因为任何一个盘子，一定有两条扫描线
            # 一条扫描线会增加yl..yr的计数
            # 一条扫描线会减少yl..yr的计数
            # 同一个盘子的两条扫描线，一定会在一起，是不可能分开的
            # 所以此时树状数组就是清空的，不需要再做撤销操作
            i = jcast('int', 1)
            while (i <= lsiz):
                Code04_Fruit1.eid[jcast('int', (jcast('int', jadd(el, i)) - 1))] = jcast('int', Code04_Fruit1.lset[i])
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= rsiz):
                Code04_Fruit1.eid[jcast('int', (jcast('int', jadd(jcast('int', jadd(el, lsiz)), i)) - 1))] = jcast('int', Code04_Fruit1.rset[i])
                i = jcast('int', (i + 1))
            Code04_Fruit1.compute(el, jcast('int', (jcast('int', jadd(el, lsiz)) - 1)), vl, mid)
            Code04_Fruit1.compute(jcast('int', jadd(el, lsiz)), er, jcast('int', jadd(mid, 1)), vr)

    @staticmethod
    def main(args):
        in_ = Code04_Fruit1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code04_Fruit1.n = jcast('int', jcall(in_, 'nextInt'))
        Code04_Fruit1.p = jcast('int', jcall(in_, 'nextInt'))
        Code04_Fruit1.q = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i < Code04_Fruit1.n):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            Code04_Fruit1.addEdge(u, v)
            Code04_Fruit1.addEdge(v, u)
            i = jcast('int', (i + 1))
        Code04_Fruit1.dfs2()
        i = jcast('int', 1)
        while (i <= Code04_Fruit1.p):
            a = jcast('int', jcall(in_, 'nextInt'))
            b = jcast('int', jcall(in_, 'nextInt'))
            c = jcast('int', jcall(in_, 'nextInt'))
            if (Code04_Fruit1.ldfn[a] > Code04_Fruit1.ldfn[b]):
                tmp = jcast('int', a)
                a = jcast('int', b)
                b = jcast('int', tmp)
            ablca = jcast('int', Code04_Fruit1.lca(a, b))
            # 类型1，a和b的lca是a或b，2个区域，4个事件产生
            # 类型2，a和b的lca不是a或b，1个区域，2个事件产生
            if ((ablca == a) or (ablca == b)):
                son = jcast('int', Code04_Fruit1.lcaSon(a, b))
                # (1 ~ dfn[son]-1) (b子树上的dfn范围)
                Code04_Fruit1.addPlate(1, Code04_Fruit1.ldfn[b], Code04_Fruit1.rdfn[b], c)
                Code04_Fruit1.delPlate(Code04_Fruit1.ldfn[son], Code04_Fruit1.ldfn[b], Code04_Fruit1.rdfn[b], c)
                # (b子树上的dfn范围) (son子树上最大的dfn序号+1 ~ n)
                Code04_Fruit1.addPlate(Code04_Fruit1.ldfn[b], jcast('int', jadd(Code04_Fruit1.rdfn[son], 1)), Code04_Fruit1.n, c)
                Code04_Fruit1.delPlate(jcast('int', jadd(Code04_Fruit1.rdfn[b], 1)), jcast('int', jadd(Code04_Fruit1.rdfn[son], 1)), Code04_Fruit1.n, c)
            else:
                # (a子树上的dfn范围) (b子树上的dfn范围)
                Code04_Fruit1.addPlate(Code04_Fruit1.ldfn[a], Code04_Fruit1.ldfn[b], Code04_Fruit1.rdfn[b], c)
                Code04_Fruit1.delPlate(jcast('int', jadd(Code04_Fruit1.rdfn[a], 1)), Code04_Fruit1.ldfn[b], Code04_Fruit1.rdfn[b], c)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code04_Fruit1.q):
            u = jcast('int', jcall(in_, 'nextInt'))
            v = jcast('int', jcall(in_, 'nextInt'))
            k = jcast('int', jcall(in_, 'nextInt'))
            Code04_Fruit1.addFruit(jstatic('Math', 'min', Code04_Fruit1.ldfn[u], Code04_Fruit1.ldfn[v]), jstatic('Math', 'max', Code04_Fruit1.ldfn[u], Code04_Fruit1.ldfn[v]), k, i)
            i = jcast('int', (i + 1))
        # 根据x排序，如果x一样，加盘子排最前、删盘子其次、水果最后
        jstatic('Arrays', 'sort', Code04_Fruit1.event, 1, jcast('int', jadd(Code04_Fruit1.cnte, 1)), (lambda a, b: ((a[1] - b[1]) if (a[1] != b[1]) else (a[0] - b[0]))))
        i = jcast('int', 1)
        while (i <= Code04_Fruit1.cnte):
            Code04_Fruit1.eid[i] = jcast('int', i)
            i = jcast('int', (i + 1))
        Code04_Fruit1.compute(1, Code04_Fruit1.cnte, 0, Code04_Fruit1.INF)
        i = jcast('int', 1)
        while (i <= Code04_Fruit1.q):
            jcall(out, 'println', Code04_Fruit1.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_21 := self), (_java_key_22 := 'ptr'), (_java_old_23 := jget(_java_obj_21, _java_key_22)), jset(_java_obj_21, _java_key_22, jcast('int', (_java_old_23 + (1)))), _java_old_23)[4]])

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
            raise TypeError("No matching overload for Code04_Fruit1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int'], ['int', 'int', 'int']], [False, False])
        if _java_choice == 0:
            return Code04_Fruit1._java_add_0(*args)
        if _java_choice == 1:
            return Code04_Fruit1._java_add_1(*args)
        raise TypeError("No matching overload for Code04_Fruit1.add")


Code04_Fruit1.MAXN = jcast('int', 40001)
Code04_Fruit1.MAXP = jcast('int', 16)
Code04_Fruit1.INF = jcast('int', 1000000001)
Code04_Fruit1.n = jcast('int', 0)
Code04_Fruit1.p = jcast('int', 0)
Code04_Fruit1.q = jcast('int', 0)
Code04_Fruit1.head = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.next = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (1 & 31)))])
Code04_Fruit1.to = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (1 & 31)))])
Code04_Fruit1.cntg = jcast('int', 0)
Code04_Fruit1.dep = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.ldfn = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.rdfn = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.stjump = jarray('int', [Code04_Fruit1.MAXN, Code04_Fruit1.MAXP])
Code04_Fruit1.cntd = jcast('int', 0)
Code04_Fruit1.tree = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.eid = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (3 & 31)))])
Code04_Fruit1.event = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (3 & 31))), 8])
Code04_Fruit1.cnte = jcast('int', 0)
Code04_Fruit1.lset = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (3 & 31)))])
Code04_Fruit1.rset = jarray('int', [jcast('int', (Code04_Fruit1.MAXN << (3 & 31)))])
Code04_Fruit1.ans = jarray('int', [Code04_Fruit1.MAXN])
Code04_Fruit1.ufe = jarray('int', [Code04_Fruit1.MAXN, 3])
Code04_Fruit1.stacksize = jcast('int', 0)
Code04_Fruit1.u = jcast('int', 0)
Code04_Fruit1.f = jcast('int', 0)
Code04_Fruit1.e = jcast('int', 0)

if __name__ == '__main__':
    Code04_Fruit1.main([])

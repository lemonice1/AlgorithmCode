# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 编码，Python版
# 一共有n个字符串，都由字符 '0'、'1'、'?' 组成
# 每个字符串最多含有一个'?'，如果不含有，说明该字符串已经确定了
# 如果字符串含有'?'，那么这个'?'必须变成'0'或'1'中的一个
# 请把所有字符串都确定下来，要求任意一个字符串不是其它字符串的前缀
# 存在方案打印"YES"，然后打印每个确定后的字符串，不存在方案打印"NO"
# 1 <= n、字符总数 <= 5 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P6965
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_BinaryCode2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'MAXE': 'MAXE', 'n': 'n', 'cntt': 'cntt', 'arr': 'arr', 'headg': 'headg', 'nextg': 'nextg', 'tog': 'tog', 'cntg': 'cntg', 'tree': 'tree', 'fa': 'fa', 'up': 'up', 'down': 'down', 'cntp': 'cntp', 'headx': 'headx', 'nextx': 'nextx', 'tox': 'tox', 'cntx': 'cntx', 'group': 'group', 'gsiz': 'gsiz', 'dfn': 'dfn', 'low': 'low', 'cntd': 'cntd', 'sta': 'sta', 'top': 'top', 'belong': 'belong', 'sccCnt': 'sccCnt', 'stau': 'stau', 'stas': 'stas', 'stae': 'stae', 'u': 'u', 'status': 'status', 'e': 'e', 'stacksize': 'stacksize'}
    MAXN = 0
    MAXP = 0
    MAXT = 0
    MAXE = 0
    n = 0
    cntt = 0
    # 每个字符串，有两个决定，所以得到两个决定串
    arr = None
    # 2-SAT建图
    headg = None
    nextg = None
    tog = None
    cntg = 0
    # 前缀树优化建图
    tree = None
    fa = None
    up = None
    down = None
    cntp = 0
    # 前缀树的节点x，拥有哪些决定串，用链式前向星实现
    headx = None
    nextx = None
    tox = None
    cntx = 0
    # 相同的决定串构成一组，进行前后缀优化建图
    group = None
    gsiz = 0
    dfn = None
    low = None
    cntd = 0
    sta = None
    top = 0
    belong = None
    sccCnt = 0
    # 迭代版需要的栈，讲解118讲了递归改迭代的技巧
    stau = None
    stas = None
    stae = None
    u = 0
    status = 0
    e = 0
    stacksize = 0
    @staticmethod
    def push(u, status, e):
        u = jcast('int', u)
        status = jcast('int', status)
        e = jcast('int', e)
        Code03_BinaryCode2.stau[Code03_BinaryCode2.stacksize] = jcast('int', u)
        Code03_BinaryCode2.stas[Code03_BinaryCode2.stacksize] = jcast('int', status)
        Code03_BinaryCode2.stae[Code03_BinaryCode2.stacksize] = jcast('int', e)
        Code03_BinaryCode2.stacksize = jcast('int', (Code03_BinaryCode2.stacksize + 1))

    @staticmethod
    def pop():
        Code03_BinaryCode2.stacksize = jcast('int', (Code03_BinaryCode2.stacksize - 1))
        Code03_BinaryCode2.u = jcast('int', Code03_BinaryCode2.stau[Code03_BinaryCode2.stacksize])
        Code03_BinaryCode2.status = jcast('int', Code03_BinaryCode2.stas[Code03_BinaryCode2.stacksize])
        Code03_BinaryCode2.e = jcast('int', Code03_BinaryCode2.stae[Code03_BinaryCode2.stacksize])

    @staticmethod
    def addEdge(u, v):
        u = jcast('int', u)
        v = jcast('int', v)
        jset(Code03_BinaryCode2.nextg, ((_java_obj_1 := Code03_BinaryCode2), (_java_key_2 := 'cntg'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code03_BinaryCode2.headg[u])
        Code03_BinaryCode2.tog[Code03_BinaryCode2.cntg] = jcast('int', v)
        Code03_BinaryCode2.headg[u] = jcast('int', Code03_BinaryCode2.cntg)

    # 递归版
    @staticmethod
    def tarjan1(u):
        u = jcast('int', u)
        jset(Code03_BinaryCode2.dfn, u, jset(Code03_BinaryCode2.low, u, ((_java_obj_4 := Code03_BinaryCode2), (_java_key_5 := 'cntd'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))))[3]))
        jset(Code03_BinaryCode2.sta, ((_java_obj_7 := Code03_BinaryCode2), (_java_key_8 := 'top'), (_java_old_9 := jget(_java_obj_7, _java_key_8)), jset(_java_obj_7, _java_key_8, jcast('int', (_java_old_9 + (1)))))[3], u)
        e = jcast('int', Code03_BinaryCode2.headg[u])
        while (e > 0):
            v = jcast('int', Code03_BinaryCode2.tog[e])
            if (Code03_BinaryCode2.dfn[v] == 0):
                Code03_BinaryCode2.tarjan1(v)
                jset(Code03_BinaryCode2.low, u, jstatic('Math', 'min', Code03_BinaryCode2.low[u], Code03_BinaryCode2.low[v]))
            else:
                if (Code03_BinaryCode2.belong[v] == 0):
                    jset(Code03_BinaryCode2.low, u, jstatic('Math', 'min', Code03_BinaryCode2.low[u], Code03_BinaryCode2.dfn[v]))
            e = jcast('int', Code03_BinaryCode2.nextg[e])
        if (Code03_BinaryCode2.dfn[u] == Code03_BinaryCode2.low[u]):
            Code03_BinaryCode2.sccCnt = jcast('int', (Code03_BinaryCode2.sccCnt + 1))
            pop = 0
            while True:
                pop = jcast('int', Code03_BinaryCode2.sta[((_java_obj_10 := Code03_BinaryCode2), (_java_key_11 := 'top'), (_java_old_12 := jget(_java_obj_10, _java_key_11)), jset(_java_obj_10, _java_key_11, jcast('int', (_java_old_12 + (-1)))), _java_old_12)[4]])
                Code03_BinaryCode2.belong[pop] = jcast('int', Code03_BinaryCode2.sccCnt)
                if not ((pop != u)):
                    break

    # 迭代版
    @staticmethod
    def tarjan2(node):
        node = jcast('int', node)
        Code03_BinaryCode2.stacksize = jcast('int', 0)
        Code03_BinaryCode2.push(node, jcast('int', (-1)), jcast('int', (-1)))
        v = 0
        while (Code03_BinaryCode2.stacksize > 0):
            Code03_BinaryCode2.pop()
            if (Code03_BinaryCode2.status == jcast('int', (-1))):
                jset(Code03_BinaryCode2.dfn, Code03_BinaryCode2.u, jset(Code03_BinaryCode2.low, Code03_BinaryCode2.u, ((_java_obj_13 := Code03_BinaryCode2), (_java_key_14 := 'cntd'), (_java_old_15 := jget(_java_obj_13, _java_key_14)), jset(_java_obj_13, _java_key_14, jcast('int', (_java_old_15 + (1)))))[3]))
                jset(Code03_BinaryCode2.sta, ((_java_obj_16 := Code03_BinaryCode2), (_java_key_17 := 'top'), (_java_old_18 := jget(_java_obj_16, _java_key_17)), jset(_java_obj_16, _java_key_17, jcast('int', (_java_old_18 + (1)))))[3], Code03_BinaryCode2.u)
                Code03_BinaryCode2.e = jcast('int', Code03_BinaryCode2.headg[Code03_BinaryCode2.u])
            else:
                v = jcast('int', Code03_BinaryCode2.tog[Code03_BinaryCode2.e])
                if (Code03_BinaryCode2.status == 0):
                    jset(Code03_BinaryCode2.low, Code03_BinaryCode2.u, jstatic('Math', 'min', Code03_BinaryCode2.low[Code03_BinaryCode2.u], Code03_BinaryCode2.low[v]))
                if ((Code03_BinaryCode2.status == 1) and (Code03_BinaryCode2.belong[v] == 0)):
                    jset(Code03_BinaryCode2.low, Code03_BinaryCode2.u, jstatic('Math', 'min', Code03_BinaryCode2.low[Code03_BinaryCode2.u], Code03_BinaryCode2.dfn[v]))
                Code03_BinaryCode2.e = jcast('int', Code03_BinaryCode2.nextg[Code03_BinaryCode2.e])
            if (Code03_BinaryCode2.e != 0):
                v = jcast('int', Code03_BinaryCode2.tog[Code03_BinaryCode2.e])
                if (Code03_BinaryCode2.dfn[v] == 0):
                    Code03_BinaryCode2.push(Code03_BinaryCode2.u, 0, Code03_BinaryCode2.e)
                    Code03_BinaryCode2.push(v, jcast('int', (-1)), jcast('int', (-1)))
                else:
                    Code03_BinaryCode2.push(Code03_BinaryCode2.u, 1, Code03_BinaryCode2.e)
            else:
                if (Code03_BinaryCode2.dfn[Code03_BinaryCode2.u] == Code03_BinaryCode2.low[Code03_BinaryCode2.u]):
                    Code03_BinaryCode2.sccCnt = jcast('int', (Code03_BinaryCode2.sccCnt + 1))
                    pop = 0
                    while True:
                        pop = jcast('int', Code03_BinaryCode2.sta[((_java_obj_19 := Code03_BinaryCode2), (_java_key_20 := 'top'), (_java_old_21 := jget(_java_obj_19, _java_key_20)), jset(_java_obj_19, _java_key_20, jcast('int', (_java_old_21 + (-1)))), _java_old_21)[4]])
                        Code03_BinaryCode2.belong[pop] = jcast('int', Code03_BinaryCode2.sccCnt)
                        if not ((pop != Code03_BinaryCode2.u)):
                            break

    @staticmethod
    def other(x):
        x = jcast('int', x)
        return jcast('int', (jcast('int', jadd(x, Code03_BinaryCode2.n)) if (x <= Code03_BinaryCode2.n) else jcast('int', (x - Code03_BinaryCode2.n))))

    @staticmethod
    def addGroup(u, x):
        u = jcast('int', u)
        x = jcast('int', x)
        jset(Code03_BinaryCode2.nextx, ((_java_obj_22 := Code03_BinaryCode2), (_java_key_23 := 'cntx'), (_java_old_24 := jget(_java_obj_22, _java_key_23)), jset(_java_obj_22, _java_key_23, jcast('int', (_java_old_24 + (1)))))[3], Code03_BinaryCode2.headx[u])
        Code03_BinaryCode2.tox[Code03_BinaryCode2.cntx] = jcast('int', x)
        Code03_BinaryCode2.headx[u] = jcast('int', Code03_BinaryCode2.cntx)

    @staticmethod
    def insert(x):
        x = jcast('int', x)
        str = Code03_BinaryCode2.arr[x]
        cur = jcast('int', 1)
        si = jcast('int', 0)
        while (si < jcall(str, 'length')):
            path = jcast('int', (0 if (jcall(str, 'charAt', si) == jchar('0')) else 1))
            if (Code03_BinaryCode2.tree[cur][path] == 0):
                jset(Code03_BinaryCode2.tree[cur], path, ((_java_obj_25 := Code03_BinaryCode2), (_java_key_26 := 'cntp'), (_java_old_27 := jget(_java_obj_25, _java_key_26)), jset(_java_obj_25, _java_key_26, jcast('int', (_java_old_27 + (1)))))[3])
                Code03_BinaryCode2.fa[Code03_BinaryCode2.cntp] = jcast('int', cur)
                jset(Code03_BinaryCode2.up, Code03_BinaryCode2.cntp, ((_java_obj_28 := Code03_BinaryCode2), (_java_key_29 := 'cntt'), (_java_old_30 := jget(_java_obj_28, _java_key_29)), jset(_java_obj_28, _java_key_29, jcast('int', (_java_old_30 + (1)))))[3])
                jset(Code03_BinaryCode2.down, Code03_BinaryCode2.cntp, ((_java_obj_31 := Code03_BinaryCode2), (_java_key_32 := 'cntt'), (_java_old_33 := jget(_java_obj_31, _java_key_32)), jset(_java_obj_31, _java_key_32, jcast('int', (_java_old_33 + (1)))))[3])
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.up[Code03_BinaryCode2.cntp], Code03_BinaryCode2.up[cur])
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.down[cur], Code03_BinaryCode2.down[Code03_BinaryCode2.cntp])
            cur = jcast('int', Code03_BinaryCode2.tree[cur][path])
            si = jcast('int', (si + 1))
        Code03_BinaryCode2.addEdge(x, Code03_BinaryCode2.up[Code03_BinaryCode2.fa[cur]])
        Code03_BinaryCode2.addEdge(Code03_BinaryCode2.up[cur], Code03_BinaryCode2.other(x))
        Code03_BinaryCode2.addEdge(x, Code03_BinaryCode2.down[cur])
        Code03_BinaryCode2.addEdge(Code03_BinaryCode2.down[Code03_BinaryCode2.fa[cur]], Code03_BinaryCode2.other(x))
        Code03_BinaryCode2.addGroup(cur, x)

    @staticmethod
    def groupLink():
        if (Code03_BinaryCode2.gsiz > 1):
            Code03_BinaryCode2.cntt = jcast('int', (Code03_BinaryCode2.cntt + 1))
            Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, Code03_BinaryCode2.other(Code03_BinaryCode2.group[1]))
            i = jcast('int', 2)
            while (i <= Code03_BinaryCode2.gsiz):
                Code03_BinaryCode2.cntt = jcast('int', (Code03_BinaryCode2.cntt + 1))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, Code03_BinaryCode2.other(Code03_BinaryCode2.group[i]))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.group[i], jcast('int', (Code03_BinaryCode2.cntt - 1)))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, jcast('int', (Code03_BinaryCode2.cntt - 1)))
                i = jcast('int', (i + 1))
            Code03_BinaryCode2.cntt = jcast('int', (Code03_BinaryCode2.cntt + 1))
            Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, Code03_BinaryCode2.other(Code03_BinaryCode2.group[Code03_BinaryCode2.gsiz]))
            i = jcast('int', jcast('int', (Code03_BinaryCode2.gsiz - 1)))
            while (i >= 1):
                Code03_BinaryCode2.cntt = jcast('int', (Code03_BinaryCode2.cntt + 1))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, Code03_BinaryCode2.other(Code03_BinaryCode2.group[i]))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.group[i], jcast('int', (Code03_BinaryCode2.cntt - 1)))
                Code03_BinaryCode2.addEdge(Code03_BinaryCode2.cntt, jcast('int', (Code03_BinaryCode2.cntt - 1)))
                i = jcast('int', (i - 1))

    @staticmethod
    def buildGraph():
        Code03_BinaryCode2.cntt = jcast('int', jcast('int', (Code03_BinaryCode2.n << (1 & 31))))
        Code03_BinaryCode2.cntp = jcast('int', 1)
        jset(Code03_BinaryCode2.up, 1, ((_java_obj_34 := Code03_BinaryCode2), (_java_key_35 := 'cntt'), (_java_old_36 := jget(_java_obj_34, _java_key_35)), jset(_java_obj_34, _java_key_35, jcast('int', (_java_old_36 + (1)))))[3])
        jset(Code03_BinaryCode2.down, 1, ((_java_obj_37 := Code03_BinaryCode2), (_java_key_38 := 'cntt'), (_java_old_39 := jget(_java_obj_37, _java_key_38)), jset(_java_obj_37, _java_key_38, jcast('int', (_java_old_39 + (1)))))[3])
        x = jcast('int', 1)
        while (x <= jcast('int', (Code03_BinaryCode2.n << (1 & 31)))):
            Code03_BinaryCode2.insert(x)
            x = jcast('int', (x + 1))
        u = jcast('int', 1)
        while (u <= Code03_BinaryCode2.cntp):
            Code03_BinaryCode2.gsiz = jcast('int', 0)
            e = jcast('int', Code03_BinaryCode2.headx[u])
            while (e > 0):
                jset(Code03_BinaryCode2.group, ((_java_obj_40 := Code03_BinaryCode2), (_java_key_41 := 'gsiz'), (_java_old_42 := jget(_java_obj_40, _java_key_41)), jset(_java_obj_40, _java_key_41, jcast('int', (_java_old_42 + (1)))))[3], Code03_BinaryCode2.tox[e])
                e = jcast('int', Code03_BinaryCode2.nextx[e])
            Code03_BinaryCode2.groupLink()
            u = jcast('int', (u + 1))

    @staticmethod
    def addString(i, s):
        i = jcast('int', i)
        mark = jcast('int', jcast('int', (-1)))
        str = jcall(s, 'toCharArray')
        si = jcast('int', 0)
        while (si < jget(str, 'length')):
            try:
                if (str[si] == jchar('?')):
                    mark = jcast('int', si)
                    raise JBreak(None)
            except JContinue as _java_control_43:
                if _java_control_43.label not in (None,):
                    raise
            except JBreak as _java_control_43:
                if _java_control_43.label not in (None,):
                    raise
                break
            si = jcast('int', (si + 1))
        if (mark == jcast('int', (-1))):
            if (str[0] == jchar('0')):
                Code03_BinaryCode2.addEdge(jcast('int', jadd(i, Code03_BinaryCode2.n)), i)
            else:
                Code03_BinaryCode2.addEdge(i, jcast('int', jadd(i, Code03_BinaryCode2.n)))
            mark = jcast('int', 0)
        str[mark] = jcast('char', jchar('0'))
        jset(Code03_BinaryCode2.arr, i, jstatic('String', 'valueOf', str))
        str[mark] = jcast('char', jchar('1'))
        jset(Code03_BinaryCode2.arr, jcast('int', jadd(i, Code03_BinaryCode2.n)), jstatic('String', 'valueOf', str))

    @staticmethod
    def main(args):
        in_ = Code03_BinaryCode2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code03_BinaryCode2.n = jcast('int', jcall(in_, 'nextInt'))
        s = None
        i = jcast('int', 1)
        while (i <= Code03_BinaryCode2.n):
            s = jcall(in_, 'nextString')
            Code03_BinaryCode2.addString(i, s)
            i = jcast('int', (i + 1))
        Code03_BinaryCode2.buildGraph()
        i = jcast('int', 1)
        while (i <= jcast('int', (Code03_BinaryCode2.n << (1 & 31)))):
            if (Code03_BinaryCode2.dfn[i] == 0):
                # tarjan1(i);
                Code03_BinaryCode2.tarjan2(i)
            i = jcast('int', (i + 1))
        check = jcast('boolean', True)
        i = jcast('int', 1)
        while (i <= Code03_BinaryCode2.n):
            try:
                if (Code03_BinaryCode2.belong[i] == Code03_BinaryCode2.belong[jcast('int', jadd(i, Code03_BinaryCode2.n))]):
                    check = jcast('boolean', False)
                    raise JBreak(None)
            except JContinue as _java_control_44:
                if _java_control_44.label not in (None,):
                    raise
            except JBreak as _java_control_44:
                if _java_control_44.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if check:
            jcall(out, 'println', 'YES')
            i = jcast('int', 1)
            while (i <= Code03_BinaryCode2.n):
                if (Code03_BinaryCode2.belong[i] < Code03_BinaryCode2.belong[jcast('int', jadd(i, Code03_BinaryCode2.n))]):
                    jcall(out, 'println', Code03_BinaryCode2.arr[i])
                else:
                    jcall(out, 'println', Code03_BinaryCode2.arr[jcast('int', jadd(i, Code03_BinaryCode2.n))])
                i = jcast('int', (i + 1))
        else:
            jcall(out, 'println', 'NO')
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
            return jcast('int', self.buffer[((_java_obj_45 := self), (_java_key_46 := 'ptr'), (_java_old_47 := jget(_java_obj_45, _java_key_46)), jset(_java_obj_45, _java_key_46, jcast('int', (_java_old_47 + (1)))), _java_old_47)[4]])

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

        def nextString(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            if (c == jcast('int', (-1))):
                return None
            sb = jnew('StringBuilder')
            while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', c))
                c = jcast('int', self.readByte())
            return jcall(sb, 'toString')

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code03_BinaryCode2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_BinaryCode2.MAXN = jcast('int', 500001)
Code03_BinaryCode2.MAXP = jcast('int', 1000002)
Code03_BinaryCode2.MAXT = jcast('int', 5000001)
Code03_BinaryCode2.MAXE = jcast('int', 10000001)
Code03_BinaryCode2.n = jcast('int', 0)
Code03_BinaryCode2.cntt = jcast('int', 0)
Code03_BinaryCode2.arr = jarray('String', [jcast('int', (Code03_BinaryCode2.MAXN << (1 & 31)))])
Code03_BinaryCode2.headg = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.nextg = jarray('int', [Code03_BinaryCode2.MAXE])
Code03_BinaryCode2.tog = jarray('int', [Code03_BinaryCode2.MAXE])
Code03_BinaryCode2.cntg = jcast('int', 0)
Code03_BinaryCode2.tree = jarray('int', [Code03_BinaryCode2.MAXP, 2])
Code03_BinaryCode2.fa = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.up = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.down = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.cntp = jcast('int', 0)
Code03_BinaryCode2.headx = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.nextx = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.tox = jarray('int', [Code03_BinaryCode2.MAXP])
Code03_BinaryCode2.cntx = jcast('int', 0)
Code03_BinaryCode2.group = jarray('int', [Code03_BinaryCode2.MAXN])
Code03_BinaryCode2.gsiz = jcast('int', 0)
Code03_BinaryCode2.dfn = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.low = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.cntd = jcast('int', 0)
Code03_BinaryCode2.sta = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.top = jcast('int', 0)
Code03_BinaryCode2.belong = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.sccCnt = jcast('int', 0)
Code03_BinaryCode2.stau = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.stas = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.stae = jarray('int', [Code03_BinaryCode2.MAXT])
Code03_BinaryCode2.u = jcast('int', 0)
Code03_BinaryCode2.status = jcast('int', 0)
Code03_BinaryCode2.e = jcast('int', 0)
Code03_BinaryCode2.stacksize = jcast('int', 0)

if __name__ == '__main__':
    Code03_BinaryCode2.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 贪玩蓝月，Python版
# 每件装备都有特征值w和战斗力v，放装备的背包是一个双端队列，只有背包中的装备是可选的
# 给定数值p，接下来有m条操作，每种操作是如下五种类型中的一种
# 操作 IF x y : 背包前端加入一件特征值x、战斗力y的装备
# 操作 IG x y : 背包后端加入一件特征值x、战斗力y的装备
# 操作 DF     : 删除背包前端的装备
# 操作 DG     : 删除背包后端的装备
# 操作 QU x y : 选择装备的特征值累加和 % p，必须在[x, y]范围，打印最大战斗力，无方案打印-1
# 1 <= m <= 5 * 10^4    1 <= p <= 500
# 0 <= 每件装备特征值、每件装备战斗力 <= 10^9
# 测试链接 : https://loj.ac/p/6515
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_BlueMoon1:
    __java_fields__ = {'MAXM': 'MAXM', 'MAXP': 'MAXP', 'MAXT': 'MAXT', 'DEEP': 'DEEP', 'm': 'm', 'p': 'p', 'op': 'op', 'x': 'x', 'y': 'y', 'knapsack': 'knapsack', 'head': 'head', 'next': 'next', 'tow': 'tow', 'tov': 'tov', 'cnt': 'cnt', 'pre': 'pre', 'dp': 'dp', 'backup': 'backup', 'ans': 'ans'}
    MAXM = 0
    MAXP = 0
    MAXT = 0
    DEEP = 0
    m = 0
    p = 0
    op = None
    x = None
    y = None
    # 背包<装备特征值%p、装备战斗力、装备出现时间点>
    knapsack = None
    # 时间轴线段树的区间上挂上生效的装备，(特征值 % p)记为w，战斗力记为v
    head = None
    next = None
    tow = None
    tov = None
    cnt = 0
    # 动态规划表不考虑当前装备的状态，上一行的状态
    pre = None
    # 动态规划表考虑当前装备的状态，本行的状态，需要更新
    dp = None
    # 动态规划表的备份
    backup = None
    # 答案
    ans = None
    @staticmethod
    def clone(a, b):
        i = jcast('int', 0)
        while (i < Code02_BlueMoon1.p):
            a[i] = jcast('long', b[i])
            i = jcast('int', (i + 1))

    @staticmethod
    def addEdge(i, w, v):
        i = jcast('int', i)
        w = jcast('int', w)
        v = jcast('int', v)
        jset(Code02_BlueMoon1.next, ((_java_obj_1 := Code02_BlueMoon1), (_java_key_2 := 'cnt'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3], Code02_BlueMoon1.head[i])
        Code02_BlueMoon1.tow[Code02_BlueMoon1.cnt] = jcast('int', w)
        Code02_BlueMoon1.tov[Code02_BlueMoon1.cnt] = jcast('int', v)
        Code02_BlueMoon1.head[i] = jcast('int', Code02_BlueMoon1.cnt)

    @staticmethod
    def add(jobl, jobr, jobw, jobv, l, r, i):
        jobl = jcast('int', jobl)
        jobr = jcast('int', jobr)
        jobw = jcast('int', jobw)
        jobv = jcast('int', jobv)
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        if ((jobl <= l) and (r <= jobr)):
            Code02_BlueMoon1.addEdge(i, jobw, jobv)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            if (jobl <= mid):
                Code02_BlueMoon1.add(jobl, jobr, jobw, jobv, l, mid, jcast('int', (i << (1 & 31))))
            if (jobr > mid):
                Code02_BlueMoon1.add(jobl, jobr, jobw, jobv, jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)))

    @staticmethod
    def dfs(l, r, i, dep):
        l = jcast('int', l)
        r = jcast('int', r)
        i = jcast('int', i)
        dep = jcast('int', dep)
        Code02_BlueMoon1.clone(Code02_BlueMoon1.backup[dep], Code02_BlueMoon1.dp)
        e = jcast('int', Code02_BlueMoon1.head[i])
        w = 0
        v = 0
        while (e > 0):
            w = jcast('int', Code02_BlueMoon1.tow[e])
            v = jcast('int', Code02_BlueMoon1.tov[e])
            Code02_BlueMoon1.clone(Code02_BlueMoon1.pre, Code02_BlueMoon1.dp)
            j = jcast('int', 0)
            while (j < Code02_BlueMoon1.p):
                if (Code02_BlueMoon1.pre[j] != jcast('int', (-1))):
                    jset(Code02_BlueMoon1.dp, jcast('int', jmod(jcast('int', jadd(j, w)), Code02_BlueMoon1.p)), jstatic('Math', 'max', Code02_BlueMoon1.dp[jcast('int', jmod(jcast('int', jadd(j, w)), Code02_BlueMoon1.p))], jcast('long', jadd(Code02_BlueMoon1.pre[j], v))))
                j = jcast('int', (j + 1))
            e = jcast('int', Code02_BlueMoon1.next[e])
        if (l == r):
            if (Code02_BlueMoon1.op[l] == 5):
                ret = jcast('long', jcast('int', (-1)))
                j = jcast('int', Code02_BlueMoon1.x[l])
                while (j <= Code02_BlueMoon1.y[l]):
                    ret = jcast('long', jstatic('Math', 'max', ret, Code02_BlueMoon1.dp[j]))
                    j = jcast('int', (j + 1))
                Code02_BlueMoon1.ans[l] = jcast('long', ret)
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
            Code02_BlueMoon1.dfs(l, mid, jcast('int', (i << (1 & 31))), jcast('int', jadd(dep, 1)))
            Code02_BlueMoon1.dfs(jcast('int', jadd(mid, 1)), r, jcast('int', (jcast('int', (i << (1 & 31))) | 1)), jcast('int', jadd(dep, 1)))
        Code02_BlueMoon1.clone(Code02_BlueMoon1.dp, Code02_BlueMoon1.backup[dep])

    @staticmethod
    def prepare():
        equip = None
        i = jcast('int', 1)
        while (i <= Code02_BlueMoon1.m):
            if (Code02_BlueMoon1.op[i] == 1):
                jcall(Code02_BlueMoon1.knapsack, 'addFirst', jarray('int', [None], [jcast('int', jmod(Code02_BlueMoon1.x[i], Code02_BlueMoon1.p)), Code02_BlueMoon1.y[i], i]))
            else:
                if (Code02_BlueMoon1.op[i] == 2):
                    jcall(Code02_BlueMoon1.knapsack, 'addLast', jarray('int', [None], [jcast('int', jmod(Code02_BlueMoon1.x[i], Code02_BlueMoon1.p)), Code02_BlueMoon1.y[i], i]))
                else:
                    if (Code02_BlueMoon1.op[i] == 3):
                        equip = jcall(Code02_BlueMoon1.knapsack, 'pollFirst')
                        Code02_BlueMoon1.add(equip[2], jcast('int', (i - 1)), equip[0], equip[1], 1, Code02_BlueMoon1.m, 1)
                    else:
                        if (Code02_BlueMoon1.op[i] == 4):
                            equip = jcall(Code02_BlueMoon1.knapsack, 'pollLast')
                            Code02_BlueMoon1.add(equip[2], jcast('int', (i - 1)), equip[0], equip[1], 1, Code02_BlueMoon1.m, 1)
            i = jcast('int', (i + 1))
        while (not jcall(Code02_BlueMoon1.knapsack, 'isEmpty')):
            equip = jcall(Code02_BlueMoon1.knapsack, 'pollFirst')
            Code02_BlueMoon1.add(equip[2], Code02_BlueMoon1.m, equip[0], equip[1], 1, Code02_BlueMoon1.m, 1)
        i = jcast('int', 0)
        while (i < Code02_BlueMoon1.p):
            Code02_BlueMoon1.dp[i] = jcast('long', jcast('int', (-1)))
            i = jcast('int', (i + 1))
        Code02_BlueMoon1.dp[0] = jcast('long', 0)

    @staticmethod
    def main(args):
        in_ = Code02_BlueMoon1.FastReader(_java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextInt')
        Code02_BlueMoon1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_BlueMoon1.p = jcast('int', jcall(in_, 'nextInt'))
        t = None
        i = jcast('int', 1)
        while (i <= Code02_BlueMoon1.m):
            t = jcall(in_, 'nextString')
            if jcall(t, 'equals', 'IF'):
                Code02_BlueMoon1.op[i] = jcast('int', 1)
                jset(Code02_BlueMoon1.x, i, jcall(in_, 'nextInt'))
                jset(Code02_BlueMoon1.y, i, jcall(in_, 'nextInt'))
            else:
                if jcall(t, 'equals', 'IG'):
                    Code02_BlueMoon1.op[i] = jcast('int', 2)
                    jset(Code02_BlueMoon1.x, i, jcall(in_, 'nextInt'))
                    jset(Code02_BlueMoon1.y, i, jcall(in_, 'nextInt'))
                else:
                    if jcall(t, 'equals', 'DF'):
                        Code02_BlueMoon1.op[i] = jcast('int', 3)
                    else:
                        if jcall(t, 'equals', 'DG'):
                            Code02_BlueMoon1.op[i] = jcast('int', 4)
                        else:
                            Code02_BlueMoon1.op[i] = jcast('int', 5)
                            jset(Code02_BlueMoon1.x, i, jcall(in_, 'nextInt'))
                            jset(Code02_BlueMoon1.y, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        Code02_BlueMoon1.prepare()
        Code02_BlueMoon1.dfs(1, Code02_BlueMoon1.m, 1, 1)
        i = jcast('int', 1)
        while (i <= Code02_BlueMoon1.m):
            if (Code02_BlueMoon1.op[i] == 5):
                jcall(out, 'println', Code02_BlueMoon1.ans[i])
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')

    # 读写工具类
    class FastReader:
        __java_fields__ = {'BUFFER_SIZE': 'BUFFER_SIZE', 'in': 'in_', 'buffer': 'buffer', 'ptr': 'ptr', 'len': 'len'}
        BUFFER_SIZE = 0
        # in_：实例字段，在构造函数中初始化。
        # buffer：实例字段，在构造函数中初始化。
        # ptr：实例字段，在构造函数中初始化。
        # len：实例字段，在构造函数中初始化。
        def _java_init_0(self):
            self.in_ = jget(System, 'in')
            self.buffer = jarray('byte', [Code02_BlueMoon1.FastReader.BUFFER_SIZE])
            self.ptr = jcast('int', jset(self, 'len', 0))

        def hasNextByte(self):
            if (self.ptr < self.len):
                return jcast('boolean', True)
            self.ptr = jcast('int', 0)
            self.len = jcast('int', jcall(self.in_, 'read', self.buffer))
            return jcast('boolean', (self.len > 0))

        def readByte(self):
            if (not self.hasNextByte()):
                return jcast('byte', jcast('int', (-1)))
            return jcast('byte', self.buffer[((_java_obj_4 := self), (_java_key_5 := 'ptr'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (1)))), _java_old_6)[4]])

        def nextInt(self):
            num = jcast('int', 0)
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            minus = jcast('boolean', False)
            if (b == jchar('-')):
                minus = jcast('boolean', True)
                b = jcast('byte', self.readByte())
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                num = jcast('int', jcast('int', jadd(jcast('int', (num * 10)), jcast('int', (b - jchar('0'))))))
                b = jcast('byte', self.readByte())
            return jcast('int', (jcast('int', (-num)) if minus else num))

        def nextString(self):
            b = jcast('byte', self.readByte())
            while self.isWhitespace(b):
                b = jcast('byte', self.readByte())
            sb = jnew('StringBuilder', 1000)
            while ((not self.isWhitespace(b)) and (b != jcast('int', (-1)))):
                jcall(sb, 'append', jcast('char', b))
                b = jcast('byte', self.readByte())
            return jcall(sb, 'toString')

        def isWhitespace(self, b):
            b = jcast('byte', b)
            return jcast('boolean', ((((b == jchar(' ')) or (b == jchar('\n'))) or (b == jchar('\r'))) or (b == jchar('\t'))))

        def __init__(self, *args, _java_ctor=None):
            self.in_ = None
            self.buffer = None
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [[]], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_BlueMoon1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_BlueMoon1.MAXM = jcast('int', 50001)
Code02_BlueMoon1.MAXP = jcast('int', 501)
Code02_BlueMoon1.MAXT = jcast('int', 1000001)
Code02_BlueMoon1.DEEP = jcast('int', 20)
Code02_BlueMoon1.m = jcast('int', 0)
Code02_BlueMoon1.p = jcast('int', 0)
Code02_BlueMoon1.op = jarray('int', [Code02_BlueMoon1.MAXM])
Code02_BlueMoon1.x = jarray('int', [Code02_BlueMoon1.MAXM])
Code02_BlueMoon1.y = jarray('int', [Code02_BlueMoon1.MAXM])
Code02_BlueMoon1.knapsack = jnew('ArrayDeque')
Code02_BlueMoon1.head = jarray('int', [jcast('int', (Code02_BlueMoon1.MAXM << (2 & 31)))])
Code02_BlueMoon1.next = jarray('int', [Code02_BlueMoon1.MAXT])
Code02_BlueMoon1.tow = jarray('int', [Code02_BlueMoon1.MAXT])
Code02_BlueMoon1.tov = jarray('int', [Code02_BlueMoon1.MAXT])
Code02_BlueMoon1.cnt = jcast('int', 0)
Code02_BlueMoon1.pre = jarray('long', [Code02_BlueMoon1.MAXP])
Code02_BlueMoon1.dp = jarray('long', [Code02_BlueMoon1.MAXP])
Code02_BlueMoon1.backup = jarray('long', [Code02_BlueMoon1.DEEP, Code02_BlueMoon1.MAXP])
Code02_BlueMoon1.ans = jarray('long', [Code02_BlueMoon1.MAXM])
Code02_BlueMoon1.FastReader.BUFFER_SIZE = jcast('int', jcast('int', (1 << (16 & 31))))

if __name__ == '__main__':
    Code02_BlueMoon1.main([])

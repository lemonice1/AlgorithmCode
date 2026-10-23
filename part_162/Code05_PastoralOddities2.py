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

# 点的度都是奇数的最小瓶颈，Python版
# 一共有n个点，初始没有边，依次加入m条无向边，每条边有边权
# 每次加入后，询问是否存在一个边集，满足每个点连接的边的数量都是奇数
# 如果存在，希望边集的最大边权，尽可能小，如果不存在打印-1
# 2 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 1 <= 边权 <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/CF603E
# 测试链接 : https://codeforces.com/problemset/problem/603/E
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_PastoralOddities2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'n': 'n', 'm': 'm', 'edge': 'edge', 'wsort': 'wsort', 'oddnum': 'oddnum', 'father': 'father', 'siz': 'siz', 'rollback': 'rollback', 'opsize': 'opsize', 'ans': 'ans'}
    MAXN = 0
    MAXM = 0
    n = 0
    m = 0
    # edge代表所有边依次出现
    # wsort代表所有边按边权排序
    # 每条边有：端点x、端点y、边权w、时序tim、边权排名rak
    edge = None
    wsort = None
    # 可撤销并查集 + 节点数为奇数的连通区数量为oddnum
    oddnum = 0
    father = None
    siz = None
    rollback = None
    opsize = 0
    ans = None
    @staticmethod
    def find(i):
        i = jcast('int', i)
        while (i != Code05_PastoralOddities2.father[i]):
            i = jcast('int', Code05_PastoralOddities2.father[i])
        return jcast('int', i)

    @staticmethod
    def union(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code05_PastoralOddities2.find(x))
        fy = jcast('int', Code05_PastoralOddities2.find(y))
        if (fx == fy):
            return jcast('boolean', False)
        if ((jcast('int', (Code05_PastoralOddities2.siz[fx] & 1)) == 1) and (jcast('int', (Code05_PastoralOddities2.siz[fy] & 1)) == 1)):
            Code05_PastoralOddities2.oddnum = jcast('int', jcast('int', (Code05_PastoralOddities2.oddnum - 2)))
        if (Code05_PastoralOddities2.siz[fx] < Code05_PastoralOddities2.siz[fy]):
            tmp = jcast('int', fx)
            fx = jcast('int', fy)
            fy = jcast('int', tmp)
        Code05_PastoralOddities2.father[fy] = jcast('int', fx)
        Code05_PastoralOddities2.siz[fx] = jcast('int', jcast('int', jadd(Code05_PastoralOddities2.siz[fx], Code05_PastoralOddities2.siz[fy])))
        jset(Code05_PastoralOddities2.rollback[((_java_obj_1 := Code05_PastoralOddities2), (_java_key_2 := 'opsize'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))))[3]], 0, fx)
        jset(Code05_PastoralOddities2.rollback[Code05_PastoralOddities2.opsize], 1, fy)
        return jcast('boolean', True)

    @staticmethod
    def undo():
        fx = jcast('int', Code05_PastoralOddities2.rollback[Code05_PastoralOddities2.opsize][0])
        fy = jcast('int', Code05_PastoralOddities2.rollback[((_java_obj_4 := Code05_PastoralOddities2), (_java_key_5 := 'opsize'), (_java_old_6 := jget(_java_obj_4, _java_key_5)), jset(_java_obj_4, _java_key_5, jcast('int', (_java_old_6 + (-1)))), _java_old_6)[4]][1])
        Code05_PastoralOddities2.father[fy] = jcast('int', fy)
        Code05_PastoralOddities2.siz[fx] = jcast('int', jcast('int', (Code05_PastoralOddities2.siz[fx] - Code05_PastoralOddities2.siz[fy])))
        if ((jcast('int', (Code05_PastoralOddities2.siz[fx] & 1)) == 1) and (jcast('int', (Code05_PastoralOddities2.siz[fy] & 1)) == 1)):
            Code05_PastoralOddities2.oddnum = jcast('int', jcast('int', jadd(Code05_PastoralOddities2.oddnum, 2)))

    # 依次出现的边在edge里，当前来到[el..er]范围
    # 权值排序后的边在wsort里，答案范围[vl..vr]，同时也是排名范围
    # 调用递归的前提 : el之前，边权排名<vl的边，已经加到图里了
    # 利用整体二分得到所有边的答案
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
                Code05_PastoralOddities2.ans[i] = jcast('int', vl)
                i = jcast('int', (i + 1))
        else:
            mid = jcast('int', jcast('int', (jcast('int', jadd(vl, vr)) >> (1 & 31))))
            # 1) el之前，边权排名在[vl..mid]之间的边，加到图里，通过遍历wsort[vl..mid]来加速
            unionCnt1 = jcast('int', 0)
            i = jcast('int', vl)
            while (i <= mid):
                if (Code05_PastoralOddities2.wsort[i][3] < el):
                    if Code05_PastoralOddities2.union(Code05_PastoralOddities2.wsort[i][0], Code05_PastoralOddities2.wsort[i][1]):
                        unionCnt1 = jcast('int', (unionCnt1 + 1))
                i = jcast('int', (i + 1))
            # 2) 从el开始遍历，边权排名<=mid的边，加到图里，找到第一个达标的边split
            unionCnt2 = jcast('int', 0)
            split = jcast('int', jcast('int', jadd(er, 1)))
            i = jcast('int', el)
            while (i <= er):
                try:
                    if (Code05_PastoralOddities2.edge[i][4] <= mid):
                        if Code05_PastoralOddities2.union(Code05_PastoralOddities2.edge[i][0], Code05_PastoralOddities2.edge[i][1]):
                            unionCnt2 = jcast('int', (unionCnt2 + 1))
                    if (Code05_PastoralOddities2.oddnum == 0):
                        split = jcast('int', i)
                        raise JBreak(None)
                except JContinue as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                except JBreak as _java_control_7:
                    if _java_control_7.label not in (None,):
                        raise
                    break
                i = jcast('int', (i + 1))
            # 3) 撤销2)的效果，el之前，边权排名<=mid的边，都在图中
            i = jcast('int', 1)
            while (i <= unionCnt2):
                Code05_PastoralOddities2.undo()
                i = jcast('int', (i + 1))
            # 4) 执行 compute(el, split - 1, mid + 1, vr)，此时满足子递归的前提
            Code05_PastoralOddities2.compute(el, jcast('int', (split - 1)), jcast('int', jadd(mid, 1)), vr)
            # 5) 撤销1)的效果，此时只剩下前提了，el之前，边权排名<vl的边，都在图中
            i = jcast('int', 1)
            while (i <= unionCnt1):
                Code05_PastoralOddities2.undo()
                i = jcast('int', (i + 1))
            # 6) 从el开始到split之前，边权排名<vl的边，加到图里
            unionCnt3 = jcast('int', 0)
            i = jcast('int', el)
            while (i <= jcast('int', (split - 1))):
                if (Code05_PastoralOddities2.edge[i][4] < vl):
                    if Code05_PastoralOddities2.union(Code05_PastoralOddities2.edge[i][0], Code05_PastoralOddities2.edge[i][1]):
                        unionCnt3 = jcast('int', (unionCnt3 + 1))
                i = jcast('int', (i + 1))
            # 7) 执行 compute(split, er, vl, mid)，此时满足子递归的前提
            Code05_PastoralOddities2.compute(split, er, vl, mid)
            # 8) 撤销6)的效果，回到了前提
            i = jcast('int', 1)
            while (i <= unionCnt3):
                Code05_PastoralOddities2.undo()
                i = jcast('int', (i + 1))

    @staticmethod
    def prepare():
        Code05_PastoralOddities2.oddnum = jcast('int', Code05_PastoralOddities2.n)
        i = jcast('int', 1)
        while (i <= Code05_PastoralOddities2.n):
            Code05_PastoralOddities2.father[i] = jcast('int', i)
            Code05_PastoralOddities2.siz[i] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_PastoralOddities2.m):
            jset(Code05_PastoralOddities2.wsort[i], 0, Code05_PastoralOddities2.edge[i][0])
            jset(Code05_PastoralOddities2.wsort[i], 1, Code05_PastoralOddities2.edge[i][1])
            jset(Code05_PastoralOddities2.wsort[i], 2, Code05_PastoralOddities2.edge[i][2])
            jset(Code05_PastoralOddities2.wsort[i], 3, Code05_PastoralOddities2.edge[i][3])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_PastoralOddities2.wsort, 1, jcast('int', jadd(Code05_PastoralOddities2.m, 1)), (lambda a, b: (a[2] - b[2])))
        # edge数组、wsort数组，每条边设置排名信息
        i = jcast('int', 1)
        while (i <= Code05_PastoralOddities2.m):
            jset(Code05_PastoralOddities2.wsort[i], 4, i)
            jset(Code05_PastoralOddities2.edge[Code05_PastoralOddities2.wsort[i][3]], 4, i)
            i = jcast('int', (i + 1))

    @staticmethod
    def main(args):
        in_ = Code05_PastoralOddities2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code05_PastoralOddities2.n = jcast('int', jcall(in_, 'nextInt'))
        Code05_PastoralOddities2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code05_PastoralOddities2.m):
            jset(Code05_PastoralOddities2.edge[i], 0, jcall(in_, 'nextInt'))
            jset(Code05_PastoralOddities2.edge[i], 1, jcall(in_, 'nextInt'))
            jset(Code05_PastoralOddities2.edge[i], 2, jcall(in_, 'nextInt'))
            jset(Code05_PastoralOddities2.edge[i], 3, i)
            i = jcast('int', (i + 1))
        Code05_PastoralOddities2.prepare()
        Code05_PastoralOddities2.compute(1, Code05_PastoralOddities2.m, 1, jcast('int', jadd(Code05_PastoralOddities2.m, 1)))
        i = jcast('int', 1)
        while (i <= Code05_PastoralOddities2.m):
            if (Code05_PastoralOddities2.ans[i] == jcast('int', jadd(Code05_PastoralOddities2.m, 1))):
                jcall(out, 'println', jcast('int', (-1)))
            else:
                jcall(out, 'println', Code05_PastoralOddities2.wsort[Code05_PastoralOddities2.ans[i]][2])
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
            return jcast('int', self.buffer[((_java_obj_8 := self), (_java_key_9 := 'ptr'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))), _java_old_10)[4]])

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
            raise TypeError("No matching overload for Code05_PastoralOddities2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_PastoralOddities2.MAXN = jcast('int', 100001)
Code05_PastoralOddities2.MAXM = jcast('int', 300001)
Code05_PastoralOddities2.n = jcast('int', 0)
Code05_PastoralOddities2.m = jcast('int', 0)
Code05_PastoralOddities2.edge = jarray('int', [Code05_PastoralOddities2.MAXM, 5])
Code05_PastoralOddities2.wsort = jarray('int', [Code05_PastoralOddities2.MAXM, 5])
Code05_PastoralOddities2.oddnum = jcast('int', 0)
Code05_PastoralOddities2.father = jarray('int', [Code05_PastoralOddities2.MAXN])
Code05_PastoralOddities2.siz = jarray('int', [Code05_PastoralOddities2.MAXN])
Code05_PastoralOddities2.rollback = jarray('int', [Code05_PastoralOddities2.MAXN, 2])
Code05_PastoralOddities2.opsize = jcast('int', 0)
Code05_PastoralOddities2.ans = jarray('int', [Code05_PastoralOddities2.MAXM])

if __name__ == '__main__':
    Code05_PastoralOddities2.main([])

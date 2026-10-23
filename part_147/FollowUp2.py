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

# 可并堆2，Python版
# 这道题课上没有讲，一个值得实现的左偏树模版题
# 完全是课上讲过的代码，看懂课就能看懂如下实现
# 给定n个元素，编号为1到n，给定每个元素的值num[i]
# 初始时每个元素单独组成一个集合，接下来有m次操作，类型有四种，格式如下
# 操作 0 x y   : 集合x中删除元素y，题目保证y一定在集合x中
# 操作 1 x     : 查询集合x中的最小值，这是唯一需要打印的操作
# 操作 2 x y   : 集合y合并到集合x，题目保证以后不会再有以y做集合编号的操作
# 操作 3 x y z : 集合x中元素y的权值修改为z，题目保证修改操作值只可能变小
# 测试链接 : https://www.luogu.com.cn/problem/P11266
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp2:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'num': 'num', 'up': 'up', 'ls': 'ls', 'rs': 'rs', 'dist': 'dist', 'father': 'father', 'root': 'root'}
    MAXN = 0
    n = 0
    m = 0
    num = None
    up = None
    ls = None
    rs = None
    dist = None
    father = None
    # root[x]表示集合x的堆头节点编号
    root = None
    @staticmethod
    def prepare():
        FollowUp2.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= FollowUp2.n):
            jset(FollowUp2.up, i, jset(FollowUp2.ls, i, jset(FollowUp2.rs, i, jset(FollowUp2.dist, i, 0))))
            FollowUp2.father[i] = jcast('int', i)
            # 初始每个集合i只有元素i
            FollowUp2.root[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(FollowUp2.father, i, (i if (FollowUp2.father[i] == i) else FollowUp2.find(FollowUp2.father[i])))
        return jcast('int', FollowUp2.father[i])

    @staticmethod
    def merge(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if ((i == 0) or (j == 0)):
            return jcast('int', jcast('int', jadd(i, j)))
        tmp = 0
        # 小根堆
        # 值越小越优先
        # 值一样，按照编号越小越优先
        if ((FollowUp2.num[i] > FollowUp2.num[j]) or ((FollowUp2.num[i] == FollowUp2.num[j]) and (i > j))):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(FollowUp2.rs, i, FollowUp2.merge(FollowUp2.rs[i], j))
        jset(FollowUp2.up, FollowUp2.rs[i], i)
        if (FollowUp2.dist[FollowUp2.ls[i]] < FollowUp2.dist[FollowUp2.rs[i]]):
            tmp = jcast('int', FollowUp2.ls[i])
            FollowUp2.ls[i] = jcast('int', FollowUp2.rs[i])
            FollowUp2.rs[i] = jcast('int', tmp)
        FollowUp2.dist[i] = jcast('int', jcast('int', jadd(FollowUp2.dist[FollowUp2.rs[i]], 1)))
        jset(FollowUp2.father, FollowUp2.ls[i], jset(FollowUp2.father, FollowUp2.rs[i], i))
        return jcast('int', i)

    @staticmethod
    def remove(i):
        i = jcast('int', i)
        h = jcast('int', FollowUp2.find(i))
        jset(FollowUp2.father, FollowUp2.ls[i], FollowUp2.ls[i])
        jset(FollowUp2.father, FollowUp2.rs[i], FollowUp2.rs[i])
        s = jcast('int', FollowUp2.merge(FollowUp2.ls[i], FollowUp2.rs[i]))
        f = jcast('int', FollowUp2.up[i])
        FollowUp2.father[i] = jcast('int', s)
        FollowUp2.up[s] = jcast('int', f)
        if (h != i):
            FollowUp2.father[s] = jcast('int', h)
            if (FollowUp2.ls[f] == i):
                FollowUp2.ls[f] = jcast('int', s)
            else:
                FollowUp2.rs[f] = jcast('int', s)
            d = jcast('int', FollowUp2.dist[s])
            tmp = 0
            while (FollowUp2.dist[f] > jcast('int', jadd(d, 1))):
                FollowUp2.dist[f] = jcast('int', jcast('int', jadd(d, 1)))
                if (FollowUp2.dist[FollowUp2.ls[f]] < FollowUp2.dist[FollowUp2.rs[f]]):
                    tmp = jcast('int', FollowUp2.ls[f])
                    FollowUp2.ls[f] = jcast('int', FollowUp2.rs[f])
                    FollowUp2.rs[f] = jcast('int', tmp)
                f = jcast('int', FollowUp2.up[f])
                d = jcast('int', (d + 1))
        jset(FollowUp2.up, i, jset(FollowUp2.ls, i, jset(FollowUp2.rs, i, jset(FollowUp2.dist, i, 0))))
        return jcast('int', FollowUp2.father[s])

    @staticmethod
    def main(args):
        in_ = FollowUp2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        FollowUp2.n = jcast('int', jcall(in_, 'nextInt'))
        FollowUp2.m = jcast('int', jcall(in_, 'nextInt'))
        FollowUp2.prepare()
        i = jcast('int', 1)
        while (i <= FollowUp2.n):
            jset(FollowUp2.num, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= FollowUp2.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                # 删除后需要更新集合x的堆头
                jset(FollowUp2.root, x, FollowUp2.remove(y))
                if (FollowUp2.root[x] != 0):
                    jset(FollowUp2.father, FollowUp2.root[x], FollowUp2.root[x])
                    jset(FollowUp2.up, FollowUp2.root[x], 0)
            else:
                if (op == 1):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', FollowUp2.num[FollowUp2.root[x]])
                else:
                    if (op == 2):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        # 合并集合x和集合y
                        jset(FollowUp2.root, x, FollowUp2.merge(FollowUp2.root[x], FollowUp2.root[y]))
                        if (FollowUp2.root[x] != 0):
                            jset(FollowUp2.father, FollowUp2.root[x], FollowUp2.root[x])
                            jset(FollowUp2.up, FollowUp2.root[x], 0)
                    else:
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        z = jcast('int', jcall(in_, 'nextInt'))
                        h = jcast('int', FollowUp2.remove(y))
                        FollowUp2.num[y] = jcast('int', z)
                        # y改值后重新作为单点堆
                        FollowUp2.father[y] = jcast('int', y)
                        # 合并到集合x
                        jset(FollowUp2.root, x, FollowUp2.merge(h, y))
                        if (FollowUp2.root[x] != 0):
                            jset(FollowUp2.father, FollowUp2.root[x], FollowUp2.root[x])
                            jset(FollowUp2.up, FollowUp2.root[x], 0)
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
            return jcast('int', self.buffer[((_java_obj_1 := self), (_java_key_2 := 'ptr'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4]])

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
            raise TypeError("No matching overload for FollowUp2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUp2.MAXN = jcast('int', 1000001)
FollowUp2.n = jcast('int', 0)
FollowUp2.m = jcast('int', 0)
FollowUp2.num = jarray('int', [FollowUp2.MAXN])
FollowUp2.up = jarray('int', [FollowUp2.MAXN])
FollowUp2.ls = jarray('int', [FollowUp2.MAXN])
FollowUp2.rs = jarray('int', [FollowUp2.MAXN])
FollowUp2.dist = jarray('int', [FollowUp2.MAXN])
FollowUp2.father = jarray('int', [FollowUp2.MAXN])
FollowUp2.root = jarray('int', [FollowUp2.MAXN])

if __name__ == '__main__':
    FollowUp2.main([])

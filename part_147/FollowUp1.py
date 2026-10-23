# -*- coding: utf-8 -*-
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
# 注意打注释位置的代码即可
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class FollowUp1:
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
        FollowUp1.dist[0] = jcast('int', jcast('int', (-1)))
        i = jcast('int', 1)
        while (i <= FollowUp1.n):
            jset(FollowUp1.up, i, jset(FollowUp1.ls, i, jset(FollowUp1.rs, i, jset(FollowUp1.dist, i, 0))))
            FollowUp1.father[i] = jcast('int', i)
            # 初始每个集合i只有元素i
            FollowUp1.root[i] = jcast('int', i)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        jset(FollowUp1.father, i, (i if (FollowUp1.father[i] == i) else FollowUp1.find(FollowUp1.father[i])))
        return jcast('int', FollowUp1.father[i])

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
        if ((FollowUp1.num[i] > FollowUp1.num[j]) or ((FollowUp1.num[i] == FollowUp1.num[j]) and (i > j))):
            tmp = jcast('int', i)
            i = jcast('int', j)
            j = jcast('int', tmp)
        jset(FollowUp1.rs, i, FollowUp1.merge(FollowUp1.rs[i], j))
        jset(FollowUp1.up, FollowUp1.rs[i], i)
        if (FollowUp1.dist[FollowUp1.ls[i]] < FollowUp1.dist[FollowUp1.rs[i]]):
            tmp = jcast('int', FollowUp1.ls[i])
            FollowUp1.ls[i] = jcast('int', FollowUp1.rs[i])
            FollowUp1.rs[i] = jcast('int', tmp)
        FollowUp1.dist[i] = jcast('int', jcast('int', jadd(FollowUp1.dist[FollowUp1.rs[i]], 1)))
        jset(FollowUp1.father, FollowUp1.ls[i], jset(FollowUp1.father, FollowUp1.rs[i], i))
        return jcast('int', i)

    @staticmethod
    def remove(i):
        i = jcast('int', i)
        h = jcast('int', FollowUp1.find(i))
        jset(FollowUp1.father, FollowUp1.ls[i], FollowUp1.ls[i])
        jset(FollowUp1.father, FollowUp1.rs[i], FollowUp1.rs[i])
        s = jcast('int', FollowUp1.merge(FollowUp1.ls[i], FollowUp1.rs[i]))
        f = jcast('int', FollowUp1.up[i])
        FollowUp1.father[i] = jcast('int', s)
        FollowUp1.up[s] = jcast('int', f)
        if (h != i):
            FollowUp1.father[s] = jcast('int', h)
            if (FollowUp1.ls[f] == i):
                FollowUp1.ls[f] = jcast('int', s)
            else:
                FollowUp1.rs[f] = jcast('int', s)
            d = jcast('int', FollowUp1.dist[s])
            tmp = 0
            while (FollowUp1.dist[f] > jcast('int', jadd(d, 1))):
                FollowUp1.dist[f] = jcast('int', jcast('int', jadd(d, 1)))
                if (FollowUp1.dist[FollowUp1.ls[f]] < FollowUp1.dist[FollowUp1.rs[f]]):
                    tmp = jcast('int', FollowUp1.ls[f])
                    FollowUp1.ls[f] = jcast('int', FollowUp1.rs[f])
                    FollowUp1.rs[f] = jcast('int', tmp)
                f = jcast('int', FollowUp1.up[f])
                d = jcast('int', (d + 1))
        jset(FollowUp1.up, i, jset(FollowUp1.ls, i, jset(FollowUp1.rs, i, jset(FollowUp1.dist, i, 0))))
        return jcast('int', FollowUp1.father[s])

    @staticmethod
    def main(args):
        in_ = FollowUp1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        FollowUp1.n = jcast('int', jcall(in_, 'nextInt'))
        FollowUp1.m = jcast('int', jcall(in_, 'nextInt'))
        FollowUp1.prepare()
        i = jcast('int', 1)
        while (i <= FollowUp1.n):
            jset(FollowUp1.num, i, jcall(in_, 'nextInt'))
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        z = 0
        while (i <= FollowUp1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                x = jcast('int', jcall(in_, 'nextInt'))
                y = jcast('int', jcall(in_, 'nextInt'))
                # 删除后需要更新集合x的堆头
                jset(FollowUp1.root, x, FollowUp1.remove(y))
                if (FollowUp1.root[x] != 0):
                    jset(FollowUp1.father, FollowUp1.root[x], FollowUp1.root[x])
                    jset(FollowUp1.up, FollowUp1.root[x], 0)
            else:
                if (op == 1):
                    x = jcast('int', jcall(in_, 'nextInt'))
                    jcall(out, 'println', FollowUp1.num[FollowUp1.root[x]])
                else:
                    if (op == 2):
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        # 合并集合x和集合y
                        jset(FollowUp1.root, x, FollowUp1.merge(FollowUp1.root[x], FollowUp1.root[y]))
                        if (FollowUp1.root[x] != 0):
                            jset(FollowUp1.father, FollowUp1.root[x], FollowUp1.root[x])
                            jset(FollowUp1.up, FollowUp1.root[x], 0)
                    else:
                        x = jcast('int', jcall(in_, 'nextInt'))
                        y = jcast('int', jcall(in_, 'nextInt'))
                        z = jcast('int', jcall(in_, 'nextInt'))
                        h = jcast('int', FollowUp1.remove(y))
                        FollowUp1.num[y] = jcast('int', z)
                        # y改值后重新作为单点堆
                        FollowUp1.father[y] = jcast('int', y)
                        # 合并到集合x
                        jset(FollowUp1.root, x, FollowUp1.merge(h, y))
                        if (FollowUp1.root[x] != 0):
                            jset(FollowUp1.father, FollowUp1.root[x], FollowUp1.root[x])
                            jset(FollowUp1.up, FollowUp1.root[x], 0)
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
            raise TypeError("No matching overload for FollowUp1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


FollowUp1.MAXN = jcast('int', 1000001)
FollowUp1.n = jcast('int', 0)
FollowUp1.m = jcast('int', 0)
FollowUp1.num = jarray('int', [FollowUp1.MAXN])
FollowUp1.up = jarray('int', [FollowUp1.MAXN])
FollowUp1.ls = jarray('int', [FollowUp1.MAXN])
FollowUp1.rs = jarray('int', [FollowUp1.MAXN])
FollowUp1.dist = jarray('int', [FollowUp1.MAXN])
FollowUp1.father = jarray('int', [FollowUp1.MAXN])
FollowUp1.root = jarray('int', [FollowUp1.MAXN])

if __name__ == '__main__':
    FollowUp1.main([])

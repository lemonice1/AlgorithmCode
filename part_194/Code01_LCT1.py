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

# LCT模版题，Python版
# 一共n个点，每个点给定点权，一共m条操作，操作类型如下
# 操作 0 x y : 查询点x到点y的路径上，所有点权的异或和，保证x和y连通
# 操作 1 x y : 点x和点y之间增加直接边，如果x和y已经连通则忽略
# 操作 2 x y : 删除点x和点y之间的直接边，如果不存在这条直接边则忽略
# 操作 3 x y : 点x的点权变成y
# 1 <= n <= 10^5
# 1 <= m <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P3690
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_LCT1:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'm': 'm', 'arr': 'arr', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'xorsum': 'xorsum'}
    MAXN = 0
    n = 0
    m = 0
    arr = None
    # 既保存辅助splay内，每个节点的父节点
    # 也保存沿虚边向上跳到的原树父节点，认父不认子
    fa = None
    ls = None
    rs = None
    # 翻转操作的懒更新标记
    rev = None
    # 提根之前，先处理沿途的翻转标记，准备一个栈记录沿途节点
    sta = None
    # 本题需要异或和
    xorsum = None
    # 不同题目实现不同的up方法
    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code01_LCT1.xorsum[x] = jcast('int', jcast('int', (jcast('int', (Code01_LCT1.xorsum[Code01_LCT1.ls[x]] ^ Code01_LCT1.xorsum[Code01_LCT1.rs[x]])) ^ Code01_LCT1.arr[x])))

    # 判断节点x是不是辅助splay的顶部节点
    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code01_LCT1.ls[Code01_LCT1.fa[x]] != x) and (Code01_LCT1.rs[Code01_LCT1.fa[x]] != x)))

    # x不是辅助splay的顶部节点才能调用，返回x是其父的哪侧儿子
    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code01_LCT1.ls[Code01_LCT1.fa[x]] == x) else 1))

    # 翻转以x为根的辅助splay，交换左右儿子，打上翻转标记
    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code01_LCT1.ls[x])
            Code01_LCT1.ls[x] = jcast('int', Code01_LCT1.rs[x])
            Code01_LCT1.rs[x] = jcast('int', tmp)
            Code01_LCT1.rev[x] = jcast('boolean', (not Code01_LCT1.rev[x]))

    # 处理翻转懒更新
    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code01_LCT1.rev[x]:
            Code01_LCT1.reverse(Code01_LCT1.ls[x])
            Code01_LCT1.reverse(Code01_LCT1.rs[x])
            Code01_LCT1.rev[x] = jcast('boolean', False)

    # x向上旋转
    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code01_LCT1.fa[x])
        g = jcast('int', Code01_LCT1.fa[f])
        if (Code01_LCT1.lr(x) == 0):
            Code01_LCT1.ls[f] = jcast('int', Code01_LCT1.rs[x])
            if (Code01_LCT1.ls[f] != 0):
                jset(Code01_LCT1.fa, Code01_LCT1.ls[f], f)
            Code01_LCT1.rs[x] = jcast('int', f)
        else:
            Code01_LCT1.rs[f] = jcast('int', Code01_LCT1.ls[x])
            if (Code01_LCT1.rs[f] != 0):
                jset(Code01_LCT1.fa, Code01_LCT1.rs[f], f)
            Code01_LCT1.ls[x] = jcast('int', f)
        if (not Code01_LCT1.isroot(f)):
            if (Code01_LCT1.lr(f) == 0):
                Code01_LCT1.ls[g] = jcast('int', x)
            else:
                Code01_LCT1.rs[g] = jcast('int', x)
        Code01_LCT1.fa[f] = jcast('int', x)
        Code01_LCT1.fa[x] = jcast('int', g)
        Code01_LCT1.up(f)
        Code01_LCT1.up(x)

    # x提到辅助splay的顶部
    @staticmethod
    def splay(x):
        x = jcast('int', x)
        siz = jcast('int', 0)
        jset(Code01_LCT1.sta, (siz := jcast('int', (siz + (1)))), x)
        y = jcast('int', x)
        while (not Code01_LCT1.isroot(y)):
            jset(Code01_LCT1.sta, (siz := jcast('int', (siz + (1)))), Code01_LCT1.fa[y])
            y = jcast('int', Code01_LCT1.fa[y])
        while (siz != 0):
            Code01_LCT1.down(Code01_LCT1.sta[((_java_old_1 := siz), (siz := jcast('int', (siz + (-1)))), _java_old_1)[2]])
        while (not Code01_LCT1.isroot(x)):
            f = jcast('int', Code01_LCT1.fa[x])
            if (not Code01_LCT1.isroot(f)):
                if (Code01_LCT1.lr(x) == Code01_LCT1.lr(f)):
                    Code01_LCT1.rotate(f)
                else:
                    Code01_LCT1.rotate(x)
            Code01_LCT1.rotate(x)

    # 打通当前原树根到x的路径，使其成为一条实链
    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code01_LCT1.splay(x)
            Code01_LCT1.rs[x] = jcast('int', y)
            Code01_LCT1.up(x)
            y = jcast('int', x)
            x = jcast('int', Code01_LCT1.fa[x])

    # 让x变成原树的根，不改变连通方式
    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code01_LCT1.access(x)
        Code01_LCT1.splay(x)
        Code01_LCT1.reverse(x)

    # 建立根到x的实链，根变成辅助splay的顶，返回x所在原树的根
    @staticmethod
    def findroot(x):
        x = jcast('int', x)
        Code01_LCT1.access(x)
        Code01_LCT1.splay(x)
        Code01_LCT1.down(x)
        while (Code01_LCT1.ls[x] != 0):
            x = jcast('int', Code01_LCT1.ls[x])
            Code01_LCT1.down(x)
        Code01_LCT1.splay(x)
        return jcast('int', x)

    # 点x到点y的路径暴露出来，这条路径成为一条实链，组成一棵以y为顶部的辅助splay树
    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_LCT1.makeroot(x)
        Code01_LCT1.access(y)
        Code01_LCT1.splay(y)

    # 原树中连接x和y，如果原本连通则忽略
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_LCT1.makeroot(x)
        if (Code01_LCT1.findroot(y) != x):
            Code01_LCT1.fa[x] = jcast('int', y)

    # 原树中切断x和y之间的直接边，没有直接边则忽略
    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code01_LCT1.makeroot(x)
        if ((((Code01_LCT1.findroot(y) == x) and (Code01_LCT1.fa[y] == x)) and (Code01_LCT1.ls[y] == 0)) and (Code01_LCT1.rs[x] == y)):
            jset(Code01_LCT1.fa, y, jset(Code01_LCT1.rs, x, 0))
            Code01_LCT1.up(x)

    @staticmethod
    def main(args):
        in_ = Code01_LCT1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_LCT1.n = jcast('int', jcall(in_, 'nextInt'))
        Code01_LCT1.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_LCT1.n):
            jset(Code01_LCT1.arr, i, jcall(in_, 'nextInt'))
            Code01_LCT1.xorsum[i] = jcast('int', Code01_LCT1.arr[i])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        op = 0
        x = 0
        y = 0
        while (i <= Code01_LCT1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                Code01_LCT1.split(x, y)
                jcall(out, 'println', Code01_LCT1.xorsum[y])
            else:
                if (op == 1):
                    Code01_LCT1.link(x, y)
                else:
                    if (op == 2):
                        Code01_LCT1.cut(x, y)
                    else:
                        Code01_LCT1.splay(x)
                        Code01_LCT1.arr[x] = jcast('int', y)
                        Code01_LCT1.up(x)
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
            return jcast('int', self.buffer[((_java_obj_2 := self), (_java_key_3 := 'ptr'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))), _java_old_4)[4]])

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
            raise TypeError("No matching overload for Code01_LCT1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code01_LCT1.MAXN = jcast('int', 100001)
Code01_LCT1.n = jcast('int', 0)
Code01_LCT1.m = jcast('int', 0)
Code01_LCT1.arr = jarray('int', [Code01_LCT1.MAXN])
Code01_LCT1.fa = jarray('int', [Code01_LCT1.MAXN])
Code01_LCT1.ls = jarray('int', [Code01_LCT1.MAXN])
Code01_LCT1.rs = jarray('int', [Code01_LCT1.MAXN])
Code01_LCT1.rev = jarray('boolean', [Code01_LCT1.MAXN])
Code01_LCT1.sta = jarray('int', [Code01_LCT1.MAXN])
Code01_LCT1.xorsum = jarray('int', [Code01_LCT1.MAXN])

if __name__ == '__main__':
    Code01_LCT1.main([])

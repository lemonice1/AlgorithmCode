# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# LCT与动态图，Python版
# 初始有n个孤立节点，接下来有q条操作，操作类型如下
# 操作 1 x y : 点x和点y之间增加一条无向边，两点之前可能连通
# 操作 2 x y : 打印点x到点y的路径中，必经边的数量，不连通打印-1
# 操作 3 x y : 打印点x到点y的路径中，必经点的数量，不连通打印-1
# 必经点包括节点x和节点y本身
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 1 <= n <= 10^5
# 1 <= q <= 3 * 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P5489
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code08_DynamicGraph2:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXT': 'MAXT', 'n': 'n', 'q': 'q', 'father': 'father', 'fa': 'fa', 'ls': 'ls', 'rs': 'rs', 'rev': 'rev', 'sta': 'sta', 'cnt': 'cnt', 'val': 'val', 'sum': 'sum', 'zeroTag': 'zeroTag', 'road': 'road', 'roadLen': 'roadLen'}
    MAXN = 0
    MAXT = 0
    n = 0
    q = 0
    # 并查集维护连通性，因为本题卡常，用LCT判断连通性会超时
    father = None
    # 节点x参与割边LCT和割点LCT，两套LCT共用一套数组，但彼此独立
    # x表示割边LCT中的点，x+n表示割点LCT中的点
    fa = None
    ls = None
    rs = None
    rev = None
    sta = None
    # 割边LCT需要给边分配编号，割点LCT需要给方点分配编号
    # 都用cnt进行分配，初始值2*n，然后(++cnt)产生新编号
    cnt = 0
    # 两套LCT都有单点贡献和贡献汇总，并且汇总函数up都是一样的
    val = None
    sum = None
    # 只给割边LCT使用，zeroTag[x]表示以x为根的辅助splay中，所有边节点的贡献变成0
    zeroTag = None
    # 收集割点LCT中的路径
    road = None
    roadLen = 0
    @staticmethod
    def find(x):
        x = jcast('int', x)
        if (Code08_DynamicGraph2.father[x] != x):
            jset(Code08_DynamicGraph2.father, x, Code08_DynamicGraph2.find(Code08_DynamicGraph2.father[x]))
        return jcast('int', Code08_DynamicGraph2.father[x])

    @staticmethod
    def up(x):
        x = jcast('int', x)
        Code08_DynamicGraph2.sum[x] = jcast('int', jcast('int', jadd(jcast('int', jadd(Code08_DynamicGraph2.sum[Code08_DynamicGraph2.ls[x]], Code08_DynamicGraph2.sum[Code08_DynamicGraph2.rs[x]])), Code08_DynamicGraph2.val[x])))

    @staticmethod
    def isroot(x):
        x = jcast('int', x)
        return jcast('boolean', ((Code08_DynamicGraph2.ls[Code08_DynamicGraph2.fa[x]] != x) and (Code08_DynamicGraph2.rs[Code08_DynamicGraph2.fa[x]] != x)))

    @staticmethod
    def lr(x):
        x = jcast('int', x)
        return jcast('int', (0 if (Code08_DynamicGraph2.ls[Code08_DynamicGraph2.fa[x]] == x) else 1))

    @staticmethod
    def reverse(x):
        x = jcast('int', x)
        if (x != 0):
            tmp = jcast('int', Code08_DynamicGraph2.ls[x])
            Code08_DynamicGraph2.ls[x] = jcast('int', Code08_DynamicGraph2.rs[x])
            Code08_DynamicGraph2.rs[x] = jcast('int', tmp)
            Code08_DynamicGraph2.rev[x] = jcast('boolean', (not Code08_DynamicGraph2.rev[x]))

    # 只对割边LCT生效，整棵辅助splay的贡献变成0
    @staticmethod
    def setZero(x):
        x = jcast('int', x)
        if (x != 0):
            Code08_DynamicGraph2.val[x] = jcast('int', 0)
            Code08_DynamicGraph2.sum[x] = jcast('int', 0)
            Code08_DynamicGraph2.zeroTag[x] = jcast('boolean', True)

    @staticmethod
    def down(x):
        x = jcast('int', x)
        if Code08_DynamicGraph2.rev[x]:
            Code08_DynamicGraph2.reverse(Code08_DynamicGraph2.ls[x])
            Code08_DynamicGraph2.reverse(Code08_DynamicGraph2.rs[x])
            Code08_DynamicGraph2.rev[x] = jcast('boolean', False)
        # zeroTag只对割边LCT生效
        if Code08_DynamicGraph2.zeroTag[x]:
            Code08_DynamicGraph2.setZero(Code08_DynamicGraph2.ls[x])
            Code08_DynamicGraph2.setZero(Code08_DynamicGraph2.rs[x])
            Code08_DynamicGraph2.zeroTag[x] = jcast('boolean', False)

    @staticmethod
    def rotate(x):
        x = jcast('int', x)
        f = jcast('int', Code08_DynamicGraph2.fa[x])
        g = jcast('int', Code08_DynamicGraph2.fa[f])
        if (Code08_DynamicGraph2.lr(x) == 0):
            Code08_DynamicGraph2.ls[f] = jcast('int', Code08_DynamicGraph2.rs[x])
            if (Code08_DynamicGraph2.ls[f] != 0):
                jset(Code08_DynamicGraph2.fa, Code08_DynamicGraph2.ls[f], f)
            Code08_DynamicGraph2.rs[x] = jcast('int', f)
        else:
            Code08_DynamicGraph2.rs[f] = jcast('int', Code08_DynamicGraph2.ls[x])
            if (Code08_DynamicGraph2.rs[f] != 0):
                jset(Code08_DynamicGraph2.fa, Code08_DynamicGraph2.rs[f], f)
            Code08_DynamicGraph2.ls[x] = jcast('int', f)
        if (not Code08_DynamicGraph2.isroot(f)):
            if (Code08_DynamicGraph2.lr(f) == 0):
                Code08_DynamicGraph2.ls[g] = jcast('int', x)
            else:
                Code08_DynamicGraph2.rs[g] = jcast('int', x)
        Code08_DynamicGraph2.fa[f] = jcast('int', x)
        Code08_DynamicGraph2.fa[x] = jcast('int', g)
        Code08_DynamicGraph2.up(f)
        Code08_DynamicGraph2.up(x)

    @staticmethod
    def splay(x):
        x = jcast('int', x)
        size = jcast('int', 0)
        jset(Code08_DynamicGraph2.sta, (size := jcast('int', (size + (1)))), x)
        y = jcast('int', x)
        while (not Code08_DynamicGraph2.isroot(y)):
            jset(Code08_DynamicGraph2.sta, (size := jcast('int', (size + (1)))), Code08_DynamicGraph2.fa[y])
            y = jcast('int', Code08_DynamicGraph2.fa[y])
        while (size != 0):
            Code08_DynamicGraph2.down(Code08_DynamicGraph2.sta[((_java_old_1 := size), (size := jcast('int', (size + (-1)))), _java_old_1)[2]])
        while (not Code08_DynamicGraph2.isroot(x)):
            f = jcast('int', Code08_DynamicGraph2.fa[x])
            if (not Code08_DynamicGraph2.isroot(f)):
                if (Code08_DynamicGraph2.lr(x) == Code08_DynamicGraph2.lr(f)):
                    Code08_DynamicGraph2.rotate(f)
                else:
                    Code08_DynamicGraph2.rotate(x)
            Code08_DynamicGraph2.rotate(x)
        Code08_DynamicGraph2.up(x)

    @staticmethod
    def access(x):
        x = jcast('int', x)
        y = jcast('int', 0)
        while (x != 0):
            Code08_DynamicGraph2.splay(x)
            Code08_DynamicGraph2.rs[x] = jcast('int', y)
            Code08_DynamicGraph2.up(x)
            y = jcast('int', x)
            x = jcast('int', Code08_DynamicGraph2.fa[x])

    @staticmethod
    def makeroot(x):
        x = jcast('int', x)
        Code08_DynamicGraph2.access(x)
        Code08_DynamicGraph2.splay(x)
        Code08_DynamicGraph2.reverse(x)

    @staticmethod
    def split(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code08_DynamicGraph2.makeroot(x)
        Code08_DynamicGraph2.access(y)
        Code08_DynamicGraph2.splay(y)

    # 保证x和y当前不连通，所以化简了写法
    @staticmethod
    def link(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code08_DynamicGraph2.makeroot(x)
        Code08_DynamicGraph2.fa[x] = jcast('int', y)

    # 保证x和y之间存在直接边，所以化简了写法
    @staticmethod
    def cut(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        Code08_DynamicGraph2.split(x, y)
        Code08_DynamicGraph2.fa[x] = jcast('int', 0)
        Code08_DynamicGraph2.ls[y] = jcast('int', 0)
        Code08_DynamicGraph2.up(y)

    # 中序遍历收集节点，相当于实链中，从上到下依次收集节点
    @staticmethod
    def inOrder(x):
        x = jcast('int', x)
        if (x != 0):
            # 先处理翻转的懒更新，左右儿子确保更新正确
            Code08_DynamicGraph2.down(x)
            Code08_DynamicGraph2.inOrder(Code08_DynamicGraph2.ls[x])
            jset(Code08_DynamicGraph2.road, ((_java_obj_2 := Code08_DynamicGraph2), (_java_key_3 := 'roadLen'), (_java_old_4 := jget(_java_obj_2, _java_key_3)), jset(_java_obj_2, _java_key_3, jcast('int', (_java_old_4 + (1)))))[3], x)
            Code08_DynamicGraph2.inOrder(Code08_DynamicGraph2.rs[x])

    @staticmethod
    def addEdge(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        fx = jcast('int', Code08_DynamicGraph2.find(x))
        fy = jcast('int', Code08_DynamicGraph2.find(y))
        if (fx != fy):
            Code08_DynamicGraph2.father[fy] = jcast('int', fx)
            # 割边LCT中，新边变成LCT中的点，新边是割边，贡献是1
            edge = jcast('int', ((_java_obj_5 := Code08_DynamicGraph2), (_java_key_6 := 'cnt'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (1)))))[3])
            Code08_DynamicGraph2.val[edge] = jcast('int', 1)
            Code08_DynamicGraph2.sum[edge] = jcast('int', 1)
            Code08_DynamicGraph2.link(x, edge)
            Code08_DynamicGraph2.link(y, edge)
            # 割点LCT中，此时是割边，两个圆点直接连接，不建立方点
            Code08_DynamicGraph2.link(jcast('int', jadd(x, Code08_DynamicGraph2.n)), jcast('int', jadd(y, Code08_DynamicGraph2.n)))
        else:
            # 如果x和y已经连通，那么此时形成环
            # 割边LCT中，x到y路径上的所有边都进入环
            # 从此不再是割边，贡献都变成0
            Code08_DynamicGraph2.split(x, y)
            Code08_DynamicGraph2.setZero(y)
            # 切换到割点LCT中对应的两个状态节点
            x = jcast('int', jcast('int', jadd(x, Code08_DynamicGraph2.n)))
            y = jcast('int', jcast('int', jadd(y, Code08_DynamicGraph2.n)))
            # 暴露当前动态圆方树中x到y的路径
            Code08_DynamicGraph2.split(x, y)
            if (Code08_DynamicGraph2.sum[y] > 2):
                # 辅助splay中，按照中序遍历收集节点，核心是中序
                # 等同于按照当前实链从x到y的顺序收集所有节点
                Code08_DynamicGraph2.roadLen = jcast('int', 0)
                Code08_DynamicGraph2.inOrder(y)
                # 删除原来路径中的边
                i = jcast('int', 2)
                while (i <= Code08_DynamicGraph2.roadLen):
                    Code08_DynamicGraph2.cut(Code08_DynamicGraph2.road[jcast('int', (i - 1))], Code08_DynamicGraph2.road[i])
                    i = jcast('int', (i + 1))
                # 新建方点，形成更大的点双连通分量
                square = jcast('int', ((_java_obj_8 := Code08_DynamicGraph2), (_java_key_9 := 'cnt'), (_java_old_10 := jget(_java_obj_8, _java_key_9)), jset(_java_obj_8, _java_key_9, jcast('int', (_java_old_10 + (1)))))[3])
                # 原路径上的所有圆点和旧方点，连接到新方点
                i = jcast('int', 1)
                while (i <= Code08_DynamicGraph2.roadLen):
                    Code08_DynamicGraph2.link(Code08_DynamicGraph2.road[i], square)
                    i = jcast('int', (i + 1))

    @staticmethod
    def queryCute(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (Code08_DynamicGraph2.find(x) != Code08_DynamicGraph2.find(y)):
            return jcast('int', jcast('int', (-1)))
        Code08_DynamicGraph2.split(x, y)
        return jcast('int', Code08_DynamicGraph2.sum[y])

    @staticmethod
    def queryCutv(x, y):
        x = jcast('int', x)
        y = jcast('int', y)
        if (Code08_DynamicGraph2.find(x) != Code08_DynamicGraph2.find(y)):
            return jcast('int', jcast('int', (-1)))
        x = jcast('int', jcast('int', jadd(x, Code08_DynamicGraph2.n)))
        y = jcast('int', jcast('int', jadd(y, Code08_DynamicGraph2.n)))
        Code08_DynamicGraph2.split(x, y)
        return jcast('int', Code08_DynamicGraph2.sum[y])

    @staticmethod
    def main(args):
        in_ = Code08_DynamicGraph2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code08_DynamicGraph2.n = jcast('int', jcall(in_, 'nextInt'))
        Code08_DynamicGraph2.q = jcast('int', jcall(in_, 'nextInt'))
        Code08_DynamicGraph2.cnt = jcast('int', jcast('int', (Code08_DynamicGraph2.n << (1 & 31))))
        # 并查集初始化
        # 割边LCT中的原节点贡献为0，无需设置
        # 割点LCT中的原节点是圆点，设置贡献是1
        i = jcast('int', 1)
        while (i <= Code08_DynamicGraph2.n):
            Code08_DynamicGraph2.father[i] = jcast('int', i)
            Code08_DynamicGraph2.val[jcast('int', jadd(i, Code08_DynamicGraph2.n))] = jcast('int', 1)
            Code08_DynamicGraph2.sum[jcast('int', jadd(i, Code08_DynamicGraph2.n))] = jcast('int', 1)
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        lastAns = jcast('int', 0)
        curAns = 0
        op = 0
        x = 0
        y = 0
        while (i <= Code08_DynamicGraph2.q):
            op = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcall(in_, 'nextInt'))
            y = jcast('int', jcall(in_, 'nextInt'))
            x = jcast('int', jcast('int', (x ^ lastAns)))
            y = jcast('int', jcast('int', (y ^ lastAns)))
            if (op == 1):
                Code08_DynamicGraph2.addEdge(x, y)
            else:
                if (op == 2):
                    curAns = jcast('int', Code08_DynamicGraph2.queryCute(x, y))
                else:
                    curAns = jcast('int', Code08_DynamicGraph2.queryCutv(x, y))
                jcall(out, 'println', curAns)
                if (curAns != jcast('int', (-1))):
                    lastAns = jcast('int', curAns)
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
            return jcast('int', self.buffer[((_java_obj_11 := self), (_java_key_12 := 'ptr'), (_java_old_13 := jget(_java_obj_11, _java_key_12)), jset(_java_obj_11, _java_key_12, jcast('int', (_java_old_13 + (1)))), _java_old_13)[4]])

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
            raise TypeError("No matching overload for Code08_DynamicGraph2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code08_DynamicGraph2.MAXN = jcast('int', 100001)
Code08_DynamicGraph2.MAXT = jcast('int', 400001)
Code08_DynamicGraph2.n = jcast('int', 0)
Code08_DynamicGraph2.q = jcast('int', 0)
Code08_DynamicGraph2.father = jarray('int', [Code08_DynamicGraph2.MAXN])
Code08_DynamicGraph2.fa = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.ls = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.rs = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.rev = jarray('boolean', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.sta = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.cnt = jcast('int', 0)
Code08_DynamicGraph2.val = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.sum = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.zeroTag = jarray('boolean', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.road = jarray('int', [Code08_DynamicGraph2.MAXT])
Code08_DynamicGraph2.roadLen = jcast('int', 0)

if __name__ == '__main__':
    Code08_DynamicGraph2.main([])

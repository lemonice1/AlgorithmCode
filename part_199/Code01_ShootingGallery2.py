# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 射击场，Python版
# 每个靶子是一个矩形区域，x轴的范围[l, r]，y轴的范围[d, u]，还有z轴的数值
# 空间里有n个靶子，接下来有m发子弹，每发子弹给定出发时的x和y坐标，子弹沿z轴前进
# 子弹会击中前进过程中遇到的第一个尚未消失的靶子，随后击中的靶子和这发子弹都消失
# 对于每一发子弹，打印它击中的靶子编号，如果没有击中打印0
# 1 <= n、m <= 10^5
# 0 <= 坐标值 <= 10^7
# 测试链接 : https://www.luogu.com.cn/problem/CF44G
# 测试链接 : https://codeforces.com/problemset/problem/44/G
# 对应实现保留相同的算法逻辑
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code01_ShootingGallery2:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'n': 'n', 'm': 'm', 'target': 'target', 'x': 'x', 'y': 'y', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'alive': 'alive', 'aliveSiz': 'aliveSiz', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'idmin': 'idmin', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'bullet': 'bullet', 'ans': 'ans', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0
    n = 0
    m = 0
    # l、r、d、u、z、id
    target = None
    # 子弹的K-D树
    x = None
    y = None
    cntkdt = 0
    root = 0
    ls = None
    rs = None
    # 节点是否存活
    alive = None
    # 子树的存活节点数量，平衡性只用aliveSiz判断
    aliveSiz = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    # 区域内的子弹最小编号
    idmin = None
    # 替罪羊树的重构
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    # 答案的查询和收集
    bullet = 0
    ans = None
    @staticmethod
    def init(qx, qy):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code01_ShootingGallery2.cntkdt = jcast('int', (Code01_ShootingGallery2.cntkdt + 1))
        Code01_ShootingGallery2.x[Code01_ShootingGallery2.cntkdt] = jcast('int', qx)
        Code01_ShootingGallery2.y[Code01_ShootingGallery2.cntkdt] = jcast('int', qy)
        jset(Code01_ShootingGallery2.ls, Code01_ShootingGallery2.cntkdt, jset(Code01_ShootingGallery2.rs, Code01_ShootingGallery2.cntkdt, 0))
        Code01_ShootingGallery2.alive[Code01_ShootingGallery2.cntkdt] = jcast('boolean', True)
        Code01_ShootingGallery2.aliveSiz[Code01_ShootingGallery2.cntkdt] = jcast('int', 1)
        jset(Code01_ShootingGallery2.xmin, Code01_ShootingGallery2.cntkdt, jset(Code01_ShootingGallery2.xmax, Code01_ShootingGallery2.cntkdt, qx))
        jset(Code01_ShootingGallery2.ymin, Code01_ShootingGallery2.cntkdt, jset(Code01_ShootingGallery2.ymax, Code01_ShootingGallery2.cntkdt, qy))
        Code01_ShootingGallery2.idmin[Code01_ShootingGallery2.cntkdt] = jcast('int', Code01_ShootingGallery2.cntkdt)
        return jcast('int', Code01_ShootingGallery2.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        l = jcast('int', Code01_ShootingGallery2.ls[i])
        r = jcast('int', Code01_ShootingGallery2.rs[i])
        if Code01_ShootingGallery2.alive[i]:
            Code01_ShootingGallery2.aliveSiz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code01_ShootingGallery2.aliveSiz[l])), Code01_ShootingGallery2.aliveSiz[r])))
            jset(Code01_ShootingGallery2.xmin, i, jset(Code01_ShootingGallery2.xmax, i, Code01_ShootingGallery2.x[i]))
            jset(Code01_ShootingGallery2.ymin, i, jset(Code01_ShootingGallery2.ymax, i, Code01_ShootingGallery2.y[i]))
            Code01_ShootingGallery2.idmin[i] = jcast('int', i)
        else:
            Code01_ShootingGallery2.aliveSiz[i] = jcast('int', jcast('int', jadd(Code01_ShootingGallery2.aliveSiz[l], Code01_ShootingGallery2.aliveSiz[r])))
            jset(Code01_ShootingGallery2.xmin, i, jset(Code01_ShootingGallery2.ymin, i, Code01_ShootingGallery2.INF))
            jset(Code01_ShootingGallery2.xmax, i, jset(Code01_ShootingGallery2.ymax, i, jcast('int', (-Code01_ShootingGallery2.INF))))
            Code01_ShootingGallery2.idmin[i] = jcast('int', Code01_ShootingGallery2.INF)
        if (Code01_ShootingGallery2.aliveSiz[l] != 0):
            jset(Code01_ShootingGallery2.xmin, i, jstatic('Math', 'min', Code01_ShootingGallery2.xmin[i], Code01_ShootingGallery2.xmin[l]))
            jset(Code01_ShootingGallery2.xmax, i, jstatic('Math', 'max', Code01_ShootingGallery2.xmax[i], Code01_ShootingGallery2.xmax[l]))
            jset(Code01_ShootingGallery2.ymin, i, jstatic('Math', 'min', Code01_ShootingGallery2.ymin[i], Code01_ShootingGallery2.ymin[l]))
            jset(Code01_ShootingGallery2.ymax, i, jstatic('Math', 'max', Code01_ShootingGallery2.ymax[i], Code01_ShootingGallery2.ymax[l]))
            jset(Code01_ShootingGallery2.idmin, i, jstatic('Math', 'min', Code01_ShootingGallery2.idmin[i], Code01_ShootingGallery2.idmin[l]))
        if (Code01_ShootingGallery2.aliveSiz[r] != 0):
            jset(Code01_ShootingGallery2.xmin, i, jstatic('Math', 'min', Code01_ShootingGallery2.xmin[i], Code01_ShootingGallery2.xmin[r]))
            jset(Code01_ShootingGallery2.xmax, i, jstatic('Math', 'max', Code01_ShootingGallery2.xmax[i], Code01_ShootingGallery2.xmax[r]))
            jset(Code01_ShootingGallery2.ymin, i, jstatic('Math', 'min', Code01_ShootingGallery2.ymin[i], Code01_ShootingGallery2.ymin[r]))
            jset(Code01_ShootingGallery2.ymax, i, jstatic('Math', 'max', Code01_ShootingGallery2.ymax[i], Code01_ShootingGallery2.ymax[r]))
            jset(Code01_ShootingGallery2.idmin, i, jstatic('Math', 'min', Code01_ShootingGallery2.idmin[i], Code01_ShootingGallery2.idmin[r]))

    # 先按照维度坐标比较，坐标相同时按kdt节点编号比较
    # 建树、插入、删除使用相同的比较规则
    # 即便发生重构，根据比较规则，删除时也能确定唯一的方向
    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('int', (Code01_ShootingGallery2.x[i] if (dimension == 0) else Code01_ShootingGallery2.y[i]))
        v2 = jcast('int', (Code01_ShootingGallery2.x[j] if (dimension == 0) else Code01_ShootingGallery2.y[j]))
        return jcast('int', ((jcast('int', (-1)) if (v1 < v2) else 1) if (v1 != v2) else jcast('int', (i - j))))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code01_ShootingGallery2.arr[i])
        Code01_ShootingGallery2.arr[i] = jcast('int', Code01_ShootingGallery2.arr[j])
        Code01_ShootingGallery2.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code01_ShootingGallery2.first = jcast('int', l)
        Code01_ShootingGallery2.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code01_ShootingGallery2.last):
            cmp = jcast('int', Code01_ShootingGallery2.compareNode(Code01_ShootingGallery2.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code01_ShootingGallery2.swap(((_java_obj_1 := Code01_ShootingGallery2), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code01_ShootingGallery2.swap(i, ((_java_obj_5 := Code01_ShootingGallery2), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, k, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code01_ShootingGallery2.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code01_ShootingGallery2.partition(l, r, pidx, dimension)
                if (k < Code01_ShootingGallery2.first):
                    r = jcast('int', jcast('int', (Code01_ShootingGallery2.first - 1)))
                else:
                    if (k > Code01_ShootingGallery2.last):
                        l = jcast('int', jcast('int', jadd(Code01_ShootingGallery2.last, 1)))
                    else:
                        raise JBreak(None)
            except JContinue as _java_control_8:
                if _java_control_8.label not in (None,):
                    raise
            except JBreak as _java_control_8:
                if _java_control_8.label not in (None,):
                    raise
                break

    @staticmethod
    def build(l, r, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        dimension = jcast('int', dimension)
        if (l > r):
            return jcast('int', 0)
        mid = jcast('int', jcast('int', (jcast('int', jadd(l, r)) >> (1 & 31))))
        Code01_ShootingGallery2.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code01_ShootingGallery2.arr[mid])
        jset(Code01_ShootingGallery2.ls, rt, Code01_ShootingGallery2.build(l, jcast('int', (mid - 1)), jcast('int', (dimension ^ 1))))
        jset(Code01_ShootingGallery2.rs, rt, Code01_ShootingGallery2.build(jcast('int', jadd(mid, 1)), r, jcast('int', (dimension ^ 1))))
        Code01_ShootingGallery2.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code01_ShootingGallery2.ALPHA * Code01_ShootingGallery2.aliveSiz[i]) >= jstatic('Math', 'max', Code01_ShootingGallery2.aliveSiz[Code01_ShootingGallery2.ls[i]], Code01_ShootingGallery2.aliveSiz[Code01_ShootingGallery2.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if ((i != 0) and (Code01_ShootingGallery2.aliveSiz[i] != 0)):
            if Code01_ShootingGallery2.alive[i]:
                jset(Code01_ShootingGallery2.arr, ((_java_obj_9 := Code01_ShootingGallery2), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code01_ShootingGallery2.dfs(Code01_ShootingGallery2.ls[i])
            Code01_ShootingGallery2.dfs(Code01_ShootingGallery2.rs[i])

    @staticmethod
    def rebuild():
        if (Code01_ShootingGallery2.top != 0):
            Code01_ShootingGallery2.treeSiz = jcast('int', 0)
            Code01_ShootingGallery2.dfs(Code01_ShootingGallery2.top)
            newRoot = jcast('int', Code01_ShootingGallery2.build(1, Code01_ShootingGallery2.treeSiz, Code01_ShootingGallery2.topDimension))
            if (Code01_ShootingGallery2.topFather == 0):
                Code01_ShootingGallery2.root = jcast('int', newRoot)
            else:
                if (Code01_ShootingGallery2.topSide == 1):
                    Code01_ShootingGallery2.ls[Code01_ShootingGallery2.topFather] = jcast('int', newRoot)
                else:
                    Code01_ShootingGallery2.rs[Code01_ShootingGallery2.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_add_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if ((u == 0) or (Code01_ShootingGallery2.aliveSiz[u] == 0)):
            return jcast('int', insertNode)
        if (Code01_ShootingGallery2.compareNode(insertNode, u, dimension) <= 0):
            jset(Code01_ShootingGallery2.ls, u, Code01_ShootingGallery2._java_add_0(insertNode, Code01_ShootingGallery2.ls[u], u, 1, jcast('int', (dimension ^ 1))))
        else:
            jset(Code01_ShootingGallery2.rs, u, Code01_ShootingGallery2._java_add_0(insertNode, Code01_ShootingGallery2.rs[u], u, 2, jcast('int', (dimension ^ 1))))
        Code01_ShootingGallery2.maintain(u)
        if (not Code01_ShootingGallery2.balance(u)):
            Code01_ShootingGallery2.top = jcast('int', u)
            Code01_ShootingGallery2.topFather = jcast('int', fa)
            Code01_ShootingGallery2.topSide = jcast('int', side)
            Code01_ShootingGallery2.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_add_1(qx, qy):
        qx = jcast('int', qx)
        qy = jcast('int', qy)
        Code01_ShootingGallery2.top = jcast('int', jset(Code01_ShootingGallery2, 'topFather', jset(Code01_ShootingGallery2, 'topSide', jset(Code01_ShootingGallery2, 'topDimension', 0))))
        insertNode = jcast('int', Code01_ShootingGallery2.init(qx, qy))
        Code01_ShootingGallery2.root = jcast('int', Code01_ShootingGallery2._java_add_0(insertNode, Code01_ShootingGallery2.root, 0, 0, 0))
        Code01_ShootingGallery2.rebuild()

    @staticmethod
    def _java_remove_0(removeNode, u, fa, side, dimension):
        removeNode = jcast('int', removeNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == removeNode):
            Code01_ShootingGallery2.alive[u] = jcast('boolean', False)
        else:
            if (Code01_ShootingGallery2.compareNode(removeNode, u, dimension) <= 0):
                Code01_ShootingGallery2._java_remove_0(removeNode, Code01_ShootingGallery2.ls[u], u, 1, jcast('int', (dimension ^ 1)))
            else:
                Code01_ShootingGallery2._java_remove_0(removeNode, Code01_ShootingGallery2.rs[u], u, 2, jcast('int', (dimension ^ 1)))
        Code01_ShootingGallery2.maintain(u)
        if (not Code01_ShootingGallery2.balance(u)):
            Code01_ShootingGallery2.top = jcast('int', u)
            Code01_ShootingGallery2.topFather = jcast('int', fa)
            Code01_ShootingGallery2.topSide = jcast('int', side)
            Code01_ShootingGallery2.topDimension = jcast('int', dimension)

    @staticmethod
    def _java_remove_1(removeNode):
        removeNode = jcast('int', removeNode)
        Code01_ShootingGallery2.top = jcast('int', jset(Code01_ShootingGallery2, 'topFather', jset(Code01_ShootingGallery2, 'topSide', jset(Code01_ShootingGallery2, 'topDimension', 0))))
        Code01_ShootingGallery2._java_remove_0(removeNode, Code01_ShootingGallery2.root, 0, 0, 0)
        Code01_ShootingGallery2.rebuild()

    @staticmethod
    def query(ql, qr, qd, qu, i):
        ql = jcast('int', ql)
        qr = jcast('int', qr)
        qd = jcast('int', qd)
        qu = jcast('int', qu)
        i = jcast('int', i)
        if (((i == 0) or (Code01_ShootingGallery2.aliveSiz[i] == 0)) or (Code01_ShootingGallery2.idmin[i] >= Code01_ShootingGallery2.bullet)):
            return
        if ((((Code01_ShootingGallery2.xmax[i] < ql) or (qr < Code01_ShootingGallery2.xmin[i])) or (Code01_ShootingGallery2.ymax[i] < qd)) or (qu < Code01_ShootingGallery2.ymin[i])):
            return
        if ((((ql <= Code01_ShootingGallery2.xmin[i]) and (Code01_ShootingGallery2.xmax[i] <= qr)) and (qd <= Code01_ShootingGallery2.ymin[i])) and (Code01_ShootingGallery2.ymax[i] <= qu)):
            Code01_ShootingGallery2.bullet = jcast('int', jstatic('Math', 'min', Code01_ShootingGallery2.bullet, Code01_ShootingGallery2.idmin[i]))
            return
        if ((((Code01_ShootingGallery2.alive[i] and (ql <= Code01_ShootingGallery2.x[i])) and (Code01_ShootingGallery2.x[i] <= qr)) and (qd <= Code01_ShootingGallery2.y[i])) and (Code01_ShootingGallery2.y[i] <= qu)):
            Code01_ShootingGallery2.bullet = jcast('int', jstatic('Math', 'min', Code01_ShootingGallery2.bullet, i))
        l = jcast('int', Code01_ShootingGallery2.ls[i])
        r = jcast('int', Code01_ShootingGallery2.rs[i])
        if (Code01_ShootingGallery2.idmin[l] < Code01_ShootingGallery2.idmin[r]):
            Code01_ShootingGallery2.query(ql, qr, qd, qu, l)
            Code01_ShootingGallery2.query(ql, qr, qd, qu, r)
        else:
            Code01_ShootingGallery2.query(ql, qr, qd, qu, r)
            Code01_ShootingGallery2.query(ql, qr, qd, qu, l)

    @staticmethod
    def main(args):
        in_ = Code01_ShootingGallery2.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code01_ShootingGallery2.n = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        while (i <= Code01_ShootingGallery2.n):
            jset(Code01_ShootingGallery2.target[i], 0, jcall(in_, 'nextInt'))
            jset(Code01_ShootingGallery2.target[i], 1, jcall(in_, 'nextInt'))
            jset(Code01_ShootingGallery2.target[i], 2, jcall(in_, 'nextInt'))
            jset(Code01_ShootingGallery2.target[i], 3, jcall(in_, 'nextInt'))
            jset(Code01_ShootingGallery2.target[i], 4, jcall(in_, 'nextInt'))
            jset(Code01_ShootingGallery2.target[i], 5, i)
            i = jcast('int', (i + 1))
        jset(Code01_ShootingGallery2.xmin, 0, jset(Code01_ShootingGallery2.ymin, 0, Code01_ShootingGallery2.INF))
        jset(Code01_ShootingGallery2.xmax, 0, jset(Code01_ShootingGallery2.ymax, 0, jcast('int', (-Code01_ShootingGallery2.INF))))
        Code01_ShootingGallery2.idmin[0] = jcast('int', Code01_ShootingGallery2.INF)
        Code01_ShootingGallery2.m = jcast('int', jcall(in_, 'nextInt'))
        i = jcast('int', 1)
        qx = 0
        qy = 0
        while (i <= Code01_ShootingGallery2.m):
            qx = jcast('int', jcall(in_, 'nextInt'))
            qy = jcast('int', jcall(in_, 'nextInt'))
            Code01_ShootingGallery2._java_add_1(qx, qy)
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code01_ShootingGallery2.target, 1, jcast('int', jadd(Code01_ShootingGallery2.n, 1)), (lambda a, b: (a[4] - b[4])))
        k = jcast('int', 1)
        while (k <= Code01_ShootingGallery2.n):
            Code01_ShootingGallery2.bullet = jcast('int', Code01_ShootingGallery2.INF)
            Code01_ShootingGallery2.query(Code01_ShootingGallery2.target[k][0], Code01_ShootingGallery2.target[k][1], Code01_ShootingGallery2.target[k][2], Code01_ShootingGallery2.target[k][3], Code01_ShootingGallery2.root)
            if (Code01_ShootingGallery2.bullet != Code01_ShootingGallery2.INF):
                Code01_ShootingGallery2.ans[Code01_ShootingGallery2.bullet] = jcast('int', Code01_ShootingGallery2.target[k][5])
                Code01_ShootingGallery2._java_remove_1(Code01_ShootingGallery2.bullet)
            k = jcast('int', (k + 1))
        i = jcast('int', 1)
        while (i <= Code01_ShootingGallery2.m):
            jcall(out, 'println', Code01_ShootingGallery2.ans[i])
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
            return jcast('int', self.buffer[((_java_obj_12 := self), (_java_key_13 := 'ptr'), (_java_old_14 := jget(_java_obj_12, _java_key_13)), jset(_java_obj_12, _java_key_13, jcast('int', (_java_old_14 + (1)))), _java_old_14)[4]])

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
            raise TypeError("No matching overload for Code01_ShootingGallery2.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int', 'int']], [False, False])
        if _java_choice == 0:
            return Code01_ShootingGallery2._java_add_0(*args)
        if _java_choice == 1:
            return Code01_ShootingGallery2._java_add_1(*args)
        raise TypeError("No matching overload for Code01_ShootingGallery2.add")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code01_ShootingGallery2._java_remove_0(*args)
        if _java_choice == 1:
            return Code01_ShootingGallery2._java_remove_1(*args)
        raise TypeError("No matching overload for Code01_ShootingGallery2.remove")


Code01_ShootingGallery2.MAXN = jcast('int', 100001)
Code01_ShootingGallery2.INF = jcast('int', jcast('int', (1 << (30 & 31))))
Code01_ShootingGallery2.n = jcast('int', 0)
Code01_ShootingGallery2.m = jcast('int', 0)
Code01_ShootingGallery2.target = jarray('int', [Code01_ShootingGallery2.MAXN, 6])
Code01_ShootingGallery2.x = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.y = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.cntkdt = jcast('int', 0)
Code01_ShootingGallery2.root = jcast('int', 0)
Code01_ShootingGallery2.ls = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.rs = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.alive = jarray('boolean', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.aliveSiz = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.xmin = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.xmax = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.ymin = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.ymax = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.idmin = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.ALPHA = jcast('double', 0.7)
Code01_ShootingGallery2.top = jcast('int', 0)
Code01_ShootingGallery2.topFather = jcast('int', 0)
Code01_ShootingGallery2.topSide = jcast('int', 0)
Code01_ShootingGallery2.topDimension = jcast('int', 0)
Code01_ShootingGallery2.arr = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.treeSiz = jcast('int', 0)
Code01_ShootingGallery2.bullet = jcast('int', 0)
Code01_ShootingGallery2.ans = jarray('int', [Code01_ShootingGallery2.MAXN])
Code01_ShootingGallery2.first = jcast('int', 0)
Code01_ShootingGallery2.last = jcast('int', 0)

if __name__ == '__main__':
    Code01_ShootingGallery2.main([])

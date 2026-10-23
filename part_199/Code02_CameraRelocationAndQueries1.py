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

# 摄像头的修改和查询，Python版
# 三维空间中有n个摄像头，给定每个摄像头的初始位置，三维坐标(x, y, z)
# 接下来有m条操作，格式如下
# 操作 0 i x y z : 第i号摄像头位置变成(x, y, z)
# 操作 1 x y z r : 一个球体出现了，球心在(x, y, z)，半径为r
# 题目保证该球体的表面会恰好碰到一个摄像头
# 打印这个摄像头的编号，注意在内部的摄像头不算数
# 本题要求强制在线，得到操作参数的规则，打开测试链接查看
# 1 <= n、m <= 65536    随机生成坐标的绝对值 <= 100，至少小数点后5位
# 测试链接 : https://www.luogu.com.cn/problem/P11716
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_CameraRelocationAndQueries1:
    __java_fields__ = {'MAXN': 'MAXN', 'INF': 'INF', 'EPS': 'EPS', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b', 'lastAns': 'lastAns', 'x': 'x', 'y': 'y', 'z': 'z', 'kdtToCamera': 'kdtToCamera', 'cameraToKdt': 'cameraToKdt', 'cntkdt': 'cntkdt', 'root': 'root', 'ls': 'ls', 'rs': 'rs', 'alive': 'alive', 'aliveSiz': 'aliveSiz', 'xmin': 'xmin', 'xmax': 'xmax', 'ymin': 'ymin', 'ymax': 'ymax', 'zmin': 'zmin', 'zmax': 'zmax', 'ALPHA': 'ALPHA', 'top': 'top', 'topFather': 'topFather', 'topSide': 'topSide', 'topDimension': 'topDimension', 'arr': 'arr', 'treeSiz': 'treeSiz', 'first': 'first', 'last': 'last'}
    MAXN = 0
    INF = 0.0
    EPS = 0.0
    n = 0
    m = 0
    # 加密参数
    a = 0.0
    b = 0.0
    lastAns = 0.0
    # 三维坐标
    x = None
    y = None
    z = None
    # kdt节点编号对应的摄像头编号
    kdtToCamera = None
    # 摄像头编号对应的kdt节点编号
    cameraToKdt = None
    cntkdt = 0
    root = 0
    ls = None
    rs = None
    alive = None
    aliveSiz = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    zmin = None
    zmax = None
    ALPHA = 0.0
    top = 0
    topFather = 0
    topSide = 0
    topDimension = 0
    arr = None
    treeSiz = 0
    @staticmethod
    def init(qx, qy, qz, camera):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        camera = jcast('int', camera)
        Code02_CameraRelocationAndQueries1.cntkdt = jcast('int', (Code02_CameraRelocationAndQueries1.cntkdt + 1))
        Code02_CameraRelocationAndQueries1.x[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('double', qx)
        Code02_CameraRelocationAndQueries1.y[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('double', qy)
        Code02_CameraRelocationAndQueries1.z[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('double', qz)
        Code02_CameraRelocationAndQueries1.kdtToCamera[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('int', camera)
        jset(Code02_CameraRelocationAndQueries1.ls, Code02_CameraRelocationAndQueries1.cntkdt, jset(Code02_CameraRelocationAndQueries1.rs, Code02_CameraRelocationAndQueries1.cntkdt, 0))
        Code02_CameraRelocationAndQueries1.alive[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('boolean', True)
        Code02_CameraRelocationAndQueries1.aliveSiz[Code02_CameraRelocationAndQueries1.cntkdt] = jcast('int', 1)
        jset(Code02_CameraRelocationAndQueries1.xmin, Code02_CameraRelocationAndQueries1.cntkdt, jset(Code02_CameraRelocationAndQueries1.xmax, Code02_CameraRelocationAndQueries1.cntkdt, qx))
        jset(Code02_CameraRelocationAndQueries1.ymin, Code02_CameraRelocationAndQueries1.cntkdt, jset(Code02_CameraRelocationAndQueries1.ymax, Code02_CameraRelocationAndQueries1.cntkdt, qy))
        jset(Code02_CameraRelocationAndQueries1.zmin, Code02_CameraRelocationAndQueries1.cntkdt, jset(Code02_CameraRelocationAndQueries1.zmax, Code02_CameraRelocationAndQueries1.cntkdt, qz))
        return jcast('int', Code02_CameraRelocationAndQueries1.cntkdt)

    @staticmethod
    def maintain(i):
        i = jcast('int', i)
        l = jcast('int', Code02_CameraRelocationAndQueries1.ls[i])
        r = jcast('int', Code02_CameraRelocationAndQueries1.rs[i])
        if Code02_CameraRelocationAndQueries1.alive[i]:
            Code02_CameraRelocationAndQueries1.aliveSiz[i] = jcast('int', jcast('int', jadd(jcast('int', jadd(1, Code02_CameraRelocationAndQueries1.aliveSiz[l])), Code02_CameraRelocationAndQueries1.aliveSiz[r])))
            jset(Code02_CameraRelocationAndQueries1.xmin, i, jset(Code02_CameraRelocationAndQueries1.xmax, i, Code02_CameraRelocationAndQueries1.x[i]))
            jset(Code02_CameraRelocationAndQueries1.ymin, i, jset(Code02_CameraRelocationAndQueries1.ymax, i, Code02_CameraRelocationAndQueries1.y[i]))
            jset(Code02_CameraRelocationAndQueries1.zmin, i, jset(Code02_CameraRelocationAndQueries1.zmax, i, Code02_CameraRelocationAndQueries1.z[i]))
        else:
            Code02_CameraRelocationAndQueries1.aliveSiz[i] = jcast('int', jcast('int', jadd(Code02_CameraRelocationAndQueries1.aliveSiz[l], Code02_CameraRelocationAndQueries1.aliveSiz[r])))
            jset(Code02_CameraRelocationAndQueries1.xmin, i, jset(Code02_CameraRelocationAndQueries1.ymin, i, jset(Code02_CameraRelocationAndQueries1.zmin, i, Code02_CameraRelocationAndQueries1.INF)))
            jset(Code02_CameraRelocationAndQueries1.xmax, i, jset(Code02_CameraRelocationAndQueries1.ymax, i, jset(Code02_CameraRelocationAndQueries1.zmax, i, (-Code02_CameraRelocationAndQueries1.INF))))
        if (Code02_CameraRelocationAndQueries1.aliveSiz[l] != 0):
            jset(Code02_CameraRelocationAndQueries1.xmin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.xmin[i], Code02_CameraRelocationAndQueries1.xmin[l]))
            jset(Code02_CameraRelocationAndQueries1.xmax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.xmax[i], Code02_CameraRelocationAndQueries1.xmax[l]))
            jset(Code02_CameraRelocationAndQueries1.ymin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.ymin[i], Code02_CameraRelocationAndQueries1.ymin[l]))
            jset(Code02_CameraRelocationAndQueries1.ymax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.ymax[i], Code02_CameraRelocationAndQueries1.ymax[l]))
            jset(Code02_CameraRelocationAndQueries1.zmin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.zmin[i], Code02_CameraRelocationAndQueries1.zmin[l]))
            jset(Code02_CameraRelocationAndQueries1.zmax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.zmax[i], Code02_CameraRelocationAndQueries1.zmax[l]))
        if (Code02_CameraRelocationAndQueries1.aliveSiz[r] != 0):
            jset(Code02_CameraRelocationAndQueries1.xmin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.xmin[i], Code02_CameraRelocationAndQueries1.xmin[r]))
            jset(Code02_CameraRelocationAndQueries1.xmax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.xmax[i], Code02_CameraRelocationAndQueries1.xmax[r]))
            jset(Code02_CameraRelocationAndQueries1.ymin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.ymin[i], Code02_CameraRelocationAndQueries1.ymin[r]))
            jset(Code02_CameraRelocationAndQueries1.ymax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.ymax[i], Code02_CameraRelocationAndQueries1.ymax[r]))
            jset(Code02_CameraRelocationAndQueries1.zmin, i, jstatic('Math', 'min', Code02_CameraRelocationAndQueries1.zmin[i], Code02_CameraRelocationAndQueries1.zmin[r]))
            jset(Code02_CameraRelocationAndQueries1.zmax, i, jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.zmax[i], Code02_CameraRelocationAndQueries1.zmax[r]))

    @staticmethod
    def compareNode(i, j, dimension):
        i = jcast('int', i)
        j = jcast('int', j)
        dimension = jcast('int', dimension)
        v1 = jcast('double', (Code02_CameraRelocationAndQueries1.x[i] if (dimension == 0) else (Code02_CameraRelocationAndQueries1.y[i] if (dimension == 1) else Code02_CameraRelocationAndQueries1.z[i])))
        v2 = jcast('double', (Code02_CameraRelocationAndQueries1.x[j] if (dimension == 0) else (Code02_CameraRelocationAndQueries1.y[j] if (dimension == 1) else Code02_CameraRelocationAndQueries1.z[j])))
        return jcast('int', ((jcast('int', (-1)) if (v1 < v2) else 1) if (v1 != v2) else jcast('int', (i - j))))

    @staticmethod
    def swap(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        tmp = jcast('int', Code02_CameraRelocationAndQueries1.arr[i])
        Code02_CameraRelocationAndQueries1.arr[i] = jcast('int', Code02_CameraRelocationAndQueries1.arr[j])
        Code02_CameraRelocationAndQueries1.arr[j] = jcast('int', tmp)

    first = 0
    last = 0
    @staticmethod
    def partition(l, r, pidx, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        pidx = jcast('int', pidx)
        dimension = jcast('int', dimension)
        Code02_CameraRelocationAndQueries1.first = jcast('int', l)
        Code02_CameraRelocationAndQueries1.last = jcast('int', r)
        i = jcast('int', l)
        while (i <= Code02_CameraRelocationAndQueries1.last):
            cmp = jcast('int', Code02_CameraRelocationAndQueries1.compareNode(Code02_CameraRelocationAndQueries1.arr[i], pidx, dimension))
            if (cmp == 0):
                i = jcast('int', (i + 1))
            else:
                if (cmp < 0):
                    Code02_CameraRelocationAndQueries1.swap(((_java_obj_1 := Code02_CameraRelocationAndQueries1), (_java_key_2 := 'first'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], ((_java_old_4 := i), (i := jcast('int', (i + (1)))), _java_old_4)[2])
                else:
                    Code02_CameraRelocationAndQueries1.swap(i, ((_java_obj_5 := Code02_CameraRelocationAndQueries1), (_java_key_6 := 'last'), (_java_old_7 := jget(_java_obj_5, _java_key_6)), jset(_java_obj_5, _java_key_6, jcast('int', (_java_old_7 + (-1)))), _java_old_7)[4])

    @staticmethod
    def randSelect(l, r, k, dimension):
        l = jcast('int', l)
        r = jcast('int', r)
        k = jcast('int', k)
        dimension = jcast('int', dimension)
        while (l <= r):
            try:
                pidx = jcast('int', Code02_CameraRelocationAndQueries1.arr[jcast('int', jadd(l, jcast('int', (jstatic('Math', 'random') * jcast('int', jadd(jcast('int', (r - l)), 1))))))])
                Code02_CameraRelocationAndQueries1.partition(l, r, pidx, dimension)
                if (k < Code02_CameraRelocationAndQueries1.first):
                    r = jcast('int', jcast('int', (Code02_CameraRelocationAndQueries1.first - 1)))
                else:
                    if (k > Code02_CameraRelocationAndQueries1.last):
                        l = jcast('int', jcast('int', jadd(Code02_CameraRelocationAndQueries1.last, 1)))
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
        Code02_CameraRelocationAndQueries1.randSelect(l, r, mid, dimension)
        rt = jcast('int', Code02_CameraRelocationAndQueries1.arr[mid])
        jset(Code02_CameraRelocationAndQueries1.ls, rt, Code02_CameraRelocationAndQueries1.build(l, jcast('int', (mid - 1)), jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3))))
        jset(Code02_CameraRelocationAndQueries1.rs, rt, Code02_CameraRelocationAndQueries1.build(jcast('int', jadd(mid, 1)), r, jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3))))
        Code02_CameraRelocationAndQueries1.maintain(rt)
        return jcast('int', rt)

    @staticmethod
    def balance(i):
        i = jcast('int', i)
        return jcast('boolean', ((Code02_CameraRelocationAndQueries1.ALPHA * Code02_CameraRelocationAndQueries1.aliveSiz[i]) >= jstatic('Math', 'max', Code02_CameraRelocationAndQueries1.aliveSiz[Code02_CameraRelocationAndQueries1.ls[i]], Code02_CameraRelocationAndQueries1.aliveSiz[Code02_CameraRelocationAndQueries1.rs[i]])))

    @staticmethod
    def dfs(i):
        i = jcast('int', i)
        if ((i != 0) and (Code02_CameraRelocationAndQueries1.aliveSiz[i] != 0)):
            if Code02_CameraRelocationAndQueries1.alive[i]:
                jset(Code02_CameraRelocationAndQueries1.arr, ((_java_obj_9 := Code02_CameraRelocationAndQueries1), (_java_key_10 := 'treeSiz'), (_java_old_11 := jget(_java_obj_9, _java_key_10)), jset(_java_obj_9, _java_key_10, jcast('int', (_java_old_11 + (1)))))[3], i)
            Code02_CameraRelocationAndQueries1.dfs(Code02_CameraRelocationAndQueries1.ls[i])
            Code02_CameraRelocationAndQueries1.dfs(Code02_CameraRelocationAndQueries1.rs[i])

    @staticmethod
    def rebuild():
        if (Code02_CameraRelocationAndQueries1.top != 0):
            Code02_CameraRelocationAndQueries1.treeSiz = jcast('int', 0)
            Code02_CameraRelocationAndQueries1.dfs(Code02_CameraRelocationAndQueries1.top)
            newRoot = jcast('int', Code02_CameraRelocationAndQueries1.build(1, Code02_CameraRelocationAndQueries1.treeSiz, Code02_CameraRelocationAndQueries1.topDimension))
            if (Code02_CameraRelocationAndQueries1.topFather == 0):
                Code02_CameraRelocationAndQueries1.root = jcast('int', newRoot)
            else:
                if (Code02_CameraRelocationAndQueries1.topSide == 1):
                    Code02_CameraRelocationAndQueries1.ls[Code02_CameraRelocationAndQueries1.topFather] = jcast('int', newRoot)
                else:
                    Code02_CameraRelocationAndQueries1.rs[Code02_CameraRelocationAndQueries1.topFather] = jcast('int', newRoot)

    @staticmethod
    def _java_add_0(insertNode, u, fa, side, dimension):
        insertNode = jcast('int', insertNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if ((u == 0) or (Code02_CameraRelocationAndQueries1.aliveSiz[u] == 0)):
            return jcast('int', insertNode)
        if (Code02_CameraRelocationAndQueries1.compareNode(insertNode, u, dimension) <= 0):
            jset(Code02_CameraRelocationAndQueries1.ls, u, Code02_CameraRelocationAndQueries1._java_add_0(insertNode, Code02_CameraRelocationAndQueries1.ls[u], u, 1, jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3))))
        else:
            jset(Code02_CameraRelocationAndQueries1.rs, u, Code02_CameraRelocationAndQueries1._java_add_0(insertNode, Code02_CameraRelocationAndQueries1.rs[u], u, 2, jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3))))
        Code02_CameraRelocationAndQueries1.maintain(u)
        if (not Code02_CameraRelocationAndQueries1.balance(u)):
            Code02_CameraRelocationAndQueries1.top = jcast('int', u)
            Code02_CameraRelocationAndQueries1.topFather = jcast('int', fa)
            Code02_CameraRelocationAndQueries1.topSide = jcast('int', side)
            Code02_CameraRelocationAndQueries1.topDimension = jcast('int', dimension)
        return jcast('int', u)

    @staticmethod
    def _java_add_1(qx, qy, qz, camera):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        camera = jcast('int', camera)
        Code02_CameraRelocationAndQueries1.top = jcast('int', jset(Code02_CameraRelocationAndQueries1, 'topFather', jset(Code02_CameraRelocationAndQueries1, 'topSide', jset(Code02_CameraRelocationAndQueries1, 'topDimension', 0))))
        insertNode = jcast('int', Code02_CameraRelocationAndQueries1.init(qx, qy, qz, camera))
        Code02_CameraRelocationAndQueries1.cameraToKdt[camera] = jcast('int', insertNode)
        Code02_CameraRelocationAndQueries1.root = jcast('int', Code02_CameraRelocationAndQueries1._java_add_0(insertNode, Code02_CameraRelocationAndQueries1.root, 0, 0, 0))
        Code02_CameraRelocationAndQueries1.rebuild()

    @staticmethod
    def _java_remove_0(removeNode, u, fa, side, dimension):
        removeNode = jcast('int', removeNode)
        u = jcast('int', u)
        fa = jcast('int', fa)
        side = jcast('int', side)
        dimension = jcast('int', dimension)
        if (u == removeNode):
            Code02_CameraRelocationAndQueries1.alive[u] = jcast('boolean', False)
        else:
            if (Code02_CameraRelocationAndQueries1.compareNode(removeNode, u, dimension) <= 0):
                Code02_CameraRelocationAndQueries1._java_remove_0(removeNode, Code02_CameraRelocationAndQueries1.ls[u], u, 1, jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3)))
            else:
                Code02_CameraRelocationAndQueries1._java_remove_0(removeNode, Code02_CameraRelocationAndQueries1.rs[u], u, 2, jcast('int', jmod(jcast('int', jadd(dimension, 1)), 3)))
        Code02_CameraRelocationAndQueries1.maintain(u)
        if (not Code02_CameraRelocationAndQueries1.balance(u)):
            Code02_CameraRelocationAndQueries1.top = jcast('int', u)
            Code02_CameraRelocationAndQueries1.topFather = jcast('int', fa)
            Code02_CameraRelocationAndQueries1.topSide = jcast('int', side)
            Code02_CameraRelocationAndQueries1.topDimension = jcast('int', dimension)

    @staticmethod
    def _java_remove_1(removeNode):
        removeNode = jcast('int', removeNode)
        Code02_CameraRelocationAndQueries1.top = jcast('int', jset(Code02_CameraRelocationAndQueries1, 'topFather', jset(Code02_CameraRelocationAndQueries1, 'topSide', jset(Code02_CameraRelocationAndQueries1, 'topDimension', 0))))
        Code02_CameraRelocationAndQueries1._java_remove_0(removeNode, Code02_CameraRelocationAndQueries1.root, 0, 0, 0)
        Code02_CameraRelocationAndQueries1.rebuild()

    @staticmethod
    def mindist(qx, qy, qz, i):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        i = jcast('int', i)
        xd = jcast('double', ((Code02_CameraRelocationAndQueries1.xmin[i] - qx) if (qx < Code02_CameraRelocationAndQueries1.xmin[i]) else ((qx - Code02_CameraRelocationAndQueries1.xmax[i]) if (qx > Code02_CameraRelocationAndQueries1.xmax[i]) else 0)))
        yd = jcast('double', ((Code02_CameraRelocationAndQueries1.ymin[i] - qy) if (qy < Code02_CameraRelocationAndQueries1.ymin[i]) else ((qy - Code02_CameraRelocationAndQueries1.ymax[i]) if (qy > Code02_CameraRelocationAndQueries1.ymax[i]) else 0)))
        zd = jcast('double', ((Code02_CameraRelocationAndQueries1.zmin[i] - qz) if (qz < Code02_CameraRelocationAndQueries1.zmin[i]) else ((qz - Code02_CameraRelocationAndQueries1.zmax[i]) if (qz > Code02_CameraRelocationAndQueries1.zmax[i]) else 0)))
        return jcast('double', jadd(jadd((xd * xd), (yd * yd)), (zd * zd)))

    @staticmethod
    def maxdist(qx, qy, qz, i):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        i = jcast('int', i)
        xd2 = jcast('double', jstatic('Math', 'max', ((qx - Code02_CameraRelocationAndQueries1.xmin[i]) * (qx - Code02_CameraRelocationAndQueries1.xmin[i])), ((qx - Code02_CameraRelocationAndQueries1.xmax[i]) * (qx - Code02_CameraRelocationAndQueries1.xmax[i]))))
        yd2 = jcast('double', jstatic('Math', 'max', ((qy - Code02_CameraRelocationAndQueries1.ymin[i]) * (qy - Code02_CameraRelocationAndQueries1.ymin[i])), ((qy - Code02_CameraRelocationAndQueries1.ymax[i]) * (qy - Code02_CameraRelocationAndQueries1.ymax[i]))))
        zd2 = jcast('double', jstatic('Math', 'max', ((qz - Code02_CameraRelocationAndQueries1.zmin[i]) * (qz - Code02_CameraRelocationAndQueries1.zmin[i])), ((qz - Code02_CameraRelocationAndQueries1.zmax[i]) * (qz - Code02_CameraRelocationAndQueries1.zmax[i]))))
        return jcast('double', jadd(jadd(xd2, yd2), zd2))

    @staticmethod
    def dist(qx, qy, qz, i):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        i = jcast('int', i)
        xd = jcast('double', (qx - Code02_CameraRelocationAndQueries1.x[i]))
        yd = jcast('double', (qy - Code02_CameraRelocationAndQueries1.y[i]))
        zd = jcast('double', (qz - Code02_CameraRelocationAndQueries1.z[i]))
        return jcast('double', jadd(jadd((xd * xd), (yd * yd)), (zd * zd)))

    @staticmethod
    def _java_query_0(qx, qy, qz, low, high, i):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        low = jcast('double', low)
        high = jcast('double', high)
        i = jcast('int', i)
        if ((i == 0) or (Code02_CameraRelocationAndQueries1.aliveSiz[i] == 0)):
            return jcast('int', 0)
        if ((Code02_CameraRelocationAndQueries1.mindist(qx, qy, qz, i) > high) or (Code02_CameraRelocationAndQueries1.maxdist(qx, qy, qz, i) < low)):
            return jcast('int', 0)
        if Code02_CameraRelocationAndQueries1.alive[i]:
            d = jcast('double', Code02_CameraRelocationAndQueries1.dist(qx, qy, qz, i))
            if ((low <= d) and (d <= high)):
                return jcast('int', Code02_CameraRelocationAndQueries1.kdtToCamera[i])
        ans = jcast('int', Code02_CameraRelocationAndQueries1._java_query_0(qx, qy, qz, low, high, Code02_CameraRelocationAndQueries1.ls[i]))
        if (ans != 0):
            return jcast('int', ans)
        return jcast('int', Code02_CameraRelocationAndQueries1._java_query_0(qx, qy, qz, low, high, Code02_CameraRelocationAndQueries1.rs[i]))

    @staticmethod
    def _java_query_1(qx, qy, qz, qr):
        qx = jcast('double', qx)
        qy = jcast('double', qy)
        qz = jcast('double', qz)
        qr = jcast('double', qr)
        low = jcast('double', jstatic('Math', 'max', 0, (qr - Code02_CameraRelocationAndQueries1.EPS)))
        high = jcast('double', jadd(qr, Code02_CameraRelocationAndQueries1.EPS))
        low = jcast('double', (low * low))
        high = jcast('double', (high * high))
        return jcast('int', Code02_CameraRelocationAndQueries1._java_query_0(qx, qy, qz, low, high, Code02_CameraRelocationAndQueries1.root))

    # 解密函数，密文encrypt，明文范围 l ~ r，解密得到明文返回
    # 题目给定的加密函数f(x)，该函数是严格单调递增的
    # 所以x在其范围上不断二分，当 f(x) == 密文，x就确定了
    # 于是需要确定，不同数据各自的范围，范围够用即可
    # 关于坐标，题目说了范围 -100 ~ +100
    # 关于摄像头编号，范围明显是 1 ~ n
    # 关于半径，题目保证每次出现球体时，表面一定会恰好出现一个摄像头
    # 所以球体的半径 <= 到达最远摄像头的距离
    # 球心和摄像头的每一维的坐标都在 -100 ~ +100
    # 所以每个维度的差值最多200，一共三个维度，根据欧式距离的计算公式
    # 半径 <= sqrt(200 * 200 * 3) < 347，所以半径范围取 0 ~ 400
    @staticmethod
    def decode(encrypt, l, r):
        encrypt = jcast('double', encrypt)
        l = jcast('double', l)
        r = jcast('double', r)
        l = jcast('double', jadd((Code02_CameraRelocationAndQueries1.lastAns * l), 1))
        r = jcast('double', jadd((Code02_CameraRelocationAndQueries1.lastAns * r), 1))
        i = jcast('int', 1)
        while (i <= 60):
            mid = jcast('double', jdiv(jadd(l, r), 2))
            fx = jcast('double', ((Code02_CameraRelocationAndQueries1.a * mid) - (Code02_CameraRelocationAndQueries1.b * jstatic('Math', 'sin', mid))))
            if (fx <= encrypt):
                l = jcast('double', mid)
            else:
                r = jcast('double', mid)
            i = jcast('int', (i + 1))
        return jcast('double', jdiv((l - 1), Code02_CameraRelocationAndQueries1.lastAns))

    @staticmethod
    def main(args):
        in_ = Code02_CameraRelocationAndQueries1.FastReader(jget(System, 'in'), _java_ctor=0)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        Code02_CameraRelocationAndQueries1.n = jcast('int', jcall(in_, 'nextInt'))
        Code02_CameraRelocationAndQueries1.m = jcast('int', jcall(in_, 'nextInt'))
        Code02_CameraRelocationAndQueries1.a = jcast('double', jcall(in_, 'nextDouble'))
        Code02_CameraRelocationAndQueries1.b = jcast('double', jcall(in_, 'nextDouble'))
        Code02_CameraRelocationAndQueries1.lastAns = jcast('double', 0.1)
        jset(Code02_CameraRelocationAndQueries1.xmin, 0, jset(Code02_CameraRelocationAndQueries1.ymin, 0, jset(Code02_CameraRelocationAndQueries1.zmin, 0, Code02_CameraRelocationAndQueries1.INF)))
        jset(Code02_CameraRelocationAndQueries1.xmax, 0, jset(Code02_CameraRelocationAndQueries1.ymax, 0, jset(Code02_CameraRelocationAndQueries1.zmax, 0, (-Code02_CameraRelocationAndQueries1.INF))))
        qx = 0.0
        qy = 0.0
        qz = 0.0
        qr = 0.0
        qid = 0.0
        op = 0
        camera = 0
        kdtNode = 0
        curAns = 0
        i = jcast('int', 1)
        while (i <= Code02_CameraRelocationAndQueries1.n):
            qx = jcast('double', jcall(in_, 'nextDouble'))
            qy = jcast('double', jcall(in_, 'nextDouble'))
            qz = jcast('double', jcall(in_, 'nextDouble'))
            kdtNode = jcast('int', Code02_CameraRelocationAndQueries1.init(qx, qy, qz, i))
            Code02_CameraRelocationAndQueries1.cameraToKdt[i] = jcast('int', kdtNode)
            Code02_CameraRelocationAndQueries1.arr[i] = jcast('int', kdtNode)
            i = jcast('int', (i + 1))
        Code02_CameraRelocationAndQueries1.root = jcast('int', Code02_CameraRelocationAndQueries1.build(1, Code02_CameraRelocationAndQueries1.n, 0))
        i = jcast('int', 1)
        while (i <= Code02_CameraRelocationAndQueries1.m):
            op = jcast('int', jcall(in_, 'nextInt'))
            if (op == 0):
                qid = jcast('double', jcall(in_, 'nextDouble'))
                qx = jcast('double', jcall(in_, 'nextDouble'))
                qy = jcast('double', jcall(in_, 'nextDouble'))
                qz = jcast('double', jcall(in_, 'nextDouble'))
                qx = jcast('double', Code02_CameraRelocationAndQueries1.decode(qx, jcast('int', (-100)), 100))
                qy = jcast('double', Code02_CameraRelocationAndQueries1.decode(qy, jcast('int', (-100)), 100))
                qz = jcast('double', Code02_CameraRelocationAndQueries1.decode(qz, jcast('int', (-100)), 100))
                camera = jcast('int', jcast('int', jstatic('Math', 'round', Code02_CameraRelocationAndQueries1.decode(qid, 1, Code02_CameraRelocationAndQueries1.n))))
                Code02_CameraRelocationAndQueries1._java_remove_1(Code02_CameraRelocationAndQueries1.cameraToKdt[camera])
                Code02_CameraRelocationAndQueries1._java_add_1(qx, qy, qz, camera)
            else:
                qx = jcast('double', jcall(in_, 'nextDouble'))
                qy = jcast('double', jcall(in_, 'nextDouble'))
                qz = jcast('double', jcall(in_, 'nextDouble'))
                qr = jcast('double', jcall(in_, 'nextDouble'))
                qx = jcast('double', Code02_CameraRelocationAndQueries1.decode(qx, jcast('int', (-100)), 100))
                qy = jcast('double', Code02_CameraRelocationAndQueries1.decode(qy, jcast('int', (-100)), 100))
                qz = jcast('double', Code02_CameraRelocationAndQueries1.decode(qz, jcast('int', (-100)), 100))
                qr = jcast('double', Code02_CameraRelocationAndQueries1.decode(qr, 0, 400))
                curAns = jcast('int', Code02_CameraRelocationAndQueries1._java_query_1(qx, qy, qz, qr))
                jcall(out, 'println', curAns)
                Code02_CameraRelocationAndQueries1.lastAns = jcast('double', curAns)
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

        def nextDouble(self):
            c = 0
            while True:
                c = jcast('int', self.readByte())
                if not (((c <= jchar(' ')) and (c != jcast('int', (-1))))):
                    break
            neg = jcast('boolean', False)
            if (c == jchar('-')):
                neg = jcast('boolean', True)
                c = jcast('int', self.readByte())
            intPart = jcast('long', 0)
            while (((c > jchar(' ')) and (c != jcast('int', (-1)))) and (c != jchar('.'))):
                intPart = jcast('long', jcast('long', jadd(jcast('long', (intPart * 10)), jcast('int', (c - jchar('0'))))))
                c = jcast('int', self.readByte())
            val = jcast('double', jcast('double', intPart))
            if (c == jchar('.')):
                c = jcast('int', self.readByte())
                base = jcast('double', 0.1)
                while ((c > jchar(' ')) and (c != jcast('int', (-1)))):
                    val = jcast('double', jadd(val, (jcast('int', (c - jchar('0'))) * base)))
                    base = jcast('double', (base * 0.1))
                    c = jcast('int', self.readByte())
            return jcast('double', ((-val) if neg else val))

        def __init__(self, *args, _java_ctor=None):
            self.buffer = jarray('byte', [jcast('int', (1 << (16 & 31)))])
            self.ptr = jcast('int', 0)
            self.len = jcast('int', 0)
            self.in_ = None
            _java_choice = _java_ctor if _java_ctor is not None else jselect(args, [['InputStream']], [False])
            if _java_choice == 0:
                return self._java_init_0(*args)
            raise TypeError("No matching overload for Code02_CameraRelocationAndQueries1.FastReader.FastReader")


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')

    @staticmethod
    def add(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['double', 'double', 'double', 'int']], [False, False])
        if _java_choice == 0:
            return Code02_CameraRelocationAndQueries1._java_add_0(*args)
        if _java_choice == 1:
            return Code02_CameraRelocationAndQueries1._java_add_1(*args)
        raise TypeError("No matching overload for Code02_CameraRelocationAndQueries1.add")

    @staticmethod
    def remove(*args):
        _java_choice = jselect(args, [['int', 'int', 'int', 'int', 'int'], ['int']], [False, False])
        if _java_choice == 0:
            return Code02_CameraRelocationAndQueries1._java_remove_0(*args)
        if _java_choice == 1:
            return Code02_CameraRelocationAndQueries1._java_remove_1(*args)
        raise TypeError("No matching overload for Code02_CameraRelocationAndQueries1.remove")

    @staticmethod
    def query(*args):
        _java_choice = jselect(args, [['double', 'double', 'double', 'double', 'double', 'int'], ['double', 'double', 'double', 'double']], [False, False])
        if _java_choice == 0:
            return Code02_CameraRelocationAndQueries1._java_query_0(*args)
        if _java_choice == 1:
            return Code02_CameraRelocationAndQueries1._java_query_1(*args)
        raise TypeError("No matching overload for Code02_CameraRelocationAndQueries1.query")


Code02_CameraRelocationAndQueries1.MAXN = jcast('int', 200001)
Code02_CameraRelocationAndQueries1.INF = jcast('double', 1e+100)
Code02_CameraRelocationAndQueries1.EPS = jcast('double', 1e-08)
Code02_CameraRelocationAndQueries1.n = jcast('int', 0)
Code02_CameraRelocationAndQueries1.m = jcast('int', 0)
Code02_CameraRelocationAndQueries1.a = jcast('double', 0.0)
Code02_CameraRelocationAndQueries1.b = jcast('double', 0.0)
Code02_CameraRelocationAndQueries1.lastAns = jcast('double', 0.0)
Code02_CameraRelocationAndQueries1.x = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.y = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.z = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.kdtToCamera = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.cameraToKdt = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.cntkdt = jcast('int', 0)
Code02_CameraRelocationAndQueries1.root = jcast('int', 0)
Code02_CameraRelocationAndQueries1.ls = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.rs = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.alive = jarray('boolean', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.aliveSiz = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.xmin = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.xmax = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.ymin = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.ymax = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.zmin = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.zmax = jarray('double', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.ALPHA = jcast('double', 0.7)
Code02_CameraRelocationAndQueries1.top = jcast('int', 0)
Code02_CameraRelocationAndQueries1.topFather = jcast('int', 0)
Code02_CameraRelocationAndQueries1.topSide = jcast('int', 0)
Code02_CameraRelocationAndQueries1.topDimension = jcast('int', 0)
Code02_CameraRelocationAndQueries1.arr = jarray('int', [Code02_CameraRelocationAndQueries1.MAXN])
Code02_CameraRelocationAndQueries1.treeSiz = jcast('int', 0)
Code02_CameraRelocationAndQueries1.first = jcast('int', 0)
Code02_CameraRelocationAndQueries1.last = jcast('int', 0)

if __name__ == '__main__':
    Code02_CameraRelocationAndQueries1.main([])

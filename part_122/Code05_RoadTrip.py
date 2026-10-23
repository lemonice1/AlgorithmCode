# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 开车旅行
# 给定一个长度为n的数组arr，下标1 ~ n范围，数组无重复值
# 近的定义、距离的定义，和题目4一致
# a和b同坐一辆车开始往右旅行，a先开车，b后开车，此后每到达一点都换人驾驶
# 如果a在某点驾驶，那么车去往该点右侧第二近的点，如果b在某点驾驶，那么车去往该点右侧第一近的点
# a和b从s位置出发，如果开车总距离超过x，或轮到某人时右侧无点可选，那么旅行停止
# 问题1 : 给定距离x0，返回1 ~ n-1中从哪个点出发，a行驶距离 / b行驶距离，比值最小
# 如果从多个点出发时，比值都为最小，那么返回arr中的值最大的点
# 问题2 : 给定s、x，返回旅行停止时，a开了多少距离、b开了多少距离
# 问题1只调用1次
# 问题2调用m次，每组有不同的s、x
# 1 <= n、m、s <= 10^5
# -10^9 <= arr[i] <= 10^9
# 1 <= x0、x <= 10^9
# 测试链接 : https://www.luogu.com.cn/problem/P1081
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code05_RoadTrip:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXP': 'MAXP', 'arr': 'arr', 'to1': 'to1', 'dist1': 'dist1', 'to2': 'to2', 'dist2': 'dist2', 'rank': 'rank', 'last': 'last', 'next': 'next', 'stto': 'stto', 'stdist': 'stdist', 'sta': 'sta', 'stb': 'stb', 'n': 'n', 'm': 'm', 'a': 'a', 'b': 'b'}
    MAXN = 0
    MAXP = 0
    arr = None
    to1 = None
    dist1 = None
    to2 = None
    dist2 = None
    rank = None
    last = None
    next = None
    # stto[i][p] : 从i位置出发，a和b轮流开2^p轮之后，车到达了几号点
    stto = None
    # stdist[i][p] : 从i位置出发，a和b轮流开2^p轮之后，总距离是多少
    stdist = None
    # sta[i][p] : 从i位置出发，a和b轮流开2^p轮之后，a行驶了多少距离
    sta = None
    # stb[i][p] : 从i位置出发，a和b轮流开2^p轮之后，b行驶了多少距离
    stb = None
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code05_RoadTrip.n = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.n):
            jcall(in_, 'nextToken')
            Code05_RoadTrip.arr[i] = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', (i + 1))
        Code05_RoadTrip.near()
        Code05_RoadTrip.st()
        jcall(in_, 'nextToken')
        x0 = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'println', Code05_RoadTrip.best(x0))
        jcall(in_, 'nextToken')
        Code05_RoadTrip.m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.m):
            jcall(in_, 'nextToken')
            s = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            x = jcast('int', jcast('int', jget(in_, 'nval')))
            Code05_RoadTrip.travel(s, x)
            jcall(out, 'println', jadd(jadd(Code05_RoadTrip.a, ' '), Code05_RoadTrip.b))
            i = jcast('int', (i + 1))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def near():
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.n):
            jset(Code05_RoadTrip.rank[i], 0, i)
            jset(Code05_RoadTrip.rank[i], 1, Code05_RoadTrip.arr[i])
            i = jcast('int', (i + 1))
        jstatic('Arrays', 'sort', Code05_RoadTrip.rank, 1, jcast('int', jadd(Code05_RoadTrip.n, 1)), (lambda a, b: jcast('int', (a[1] - b[1]))))
        jset(Code05_RoadTrip.rank[0], 0, 0)
        jset(Code05_RoadTrip.rank[jcast('int', jadd(Code05_RoadTrip.n, 1))], 0, 0)
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.n):
            jset(Code05_RoadTrip.last, Code05_RoadTrip.rank[i][0], Code05_RoadTrip.rank[jcast('int', (i - 1))][0])
            jset(Code05_RoadTrip.next, Code05_RoadTrip.rank[i][0], Code05_RoadTrip.rank[jcast('int', jadd(i, 1))][0])
            i = jcast('int', (i + 1))
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.n):
            Code05_RoadTrip.to1[i] = jcast('int', 0)
            Code05_RoadTrip.dist1[i] = jcast('int', 0)
            Code05_RoadTrip.to2[i] = jcast('int', 0)
            Code05_RoadTrip.dist2[i] = jcast('int', 0)
            Code05_RoadTrip.update(i, Code05_RoadTrip.last[i])
            Code05_RoadTrip.update(i, Code05_RoadTrip.last[Code05_RoadTrip.last[i]])
            Code05_RoadTrip.update(i, Code05_RoadTrip.next[i])
            Code05_RoadTrip.update(i, Code05_RoadTrip.next[Code05_RoadTrip.next[i]])
            Code05_RoadTrip.delete(i)
            i = jcast('int', (i + 1))

    @staticmethod
    def update(i, j):
        i = jcast('int', i)
        j = jcast('int', j)
        if (j == 0):
            return
        dist = jcast('int', jstatic('Math', 'abs', jcast('int', (Code05_RoadTrip.arr[i] - Code05_RoadTrip.arr[j]))))
        if (((Code05_RoadTrip.to1[i] == 0) or (dist < Code05_RoadTrip.dist1[i])) or ((dist == Code05_RoadTrip.dist1[i]) and (Code05_RoadTrip.arr[j] < Code05_RoadTrip.arr[Code05_RoadTrip.to1[i]]))):
            Code05_RoadTrip.to2[i] = jcast('int', Code05_RoadTrip.to1[i])
            Code05_RoadTrip.dist2[i] = jcast('int', Code05_RoadTrip.dist1[i])
            Code05_RoadTrip.to1[i] = jcast('int', j)
            Code05_RoadTrip.dist1[i] = jcast('int', dist)
        else:
            if (((Code05_RoadTrip.to2[i] == 0) or (dist < Code05_RoadTrip.dist2[i])) or ((dist == Code05_RoadTrip.dist2[i]) and (Code05_RoadTrip.arr[j] < Code05_RoadTrip.arr[Code05_RoadTrip.to2[i]]))):
                Code05_RoadTrip.to2[i] = jcast('int', j)
                Code05_RoadTrip.dist2[i] = jcast('int', dist)

    @staticmethod
    def delete(i):
        i = jcast('int', i)
        l = jcast('int', Code05_RoadTrip.last[i])
        r = jcast('int', Code05_RoadTrip.next[i])
        if (l != 0):
            Code05_RoadTrip.next[l] = jcast('int', r)
        if (r != 0):
            Code05_RoadTrip.last[r] = jcast('int', l)

    @staticmethod
    def st():
        # 倍增初始化
        i = jcast('int', 1)
        while (i <= Code05_RoadTrip.n):
            jset(Code05_RoadTrip.stto[i], 0, Code05_RoadTrip.to1[Code05_RoadTrip.to2[i]])
            jset(Code05_RoadTrip.stdist[i], 0, jcast('int', jadd(Code05_RoadTrip.dist2[i], Code05_RoadTrip.dist1[Code05_RoadTrip.to2[i]])))
            jset(Code05_RoadTrip.sta[i], 0, Code05_RoadTrip.dist2[i])
            jset(Code05_RoadTrip.stb[i], 0, Code05_RoadTrip.dist1[Code05_RoadTrip.to2[i]])
            i = jcast('int', (i + 1))
        # 生成倍增表
        p = jcast('int', 1)
        while (p <= Code05_RoadTrip.MAXP):
            i = jcast('int', 1)
            while (i <= Code05_RoadTrip.n):
                jset(Code05_RoadTrip.stto[i], p, Code05_RoadTrip.stto[Code05_RoadTrip.stto[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])
                if (Code05_RoadTrip.stto[i][p] != 0):
                    jset(Code05_RoadTrip.stdist[i], p, jcast('int', jadd(Code05_RoadTrip.stdist[i][jcast('int', (p - 1))], Code05_RoadTrip.stdist[Code05_RoadTrip.stto[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])))
                    jset(Code05_RoadTrip.sta[i], p, jcast('int', jadd(Code05_RoadTrip.sta[i][jcast('int', (p - 1))], Code05_RoadTrip.sta[Code05_RoadTrip.stto[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])))
                    jset(Code05_RoadTrip.stb[i], p, jcast('int', jadd(Code05_RoadTrip.stb[i][jcast('int', (p - 1))], Code05_RoadTrip.stb[Code05_RoadTrip.stto[i][jcast('int', (p - 1))]][jcast('int', (p - 1))])))
                i = jcast('int', (i + 1))
            p = jcast('int', (p + 1))

    @staticmethod
    def best(x0):
        x0 = jcast('int', x0)
        ans = jcast('int', 0)
        min = jcast('double', jget(Double, 'MAX_VALUE'))
        cur = 0.0
        i = jcast('int', 1)
        while (i < Code05_RoadTrip.n):
            Code05_RoadTrip.travel(i, x0)
            # cur这么设置更安全一些
            cur = jcast('double', (jget(Double, 'MAX_VALUE') if (Code05_RoadTrip.b == 0) else jdiv(jcast('double', Code05_RoadTrip.a), jcast('double', Code05_RoadTrip.b))))
            if (((ans == 0) or (cur < min)) or ((cur == min) and (Code05_RoadTrip.arr[i] > Code05_RoadTrip.arr[ans]))):
                ans = jcast('int', i)
                min = jcast('double', cur)
            i = jcast('int', (i + 1))
        return jcast('int', ans)

    a = 0
    b = 0
    @staticmethod
    def travel(s, x):
        s = jcast('int', s)
        x = jcast('int', x)
        Code05_RoadTrip.a = jcast('int', 0)
        Code05_RoadTrip.b = jcast('int', 0)
        p = jcast('int', Code05_RoadTrip.MAXP)
        while (p >= 0):
            if ((Code05_RoadTrip.stto[s][p] != 0) and (x >= Code05_RoadTrip.stdist[s][p])):
                x = jcast('int', jcast('int', (x - Code05_RoadTrip.stdist[s][p])))
                Code05_RoadTrip.a = jcast('int', jcast('int', jadd(Code05_RoadTrip.a, Code05_RoadTrip.sta[s][p])))
                Code05_RoadTrip.b = jcast('int', jcast('int', jadd(Code05_RoadTrip.b, Code05_RoadTrip.stb[s][p])))
                s = jcast('int', Code05_RoadTrip.stto[s][p])
            p = jcast('int', (p - 1))
        if (Code05_RoadTrip.dist2[s] <= x):
            Code05_RoadTrip.a = jcast('int', jcast('int', jadd(Code05_RoadTrip.a, Code05_RoadTrip.dist2[s])))

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code05_RoadTrip.MAXN = jcast('int', 100002)
Code05_RoadTrip.MAXP = jcast('int', 20)
Code05_RoadTrip.arr = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.to1 = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.dist1 = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.to2 = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.dist2 = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.rank = jarray('int', [Code05_RoadTrip.MAXN, 2])
Code05_RoadTrip.last = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.next = jarray('int', [Code05_RoadTrip.MAXN])
Code05_RoadTrip.stto = jarray('int', [Code05_RoadTrip.MAXN, jcast('int', jadd(Code05_RoadTrip.MAXP, 1))])
Code05_RoadTrip.stdist = jarray('int', [Code05_RoadTrip.MAXN, jcast('int', jadd(Code05_RoadTrip.MAXP, 1))])
Code05_RoadTrip.sta = jarray('int', [Code05_RoadTrip.MAXN, jcast('int', jadd(Code05_RoadTrip.MAXP, 1))])
Code05_RoadTrip.stb = jarray('int', [Code05_RoadTrip.MAXN, jcast('int', jadd(Code05_RoadTrip.MAXP, 1))])
Code05_RoadTrip.n = jcast('int', 0)
Code05_RoadTrip.m = jcast('int', 0)
Code05_RoadTrip.a = jcast('int', 0)
Code05_RoadTrip.b = jcast('int', 0)

if __name__ == '__main__':
    Code05_RoadTrip.main([])

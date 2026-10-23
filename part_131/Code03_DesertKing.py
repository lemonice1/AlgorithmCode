# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 最优比率生成树
# 一共有n个村庄，每个村庄由(x, y, z)表示
# 其中(x,y)代表村庄在二维地图中的位置，z代表其海拔高度
# 任意两个村庄之间的距离就是二维地图中的欧式距离
# 任意两个村庄之间的修路花费就是海拔差值的绝对值
# 现在想把所有村庄连通起来，希望修路的条数尽量少，同时希望让
# 总花费 / 总距离，这个比值尽量小，返回最小的比值是多少，结果保留小数点后3位其余部分舍弃
# 2 <= n <= 10^3
# 0 <= x、y <= 10^4
# 0 <= z <= 10^7
# 测试链接 : http://poj.org/problem?id=2728
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code03_DesertKing:
    __java_fields__ = {'MAXN': 'MAXN', 'sml': 'sml', 'x': 'x', 'y': 'y', 'z': 'z', 'dist': 'dist', 'cost': 'cost', 'visit': 'visit', 'value': 'value', 'n': 'n'}
    MAXN = 0
    sml = 0.0
    x = None
    y = None
    z = None
    dist = None
    cost = None
    visit = None
    value = None
    n = 0
    # 邻接矩阵结构下的prim算法，从节点1出发得到最小生成树的权值和
    @staticmethod
    def prim(x):
        x = jcast('double', x)
        # 结余值做边权，进而统计距离
        # 距离只和边权有关，原始的dist、cost不重要
        # 从1号点出发，更新到所有点的距离，也就是value数组
        i = jcast('int', 1)
        while (i <= Code03_DesertKing.n):
            Code03_DesertKing.visit[i] = jcast('boolean', False)
            Code03_DesertKing.value[i] = jcast('double', (Code03_DesertKing.cost[1][i] - (x * Code03_DesertKing.dist[1][i])))
            i = jcast('int', (i + 1))
        Code03_DesertKing.visit[1] = jcast('boolean', True)
        sum = jcast('double', 0)
        # 最小生成树一定有n-1条边，所以一共有n-1轮解锁，每次解锁新的点进入最小生成树的点集
        i = jcast('int', 1)
        while (i <= jcast('int', (Code03_DesertKing.n - 1))):
            # 在没有解锁的点中，找到离最小生成树的点集最近的点，进行解锁
            minDist = jcast('double', jget(Double, 'MAX_VALUE'))
            next = jcast('int', 0)
            j = jcast('int', 1)
            while (j <= Code03_DesertKing.n):
                if ((not Code03_DesertKing.visit[j]) and (Code03_DesertKing.value[j] < minDist)):
                    minDist = jcast('double', Code03_DesertKing.value[j])
                    next = jcast('int', j)
                j = jcast('int', (j + 1))
            # 最小的边进入最小生成树的边集，解锁的点进入最小生成树的点集
            sum = jcast('double', jadd(sum, minDist))
            Code03_DesertKing.visit[next] = jcast('boolean', True)
            # 查看新的解锁点能不能拉进其他点的距离
            j = jcast('int', 1)
            while (j <= Code03_DesertKing.n):
                if ((not Code03_DesertKing.visit[j]) and (Code03_DesertKing.value[j] > (Code03_DesertKing.cost[next][j] - (x * Code03_DesertKing.dist[next][j])))):
                    Code03_DesertKing.value[j] = jcast('double', (Code03_DesertKing.cost[next][j] - (x * Code03_DesertKing.dist[next][j])))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        # 返回最小生成树的权值和
        return jcast('double', sum)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code03_DesertKing.n = jcast('int', jcast('int', jget(in_, 'nval')))
        while (Code03_DesertKing.n != 0):
            i = jcast('int', 1)
            while (i <= Code03_DesertKing.n):
                jcall(in_, 'nextToken')
                Code03_DesertKing.x[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code03_DesertKing.y[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                Code03_DesertKing.z[i] = jcast('int', jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            i = jcast('int', 1)
            while (i <= Code03_DesertKing.n):
                j = jcast('int', 1)
                while (j <= Code03_DesertKing.n):
                    if (i != j):
                        jset(Code03_DesertKing.dist[i], j, jstatic('Math', 'sqrt', jcast('int', jadd(jcast('int', (jcast('int', (Code03_DesertKing.x[i] - Code03_DesertKing.x[j])) * jcast('int', (Code03_DesertKing.x[i] - Code03_DesertKing.x[j])))), jcast('int', (jcast('int', (Code03_DesertKing.y[i] - Code03_DesertKing.y[j])) * jcast('int', (Code03_DesertKing.y[i] - Code03_DesertKing.y[j]))))))))
                        jset(Code03_DesertKing.cost[i], j, jstatic('Math', 'abs', jcast('int', (Code03_DesertKing.z[i] - Code03_DesertKing.z[j]))))
                    j = jcast('int', (j + 1))
                i = jcast('int', (i + 1))
            l = jcast('double', 0)
            r = jcast('double', 100)
            x = 0.0
            ans = jcast('double', 0)
            while ((l < r) and ((r - l) >= Code03_DesertKing.sml)):
                x = jcast('double', jdiv(jadd(l, r), 2))
                # 如果最小生成树的权值 <= 0，达标，左侧二分找寻更小比值
                # 如果最小生成树的权值 > 0，不达标，右侧二分找寻更大比值
                if (Code03_DesertKing.prim(x) <= 0):
                    ans = jcast('double', x)
                    r = jcast('double', (x - Code03_DesertKing.sml))
                else:
                    l = jcast('double', jadd(x, Code03_DesertKing.sml))
            jcall(out, 'printf', '%.3f\n', ans)
            jcall(in_, 'nextToken')
            Code03_DesertKing.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code03_DesertKing.MAXN = jcast('int', 1001)
Code03_DesertKing.sml = jcast('double', 1e-06)
Code03_DesertKing.x = jarray('int', [Code03_DesertKing.MAXN])
Code03_DesertKing.y = jarray('int', [Code03_DesertKing.MAXN])
Code03_DesertKing.z = jarray('int', [Code03_DesertKing.MAXN])
Code03_DesertKing.dist = jarray('double', [Code03_DesertKing.MAXN, Code03_DesertKing.MAXN])
Code03_DesertKing.cost = jarray('double', [Code03_DesertKing.MAXN, Code03_DesertKing.MAXN])
Code03_DesertKing.visit = jarray('boolean', [Code03_DesertKing.MAXN])
Code03_DesertKing.value = jarray('double', [Code03_DesertKing.MAXN])
Code03_DesertKing.n = jcast('int', 0)

if __name__ == '__main__':
    Code03_DesertKing.main([])

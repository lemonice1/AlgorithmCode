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

# 粉刷木板的最大收益
# 一共有n个木板，每个木板长度为1，最多粉刷一次，也可以不刷
# 一共有m个工人，每个工人用(li, pi, si)表示：
# 该工人必须刷连续区域的木板，并且连续的长度不超过li
# 该工人每刷一块木板可以得到pi的钱
# 该工人刷的连续区域必须包含si位置的木板
# 返回所有工人最多能获得多少钱
# 1 <= n <= 16000
# 1 <= m <= 100
# 1 <= pi <= 10000
# 测试链接 : http://poj.org/problem?id=1821
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code04_PaintingMaximumScore:
    __java_fields__ = {'MAXN': 'MAXN', 'MAXM': 'MAXM', 'workers': 'workers', 'dp': 'dp', 'queue': 'queue', 'l': 'l', 'r': 'r', 'n': 'n', 'm': 'm'}
    MAXN = 0
    MAXM = 0
    workers = None
    dp = None
    queue = None
    l = 0
    r = 0
    n = 0
    m = 0
    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        while (jcall(in_, 'nextToken') != jget(StreamTokenizer, 'TT_EOF')):
            Code04_PaintingMaximumScore.n = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            Code04_PaintingMaximumScore.m = jcast('int', jcast('int', jget(in_, 'nval')))
            i = jcast('int', 1)
            while (i <= Code04_PaintingMaximumScore.m):
                jcall(in_, 'nextToken')
                jset(Code04_PaintingMaximumScore.workers[i], 0, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code04_PaintingMaximumScore.workers[i], 1, jcast('int', jget(in_, 'nval')))
                jcall(in_, 'nextToken')
                jset(Code04_PaintingMaximumScore.workers[i], 2, jcast('int', jget(in_, 'nval')))
                i = jcast('int', (i + 1))
            jcall(out, 'println', Code04_PaintingMaximumScore.compute())
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    @staticmethod
    def compute():
        jstatic('Arrays', 'sort', Code04_PaintingMaximumScore.workers, 1, jcast('int', jadd(Code04_PaintingMaximumScore.m, 1)), Code04_PaintingMaximumScore.WorkerComparator())
        i = jcast('int', 1)
        li = 0
        pi = 0
        si = 0
        while (i <= Code04_PaintingMaximumScore.m):
            li = jcast('int', Code04_PaintingMaximumScore.workers[i][0])
            pi = jcast('int', Code04_PaintingMaximumScore.workers[i][1])
            si = jcast('int', Code04_PaintingMaximumScore.workers[i][2])
            Code04_PaintingMaximumScore.l = jcast('int', jset(Code04_PaintingMaximumScore, 'r', 0))
            j = jcast('int', jstatic('Math', 'max', 0, jcast('int', (si - li))))
            while (j < si):
                while ((Code04_PaintingMaximumScore.l < Code04_PaintingMaximumScore.r) and (Code04_PaintingMaximumScore.value(i, pi, Code04_PaintingMaximumScore.queue[jcast('int', (Code04_PaintingMaximumScore.r - 1))]) <= Code04_PaintingMaximumScore.value(i, pi, j))):
                    Code04_PaintingMaximumScore.r = jcast('int', (Code04_PaintingMaximumScore.r - 1))
                jset(Code04_PaintingMaximumScore.queue, ((_java_obj_1 := Code04_PaintingMaximumScore), (_java_key_2 := 'r'), (_java_old_3 := jget(_java_obj_1, _java_key_2)), jset(_java_obj_1, _java_key_2, jcast('int', (_java_old_3 + (1)))), _java_old_3)[4], j)
                j = jcast('int', (j + 1))
            j = jcast('int', 1)
            while (j <= Code04_PaintingMaximumScore.n):
                jset(Code04_PaintingMaximumScore.dp[i], j, jstatic('Math', 'max', Code04_PaintingMaximumScore.dp[jcast('int', (i - 1))][j], Code04_PaintingMaximumScore.dp[i][jcast('int', (j - 1))]))
                if (j >= si):
                    if ((Code04_PaintingMaximumScore.l < Code04_PaintingMaximumScore.r) and (Code04_PaintingMaximumScore.queue[Code04_PaintingMaximumScore.l] == jcast('int', (jcast('int', (j - li)) - 1)))):
                        Code04_PaintingMaximumScore.l = jcast('int', (Code04_PaintingMaximumScore.l + 1))
                    if (Code04_PaintingMaximumScore.l < Code04_PaintingMaximumScore.r):
                        jset(Code04_PaintingMaximumScore.dp[i], j, jstatic('Math', 'max', Code04_PaintingMaximumScore.dp[i][j], jcast('int', jadd(Code04_PaintingMaximumScore.value(i, pi, Code04_PaintingMaximumScore.queue[Code04_PaintingMaximumScore.l]), jcast('int', (pi * j))))))
                j = jcast('int', (j + 1))
            i = jcast('int', (i + 1))
        return jcast('int', Code04_PaintingMaximumScore.dp[Code04_PaintingMaximumScore.m][Code04_PaintingMaximumScore.n])

    # 之前工人负责的区域以j号木板结尾时，返回指标的值
    @staticmethod
    def value(i, pi, j):
        i = jcast('int', i)
        pi = jcast('int', pi)
        j = jcast('int', j)
        return jcast('int', jcast('int', (Code04_PaintingMaximumScore.dp[jcast('int', (i - 1))][j] - jcast('int', (pi * j)))))

    # 比较器接口保留在兼容层中，Python 可使用函数或 lambda 表达式定义比较规则
    class WorkerComparator:
        __java_fields__ = {}
        def compare(self, o1, o2):
            return jcast('int', jcast('int', (o1[2] - o2[2])))

        def __init__(self, *args, _java_ctor=None):
            if args:
                raise TypeError('This class has a no-argument constructor')


    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code04_PaintingMaximumScore.MAXN = jcast('int', 16001)
Code04_PaintingMaximumScore.MAXM = jcast('int', 101)
Code04_PaintingMaximumScore.workers = jarray('int', [Code04_PaintingMaximumScore.MAXM, 3])
Code04_PaintingMaximumScore.dp = jarray('int', [Code04_PaintingMaximumScore.MAXM, Code04_PaintingMaximumScore.MAXN])
Code04_PaintingMaximumScore.queue = jarray('int', [Code04_PaintingMaximumScore.MAXN])
Code04_PaintingMaximumScore.l = jcast('int', 0)
Code04_PaintingMaximumScore.r = jcast('int', 0)
Code04_PaintingMaximumScore.n = jcast('int', 0)
Code04_PaintingMaximumScore.m = jcast('int', 0)

if __name__ == '__main__':
    Code04_PaintingMaximumScore.main([])

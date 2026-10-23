# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 全变成1的最少操作次数
# 一共有n个点，m条无向边，每个点的初始状态都是0
# 可以操作任意一个点，操作后该点以及相邻点的状态都会改变
# 最终是希望所有点都变成1状态，那么可能会若干方案都可以做到
# 那么其中存在需要最少操作次数的方案，打印这个最少操作次数
# 题目保证一定能做到所有点都变成1状态，并且没有重边和自环
# 1 <= n <= 35
# 1 <= m <= 595
# 测试链接 : https://www.luogu.com.cn/problem/P2962
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code02_MinimumOperations:
    __java_fields__ = {'MAXN': 'MAXN', 'mat': 'mat', 'op': 'op', 'n': 'n', 'ans': 'ans'}
    MAXN = 0
    mat = None
    op = None
    n = 0
    ans = 0
    @staticmethod
    def prepare():
        i = jcast('int', 1)
        while (i <= Code02_MinimumOperations.n):
            j = jcast('int', 1)
            while (j <= Code02_MinimumOperations.n):
                jset(Code02_MinimumOperations.mat[i], j, 0)
                j = jcast('int', (j + 1))
            jset(Code02_MinimumOperations.mat[i], i, 1)
            jset(Code02_MinimumOperations.mat[i], jcast('int', jadd(Code02_MinimumOperations.n, 1)), 1)
            Code02_MinimumOperations.op[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    # 高斯消元解决异或方程组模版
    @staticmethod
    def gauss(n):
        n = jcast('int', n)
        i = jcast('int', 1)
        while (i <= n):
            try:
                j = jcast('int', 1)
                while (j <= n):
                    try:
                        if ((j < i) and (Code02_MinimumOperations.mat[j][j] == 1)):
                            raise JContinue(None)
                        if (Code02_MinimumOperations.mat[j][i] == 1):
                            Code02_MinimumOperations.swap(i, j)
                            raise JBreak(None)
                    except JContinue as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                    except JBreak as _java_control_2:
                        if _java_control_2.label not in (None,):
                            raise
                        break
                    j = jcast('int', (j + 1))
                if (Code02_MinimumOperations.mat[i][i] == 1):
                    j = jcast('int', 1)
                    while (j <= n):
                        if ((i != j) and (Code02_MinimumOperations.mat[j][i] == 1)):
                            k = jcast('int', i)
                            while (k <= jcast('int', jadd(n, 1))):
                                ((_java_obj_3 := Code02_MinimumOperations.mat[j]), (_java_key_4 := k), jset(_java_obj_3, _java_key_4, jcast('int', (jget(_java_obj_3, _java_key_4) ^ Code02_MinimumOperations.mat[i][k]))))[2]
                                k = jcast('int', (k + 1))
                        j = jcast('int', (j + 1))
            except JContinue as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
            except JBreak as _java_control_1:
                if _java_control_1.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))

    @staticmethod
    def swap(a, b):
        a = jcast('int', a)
        b = jcast('int', b)
        tmp = Code02_MinimumOperations.mat[a]
        Code02_MinimumOperations.mat[a] = Code02_MinimumOperations.mat[b]
        Code02_MinimumOperations.mat[b] = tmp

    @staticmethod
    def dfs(i, num):
        i = jcast('int', i)
        num = jcast('int', num)
        # 剪枝
        if (num >= Code02_MinimumOperations.ans):
            return
        if (i == 0):
            Code02_MinimumOperations.ans = jcast('int', num)
        else:
            if (Code02_MinimumOperations.mat[i][i] == 0):
                # 当前是自由元
                # 自由元一定不依赖主元
                # 自由元也一定不依赖其他自由元
                # 所以当前自由元一定可以自行决定要不要操作
                Code02_MinimumOperations.op[i] = jcast('int', 0)
                Code02_MinimumOperations.dfs(jcast('int', (i - 1)), num)
                Code02_MinimumOperations.op[i] = jcast('int', 1)
                Code02_MinimumOperations.dfs(jcast('int', (i - 1)), jcast('int', jadd(num, 1)))
            else:
                # 当前是主元
                # 主元可能被其他自由元影响
                # 而且一定有，当前主元的编号 < 影响它的自由元编号
                # 所以会影响当前主元的自由元们，一定已经确定了要不要操作
                # 那么当前主元要不要操作，也就确定了
                cur = jcast('int', Code02_MinimumOperations.mat[i][jcast('int', jadd(Code02_MinimumOperations.n, 1))])
                j = jcast('int', jcast('int', jadd(i, 1)))
                while (j <= Code02_MinimumOperations.n):
                    if (Code02_MinimumOperations.mat[i][j] == 1):
                        cur = jcast('int', jcast('int', (cur ^ Code02_MinimumOperations.op[j])))
                    j = jcast('int', (j + 1))
                Code02_MinimumOperations.dfs(jcast('int', (i - 1)), jcast('int', jadd(num, cur)))

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code02_MinimumOperations.n = jcast('int', jcast('int', jget(in_, 'nval')))
        Code02_MinimumOperations.prepare()
        jcall(in_, 'nextToken')
        m = jcast('int', jcast('int', jget(in_, 'nval')))
        i = jcast('int', 1)
        u = 0
        v = 0
        while (i <= m):
            jcall(in_, 'nextToken')
            u = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            v = jcast('int', jcast('int', jget(in_, 'nval')))
            jset(Code02_MinimumOperations.mat[u], v, 1)
            jset(Code02_MinimumOperations.mat[v], u, 1)
            i = jcast('int', (i + 1))
        Code02_MinimumOperations.gauss(Code02_MinimumOperations.n)
        sign = jcast('int', 1)
        i = jcast('int', 1)
        while (i <= Code02_MinimumOperations.n):
            try:
                if (Code02_MinimumOperations.mat[i][i] == 0):
                    sign = jcast('int', 0)
                    raise JBreak(None)
            except JContinue as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
            except JBreak as _java_control_5:
                if _java_control_5.label not in (None,):
                    raise
                break
            i = jcast('int', (i + 1))
        if (sign == 1):
            # 唯一解
            Code02_MinimumOperations.ans = jcast('int', 0)
            i = jcast('int', 1)
            while (i <= Code02_MinimumOperations.n):
                if (Code02_MinimumOperations.mat[i][jcast('int', jadd(Code02_MinimumOperations.n, 1))] == 1):
                    Code02_MinimumOperations.ans = jcast('int', (Code02_MinimumOperations.ans + 1))
                i = jcast('int', (i + 1))
        else:
            # 多解
            Code02_MinimumOperations.ans = jcast('int', Code02_MinimumOperations.n)
            Code02_MinimumOperations.dfs(Code02_MinimumOperations.n, 0)
        jcall(out, 'println', Code02_MinimumOperations.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code02_MinimumOperations.MAXN = jcast('int', 37)
Code02_MinimumOperations.mat = jarray('int', [Code02_MinimumOperations.MAXN, Code02_MinimumOperations.MAXN])
Code02_MinimumOperations.op = jarray('int', [Code02_MinimumOperations.MAXN])
Code02_MinimumOperations.n = jcast('int', 0)
Code02_MinimumOperations.ans = jcast('int', 0)

if __name__ == '__main__':
    Code02_MinimumOperations.main([])

# -*- coding: utf-8 -*-
from pathlib import Path as _Path
import sys as _sys
_root = str(_Path(__file__).resolve().parent.parent)
if _root not in _sys.path:
    _sys.path.insert(0, _root)
from algorithm_runtime import *
from _python_support import jmatches, jselect

_sys.setrecursionlimit(max(_sys.getrecursionlimit(), 1000000))

# 甄别食物链
# 一共有n只动物，编号1 ~ n，每只动物都是A、B、C中的一种，A吃B、B吃C、C吃A
# 一共有k句话，希望你判断哪些话是假话，每句话是如下两类句子中的一类
# 1 X Y : 第X只动物和第Y只动物是同类
# 2 X Y : 第X只动物吃第Y只动物
# 当前的话与前面的某些真话冲突，视为假话
# 当前的话提到的X和Y，有任何一个大于n，视为假话
# 当前的话如果关于吃，又有X==Y，视为假话
# 返回k句话中，假话的数量
# 1 <= n <= 5 * 10^4    1 <= k <= 10^5
# 测试链接 : https://www.luogu.com.cn/problem/P2024
# Python 版本保留标准输入输出入口；在线提交时需一并提供公共辅助模块
class Code06_JudgeFoodChain:
    __java_fields__ = {'MAXN': 'MAXN', 'n': 'n', 'k': 'k', 'ans': 'ans', 'father': 'father', 'dist': 'dist'}
    MAXN = 0
    n = 0
    k = 0
    ans = 0
    father = None
    # dist[i] = 0，代表i和头是同类
    # dist[i] = 1，代表i吃头
    # dist[i] = 2，代表i被头吃
    dist = None
    @staticmethod
    def prepare():
        Code06_JudgeFoodChain.ans = jcast('int', 0)
        i = jcast('int', 1)
        while (i <= Code06_JudgeFoodChain.n):
            Code06_JudgeFoodChain.father[i] = jcast('int', i)
            Code06_JudgeFoodChain.dist[i] = jcast('int', 0)
            i = jcast('int', (i + 1))

    @staticmethod
    def find(i):
        i = jcast('int', i)
        if (i != Code06_JudgeFoodChain.father[i]):
            tmp = jcast('int', Code06_JudgeFoodChain.father[i])
            jset(Code06_JudgeFoodChain.father, i, Code06_JudgeFoodChain.find(tmp))
            Code06_JudgeFoodChain.dist[i] = jcast('int', jcast('int', jmod(jcast('int', jadd(Code06_JudgeFoodChain.dist[i], Code06_JudgeFoodChain.dist[tmp])), 3)))
        return jcast('int', Code06_JudgeFoodChain.father[i])

    # op == 1, 1 l r，l和r是同类
    # op == 2, 2 l r，l吃r
    @staticmethod
    def union(op, l, r):
        op = jcast('int', op)
        l = jcast('int', l)
        r = jcast('int', r)
        lf = jcast('int', Code06_JudgeFoodChain.find(l))
        rf = jcast('int', Code06_JudgeFoodChain.find(r))
        v = jcast('int', (0 if (op == 1) else 1))
        if (lf != rf):
            Code06_JudgeFoodChain.father[lf] = jcast('int', rf)
            Code06_JudgeFoodChain.dist[lf] = jcast('int', jcast('int', jmod(jcast('int', jadd(jcast('int', jadd(jcast('int', (Code06_JudgeFoodChain.dist[r] - Code06_JudgeFoodChain.dist[l])), v)), 3)), 3)))

    @staticmethod
    def check(op, l, r):
        op = jcast('int', op)
        l = jcast('int', l)
        r = jcast('int', r)
        if (((l > Code06_JudgeFoodChain.n) or (r > Code06_JudgeFoodChain.n)) or ((op == 2) and (l == r))):
            return jcast('boolean', False)
        if (Code06_JudgeFoodChain.find(l) == Code06_JudgeFoodChain.find(r)):
            if (op == 1):
                if (Code06_JudgeFoodChain.dist[l] != Code06_JudgeFoodChain.dist[r]):
                    return jcast('boolean', False)
            else:
                if (jcast('int', jmod(jcast('int', jadd(jcast('int', (Code06_JudgeFoodChain.dist[l] - Code06_JudgeFoodChain.dist[r])), 3)), 3)) != 1):
                    return jcast('boolean', False)
        return jcast('boolean', True)

    @staticmethod
    def main(args):
        br = jnew('BufferedReader', jnew('InputStreamReader', jget(System, 'in')))
        in_ = jnew('StreamTokenizer', br)
        out = jnew('PrintWriter', jnew('OutputStreamWriter', jget(System, 'out')))
        jcall(in_, 'nextToken')
        Code06_JudgeFoodChain.n = jcast('int', jcast('int', jget(in_, 'nval')))
        jcall(in_, 'nextToken')
        Code06_JudgeFoodChain.k = jcast('int', jcast('int', jget(in_, 'nval')))
        Code06_JudgeFoodChain.prepare()
        i = jcast('int', 1)
        op = 0
        l = 0
        r = 0
        while (i <= Code06_JudgeFoodChain.k):
            jcall(in_, 'nextToken')
            op = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            l = jcast('int', jcast('int', jget(in_, 'nval')))
            jcall(in_, 'nextToken')
            r = jcast('int', jcast('int', jget(in_, 'nval')))
            if (not Code06_JudgeFoodChain.check(op, l, r)):
                Code06_JudgeFoodChain.ans = jcast('int', (Code06_JudgeFoodChain.ans + 1))
            else:
                Code06_JudgeFoodChain.union(op, l, r)
            i = jcast('int', (i + 1))
        jcall(out, 'println', Code06_JudgeFoodChain.ans)
        jcall(out, 'flush')
        jcall(out, 'close')
        jcall(br, 'close')

    def __init__(self, *args, _java_ctor=None):
        if args:
            raise TypeError('This class has a no-argument constructor')


Code06_JudgeFoodChain.MAXN = jcast('int', 50001)
Code06_JudgeFoodChain.n = jcast('int', 0)
Code06_JudgeFoodChain.k = jcast('int', 0)
Code06_JudgeFoodChain.ans = jcast('int', 0)
Code06_JudgeFoodChain.father = jarray('int', [Code06_JudgeFoodChain.MAXN])
Code06_JudgeFoodChain.dist = jarray('int', [Code06_JudgeFoodChain.MAXN])

if __name__ == '__main__':
    Code06_JudgeFoodChain.main([])
